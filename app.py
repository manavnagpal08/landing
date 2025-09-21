import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="ScreenerPro - Landing", layout="wide")

# --- Lottie Helper ---
def lottie_player(url, height=300, width=300):
    components.html(f"""
        <script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
        <lottie-player 
            src="{url}"  
            background="transparent"  
            speed="1"  
            style="width:{width}px; height:{height}px;"  
            loop  
            autoplay>
        </lottie-player>
    """, height=height, width=width)

# --- Hero Section with Animation ---
col1, col2 = st.columns([1,1])

with col1:
    st.markdown("""
        <h1 style="font-size:3rem; font-weight:900; color:white;">
            🚀 Welcome to ScreenerPro
        </h1>
        <p style="font-size:1.2rem; color:#cbd5e1;">
            AI-powered candidate portal for resume screening, certificates, jobs, and collaboration.
        </p>
        <a href="/app" target="_self" 
           style="background:linear-gradient(90deg,#6366f1,#8b5cf6);
                  color:white;padding:15px 30px;border-radius:40px;
                  text-decoration:none;font-weight:700;">
            ✨ Get Started
        </a>
    """, unsafe_allow_html=True)

with col2:
    # 🎬 Show your custom Lottie animation here
    lottie_player("https://lottie.host/b6153b9c-9387-4ff5-ac00-088b39ae59e5/Rp55GIhfnj.lottie", 400, 400)
