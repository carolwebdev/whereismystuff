import streamlit as st
import pandas as pd
import re
import os
from io import BytesIO
import tempfile
from gtts import gTTS

class AssistenteDeBusca:
    def __init__(self, arquivo_excel=None):
        self.objeto_para_caixa = {}
        if arquivo_excel:
            self.carregar_dados(arquivo_excel)
        
    def carregar_dados(self, arquivo_excel=None):
        try:
            # Usa o arquivo enviado ou tenta encontrar um padrão
            if arquivo_excel:
                df = pd.read_excel(arquivo_excel)
            else:
                st.error("Nenhum arquivo Excel fornecido.")
                return False
                
            # Cria dicionário objeto → caixa
            for nome_caixa in df.columns:
                for item in df[nome_caixa].dropna():
                    item_normalizado = str(item).strip().lower()
                    if item_normalizado:
                        self.objeto_para_caixa[item_normalizado] = nome_caixa
            return True
        except Exception as e:
            st.error(f"Erro ao carregar dados: {str(e)}")
            return False
    
    def processar_pergunta(self, pergunta):
        # Lista de padrões para reconhecer perguntas sobre localização
        padroes = [
            r"onde est[áa][o]?\s+([^?]+)",
            r"onde (coloquei|guardei|deixei|encontro|acho)\s+([^?]+)",
            r"em qual caixa est[áa][o]?\s+([^?]+)",
            r"onde fica[m]?\s+([^?]+)",
            r"localiz[ea][r]?\s+([^?]+)",
            r"encontra[r]?\s+([^?]+)",
            r"^([^?]+)$"  # Captura apenas o objeto se for apenas ele
        ]
        
        # Tentar encontrar um objeto na pergunta
        for padrao in padroes:
            match = re.search(padrao, pergunta.lower())
            if match:
                # Pega o último grupo capturado (o objeto)
                objeto = match.group(match.lastindex).strip()
                if objeto:
                    return self.onde_esta(objeto)
        
        return "Não entendi sua pergunta. Tente perguntar como 'Onde está meu livro?' ou apenas digite o nome do objeto."
    
    def onde_esta(self, objeto):
        obj_normalizado = objeto.strip().lower()
        resultados = []

        for nome_objeto, nome_caixa in self.objeto_para_caixa.items():
            if obj_normalizado in nome_objeto:
                resultados.append((nome_objeto, nome_caixa))

        if resultados:
            if len(resultados) == 1:
                nome_objeto, nome_caixa = resultados[0]
                return f'"{nome_objeto}" está na caixa "{nome_caixa}".'
            else:
                resposta = f'Encontrei {len(resultados)} objetos que correspondem a "{objeto}":\n\n'
                for nome_objeto, nome_caixa in resultados:
                    resposta += f'• "{nome_objeto}" está na caixa "{nome_caixa}"\n'
                return resposta
        else:
            sugestoes = self.encontrar_sugestoes(obj_normalizado)
            if sugestoes:
                resp = f'Não encontrei nenhum objeto chamado "{objeto}".\n\nVocê quis dizer:'
                for s in sugestoes[:5]:  # Limita a 5 sugestões
                    resp += f'\n• {s}?'
                return resp
            else:
                return f'Não encontrei nenhum objeto chamado "{objeto}" nas caixas catalogadas.'
    
    def encontrar_sugestoes(self, termo):
        """Encontra objetos similares para sugerir"""
        sugestoes = []
        
        # Método simples: se o termo é uma substring de algum objeto
        for nome_objeto in self.objeto_para_caixa.keys():
            # Se o objeto contém pelo menos 2 caracteres do termo pesquisado
            if len(termo) >= 2 and any(parte in nome_objeto for parte in termo.split()):
                sugestoes.append(nome_objeto)
                
        return sugestoes
    
    def listar_todos_objetos(self):
        """Lista todos os objetos catalogados"""
        if not self.objeto_para_caixa:
            return "Nenhum objeto foi catalogado ainda."
            
        objetos_por_caixa = {}
        for objeto, caixa in self.objeto_para_caixa.items():
            if caixa not in objetos_por_caixa:
                objetos_por_caixa[caixa] = []
            objetos_por_caixa[caixa].append(objeto)
            
        resposta = "Lista de todos os objetos catalogados:\n\n"
        for caixa, objetos in sorted(objetos_por_caixa.items()):
            resposta += f"Caixa: {caixa}\n"
            for obj in sorted(objetos):
                resposta += f"• {obj}\n"
            resposta += "\n"
            
        return resposta

def text_to_audio(texto):
    """Converte texto em áudio usando gTTS e retorna um link para o áudio"""
    try:
        tts = gTTS(text=texto, lang='pt-br', slow=False)
        audio_file = BytesIO()
        tts.write_to_fp(audio_file)
        audio_file.seek(0)
        return audio_file
    except Exception as e:
        st.error(f"Erro ao gerar áudio: {str(e)}")
        return None

def main():
    st.set_page_config(
        page_title="Assistente de Busca de Objetos",
        page_icon="🔍",
        layout="centered",
        initial_sidebar_state="collapsed",
    )
    
    st.title("🔍 Assistente de Busca de Objetos")
    
    # Inicializa o estado da sessão para armazenar o histórico da conversa
    if 'historico_conversa' not in st.session_state:
        st.session_state.historico_conversa = []
        st.session_state.assistente = None
        st.session_state.arquivo_carregado = False
    
    # Sidebar para upload do arquivo e configurações
    with st.sidebar:
        st.header("Configurações")
        arquivo_excel = st.file_uploader("Carregar arquivo Excel com os objetos", type=['xlsx'])
        
        resposta_por_voz = st.checkbox("Ativar resposta por voz", value=True)
        
        if st.button("Limpar Histórico"):
            st.session_state.historico_conversa = []
            st.experimental_rerun()
        
        st.markdown("---")
        st.markdown("### Como usar:")
        st.markdown("""
        1. Carregue seu arquivo Excel com a lista de objetos e caixas
        2. Digite sua pergunta na caixa de texto
        3. Pergunte onde está algo, por exemplo:
           - Onde está meu livro?
           - Onde guardei a caneta?
           - Em qual caixa estão os documentos?
        """)
    
    # Carrega os dados quando o arquivo for enviado
    if arquivo_excel and not st.session_state.arquivo_carregado:
        with st.spinner("Carregando dados..."):
            st.session_state.assistente = AssistenteDeBusca(arquivo_excel)
            st.session_state.arquivo_carregado = True
            st.session_state.historico_conversa.append(
                {"autor": "Assistente", "mensagem": "Arquivo carregado com sucesso! Pergunte-me onde estão seus objetos."}
            )
    
    # Container para exibir o histórico da conversa
    conversa_container = st.container()
    
    # Input para a pergunta
    pergunta = st.text_input("Sua pergunta:", placeholder="Onde está meu...?")
    col1, col2 = st.columns([3, 1])
    
    with col1:
        enviar = st.button("Enviar Pergunta", use_container_width=True)
    
    with col2:
        listar = st.button("Listar Todos", use_container_width=True)
    
    # Processar a pergunta quando o botão for clicado
    if enviar and pergunta and st.session_state.assistente:
        st.session_state.historico_conversa.append({"autor": "Você", "mensagem": pergunta})
        resposta = st.session_state.assistente.processar_pergunta(pergunta)
        st.session_state.historico_conversa.append({"autor": "Assistente", "mensagem": resposta})
        
        # Limpar o campo de entrada
        st.experimental_rerun()
    
    # Processar o botão "Listar Todos"
    if listar and st.session_state.assistente:
        resposta = st.session_state.assistente.listar_todos_objetos()
        st.session_state.historico_conversa.append({"autor": "Assistente", "mensagem": resposta})
        st.experimental_rerun()

        # ... (seu código existente para carregar o arquivo Excel, etc.) ...

        # HTML para botão de gravação e script da Web Speech API
        st.components.v1.html(
            """
            <script>
            const recognition = new webkitSpeechRecognition() || new SpeechRecognition(); // Para compatibilidade com Chrome e outros navegadores
            recognition.lang = 'pt-BR'; // Defina o idioma
            recognition.interimResults = false; // Apenas resultados finais
            const recordButton = document.getElementById('recordButton');
            const recognizedText = document.getElementById('recognizedText');

            recordButton.addEventListener('click', () => {
                recognition.start();
                recordButton.disabled = true; // Desativa o botão durante a gravação
                recognizedText.textContent = 'Ouvindo...';
            });

            recognition.onresult = (event) => {
                const speechResult = event.results[0][0].transcript;
                recognizedText.textContent = speechResult;
                Streamlit.set({ 'final_transcript': speechResult }); // Envia para o Streamlit
                recognition.stop();
                recordButton.disabled = false; // Reativa o botão
            };

            recognition.onerror = (event) => {
                recognizedText.textContent = 'Erro ao reconhecer a fala.';
                recognition.stop();
                recordButton.disabled = false;
            };

            recognition.onend = () => {
                recordButton.disabled = false;
            };
            </script>
            <div>
                <button id="recordButton">Iniciar Gravação</button>
                <p id="recognizedText"></p>
            </div>
            """
        )

        final_transcript = st.text_area("Texto Reconhecido", key="final_transcript", value="")

        if final_transcript:
            st.session_state.historico_conversa.append({"autor": "Você", "mensagem": final_transcript})
            resposta = st.session_state.assistente.processar_pergunta(final_transcript)
            st.session_state.historico_conversa.append({"autor": "Assistente", "mensagem": resposta})
            st.experimental_rerun()
    
    # Exibir o histórico da conversa
    with conversa_container:
        if not st.session_state.historico_conversa:
            if not st.session_state.arquivo_carregado:
                st.info("👋 Olá! Carregue seu arquivo Excel com a lista de objetos para começar.")
            else:
                st.info("👋 Olá! Pergunte-me onde estão seus objetos.")
        else:
            for mensagem in st.session_state.historico_conversa:
                autor = mensagem["autor"]
                texto = mensagem["mensagem"]
                
                # Estilo diferente para cada autor
                if autor == "Você":
                    st.markdown(f"**Você:**")
                    st.markdown(f"{texto}")
                else:
                    st.markdown(f"**Assistente:**")
                    st.markdown(f"{texto}")
                    
                    # Reproduzir em áudio se a opção estiver ativada
                    if resposta_por_voz and autor == "Assistente" and len(texto) < 500:
                        audio_bytes = text_to_audio(texto)
                        if audio_bytes:
                            st.audio(audio_bytes, format="audio/mp3")
                
                st.markdown("---")
    
    # Aviso quando não há arquivo carregado
    if not st.session_state.arquivo_carregado:
        st.warning("⚠️ Carregue um arquivo Excel com seus objetos para começar a usar o assistente.")

if __name__ == "__main__":
    main()