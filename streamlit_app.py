import streamlit as st
import random

# Lista de perguntas em caixa alta
questions = [
    {
        "question": "O QUE É O ESTOL?",
        "options": {
            "A": "A AERONAVE PERDE SUSTENTAÇÃO",
            "B": "A AERONAVE AUMENTA A VELOCIDADE",
            "C": "A AERONAVE GANHA SUSTENTAÇÃO",
            "D": "A AERONAVE DIMINUI A ALTITUDE",
        },
        "answer": "A",
        "explanation": "ESTOL É O FENÔMENO AERODINÂMICO EM QUE A ASA PERDE A SUSTENTAÇÃO DEVIDO AO ÂNGULO DE ATAQUE EXCESSIVO, RESULTANDO EM PERDA DE ALTITUDE E POSSÍVEL QUEDA DA AERONAVE."
    },
    {
        "question": "QUAL É A VELOCIDADE DO SOM NO AR?",
        "options": {
            "A": "1235 KM/H",
            "B": "1000 KM/H",
            "C": "1500 KM/H",
            "D": "343 M/S",
        },
        "answer": "D",
        "explanation": "A VELOCIDADE DO SOM NO AR, AO NÍVEL DO MAR E A UMA TEMPERATURA DE 20°C, É DE APROXIMADAMENTE 343 METROS POR SEGUNDO (M/S)."
    },
    # Adicione mais perguntas conforme necessário
]

# Embaralha as perguntas
random.shuffle(questions)

# Inicializa variáveis de estado
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
    st.session_state.score = 0
    st.session_state.selected_option = None
    st.session_state.show_explanation = False

# Função para exibir a pergunta atual
def show_question():
    q = questions[st.session_state.current_question]
    st.subheader(f"PERGUNTA {st.session_state.current_question + 1}:")
    st.write(q["question"])
    options = list(q["options"].items())
    for key, value in options:
        st.radio("ESCOLHA UMA OPÇÃO:", options=[f"{k}) {v}" for k, v in q["options"].items()], key="selected_option")
    if st.button("RESPONDER"):
        selected = st.session_state.selected_option
        if selected:
            selected_key = selected[0]
            if selected_key == q["answer"]:
                st.session_state.score += 1
                st.success("RESPOSTA CORRETA!")
            else:
                st.error(f"RESPOSTA INCORRETA! A RESPOSTA CORRETA É: {q['answer']}) {q['options'][q['answer']]}")
            st.write(f"EXPLICAÇÃO: {q['explanation']}")
            st.session_state.show_explanation = True

# Função para avançar para a próxima pergunta
def next_question():
    if st.session_state.current_question + 1 < len(questions):
        st.session_state.current_question += 1
        st.session_state.selected_option = None
        st.session_state.show_explanation = False
    else:
        st.write(f"QUIZ FINALIZADO! SUA PONTUAÇÃO: {st.session_state.score} DE {len(questions)}")
        if st.button("REINICIAR QUIZ"):
            st.session_state.current_question = 0
            st.session_state.score = 0
            st.session_state.selected_option = None
            st.session_state.show_explanation = False

# Exibe a pergunta ou avança para a próxima
if not st.session_state.show_explanation:
    show_question()
else:
    if st.button("PRÓXIMA PERGUNTA"):
        next_question()
