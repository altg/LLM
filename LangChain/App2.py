import streamlit as st
import pickle
from Questions import *


with open("objects.pkl", 'rb') as file:
    obj = pickle.load(file)

if "score" not in st.session_state:
    st.session_state.score = 0

if "metric_visible" not in st.session_state:
    st.session_state.metric_visible = "hidden"

if "question_index" not in st.session_state:
    st.session_state.question_index = 0

if "mcq_disabled" not in st.session_state:
    st.session_state.mcq_disabled = False

if "last_question" not in st.session_state:
    st.session_state.last_question = False

num_of_Q = len(obj.Questions)

Q = obj.Questions[st.session_state.question_index]


def get_next_question():
    if st.session_state.question_index < num_of_Q - 1:
        st.session_state.question_index += 1
    else:
        st.session_state.last_question = True
    st.session_state.mcq_disabled = False
    

def get_MCs(MultipleChoices):
      
    MCs = ['']
    for k , v in enumerate(MultipleChoices):
            MCs.append(v.choice_ans)
    return MCs
    



def show_results(correct_ans, MCs):

    st.session_state.mcq_disabled = True
    selected_ndx = MCs.index(st.session_state.mcq) - 1

    if selected_ndx == correct_ans:
      st.text("Correct !!")
      st.session_state.score += 1
    else:
      st.text(f"""Wrong !! - {correct_ans}""")

    st.session_state.metric_visible = "visible"
       


st.metric("Score :" , st.session_state.score , label_visibility= st.session_state.metric_visible)

st.write(Q.question)

MCs = get_MCs(Q.MultipleChoices)

selected = st.radio(
        "Select One",
        MCs,
        key = "mcq",
        on_change=show_results,
        args=(Q.correct_ans , MCs),
        disabled=st.session_state.mcq_disabled
    )

st.button("Next Question" , on_click=get_next_question)