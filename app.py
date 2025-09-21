import streamlit as st
import streamlit.components.v1 as components
import sys
import importlib
import runpy
from io import BytesIO
import requests
from datetime import datetime

# IMPORTANT: Replace "YOUR_FORMSPREE_FORM_ID" with your actual Formspree form ID.
# You can get this by creating a new form on Formspree.io.
FORMSPREE_ENDPOINT = "https://formspree.io/f/mwpqevno"

# ---------- Initialize Session State ----------
# This state variable controls which page to display.
if 'show_app' not in st.session_state:
    st.session_state.show_app = False
if 'show_enquiry_form' not in st.session_state:
    st.session_state.show_enquiry_form = False
if 'dark_mode_main' not in st.session_state:
    st.session_state.dark_mode_main = True

# Function to handle the button click and change the state
def goto_app():
    st.session_state.show_app = True
    st.session_state.show_enquiry_form = False

def goto_enquiry():
    st.session_state.show_enquiry_form = True

def goto_landing():
    st.session_state.show_enquiry_form = False
    st.session_state.show_app = False

# ---------- Helper: Lottie Player ----------
def lottie_player(url, height=200, width=200):
    return components.html(f"""
        <div class="lottie-container">
            <lottie-player src="{url}" background="transparent" speed="1"
            style="width:{width}px; height:{height}px;" loop autoplay></lottie-player>
        </div>
        <script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
    """, height=height + 20, width=width)

# Function to read and return the PDF file
def get_pdf_bytes(file_path):
    try:
        with open(file_path, "rb") as f:
            pdf_bytes = f.read()
        return BytesIO(pdf_bytes)
    except FileNotFoundError:
        st.error("Error: 'screener_pro.pdf' not found. Please ensure the file is in the same folder as this script.")
        return None

def landing_page():
    # Hide the Streamlit header and footer with CSS
    st.markdown("""
        <style>
            [data-testid="stHeader"] {
                visibility: hidden;
            }
            [data-testid="stToolbar"] {
                visibility: hidden;
            }
            #MainMenu {
                visibility: hidden;
            }
        </style>
    """, unsafe_allow_html=True)
    
    # Main container for the app
    st.set_page_config(page_title="ScreenerPro - Partner Portal", layout="wide")

    # ---------- Navigation Links ----------
    col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1])
    
    with col1:
        st.markdown('<a href="https://screenerpro.streamlit.app/" target="_blank" class="nav-btn">ScreenerPro Portal</a>', unsafe_allow_html=True)
    
    with col2:
        st.button("Go to Candidate Portal", help="Enter the ScreenerPro portal", on_click=goto_app)
    
    with col3:
        st.button("Enquiry Form", on_click=goto_enquiry)

    # New download button at the top
    with col4:
        pdf_bytes = get_pdf_bytes("screener_pro.pdf")
        if pdf_bytes:
            st.download_button(
                label="Download Proposal",
                data=pdf_bytes,
                file_name="screener_pro.pdf",
                mime="application/pdf",
                help="Click to download the ScreenerPro proposal PDF."
            )

    with col5:
        # Updated LinkedIn link
        st.markdown('<a href="https://www.linkedin.com/company/screener-pro/" target="_blank" class="nav-btn"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="currentColor"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.763s.784-1.763 1.75-1.763 1.75.79 1.75 1.763-.783 1.763-1.75 1.763zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg></a>', unsafe_allow_html=True)

    # ---------- Logo + Hello Animation Section ----------
    components.html("""
    <div style="
        display:flex;
        justify-content:center;
        align-items:center;
        gap:40px;
        margin-top:40px;
        margin-bottom:40px;
    ">
        <!-- Logo with rounded corners -->
        <img src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhhq_OCSv-QmuBjXeRQXr60EfsvVA4chRPCNslo3NhjVQkoKjUtiRfTPpGoQjyQXS7sMsJifQC6Yq34cAhNbq9lMwBXZqIIbCij1adyXSuNoyxuzOTDfrPU2dnna0baimldd7Y1KCkvaAfrWC1yLGxp25SJ9s4exJ-JAc8kNcTyUSgkLWbW2DdvhpWH4GlO/s320/logo.png"
            alt="ScreenerPro Logo"
            style="height:90px; border-radius:20px; box-shadow:0 4px 15px rgba(0,0,0,0.5);">

        <!-- Animation directly beside logo -->
        <lottie-player src="https://raw.githubusercontent.com/manavnagpal08/landing/refs/heads/main/y5AhpJLGt6.json"
            background="transparent" speed="1"
            style="width:120px; height:120px;" loop autoplay>
        </lottie-player>
    </div>

    <!-- Lottie script -->
    <script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
    """, height=180)

    # ---------- Custom Fonts and Styling (Futuristic Dark Theme) ----------
    st.markdown("""
        <style>
            @import url('https://fonts.com/css2?family=Poppins:wght@400;600;700;800;900&display=swap');
            @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&display=swap');

            /* General page layout and deep space background */
            html, body {
                font-family: 'Inter', sans-serif;
                background: #070e17;
                margin: 0;
                padding: 0;
                color: #ffffff;
                overflow-x: hidden;
            }

            /* Streamlit main content container */
            .st-emotion-cache-1cypq83, .stApp {
                background-color: #070e17;
                color: #ffffff;
            }

            /* Animated background grid */
            body::before {
                content: '';
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background-image:
                    linear-gradient(rgba(255, 255, 255, 0.05) 1px, transparent 1px),
                    linear-gradient(90deg, rgba(255, 255, 255, 0.05) 1px, transparent 1px);
                background-size: 50px 50px;
                z-index: -1;
                opacity: 0.2;
                animation: moveGrid 60s linear infinite;
            }

            @keyframes moveGrid {
                from { background-position: 0 0; }
                to { background-position: 500px 500px; }
            }

            /* Glowing effect keyframes */
            @keyframes glow {
                0% { box-shadow: 0 0 5px rgba(99, 102, 241, 0.6), 0 0 10px rgba(139, 92, 246, 0.6); }
                50% { box-shadow: 0 0 20px rgba(99, 102, 241, 0.8), 0 0 25px rgba(139, 92, 246, 0.8); }
                100% { box-shadow: 0 0 5px rgba(99, 102, 241, 0.6), 0 0 10px rgba(139, 92, 246, 0.6); }
            }

            /* Navigation buttons at the top */
            .nav-btn {
                background: #0e1627;
                color: white;
                padding: 10px 20px;
                border-radius: 9999px;
                font-size: 0.9rem;
                font-weight: 600;
                text-decoration: none;
                box-shadow: 0 4px 15px rgba(0,0,0,0.3);
                transition: transform 0.3s ease, box-shadow 0.3s ease;
                border: 1px solid rgba(255,255,255,0.1);
                display: inline-flex;
                align-items: center;
                justify-content: center;
                gap: 8px;
                width: 100%;
            }
            .nav-btn:hover {
                transform: translateY(-3px);
                box-shadow: 0 6px 20px rgba(0,0,0,0.4);
            }
            .nav-btn svg {
                fill: currentColor;
            }
            
            /* Custom styling for the Streamlit button to match the others */
            div[data-testid="stColumn"] button {
                width: 100%;
                background: #0e1627 !important;
                color: white !important;
                padding: 10px 20px !important;
                border-radius: 9999px !important;
                font-size: 0.9rem !important;
                font-weight: 600 !important;
                box-shadow: 0 4px 15px rgba(0,0,0,0.3) !important;
                border: 1px solid rgba(255,255,255,0.1) !important;
                transition: transform 0.3s ease, box-shadow 0.3s ease !important;
            }
            div[data-testid="stColumn"] button:hover {
                transform: translateY(-3px) !important;
                box-shadow: 0 6px 20px rgba(0,0,0,0.4) !important;
            }

            /* Hero section - a smoother, more elegant gradient */
            .hero {
                text-align: center;
                padding: 7rem 1.5rem 5rem 1.5rem;
                background: linear-gradient(135deg, #1f2937, #070e17);
                color: white;
                border-bottom-left-radius: 50% 5%;
                border-bottom-right-radius: 50% 5%;
                box-shadow: 0 10px 40px rgba(0,0,0,0.5);
            }
            .hero h1 {
                font-family: 'Poppins', sans-serif;
                font-size: clamp(2.5rem, 5vw, 4.5rem);
                font-weight: 800;
                margin-bottom: 1.25rem;
                background: linear-gradient(90deg, #c7d2fe, #a5b4fc, #818cf8);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            }
            .hero p {
                font-size: clamp(1rem, 2vw, 1.25rem);
                max-width: 45rem;
                margin: auto;
                opacity: 0.8;
                color: #ffffff;
            }
            .cta-btn {
                display: inline-block;
                margin-top: 2rem;
                background: linear-gradient(90deg, #6366f1, #8b5cf6);
                color: white;
                padding: 1rem 2.5rem;
                border-radius: 9999px;
                font-size: 1.1rem;
                font-weight: 700;
                text-decoration: none;
                box-shadow: 0 5px 25px rgba(99, 102, 241, 0.4);
                transition: all 0.3s ease-in-out;
                border: 1px solid rgba(255,255,255,0.2);
            }
            .cta-btn:hover {
                transform: translateY(-0.25rem);
                box-shadow: 0 10px 35px rgba(99, 102, 241, 0.6);
                animation: glow 1.5s infinite ease-in-out;
            }

            /* Section Titles - with a subtle glowing gradient */
            .section-title {
                font-family: 'Poppins', sans-serif;
                font-size: clamp(2rem, 4vw, 3rem);
                font-weight: 800;
                text-align: center;
                margin: 6rem 0 3rem 0;
                color: #ffffff;
                text-shadow: 0 0 10px rgba(255,255,255,0.1);
            }
            .section-title::after {
                content: '';
                display: block;
                width: 80px;
                height: 4px;
                background: linear-gradient(90deg, #6366f1, #ec4899);
                margin: 1rem auto 0;
                border-radius: 2px;
            }
            
            /* About Section */
            .about-container {
                max-width: 900px;
                margin: 3rem auto;
                padding: 2.5rem;
                background: #0e1627;
                border-radius: 1.5rem;
                box-shadow: 0 8px 30px rgba(0,0,0,0.3);
                border: 1px solid rgba(255,255,255,0.08);
            }
            .about-container p {
                font-size: 1.1rem;
                line-height: 1.8;
                margin-bottom: 1.5rem;
            }
            .about-container h3 {
                font-family: 'Poppins', sans-serif;
                font-weight: 700;
                margin-bottom: 1rem;
                color: #ffffff;
                text-transform: uppercase;
                letter-spacing: 1px;
            }
            .about-container ul {
                list-style: none;
                padding: 0;
                margin: 0;
            }
            .about-container li {
                background: rgba(255, 255, 255, 0.05);
                margin-bottom: 0.75rem;
                padding: 1.25rem;
                border-radius: 0.75rem;
                border-left: 3px solid #6366f1;
                font-size: 1rem;
                line-height: 1.6;
                transition: background-color 0.3s ease;
            }
            .about-container li:hover {
                background: rgba(255, 255, 255, 0.1);
            }
            .about-container li b {
                color: #c7d2fe;
            }

            /* Feature Cards - with a lift-on-hover effect */
            .feature-card {
                background: #0e1627;
                padding: 2rem;
                border-radius: 1.5rem;
                box-shadow: 0 8px 30px rgba(0,0,0,0.3);
                text-align: center;
                transition: transform 0.4s ease, box-shadow 0.4s ease;
                height: 100%;
                display: flex;
                flex-direction: column;
                justify-content: flex-start;
                align-items: center;
                border: 1px solid rgba(255,255,255,0.08);
            }
            .feature-card:hover {
                transform: translateY(-0.75rem);
                box-shadow: 0 16px 50px rgba(0,0,0,0.5), 0 0 20px rgba(99, 102, 241, 0.2);
                border: 1px solid rgba(99, 102, 241, 0.6);
            }
            .feature-card h3 {
                margin-top: 1rem;
                font-size: 1.3rem;
                font-weight: 700;
                color: #ffffff;
            }
            .feature-card p {
                font-size: 0.95rem;
                color: #ffffff;
                flex-grow: 1;
            }

            .lottie-container {
                width: 100%;
                height: 120px;
                display: flex;
                justify-content: center;
                align-items: center;
            }

            /* Final CTA section */
            .final-cta {
                text-align: center;
                margin: 8rem 0;
            }
            .final-cta h2 {
                font-size: clamp(2rem, 4vw, 3rem);
                font-weight: 800;
                color: #ffffff;
            }
            .final-cta p {
                color: #ffffff;
                margin-bottom: 2rem;
            }

            /* Footer */
            .footer {
                text-align: center;
                padding: 2rem;
                color: #ffffff;
                margin-top: 5rem;
                font-size: 0.875rem;
                border-top: 1px solid #1e293b;
            }

            /* Custom Streamlit components styling */
            .stProgress > div > div > div > div {
                background-color: #ec4899;
            }
            .st-emotion-cache-1lcbm5h { /* Sidebar background */
                background-color: #0d141f;
            }
            .st-emotion-cache-16txtv8 { /* Sidebar links */
                color: #ffffff;
            }
            /* Styling for the enquiry form */
            .form-container {
                max-width: 600px;
                margin: auto;
                padding: 2rem;
                background: #0e1627;
                border-radius: 1.5rem;
                box-shadow: 0 8px 30px rgba(0,0,0,0.3);
                border: 1px solid rgba(255,255,255,0.08);
            }
            .form-title {
                text-align: center;
                font-size: 2rem;
                font-weight: 700;
                margin-bottom: 2rem;
                color: #ffffff;
            }
        </style>
    """, unsafe_allow_html=True)


    # ---------- Hero ----------
    st.markdown("""
    <div class="hero">
        <h1>🚀 ScreenerPro Partner Portal</h1>
        <p>Showcase your skills, collaborate with teams, earn badges, and apply to jobs — all in one modern career hub.</p>
        <a href="#features" class="cta-btn">✨ Get Started</a>
    </div>
    """, unsafe_allow_html=True)

    # --- New ScreenerPro About Section ---
    st.markdown("---")
    st.markdown('<div id="about-us"></div>', unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">✨ About ScreenerPro</h2>', unsafe_allow_html=True)
    st.markdown("""
    <div class="about-container">
        <p>ScreenerPro is an AI-powered platform designed to revolutionize your recruitment process. Leveraging advanced <b>Natural Language Processing (NLP)</b> and <b>Machine Learning (ML)</b> models, ScreenerPro efficiently screens resumes against job descriptions, providing instant, accurate, and unbiased candidate assessments.</p>
        <h3>Key Features:</h3>
        <ul>
            <li><b>Intelligent Resume Screening:</b> Automatically match resumes to job descriptions with AI-powered scoring.</li>
            <li><b>Detailed Candidate Analytics:</b> Gain deep insights into skills, experience, qualifications, and overall fit through comprehensive reports.</li>
            <li><b>Customizable Screening Criteria:</b> Tailor screening parameters such as minimum score, experience range, and CGPA to precisely match your hiring needs.</li>
            <li><b>Job Campaign Management:</b> Create, track, and manage all your job openings from a centralized dashboard, including applicant counts and average match scores.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("---")


    # ---------- Features ----------
    st.markdown('<div id="features"></div>', unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">🌟 All-in-One Features</h2>', unsafe_allow_html=True)

    cols = st.columns(4)
    with cols[0]:
        st.markdown('<div class="feature-card">', unsafe_allow_html=True)
        lottie_player("https://assets2.lottiefiles.com/packages/lf20_tno6cg2w.json", 120, 120)
        st.markdown('<h3>📄 Resume Screening</h3><p>AI-powered resume checks with instant feedback.</p></div>', unsafe_allow_html=True)

    with cols[1]:
        st.markdown('<div class="feature-card">', unsafe_allow_html=True)
        lottie_player("https://raw.githubusercontent.com/manavnagpal08/landing/refs/heads/main/CERTIFIACTE.json", 120, 120)
        st.markdown('<h3>🎓 Certificates</h3><p>Generate and share verified resume certificates.</p></div>', unsafe_allow_html=True)

    with cols[2]:
        st.markdown('<div class="feature-card">', unsafe_allow_html=True)
        lottie_player("https://assets1.lottiefiles.com/packages/lf20_jcikwtux.json", 120, 120)
        st.markdown('<h3>🔍 Talent Finder</h3><p>Find collaborators and discover career matches.</p></div>', unsafe_allow_html=True)

    with cols[3]:
        st.markdown('<div class="feature-card">', unsafe_allow_html=True)
        lottie_player("https://raw.githubusercontent.com/manavnagpal08/landing/refs/heads/main/Collaboration%20(3).json", 120, 120)
        st.markdown('<h3>🤝 Collaboration</h3><p>Chat, connect, and collaborate with peers.</p></div>', unsafe_allow_html=True)


    # ---------- Profile + Teams ----------
    st.markdown('<div id="profile"></div>', unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">👤 Your Profile</h2>', unsafe_allow_html=True)
    pcols = st.columns(3)
    with pcols[0]:
        st.markdown('<div class="feature-card">', unsafe_allow_html=True)
        lottie_player("https://raw.githubusercontent.com/manavnagpal08/landing/refs/heads/main/Profile%20user%20card.json", 140, 140)
        st.markdown('<h3>🌐 Profile</h3><p>Showcase your skills and personal brand.</p></div>', unsafe_allow_html=True)

    with pcols[1]:
        st.markdown('<div class="feature-card">', unsafe_allow_html=True)
        lottie_player("https://assets6.lottiefiles.com/packages/lf20_ktwnwv5m.json", 140, 140)
        st.markdown('<h3>🚀 Projects</h3><p>Highlight your best work and achievements.</p></div>', unsafe_allow_html=True)

    with pcols[2]:
        st.markdown('<div id="teams" class="feature-card">', unsafe_allow_html=True)
        lottie_player("https://raw.githubusercontent.com/manavnagpal08/landing/refs/heads/main/TEAMS.json", 140, 140)
        st.markdown('<h3>👥 Teams</h3><p>Create and join teams to collaborate efficiently.</p></div>', unsafe_allow_html=True)

    # ---------- Badges & Jobs ----------
    st.markdown('<div id="jobs"></div>', unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">🏆 Achievements & Jobs</h2>', unsafe_allow_html=True)
    ecols = st.columns(2)
    with ecols[0]:
        st.markdown('<div class="feature-card">', unsafe_allow_html=True)
        lottie_player("https://raw.githubusercontent.com/manavnagpal08/landing/refs/heads/main/Medal%20badge.json", 140, 140)
        st.markdown('<h3>🏅 Badges</h3><p>Earn recognition & climb the leaderboard.</p></div>', unsafe_allow_html=True)

    with ecols[1]:
        st.markdown('<div class="feature-card">', unsafe_allow_html=True)
        lottie_player("https://raw.githubusercontent.com/manavnagpal08/landing/refs/heads/main/Share.json", 140, 140)
        st.markdown('<h3>💼 Apply to Jobs</h3><p>One-click applications for top opportunities.</p></div>', unsafe_allow_html=True)

    st.markdown("""
        <div class="final-cta">
            <h2>Ready to Supercharge Your Career?</h2>
            <p>Join thousands already growing with ScreenerPro.</p>
        </div>
        """, unsafe_allow_html=True)

    # Using columns to center the main Join Now button on the page
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.button("🚀 Join Now", help="Enter the ScreenerPro portal", on_click=goto_app)

    st.markdown('<div class="footer">© 2025 ScreenerPro Partner Portal. All rights reserved.</div>', unsafe_allow_html=True)

def enquiry_form_page():
    """
    Defines the Streamlit page for partnering with ScreenerPro,
    including a form that submits data to Formspree.
    """
    # Hide the Streamlit header and footer with CSS
    st.markdown("""
        <style>
            [data-testid="stHeader"] {
                visibility: hidden;
            }
            [data-testid="stToolbar"] {
                visibility: hidden;
            }
            #MainMenu {
                visibility: hidden;
            }
        </style>
    """, unsafe_allow_html=True)
    # Access dark_mode from session state, defaulting to False if not set
    dark_mode = st.session_state.get('dark_mode_main', False)

    # Define colors based on dark mode
    text_color_main = '#f0f2f6' if dark_mode else '#333333'
    text_color_light = '#BBBBBB' if dark_mode else '#555555'
    text_color_footer = '#aaa' if dark_mode else '#777' # Slightly darker for footer in light mode

    # Add a back button at the top
    if st.button("← Back to Landing Page"):
        goto_landing()

    # Inject highly specific CSS to fix selectbox dropdown options visibility.
    # This is done here as a workaround since external style.css changes were not effective
    # and the user explicitly asked to modify partner.py only.
    st.markdown(f"""
        <style>
        /* Ensure the main popover background is correct */
        div[data-baseweb="popover"] > div[data-baseweb="menu"] {{
            background-color: {'#3A3A3A' if dark_mode else 'var(--background-color)'} !important;
            border: 1px solid {'rgba(255, 255, 255, 0.15)' if dark_mode else 'rgba(0, 0, 0, 0.15)'} !important;
            border-radius: 12px !important;
            box-shadow: 0 8px 20px {'rgba(0, 0, 0, 0.4)' if dark_mode else 'rgba(0, 0, 0, 0.15)'} !important;
        }}

        /* Target the text within the options with high specificity */
        div[data-baseweb="popover"] div[role="listbox"] div[role="option"] * {{
            color: {'#f0f2f6' if dark_mode else 'var(--text-color)'} !important;
        }}

        /* Ensure individual option background is transparent or set correctly */
        div[data-baseweb="popover"] div[role="listbox"] div[role="option"] {{
            background-color: transparent !important; /* Allow the listbox background to show */
            padding: 0.75rem 1.2rem !important; /* Adjust padding for better look */
        }}

        /* Hover state for options */
        div[data-baseweb="popover"] div[role="listbox"] div[role="option"]:hover {{
            background-color: {'rgba(0, 206, 201, 0.3)' if dark_mode else 'rgba(0, 206, 201, 0.2)'} !important; /* Teal hover effect */
        }}

        /* Also target the `p` tag specifically if Streamlit wraps text in it */
        div[data-baseweb="popover"] div[role="listbox"] div[role="option"] p {{
            color: {'#f0f2f6' if dark_mode else 'var(--text-color)'} !important;
        }}
        </style>
    """, unsafe_allow_html=True)


    st.title("📣 Partner With Us")
    st.markdown("---")

    st.markdown(
        f"""
        <p style="font-size: 1.2em; line-height: 1.6; color: {text_color_main};">
        ScreenerPro is committed to revolutionizing recruitment through AI. We invite
        colleges, startups, HR consultancies, and technology providers to join us
        in building a more efficient and equitable hiring ecosystem.
        </p>
        """,
        unsafe_allow_html=True
    )

    st.markdown("## 🤝 Why Partner with ScreenerPro?")

    st.markdown(
        f"""
        <ul style="list-style-type: none; padding-left: 0;">
            <li style="margin-bottom: 15px;">
                <h3 style="color: #00cec9; margin-bottom: 5px;">🚀 Use ScreenerPro API</h3>
                <p style="color: {text_color_light};">Integrate our powerful resume screening and analysis capabilities directly into your existing platforms, HRIS, or applicant tracking systems (ATS). Streamline your workflow and enhance your services with our robust API.</p>
            </li>
            <li style="margin-bottom: 15px;">
                <h3 style="color: #00cec9; margin-bottom: 5px;">🏅 Offer Certifications to Your Candidates</h3>
                <p style="color: {text_color_light};">Enhance the value proposition for your candidates. Partner with us to offer ScreenerPro-powered certifications, validating their skills and increasing their employability. This can be a significant differentiator for colleges and training institutes.</p>
            </li>
            <li style="margin-bottom: 15px;">
                <h3 style="color: #00cec9; margin-bottom: 5px;">🌐 Join as Strategic Partners</h3>
                <p style="color: {text_color_light};">Collaborate on joint ventures, co-marketing initiatives, or explore affiliate opportunities. We are open to innovative partnerships that expand our reach and deliver mutual value to the HR tech landscape.</p>
            </li>
        </ul>
        """,
        unsafe_allow_html=True
    )

    st.markdown("## ✨ Benefits of Partnership")
    st.markdown(
        f"""
        <ul style="list-style-type: none; padding-left: 0;">
            <li style="margin-bottom: 15px;">
                <h3 style="color: #00cec9; margin-bottom: 5px;">📈 Enhance Efficiency</h3>
                <p style="color: {text_color_light};">Automate initial resume screening, reducing manual effort and allowing your team to focus on high-value tasks like candidate engagement and strategic planning.</p>
            </li>
            <li style="margin-bottom: 15px;">
                <h3 style="color: #00cec9; margin-bottom: 5px;">💡 Improve Candidate Quality</h3>
                <p style="color: {text_color_light};">Leverage AI to identify the best-fit candidates based on objective criteria, leading to a higher quality talent pool and better hiring outcomes.</p>
            </li>
            <li style="margin-bottom: 15px;">
                <h3 style="color: #00cec9; margin-bottom: 5px;">🛡️ Ensure Fairness & Reduce Bias</h3>
                <p style="color: {text_color_light};">Our AI-powered screening helps in minimizing unconscious bias in the initial stages of recruitment, promoting a more equitable hiring process.</p>
            </li>
            <li style="margin-bottom: 15px;">
                <h3 style="color: #00cec9; margin-bottom: 5px;">🚀 Drive Innovation</h3>
                <p style="color: {text_color_light};">Position your organization at the forefront of HR technology by integrating cutting-edge AI solutions into your services or offerings.</p>
            </li>
        </ul>
        """,
        unsafe_allow_html=True
    )

    st.markdown("## 📝 Our Partnership Process")
    st.markdown(
        f"""
        <ol style="padding-left: 20px; color: {text_color_light};">
            <li style="margin-bottom: 10px;">
                <strong>Initial Inquiry:</strong> Fill out the form below or email us to express your interest.
            </li>
            <li style="margin-bottom: 10px;">
                <strong>Discovery Call:</strong> We'll schedule a call to understand your needs and explore potential synergies.
            </li>
            <li style="margin-bottom: 10px;">
                <strong>Proposal & Agreement:</strong> Based on our discussion, we'll draft a tailored partnership proposal.
            </li>
            <li style="margin-bottom: 10px;">
                <strong>Integration & Launch:</strong> Our teams will work together to integrate ScreenerPro's capabilities or launch our joint initiatives.
            </li>
            <li style="margin-bottom: 10px;">
                <strong>Ongoing Support:</strong> We provide continuous support to ensure a successful and lasting partnership.
            </li>
        </ol>
        """,
        unsafe_allow_html=True
    )

    st.markdown("## 📞 Get in Touch")
    st.markdown(
        f"""
        <p style="font-size: 1.1em; color: {text_color_main};">
        Ready to explore a partnership? We'd love to hear from you!
        </p>
        <p style="font-size: 1.1em; color: {text_color_main};">
        Please reach out to us at <a href="mailto:screenerpro.ai@gmail.com" style="color: #00cec9; text-decoration: none;">screenerpro.ai@gmail.com</a>
        or fill out the form below, and our partnership team will get back to you shortly.
        </p>
        """,
        unsafe_allow_html=True
    )

    with st.form("partner_form"):
        st.subheader("Partnership Inquiry Form")
        partner_type = st.selectbox(
            "I am a:",
            ["College/University", "Startup", "HR Consultancy", "Technology Provider", "Other"]
        )
        organization_name = st.text_input("Organization Name", placeholder="e.g., Tech University, Innovate Solutions Inc.")
        contact_person = st.text_input("Contact Person Name", placeholder="e.g., Jane Doe")
        contact_email = st.text_input("Contact Email", placeholder="e.g., jane.doe@example.com")
        partnership_interest = st.text_area("Tell us about your partnership interest", height=150, placeholder="Describe how you envision collaborating with ScreenerPro...")
        
        submitted = st.form_submit_button("Submit Inquiry")
        if submitted:
            submission_data = {
                "Partner Type": partner_type,
                "Organization Name": organization_name,
                "Contact Person": contact_person,
                "Contact Email": contact_email,
                "Partnership Interest": partnership_interest,
                "Submission Timestamp": datetime.now().isoformat() # ISO format for easy parsing
            }

            try:
                # Send data to Formspree
                response = requests.post(FORMSPREE_ENDPOINT, data=submission_data)
                
                if response.status_code == 200:
                    st.success("Thank you for your inquiry! We have received your message and will get back to you shortly.")
                else:
                    st.error(f"Failed to submit inquiry. Status code: {response.status_code}. Please try again.")
            except requests.exceptions.RequestException as e:
                st.error(f"Network error or connection issue: {e}. Please check your internet connection or Formspree endpoint.")
            except Exception as e:
                st.error(f"An unexpected error occurred during submission: {e}.")

    st.markdown("---")
    st.markdown(
        f"""
        <p style="font-size: 0.9em; color: {text_color_footer};">
        ScreenerPro is a product of FLIP & CLIP. All rights reserved.
        </p>
        """,
        unsafe_allow_html=True
    )

# Main app logic
if st.session_state.show_enquiry_form:
    enquiry_form_page()
elif not st.session_state.show_app:
    landing_page()
else:
    
    try:
        sys.path.insert(0, "./")
        mod = importlib.import_module("pages.app")
        if hasattr(mod, "main") and callable(mod.main):
            mod.main()
        else:

            st.success("Portal loaded!")
    except Exception as ie:
        
        try:
            st.error(f"Import failed - fallback to runpy.run_path. Import error: {str(ie)}")
            mod = None
            ie_msg = str(ie)
            st.success("Portal loaded via fallback!")
            runpy.run_path("pages/app.py")
        except Exception as e:
            st.error(f"Failed to load app.py: {e}")
