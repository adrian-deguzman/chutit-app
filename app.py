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
    # typewriter("This is bb adrian! 🐷", speed=0.1)
    # typewriter("Happy happy valentines bib...", speed=0.1)
    # typewriter("Thank you sa 3 bb valentines together", speed=0.1)
    typewriter("Ready? 👀", speed=0.1)

    time.sleep(1)

    st.session_state.stage = 'question'
    st.rerun()

# stage 2: question
elif st.session_state.stage == 'question':
    
    if not st.session_state.buttons_revealed:
        st.markdown('<div class="fade-in-text"><h1>Will you be my bb valentine? 🌹</h1></div>', unsafe_allow_html=True)
        time.sleep(2.5) 
        st.session_state.buttons_revealed = True
    else:
        st.markdown('<h1>Will you be my bb valentine? 🌹</h1>', unsafe_allow_html=True)
        
        # disable animation
        st.markdown("""
            <style>
            .stButton button {
                animation: none !important;
                transition: none !important;
            }
            </style>
        """, unsafe_allow_html=True)

    st.write("##")

    slot_counter = 0
    for row in range(5):
        c1, c2, c3 = st.columns([1, 1, 1])
        cols = [c1, c2, c3]

        for col_idx in range(3):
            current_col = cols[col_idx]
            with current_col:
                # Yes
                if slot_counter == 7:
                    if st.button("Yes na yes bib 😘", type="primary", use_container_width=True, key="yes_btn"):
                        st.session_state.stage = 'success'
                        st.rerun()

                # No
                elif slot_counter == st.session_state.no_pos:
                    if st.button("No 🥺😞😭", type="secondary", use_container_width=True, key="no_btn"):
                        if st.session_state.no_pos > 7:
                            possible_slots = [0, 1, 2, 3, 4, 5, 6]
                        else:
                            possible_slots = [8, 9, 10, 11, 12, 13, 14]
                            
                        st.session_state.no_pos = random.choice(possible_slots)
                        st.rerun()
                
                else:
                    st.write("") 
            
            slot_counter += 1

# stage 3: yipee
elif st.session_state.stage == 'success':
    st.balloons()
    st.markdown('<div class="fade-in-text"><h1>Yipeeeee! Tenchu bib happing ato! 🥰</h1></div>', unsafe_allow_html=True)
    st.image("https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExNXk3N2xsazhjamJtNXc1ZTZkMzdiaHRldmNhcXE1MXNya3A1dGZvcCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/TjSPQgowhhJdHgvnwA/giphy.gif")
    # st.image("https://tenor.com/view/cat-gif-16606050094708454978.gif")