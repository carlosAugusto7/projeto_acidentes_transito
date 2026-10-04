import os
import sqlite3
import pandas as pd
import plotly.express as px
import streamlit as st
from PIL import Image

# 1. Configuração da Página
st.set_page_config(
    page_title="Painel Executivo — Acidentes de Trânsito no Brasil",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Estilo CSS Customizado (tema azul-marinho)
st.markdown("""
    <style>
    /* Fundo geral */
    .stApp { background-color: #06182b; }
    .block-container { padding-top: 2rem; }

    /* Sidebar com degradê azul */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0b3d78 0%, #082a52 55%, #06203f 100%);
        border-right: 1px solid #14508f;
    }
    section[data-testid="stSidebar"] .stMultiSelect span[data-baseweb="tag"] {
        background-color: #1d5fa8;
        color: #ffffff;
    }

    /* Sidebar mais larga (só quando aberta) */
section[data-testid="stSidebar"][aria-expanded="true"] {
    min-width: 380px;
    width: 380px;
}

/* Menos espaço vazio acima da logo */
div[data-testid="stSidebarHeader"] { padding-bottom: 0; }
div[data-testid="stSidebarUserContent"] { padding-top: 0.5rem; }

    /* Cards de KPI */
    div[data-testid="stMetric"] {
        background: linear-gradient(145deg, #0f3157 0%, #0b2542 100%);
        border: 1px solid #1d4f85;
        border-left: 4px solid #2f9bff;
        padding: 16px;
        border-radius: 12px;
        box-shadow: 0 6px 14px rgba(0,0,0,0.35);
    }
    div[data-testid="stMetric"] label {
        color: #8fb4dd !important;
        font-size: 0.8rem !important;
        font-weight: 600 !important;
        text-transform: uppercase;
        letter-spacing: 0.04em;
    }
    div[data-testid="stMetric"] div[data-testid="stMetricValue"] {
        color: #ffffff !important;
        font-size: 1.5rem !important;
        font-weight: 700 !important;
    }

    /* Abas */
    .stTabs [data-baseweb="tab-list"] { gap: 10px; }
    .stTabs [data-baseweb="tab"] {
        height: 46px;
        white-space: pre-wrap;
        background-color: #0c2a4a;
        border-radius: 8px 8px 0 0;
        padding: 10px 20px;
        color: #9db9d8;
    }
    .stTabs [aria-selected="true"] {
        background: linear-gradient(90deg, #1d6fd1, #2f9bff) !important;
        color: #ffffff !important;
        font-weight: bold;
    }

    /* Títulos e divisores */
    h1, h2, h3 { color: #e6eef8; }
    hr { border-color: #1a3f6b; }
    </style>
""", unsafe_allow_html=True)


# 3. Função de Carregamento dos Dados
@st.cache_data
def carregar_dados():
    db_path = os.path.join("database", "acidentes.db")
    csv_path = os.path.join("dados", "simulacao_acidentes_transito_brasil.csv")

    if os.path.exists(db_path):
        conn = sqlite3.connect(db_path)
        df = pd.read_sql_query("SELECT * FROM acidentes", conn)
        conn.close()
    else:
        df = pd.read_csv(csv_path)

    df['data'] = pd.to_datetime(df['data'])
    return df


df = carregar_dados()

# 4. Cabeçalho Principal
st.title("🚗 Painel Analítico: Acidentes de Trânsito no Brasil")
st.caption("📍 Dados Históricos Consolidados | Período de Análise: 2015 a 2024")
st.caption("🎓 Disciplina: Linguagens de Programação  |  👨‍🏫 Professor: Alexandre Neves Louzada  |  👤 Aluno: Carlos Augusto Ferreira Souza")

def preparar_logo(caminho):
    """Abre a logo e remove a margem transparente ao redor do desenho."""
    img = Image.open(caminho).convert("RGBA")
    caixa = img.split()[-1].getbbox()  # área não transparente
    if caixa:
        img = img.crop(caixa)
    return img

# 5. Barra Lateral (Logo + Filtros)
pasta_base = os.path.dirname(os.path.abspath(__file__))
pasta_imagens = os.path.join(pasta_base, "imagens")

logo_path = None
if os.path.isdir(pasta_imagens):
    for arquivo in sorted(os.listdir(pasta_imagens)):
        if arquivo.lower().endswith((".png", ".jpg", ".jpeg", ".webp", ".svg")):
            logo_path = os.path.join(pasta_imagens, arquivo)
            break

if logo_path:
    st.sidebar.image(preparar_logo(logo_path), use_container_width=True)
else:
    st.sidebar.warning("Logo não encontrada na pasta 'imagens'.")
st.sidebar.markdown("<hr style='border-color:#1f4f85;'>", unsafe_allow_html=True)
st.sidebar.markdown("## 🔍 Filtros de Pesquisa")

anos = sorted(df['ano'].unique())
anos_sel = st.sidebar.multiselect("Ano", anos, default=anos)

regioes = sorted(df['regiao'].unique())
regioes_sel = st.sidebar.multiselect("Região", regioes, default=regioes)

df_base_uf = df[df['regiao'].isin(regioes_sel)]
ufs = sorted(df_base_uf['uf'].unique())
ufs_sel = st.sidebar.multiselect("Estado (UF)", ufs, default=ufs)

tipos = sorted(df['tipo_acidente'].unique())
tipos_sel = st.sidebar.multiselect("Tipo de Acidente", tipos, default=tipos)

periodos = sorted(df['periodo_dia'].unique())
periodos_sel = st.sidebar.multiselect("Período do Dia", periodos, default=periodos)

gravidades = sorted(df['nivel_gravidade'].unique())
gravidades_sel = st.sidebar.multiselect("Nível de Gravidade", gravidades, default=gravidades)

st.sidebar.markdown("---")
st.sidebar.caption("🎓 Linguagens de Programação")
st.sidebar.caption("👨‍🏫 Prof. Alexandre Neves Louzada")
st.sidebar.caption("👤 Carlos Augusto Ferreira Souza")

# Aplicação dos filtros
df_filtered = df[
    (df['ano'].isin(anos_sel)) &
    (df['regiao'].isin(regioes_sel)) &
    (df['uf'].isin(ufs_sel)) &
    (df['tipo_acidente'].isin(tipos_sel)) &
    (df['periodo_dia'].isin(periodos_sel)) &
    (df['nivel_gravidade'].isin(gravidades_sel))
]

# Se os filtros não retornarem nada, avisa e interrompe
if df_filtered.empty:
    st.warning("Nenhum dado encontrado com os filtros selecionados. Ajuste os filtros na barra lateral.")
    st.stop()

# 6. Painel de KPIs Superiores
st.markdown("### 📌 Indicadores-Chave de Desempenho (KPIs)")
kpi1, kpi2, kpi3, kpi4, kpi5, kpi6 = st.columns(6)

tot_acidentes = int(df_filtered['acidentes'].sum())
tot_feridos = int(df_filtered['feridos'].sum())
tot_obitos = int(df_filtered['obitos'].sum())

uf_top = df_filtered.groupby('uf')['acidentes'].sum().idxmax()
periodo_top = df_filtered.groupby('periodo_dia')['acidentes'].sum().idxmax()
tipo_top = df_filtered.groupby('tipo_acidente')['acidentes'].sum().idxmax()

kpi1.metric("Total Acidentes", f"{tot_acidentes:,}".replace(",", "."))
kpi2.metric("Total Feridos", f"{tot_feridos:,}".replace(",", "."))
kpi3.metric("Total Óbitos", f"{tot_obitos:,}".replace(",", "."))
kpi4.metric("UF Mais Crítica", uf_top)
kpi5.metric("Período Crítico", periodo_top)
kpi6.metric("Tipo Predominante", tipo_top)

st.markdown("---")

# 7. Estrutura em Abas Visuais
tab_tempo, tab_geo, tab_fatores, tab_dados = st.tabs([
    "📈 Série Temporal", "🗺️ Comparação Regional", "⚠️ Clima & Gravidade", "📋 Base de Dados"
])

# Template e paleta dos gráficos
graph_template = "plotly_dark"

AZUL = "#2f9bff"
CIANO = "#22d3ee"
AMBAR = "#fbbf24"
VERMELHO = "#f43f5e"
ESCALA_AZUL = ["#0b2a4a", "#14508f", "#1d7fd1", "#2f9bff", "#7cc4ff"]
ESCALA_CALOR = ["#0b2a4a", "#1d7fd1", "#22d3ee", "#fbbf24", "#f43f5e"]


def estilizar(fig, altura=450):
    """Aplica fundo transparente e cores de grade combinando com o tema."""
    fig.update_layout(
        height=altura,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#cfe0f5"),
        margin=dict(l=10, r=10, t=30, b=10),
    )
    fig.update_xaxes(gridcolor="#12385f")
    fig.update_yaxes(gridcolor="#12385f")
    return fig


with tab_tempo:
    st.subheader("Evolução Anual de Ocorrências e Vítimas")
    df_tempo = df_filtered.groupby('ano')[['acidentes', 'feridos', 'obitos']].sum().reset_index()

    fig_line = px.line(
        df_tempo, x='ano', y=['acidentes', 'feridos', 'obitos'],
        labels={'value': 'Total', 'ano': 'Ano da Ocorrência', 'variable': 'Métrica'},
        markers=True,
        template=graph_template,
        color_discrete_map={'acidentes': AZUL, 'feridos': AMBAR, 'obitos': VERMELHO}
    )
    fig_line.update_layout(legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1))
    estilizar(fig_line)
    st.plotly_chart(fig_line, use_container_width=True)

with tab_geo:
    col_a, col_b = st.columns(2)
    with col_a:
        st.subheader("Ranking de Acidentes por Estado (UF)")
        df_uf = df_filtered.groupby('uf')['acidentes'].sum().reset_index().sort_values('acidentes', ascending=True)
        fig_uf = px.bar(
            df_uf, x='acidentes', y='uf', orientation='h',
            color='acidentes', color_continuous_scale=ESCALA_AZUL,
            template=graph_template, text_auto=True
        )
        fig_uf.update_layout(coloraxis_showscale=False)
        estilizar(fig_uf)
        st.plotly_chart(fig_uf, use_container_width=True)

    with col_b:
        st.subheader("Frequência por Tipo de Acidente")
        df_tipo = df_filtered.groupby('tipo_acidente')['acidentes'].sum().reset_index().sort_values('acidentes', ascending=False)
        fig_tipo = px.bar(
            df_tipo, x='tipo_acidente', y='acidentes',
            color='acidentes', color_continuous_scale=ESCALA_CALOR,
            template=graph_template, text_auto=True
        )
        fig_tipo.update_layout(coloraxis_showscale=False)
        estilizar(fig_tipo)
        st.plotly_chart(fig_tipo, use_container_width=True)

with tab_fatores:
    col_c, col_d = st.columns(2)
    with col_c:
        st.subheader("Distribuição por Condição Climática")
        df_clima = df_filtered.groupby('condicao_climatica')['acidentes'].sum().reset_index()
        fig_pie = px.pie(
            df_clima, values='acidentes', names='condicao_climatica',
            hole=0.4, template=graph_template,
            color_discrete_sequence=[AZUL, CIANO, "#7cc4ff", AMBAR, VERMELHO, "#a78bfa"]
        )
        estilizar(fig_pie)
        st.plotly_chart(fig_pie, use_container_width=True)

    with col_d:
        st.subheader("Matriz: Período do Dia vs Gravidade")
        df_piv = df_filtered.pivot_table(
            index='periodo_dia', columns='nivel_gravidade',
            values='acidentes', aggfunc='sum', fill_value=0
        )
        fig_heat = px.imshow(
            df_piv, labels=dict(x="Gravidade", y="Período do Dia", color="Casos"),
            color_continuous_scale=ESCALA_CALOR, template=graph_template, text_auto=True
        )
        estilizar(fig_heat)
        st.plotly_chart(fig_heat, use_container_width=True)

with tab_dados:
    st.subheader("Exploração de Dados Filtrados")
    st.dataframe(df_filtered, use_container_width=True, height=400)

    st.markdown("#### 📥 Exportação dos Dados")
    csv = df_filtered.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download da Tabela em CSV",
        data=csv,
        file_name="acidentes_filtrados.csv",
        mime="text/csv"
    )

# 8. Relatório Executivo
st.markdown("---")
st.subheader("💡 Diagnóstico Executivo")
st.info("""
* **Concentração Espacial:** Unidades Federativas de grande fluxo viário (como RJ, SP, ES e MG) mantêm o topo das ocorrências registradas no período.
* **Gravidade Noturna:** O cruzamento de dados confirma que acidentes ocorridos durante o período **Noturno e Madrugada** registram as maiores proporções relativas de severidade **Alta** e **Crítica**.
* **Recomendações:** Intensificação da fiscalização com radares e patrulhamento em trechos de alta velocidade e em períodos de chuva intensa.
""")