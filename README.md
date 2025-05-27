# 🔍 WhereIsMyStuff

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**🎯 Nunca mais perca suas coisas! Organize e encontre seus itens de forma inteligente**

[🚀 **ACESSE O APP**](https://whereismystuff.streamlit.app/) | [📖 **DOCUMENTAÇÃO**](#como-usar) | [🐛 **REPORTAR BUG**](../../issues)

</div>

---

## 🌟 **O que é o WhereIsMyStuff?**

<div align="center">

```
📦 Casa Inteira    →    🔍 Item Específico    →    📍 Localização Exata
```

</div>

O **WhereIsMyStuff** é uma aplicação web intuitiva que transforma uma simples planilha Excel em um **sistema de busca inteligente** para seus pertences! 

Ideal para:
- 🏠 **Organização doméstica** - Saiba onde estão todos os itens da sua casa
- 📦 **Mudanças** - Controle o conteúdo de cada caixa
- 🏢 **Escritórios** - Gerencie inventário e materiais
- 🎒 **Viagens** - Organize suas malas e bagagens

---

## ✨ **Funcionalidades**

<table>
<tr>
<td width="50%">

### 📁 **Upload Simples**
- Faça upload de arquivos `.xlsx`
- Interface drag & drop intuitiva
- Processamento instantâneo

### 🔍 **Busca Inteligente**
- Encontre qualquer item rapidamente
- Busca parcial e completa
- Linguagem natural suportada, ex. "Onde está meu fone JBL?"
- Resultados em tempo real

</td>
<td width="50%">

### 📊 **Visualização Clara**
- Interface limpa e organizada
- Cores e ícones informativos
- Layout responsivo

### 🚀 **Acesso Online**
- Disponível 24/7 na web
- Não precisa instalar nada
- Funciona em qualquer dispositivo

</td>
</tr>
</table>

---

## 📋 **Como Usar**

### **Passo 1:** Prepare sua planilha
Crie um arquivo Excel (`.xlsx`) seguindo este formato:

```
| Quarto Principal | Cozinha        | Garagem           |
|------------------|----------------|-------------------|
| Camisa azul      | Panela grande  | Chave de fenda    |
| Relógio dourado  | Açúcar         | Martelo           |
| Livro Python     | Café           | Parafusos         |
| Carregador       | Sal            | Óleo do carro     |
```

> 💡 **Dica:** A primeira linha contém os **locais** e as linhas abaixo contêm os **itens** daquele local.

> 💡 **Dica:** Você pode criar a planilha pelo Google Sheets e depois exportá-la no formato `.xlsx`.

### **Passo 2:** Faça o upload
1. Acesse [whereismystuff.streamlit.app](https://whereismystuff.streamlit.app/)
2. Abra a drawer que fica do lado esquerdo da tela
3. Clique em **"Browse files"** ou arraste sua planilha
4. Aguarde o processamento

### **Passo 3:** Busque seus itens
- Digite o nome do item na barra de busca
- Veja instantaneamente onde ele está localizado!

---

## 🎨 **Preview da Interface**

<div align="center">

### 📱 **Tela Principal**
![image](https://github.com/user-attachments/assets/c439eb7e-a7f2-4448-bf57-e52dba5b2813)

### 📱 **Drawer para upload do arquivo**
![image](https://github.com/user-attachments/assets/2357894e-5cd8-43da-80ea-3eee974d5edf)

### 🎯 **Resultado da Busca**
![image](https://github.com/user-attachments/assets/9c9029cb-8fea-4088-a943-258860059507)


</div>

---

## 🛠️ **Tecnologias Utilizadas**

<div align="center">

| Tecnologia | Uso | Badge |
|------------|-----|-------|
| **Python** | Linguagem principal | ![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python) |
| **Streamlit** | Framework web | ![Streamlit](https://img.shields.io/badge/Streamlit-Latest-red?logo=streamlit) |
| **Pandas** | Manipulação de dados | ![Pandas](https://img.shields.io/badge/Pandas-Latest-orange?logo=pandas) |
| **OpenPyXL** | Leitura de Excel | ![OpenPyXL](https://img.shields.io/badge/OpenPyXL-Latest-green) |

</div>

---

## 📁 **Estrutura do Projeto**

```
whereismystuff/
│
├── 📄 app.py                 # Aplicação principal
├── 📄 requirements.txt       # Dependências
├── 📄 README.md             # Este arquivo
└── 📁 .streamlit/
    └── 📄 config.toml       # Configurações do Streamlit
```

---

## 🚀 **Executar Localmente**

### **Pré-requisitos**
- Python 3.8 ou superior
- pip

### **Instalação**

```bash
# 1. Clone o repositório
git clone https://github.com/seuusuario/whereismystuff.git
cd whereismystuff

# 2. Instale as dependências
pip install -r requirements.txt

# 3. Execute a aplicação
streamlit run app.py
```

A aplicação estará disponível em `http://localhost:8501`

---

## 📝 **Exemplo de Planilha**

<details>
<summary>📋 <strong>Ver estrutura detalhada</strong></summary>

```xlsx
A1: Quarto      | B1: Sala       | C1: Cozinha    | D1: Banheiro
A2: Camiseta    | B2: Controle   | C2: Panela     | D2: Shampoo
A3: Calça       | B3: Almofada   | C3: Colher     | D3: Sabonete
A4: Sapato      | B4: Revista    | C4: Prato      | D4: Escova
A5: Mochila     | B5: Óculos     | C5: Copo       | D5: Pasta
```

</details>

---

## 🤝 **Contribuindo**

Quer ajudar a melhorar o WhereIsMyStuff? Toda contribuição é bem-vinda!

### **Como contribuir:**

1. 🍴 Faça um fork do projeto
2. 🌿 Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. 💾 Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. 📤 Push para a branch (`git push origin feature/AmazingFeature`)
5. 🔄 Abra um Pull Request

### **Ideias para contribuições:**
- 📱 Melhorias na interface
- 🔍 Algoritmos de busca mais inteligentes
- 📊 Relatórios e estatísticas
- 🌐 Suporte a outros formatos de arquivo
- 🔐 Sistema de autenticação
- 🐘 Adicionar local storage 
- 📲 Criar uma webview

---

## 📄 **Licença**

<div align="center">

Este projeto está licenciado sob a **MIT License** - veja o arquivo [LICENSE](LICENSE) para detalhes.

[![MIT License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

</div>

---

## 👨‍💻 **Autor**

<div align="center">

**Criado com ❤️ por [carolwebdev](https://github.com/carolwebdev)**

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/carowebdev)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/carol-ina)

</div>

---

## 🌟 **Mostre seu apoio**

Se este projeto te ajudou, considere dar uma ⭐ no repositório!

<div align="center">

**[⭐ Star este repositório](../../stargazers)** | **[🔄 Fork este projeto](../../fork)** | **[📝 Reportar problema](../../issues)**

---

*Feito com 💜 e muito ☕*

</div>

---

## 📊 **Estatísticas**

<div align="center">

![GitHub stars](https://img.shields.io/github/stars/carolwebdev/whereismystuff?style=social)
![GitHub forks](https://img.shields.io/github/forks/carolwebdev/whereismystuff?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/carolwebdev/whereismystuff?style=social)

![GitHub last commit](https://img.shields.io/github/last-commit/carolwebdev/whereismystuff)
![GitHub issues](https://img.shields.io/github/issues/carolwebdev/whereismystuff)
![GitHub pull requests](https://img.shields.io/github/issues-pr/carolwebdev/whereismystuff)

</div>

