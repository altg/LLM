import streamlit as st
import pickle
from Questions import *

if "score" not in st.session_state:
    st.session_state.score = 0

def get_MCs(MultipleChoices):
      
    MCs = ['']

    for k , v in enumerate(MultipleChoices):
            MCs.append(v.choice_ans)

    return MCs
    

    

with open("objects.pkl", 'rb') as file:
    obj = pickle.load(file)

Q1 = obj.Questions[0]


def show_results(correct_ans, MCs):

    selected_ndx = MCs.index(st.session_state.mcq) - 1

    selected_ndx
    correct_ans

    if selected_ndx == correct_ans:
      st.write("Correct !!")
      st.session_state.score += 1
    else:
      st.write(f"""Wrong !! - {correct_ans}""")
       
 


def ask_question(Q):      
    st.write(Q.question)

    MCs = get_MCs(Q.MultipleChoices)

    selected = st.radio(
        "Select One",
        MCs,
        key = "mcq",
        on_change=show_results,
        args=(Q.correct_ans , MCs)
    )
 

    #st.text(f"""{selected_ndx} : {selected}""")

    return st.session_state.score

score = ask_question(Q1)

st.metric("Score :" , score)


