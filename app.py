import streamlit as st

st.set_page_config(page_title="Classificador de Sentimento", page_icon="💬")

st.title("💬 Classificador de Sentimento de Comentários")
st.write(
    "Insira o comentário do cliente abaixo para analisar se ele é **Positivo**, **Negativo** ou **Neutro** baseado em palavras-chave."
)

# Entrada de texto do usuário
comentario = st.text_area("Digite o comentário do cliente:")

# Listas de palavras-chave para classificação simples
palavras_positivas = [
    "bom",
    "boa",
    "excelente",
    "ótimo",
    "ótima",
    "gostei",
    "amamos",
    "perfeito",
    "maravilhoso",
    "recomendo",
    "top",
    "satisfeito",
]
palavras_negativas = [
    "ruim",
    "péssimo",
    "péssima",
    "odiei",
    "horrível",
    "demora",
    "demorado",
    "defeito",
    "decepcionado",
    "reclamar",
    "pior",
    "cancelar",
]

if st.button("Analisar Sentimento"):
    if comentario.strip() == "":
        st.warning("Por favor, digite algum comentário antes de analisar.")
    else:
        comentario_lower = comentario.lower()

        # Checa presença de palavras-chave usando condicionais
        tem_positivo = any(
            palavra in comentario_lower for palavra in palavras_positivas
        )
        tem_negativo = any(
            palavra in comentario_lower for palavra in palavras_negativas
        )

        # Classificação por condicionais
        if tem_positivo and not tem_negativo:
            st.success("😊 **Sentimento: POSITIVO**")
        elif tem_negativo and not tem_positivo:
            st.error("😡 **Sentimento: NEGATIVO**")
        elif tem_positivo and tem_negativo:
            st.info("😐 **Sentimento: MISTO / NEUTRO**")
        else:
            st.info("😐 **Sentimento: NEUTRO / NÃO IDENTIFICADO**")