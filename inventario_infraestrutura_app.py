# inventario_infraestrutura_app_v5.py
import streamlit as st
import pandas as pd
from datetime import datetime

# --- PALETA DE CORES BASEADA NA LOGO ---
COLOR_PRIMARY = "#70D1C6"  # Azul/Verde Água da logo
COLOR_TEXT_DARK = "#333333" # Cinza escuro do texto da logo
COLOR_BACKGROUND = "#FFFFFF" # Fundo branco

# --- CONFIGURAÇÃO DA PÁGINA E ESTILOS CSS ---
st.set_page_config(
    page_title="Inventário de Infraestrutura - Wedja Psicologia",
    layout="wide"
)

# Inserção de CSS customizado
st.markdown(f"""
    <style>
         /* ##### CÓDIGO DEFINITIVO PARA REMOVER ELEMENTOS DO STREAMLIT ##### */

        /* Remove a barra superior com o botão "Fork" e outros links */
        /* Este é o seletor principal para a barra que você quer remover */
        div[data-testid="stHeader"] {{
            visibility: hidden;
            height: 0%;
            position: fixed;
        }}

        /* Remove a fina linha decorativa no topo da página */
        div[data-testid="stDecoration"] {{
            visibility: hidden;
            height: 0%;
            position: fixed;
        }}
        
        /* Esconde o rodapé "Made with Streamlit" */
        footer {{
            visibility: hidden;
            height: 0%;
        }}
        
        /* ############################################################### */


        /* Fundo da página */
        .stApp {{
            background-color: {COLOR_BACKGROUND};
            color: {COLOR_TEXT_DARK};
        }}

        /* Títulos principais */
        h1, h2, h3 {{
            color: {COLOR_TEXT_DARK};
        }}
        
        /* Cabeçalho superior da aplicação (o seu, customizado) */
        div[data-testid="stTopBar"] {{
            background-color: {COLOR_PRIMARY};
        }}

        /* Título do inventário */
        .stApp > header {{
            background-color: {COLOR_PRIMARY};
            padding: 1rem;
            color: white;
            border-bottom: 5px solid {COLOR_TEXT_DARK};
        }}
        .stApp > header h1 {{
            color: white !important;
            margin: 0;
            padding: 0;
        }}
        
        /* Card de identificação */
        div.st-emotion-cache-1r4qj8v {{ /* Seletor para o st.container(border=True) */
             background-color: #f0f2f6;
             border-left: 5px solid {COLOR_PRIMARY};
             border-radius: 5px;
             padding: 1.5rem;
             margin-top: 1rem;
             margin-bottom: 1.5rem;
             box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }}

        /* Input fields */
        div[data-testid="textInputRootElement"] > label,
        div[data-testid="stRadioGroup"] > label {{
            color: {COLOR_TEXT_DARK};
            font-weight: 600;
        }}
        .stTextInput > div > div > input {{
            border: 1px solid #ccc;
            border-radius: 4px;
            padding: 0.5rem;
        }}
        .stTextInput > div > div > input:focus {{
            border-color: {COLOR_PRIMARY};
            box-shadow: 0 0 0 0.15rem rgba(112, 209, 198, 0.25);
        }}

        /* Expanders (Blocos de Perguntas) */
        .streamlit-expanderHeader {{
            background-color: {COLOR_PRIMARY};
            color: white;
            font-size: 1.2rem;
            font-weight: bold;
            border-radius: 8px;
            margin-top: 1rem;
            padding: 0.75rem 1rem;
            border: none;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }}
        .streamlit-expanderHeader:hover {{
            background-color: {COLOR_TEXT_DARK};
        }}
        .streamlit-expanderContent {{
            background-color: #f9f9f9;
            border-left: 3px solid {COLOR_PRIMARY};
            padding: 1rem;
            border-bottom-left-radius: 8px;
            border-bottom-right-radius: 8px;
            margin-bottom: 1rem;
        }}

        /* ########## ALTERAÇÃO PARA RESPONSIVIDADE ########## */
        /* Radio buttons (Likert Scale) - Responsivo */
        div[data-testid="stRadio"] > div {{
            display: flex;
            flex-wrap: wrap; /* ESSENCIAL: Permite que os itens quebrem a linha */
            justify-content: flex-start; /* Alinha os itens ao início */
        }}

        div[data-testid="stRadio"] label {{
            margin-right: 1.2rem; /* Espaçamento entre os botões */
            margin-bottom: 0.5rem; /* Espaçamento quando quebrar a linha */
            color: {COLOR_TEXT_DARK};
        }}
        /* ###################################################### */

        /* Botões */
        .stButton button {{
            background-color: {COLOR_PRIMARY};
            color: white;
            font-weight: bold;
            padding: 0.75rem 1.5rem;
            border-radius: 8px;
            border: none;
            transition: all 0.2s ease-in-out;
        }}
        .stButton button:hover {{
            background-color: {COLOR_TEXT_DARK};
            color: white;
            transform: translateY(-2px);
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.15);
        }}
        .stDownloadButton button {{
            background-color: {COLOR_TEXT_DARK};
            color: white;
        }}
    </style>
""", unsafe_allow_html=True)


# --- CABEÇALHO DA APLICAÇÃO ---
col1, col2 = st.columns([1, 3])
with col1:
    try:
        st.image("logo_wedja.jpg", width=120)
    except FileNotFoundError:
        st.warning("Logo 'logo_wedja.png' não encontrada.")
with col2:
    st.markdown("""
    <div style="display: flex; align-items: center; height: 100%;">
        <h1 style='text-align: left; color: black;'>INVENTÁRIO DE INFRAESTRUTURA</h1>
    </div>
    """, unsafe_allow_html=True)


# --- CAMPOS DE IDENTIFICAÇÃO ---
with st.container(border=True):
    st.markdown("<h3 style='text-align: center;'>Identificação do Preenchimento</h3>", unsafe_allow_html=True)
    col1_form, col2_form = st.columns(2)
    with col1_form:
        organizacao = st.text_input("Organização:")
        setor_equipe = st.text_input("Setor/Equipe:")
    with col2_form:
        respondente = st.text_input("Respondente:")
        data_turno = st.text_input("Data / Turno:", value=datetime.now().strftime('%Y-%m-%d'))

# --- INSTRUÇÕES ---
st.subheader("Instruções de Preenchimento")
st.info("""
    Avalie cada item usando a escala abaixo. Itens marcados com **(R)** são reversos e terão sua pontuação ajustada na análise.
    **1** = Discordo totalmente • **2** = Discordo • **3** = Nem discordo nem concordo • **4** = Concordo • **5** = Concordo totalmente • Use **N/A** quando não se aplica.
""")


# --- LÓGICA DO QUESTIONÁRIO (BACK-END) ---
@st.cache_data
def carregar_itens():
    try:
        df = pd.read_excel("Inventario_Infraestrutura_Likert.xlsx", sheet_name="Dados")
        return df
    except Exception:
        data = [('Instalações Físicas', 'Espaço', 'IF01', 'O espaço físico é suficiente para as atividades sem congestionamentos.', 'NÃO'), ('Instalações Físicas', 'Limpeza & Organização', 'IF02', 'A limpeza e a organização das áreas são mantidas ao longo do dia.', 'NÃO'), ('Instalações Físicas', 'Iluminação', 'IF03', 'A iluminação geral é adequada às tarefas realizadas.', 'NÃO'), ('Instalações Físicas', 'Conforto Térmico & Ventilação', 'IF04', 'A temperatura e a ventilação são adequadas ao tipo de atividade.', 'NÃO'), ('Instalações Físicas', 'Ruído & Acústica', 'IF05', 'O nível de ruído não prejudica a concentração e a comunicação.', 'NÃO'), ('Instalações Físicas', 'Sinalização', 'IF06', 'A sinalização de rotas, setores e riscos é clara e suficiente.', 'NÃO'), ('Instalações Físicas', 'Emergência', 'IF07', 'As saídas de emergência estão desobstruídas e bem sinalizadas.', 'NÃO'), ('Instalações Físicas', 'Layout & Fluxo', 'IF08', 'O layout facilita o fluxo de pessoas, materiais e informações.', 'NÃO'), ('Instalações Físicas', 'Armazenamento', 'IF09', 'As áreas de armazenamento são dimensionadas e identificadas adequadamente.', 'NÃO'), ('Instalações Físicas', 'Acessibilidade', 'IF10', 'A infraestrutura é acessível (rampas, corrimãos, largura de portas) para PCD.', 'NÃO'), ('Instalações Físicas', 'Conservação', 'IF11', 'Pisos, paredes e tetos estão em bom estado de conservação.', 'NÃO'), ('Instalações Físicas', 'Circulação (R)', 'IF12', 'Há obstáculos ou áreas obstruídas que dificultam a circulação.', 'SIM'), ('Equipamentos', 'Disponibilidade', 'EQ01', 'Os equipamentos necessários estão disponíveis quando requisitados.', 'NÃO'), ('Equipamentos', 'Adequação Técnica', 'EQ02', 'Os equipamentos possuem capacidade/recursos adequados às tarefas.', 'NÃO'), ('Equipamentos', 'Confiabilidade', 'EQ03', 'Os equipamentos operam de forma confiável, sem falhas frequentes.', 'NÃO'), ('Equipamentos', 'Manutenção Preventiva', 'EQ04', 'O plano de manutenção preventiva está atualizado e é cumprido.', 'NÃO'), ('Equipamentos', 'Registros', 'EQ05', 'O histórico de manutenção está documentado e acessível.', 'NÃO'), ('Equipamentos', 'Calibração', 'EQ06', 'Instrumentos críticos estão calibrados dentro dos prazos.', 'NÃO'), ('Equipamentos', 'Peças de Reposição', 'EQ07', 'Há disponibilidade de peças de reposição críticas.', 'NÃO'), ('Equipamentos', 'Treinamento', 'EQ08', 'Os usuários dos equipamentos recebem treinamento adequado.', 'NÃO'), ('Equipamentos', 'Documentação', 'EQ09', 'Manuais e procedimentos de operação estão acessíveis.', 'NÃO'), ('Equipamentos', 'Segurança', 'EQ10', 'Dispositivos de segurança (proteções, intertravamentos) estão instalados e operantes.', 'NÃO'), ('Equipamentos', 'Paradas (R)', 'EQ11', 'Paradas não planejadas atrapalham significativamente a rotina de trabalho.', 'SIM'), ('Equipamentos', 'Obsolescência (R)', 'EQ12', 'Há equipamentos obsoletos que comprometem a qualidade ou a segurança.', 'SIM'), ('Ferramentas', 'Disponibilidade', 'FE01', 'As ferramentas necessárias estão disponíveis quando preciso.', 'NÃO'), ('Ferramentas', 'Qualidade & Adequação', 'FE02', 'As ferramentas possuem qualidade e são adequadas ao trabalho.', 'NÃO'), ('Ferramentas', 'Ergonomia', 'FE03', 'As ferramentas manuais são ergonômicas e confortáveis de usar.', 'NÃO'), ('Ferramentas', 'Padronização', 'FE04', 'Existe padronização adequada de tipos e modelos de ferramentas.', 'NÃO'), ('Ferramentas', 'Identificação & Rastreio', 'FE05', 'Ferramentas estão identificadas (etiquetas/códigos) e rastreáveis.', 'NÃO'), ('Ferramentas', 'Armazenamento (5S)', 'FE06', 'O armazenamento é organizado (5S) e evita danos/perdas.', 'NÃO'), ('Ferramentas', 'Manutenção', 'FE07', 'Manutenção/afiação/ajustes estão em dia quando necessário.', 'NÃO'), ('Ferramentas', 'Localização (R)', 'FE08', 'Ferramentas compartilhadas raramente estão onde deveriam.', 'SIM'), ('Ferramentas', 'Treinamento', 'FE09', 'Os colaboradores são treinados para o uso correto das ferramentas.', 'NÃO'), ('Ferramentas', 'Substituição', 'FE10', 'Ferramentas danificadas são substituídas com rapidez.', 'NÃO'), ('Ferramentas', 'Improviso (R)', 'FE11', 'Existem ferramentas improvisadas em uso nas atividades.', 'SIM'), ('Ferramentas', 'Segurança', 'FE12', 'As ferramentas estão em conformidade com requisitos de segurança (isolantes, antifaísca, etc.).', 'NÃO'), ('Postos de Trabalho', 'Ergonomia', 'PT01', 'O posto permite ajuste ergonômico (altura, apoios, cadeiras).', 'NÃO'), ('Postos de Trabalho', 'Arranjo & Alcance', 'PT02', 'Materiais e dispositivos estão posicionados ao alcance adequado.', 'NÃO'), ('Postos de Trabalho', 'Iluminação Focal', 'PT03', 'A iluminação focal no posto é adequada.', 'NÃO'), ('Postos de Trabalho', 'Ruído & Vibração', 'PT04', 'Ruído e vibração no posto estão dentro de limites aceitáveis.', 'NÃO'), ('Postos de Trabalho', 'Ventilação Local', 'PT05', 'Há ventilação/exaustão local adequada quando necessário.', 'NÃO'), ('Postos de Trabalho', 'EPI', 'PT06', 'Os EPIs necessários estão disponíveis, em bom estado e são utilizados.', 'NÃO'), ('Postos de Trabalho', 'Organização (5S)', 'PT07', 'O posto está organizado (5S) e livre de excessos.', 'NÃO'), ('Postos de Trabalho', 'Instruções de Trabalho', 'PT08', 'Instruções de trabalho estão visíveis e atualizadas.', 'NÃO'), ('Postos de Trabalho', 'Recursos Digitais', 'PT09', 'Computadores, softwares e internet funcionam de forma estável.', 'NÃO'), ('Postos de Trabalho', 'Posturas (R)', 'PT10', 'O desenho do posto induz posturas forçadas ou movimentos repetitivos excessivos.', 'SIM'), ('Postos de Trabalho', 'EPI Insuficiente (R)', 'PT11', 'Há falta de EPI adequado ou em bom estado.', 'SIM'), ('Postos de Trabalho', 'Riscos de Queda/Tropeço (R)', 'PT12', 'Cabos, fios ou objetos soltos representam riscos no posto.', 'SIM')]
        df = pd.DataFrame(data, columns=["Bloco", "Dimensão", "ID", "Item", "Reverso"])
        return df

df = carregar_itens()

# --- FORMULÁRIO ---
st.subheader("Formulário de Avaliação")
permitir_na = st.checkbox("Permitir N/A (não se aplica)", value=True)
blocos = df["Bloco"].unique().tolist()
respostas = {}

for bloco in blocos:
    with st.expander(f"Bloco: {bloco}", expanded=bloco == blocos[0]):
        df_bloco = df[df["Bloco"] == bloco].copy()
        for _, row in df_bloco.iterrows():
            key = row["ID"]
            label = f'({row["ID"]}) ' + row["Item"] + (' (R)' if row["Reverso"] == "SIM" else "")
            options = [1, 2, 3, 4, 5]
            if permitir_na:
                options = ["N/A"] + options
            respostas[key] = st.radio(label, options=options, horizontal=True, key=key, index=0)

st.markdown("---")

# --- CÁLCULO E EXIBIÇÃO DOS RESULTADOS ---
if st.button("Calcular e Finalizar", type="primary"):
    # ... (O restante da lógica de cálculo permanece o mesmo) ...
    reg = []
    lookup = df.set_index("ID")[["Bloco", "Dimensão", "Item", "Reverso"]].to_dict("index")
    for k, v in respostas.items():
        reg.append({
            "ID": k, "Resposta": None if v == "N/A" else v, "Reverso": lookup[k]["Reverso"],
            "Bloco": lookup[k]["Bloco"], "Dimensão": lookup[k]["Dimensão"], "Item": lookup[k]["Item"],
        })
    dfr = pd.DataFrame(reg)
    def ajustar(x, rev):
        if pd.isna(x): return x
        x = float(x)
        return 6 - x if rev == "SIM" else x
    dfr["Resposta_Ajustada"] = dfr.apply(lambda r: ajustar(r["Resposta"], r["Reverso"]), axis=1)
    resumo_bloco = dfr.groupby("Bloco", dropna=False)["Resposta_Ajustada"].mean().rename("Média (1-5)").reset_index().sort_values("Média (1-5)", ascending=True)
    resumo_total = dfr["Resposta_Ajustada"].mean()
    st.subheader("Resultados por Bloco")
    st.dataframe(resumo_bloco, use_container_width=True, hide_index=True)
    st.metric("Média Geral", f"{resumo_total:.2f}")
    st.subheader("Gráfico (Média por Bloco)")
    st.bar_chart(resumo_bloco.set_index("Bloco"))
    st.subheader("Exportar Respostas")
    dfr_export = dfr.copy()
    dfr_export["Organização"] = organizacao
    dfr_export["Setor/Equipe"] = setor_equipe
    dfr_export["Respondente"] = respondente
    dfr_export["Data/Turno"] = data_turno
    dfr_export["Timestamp"] = datetime.now().isoformat(timespec="seconds")
    colunas_export = ["Timestamp", "Organização", "Setor/Equipe", "Respondente", "Data/Turno", "ID", "Bloco", "Item", "Resposta", "Resposta_Ajustada", "Reverso"]
    dfr_export = dfr_export[colunas_export]
    st.download_button(label="Baixar respostas (CSV)", data=dfr_export.to_csv(index=False, sep=";").encode("utf-8-sig"), file_name=f"respostas_infra_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv", mime="text/csv")
else:
    st.info("Preencha o formulário e clique em **Calcular e Finalizar** para ver os resultados.")