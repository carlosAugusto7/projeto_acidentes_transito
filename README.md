<div align="center">

# 🚗 Observatório de Segurança Viária — Brasil
### Painel Analítico e Preditivo de Acidentes de Trânsito (2015–2024)

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.30+-FF4B4B.svg?logo=streamlit&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-3.0+-003B57.svg?logo=sqlite&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.0+-150458.svg?logo=pandas&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-Express-3F4F75.svg?logo=plotly&logoColor=white)
![License](https://img.shields.io/badge/Status-Conclu%C3%ADdo-brightgreen.svg)

[🌐 Acessar Dashboard Interativo](https://projetoacidentestransito-pztkqivp9x.streamlit.app) • [📄 Ver Landing Page (GitHub Pages)](https://carlosaugusto7.github.io/projeto_acidentes_transito/)

</div>

---

## 🎓 Identificação Acadêmica

* **Curso:** Sistemas de Informação
* **Disciplina:** [Nome da sua Disciplina]
* **Professor:** Alexandre Neves Louzada
* **Aluno:** [Seu Nome Completo]
* **Período:** 2026

---

## 📌 Visão Geral do Projeto

Este projeto consiste em uma plataforma de análise exploratória, espacial e temporal dos padrões de acidentes de trânsito em rodovias e vias nacionais brasileiras entre os anos de **2015 e 2024**. 

A solução foi desenvolvida utilizando a linguagem **Python** e um pipeline de dados completo: desde a higienização e tratamento dos dados brutos, passando pela persistência relacional em **SQLite**, até a exibição executiva por meio de um **Dashboard Interativo em Streamlit**.

---

## 💡 Principais Funcionalidades

- **📌 Indicadores-Chave (KPIs) Dinâmicos:** Cálculo em tempo real do total de acidentes, vítimas (feridos/óbitos), UF mais crítica, período predominante e tipo de ocorrência mais comum.
- **📈 Análise Temporal de Tendências:** Gráficos de linha interativos (Plotly) permitindo visualizar a evolução das estatísticas ao longo da década.
- **🗺️ Diagnóstico Regional & Tipologia:** Rankings horizontais por Unidade Federativa (UF) e por tipo de acidente (colisão frontal, tombamento, atropelamento, etc.).
- **⚠️ Matriz de Fatores e Gravidade:** Cruzamento de variáveis como condições climáticas e período do dia versus o nível de gravidade das ocorrências.
- **🔍 Filtros Multivariados Integrados:** Filtragem simultânea na barra lateral por Ano, Região, Estado (UF), Tipo de Acidente, Período do Dia e Gravidade.
- **📥 Exportação de Dados:** Funcionalidade de download da base filtrada em formato `.csv` diretamente pela interface.

---

## 🛠️ Tecnologias e Ferramentas Utilizadas

| Camada / Função | Tecnologias |
| :--- | :--- |
| **Linguagem Principal** | Python 3.11+ |
| **Manipulação de Dados** | Pandas, NumPy |
| **Banco de Dados Relacional** | SQLite, SQLAlchemy |
| **Visualização Interativa** | Plotly Express, Matplotlib, Seaborn |
| **Interface do Dashboard** | Streamlit, CSS3 Customizado (Dark Theme) |
| **Versionamento & Deploy** | Git, GitHub, GitHub Pages, Streamlit Community Cloud |

---

## 📂 Estrutura do Repositório

```text
projeto-acidentes-transito/
│
├── .streamlit/
│   └── config.toml             # Configurações de tema visual do Streamlit
├── dados/
│   └── simulacao_acidentes_transito_brasil.csv  # Base de dados em CSV
├── database/
│   └── acidentes.db            # Banco de dados relacional SQLite
├── imagens/
│   └── logo_dashboard_transito.png  # Identidade visual do projeto
├── notebooks/
│   └── analise_acidentes.ipynb # EDA e prototipagem em Jupyter Notebook
├── scripts/
│   └── criar_banco.py          # Script de criação/povoamento do SQLite
├── app.py                      # Aplicação principal do Dashboard
├── index.html                  # Landing Page para publicação via GitHub Pages
├── README.md                   # Documentação completa do projeto
└── requirements.txt            # Dependências e bibliotecas Python

🚀 Como Executar o Projeto Localmente
Pré-requisitos
Certifique-se de ter o Python 3.10+ e o Git instalados no seu computador.

Passo a Passo
Clonar o repositório:

Bash
git clone [https://github.com/carlosAugusto7/projeto_acidentes_transito.git](https://github.com/carlosAugusto7/projeto_acidentes_transito.git)
cd projeto-acidentes-transito
Criar e ativar um ambiente virtual (opcional):

Bash
python -m venv venv
# No Windows (PowerShell/CMD):
venv\Scripts\activate
Instalar as dependências:

Bash
pip install -r requirements.txt
Inicializar o Banco de Dados SQLite:

Bash
python scripts/criar_banco.py
Executar a aplicação Streamlit:

Bash
streamlit run app.py
O dashboard abrirá automaticamente no seu navegador padrão no endereço http://localhost:8501.

🔗 Links de Acesso Rápido
📊 Dashboard Interativo (Streamlit Cloud): Acessar Aplicação

🌐 Página Institucional (GitHub Pages): Acessar Landing Page

📁 Código-Fonte (GitHub): Acessar Repositório

🔄 Como atualizar o seu README no GitHub:
Abra o arquivo README.md no seu VS Code.

Substitua [Nome da sua Disciplina] e [Seu Nome Completo] nos campos indicados.

Salve o arquivo (Ctrl + S).

Abra o terminal do VS Code (Ctrl + ') e envie para o GitHub: