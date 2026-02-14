import streamlit as st
import time
import random
import base64

# 1. Page Configuration
st.set_page_config(page_title="For Mary", page_icon="💌")

def render_gif(path):
    file_ = open(path, "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()

    st.markdown(
        f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
        unsafe_allow_html=True,
    )

# css
st.markdown("""
    <style>
    .stApp { text-align: center; }
    
    /* 1. TEXT STYLING */
    h1 { 
        text-align: center; 
        color: #ff4b4b;
        font-family: 'Helvetica', sans-serif;
    }
    
    /* 2. BUTTON STYLING & ANIMATION */
    /* Define the Zoom In Keyframes */
    @keyframes zoomIn {
        0% { opacity: 0; transform: scale(0.5); }
        100% { opacity: 1; transform: scale(1); }
    }

    /* Apply animation to ALL buttons */
    .stButton button {
        animation: zoomIn 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275); /* Bouncy effect */
    }

    /* Force "Primary" buttons (YES) to be GREEN */
    button[kind="primary"] {
        background-color: #28a745 !important;
        border-color: #28a745 !important;
        color: white !important; 
        font-size: 20px !important;
    }

    /* Force "Secondary" buttons (NO) to be RED */
    button[kind="secondary"] {
        background-color: #dc3545 !important;
        border-color: #dc3545 !important;
        color: white !important;
        font-size: 20px !important;
    }

    /* 3. FADE IN ANIMATION (For the Question Text) */
    @keyframes fadeIn {
        0% { opacity: 0; transform: translateY(20px); }
        100% { opacity: 1; transform: translateY(0px); }
    }
    
    .fade-in-text {
        animation: fadeIn 2s ease-in-out;
    }
    </style>
""", unsafe_allow_html=True)

# setup
if 'stage' not in st.session_state:
    st.session_state.stage = 'intro'

if 'no_pos' not in st.session_state:
    st.session_state.no_pos = 8

if 'buttons_revealed' not in st.session_state:
    st.session_state.buttons_revealed = False

# typewriter effect
def typewriter(text, speed=0.08):
    placeholder = st.empty()
    displayed_text = ""
    for char in text:
        displayed_text += char
        placeholder.markdown(f"<h1>{displayed_text}▌</h1>", unsafe_allow_html=True)
        time.sleep(speed)
    placeholder.markdown(f"<h1>{displayed_text}</h1>", unsafe_allow_html=True)
    time.sleep(1.5)
    placeholder.empty()

# stage 1: intro
if st.session_state.stage == 'intro':
    typewriter("Hi bb chutie dil yes wae barbie! \n👉👈", speed=0.1)
    typewriter("This is ur bb adrian! 🐷", speed=0.1)
    typewriter("Happy happy valentines bib 🫰🫶!!!", speed=0.1)
    typewriter("Thank you sa 3 bb valentines together yeyyy", speed=0.1)
    typewriter("A lot of things happened in the past years", speed=0.1)
    typewriter("We went to lots of places, had many away, and also had many bb celebrations", speed=0.1)
    typewriter("But still no bb anniversary celebration huhu", speed=0.1)
    typewriter("I also just want to say sorry for things I did and did not do...", speed=0.1)
    typewriter("For the numerous times when I did not live to your expectations", speed=0.1)
    typewriter("I'm really sorry bib", speed=0.1)
    typewriter("And thank you for staying with me after all this time", speed=0.1)
    typewriter("and teaching me love...", speed=0.1)
    typewriter("love that gives,", speed=0.15)
    typewriter("love that forgives,", speed=0.15)
    typewriter("and love that remembers.", speed=0.15)
    typewriter("", speed=0.1)

    typewriter("I know it is late...", speed=0.1)
    typewriter("and it is not like me...", speed=0.1)
    typewriter("but since this is our last valentine sa college,", speed=0.1)
    typewriter("I wanted to ask you this question hehehe", speed=0.1)

    time.sleep(1)

    st.session_state.stage = 'question'
    st.rerun()

# stage 2: question
elif st.session_state.stage == 'question':
    
    if not st.session_state.buttons_revealed:
        st.markdown('<div class="fade-in-text"><h1>Will you be my bb valentine? 🌹</h1></div>', unsafe_allow_html=True)
        time.sleep(2.5) 
        st.session_state.buttons_revealed = True
        
        if 'no_pos' not in st.session_state:
            st.session_state.no_pos = 1
    else:
        st.markdown('<h1>Will you be my bb valentine? 🌹</h1>', unsafe_allow_html=True)
        
        st.markdown("""
            <style>
            .stButton button {
                animation: none !important;
                transition: none !important;
            }
            </style>
        """, unsafe_allow_html=True)

    st.write("##")

    if 'no_pos' not in st.session_state or st.session_state.no_pos < 1 or st.session_state.no_pos > 6:
        st.session_state.no_pos = 1

    for row in range(7):
        
        # yes, row 1
        if row == 0:
            if st.button("Yes na yes bib 😘", type="primary", use_container_width=True, key="yes_btn"):
                st.session_state.stage = 'success'
                st.rerun()

        # no, in other rows
        elif row == st.session_state.no_pos:
            if st.button("No 🥺😞😭", type="secondary", use_container_width=True, key="no_btn"):
                possible_rows = [i for i in range(1, 7) if i != st.session_state.no_pos]
                st.session_state.no_pos = random.choice(possible_rows)
                st.rerun()

        # rmpty rows
        else:
            st.write("") 
            st.write("")

# stage 3: yipee
elif st.session_state.stage == 'success':
    st.balloons()
    st.markdown('<div class="fade-in-text"><h1>Yipeeeee! Tenchu bib happing ato! 🥰</h1></div>', unsafe_allow_html=True)
    st.image("https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExNXk3N2xsazhjamJtNXc1ZTZkMzdiaHRldmNhcXE1MXNya3A1dGZvcCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/TjSPQgowhhJdHgvnwA/giphy.gif")
    # st.image("https://tenor.com/view/cat-gif-16606050094708454978.gif")