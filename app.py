import streamlit as st
from streamlit_lottie import st_lottie
import requests

# ------------------- Helper function to load Lottie -------------------
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# ------------------- Animations (all tested & working) -------------------
lottie_ai = load_lottieurl("https://lottie.host/4d87e1e2-efcb-42c4-a79e-4a2440cd6c50/TU2k1V.json")          # AI / automation
lottie_resume = load_lottieurl("https://lottie.host/5b3130f8-20d7-4f48-8149-b11f06c74064/JSD9dG.json")      # Resume review
lottie_team = load_lottieurl("https://lottie.host/6cf3b54e-7038-43bc-936d-bb7e1aa1a5c5/TLWU2S.json")        # Team collaboration
lottie_certificate = load_lottieurl("https://lottie.host/2bca7b70-7a60-49f4-95b1-c1c80e770c6b/ajQvGI.json") # Certificate
lottie_message = load_lottieurl("https://lottie.host/765fe6a4-8e88-4d79-9b42-5c1b2d882e65/M2Btxv.json")     # Messaging
lottie_jobs = load_lottieurl("https://lottie.host/f244bb8f-3b2b-4c8f-96e7-fd7c19a1b5b3/RzyLQm.json")        # Jobs
lottie_success = load_lottieurl("https://lottie.host/12b5f3e3-3f41-4a3b-b469-36d30556f90d/2tNf2R.json")     # Success / badges

# ------------------- Page Config -------------------
st.set_page_config(page_title="ScreenerPro - Candidate Portal", layout="wide")

# ------------------- CSS Styling -------------------
st.markdown("""
    <style>
        body {
            background: linear-gradient(135deg, #fdf4ff, #eff6ff, #ecfdf5);
        }
        .hero {
            text-align: center;
            padding: 120px 20px 80px 20px;
        }
        .hero h1 {
            font-size: 3.8rem;
            font-weight: 900;
            background: linear-gradient(90deg, #2563eb, #9333ea, #f43f5e);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 25px;
        }
        .hero p {
            font-size: 1.3rem;
            color: #374151;
            margin-bottom: 40px;
        }
        .cta-btn {
            background: linear-gradient(90deg, #2563eb, #9333ea);
            color: white;
            padding: 16px 40px;
            border-radius: 40px;
            font-size: 1.2rem;
            font-weight: 600;
            text-decoration: none;
            box-shadow: 0 6px 20px rgba(124, 58, 237, 0.5);
            transition: all 0.3s ease-in-out;
        }
        .cta-btn:hover {
            transform: translateY(-4px) scale(1.05);
            box-shadow: 0 10px 28px rgba(124, 58, 237, 0.7);
        }
        .feature-card {
            background: white;
            padding: 35px;
            border-radius: 28px;
            box-shadow: 0 10px 28px rgba(0,0,0,0.1);
            text-align: center;
            transition: 0.3s;
        }
        .feature-card:hover {
            transform: translateY(-8px) scale(1.02);
            box-shadow: 0 16px 36px rgba(0,0,0,0.15);
        }
        .feature-card h3 {
            font-size: 1.4rem;
            color: #2563eb;
            margin-top: 15px;
        }
        .wave {
            position: relative;
            margin-top: -80px;
        }
        .footer {
            text-align: center;
            padding: 40px;
            color: gray;
            margin-top: 80px;
            font-size: 0.9rem;
        }
    </style>
""", unsafe_allow_html=True)

# ------------------- Hero Section -------------------
st.markdown("""
<div class="hero">
    <h1>Welcome to ScreenerPro Candidate Portal 🚀</h1>
    <p>Build your career profile, showcase projects, collaborate with teams, and apply to jobs — all in one place.</p>
    <a href="#features" class="cta-btn">✨ Explore Features</a>
</div>
""", unsafe_allow_html=True)

# ------------------- Wave Shape -------------------
st.markdown("""
<div class="wave">
<svg viewBox="0 0 1440 320"><path fill="#fff" fill-opacity="1" 
d="M0,224L48,224C96,224,192,224,288,229.3C384,235,480,245,576,229.3C672,213,768,171,864,165.3C960,160,1056,192,1152,202.7C1248,213,1344,203,1392,197.3L1440,192L1440,320L0,320Z"></path></svg>
</div>
""", unsafe_allow_html=True)

# ------------------- Features Section -------------------
st.markdown("<h2 id='features' style='text-align:center; font-size:2.5rem;'>✨ Portal Highlights</h2>", unsafe_allow_html=True)

# 2 rows of features
row1 = st.columns(3)
with row1[0]:
    st.markdown('<div class="feature-card">', unsafe_allow_html=True)
    st_lottie(lottie_resume, height=140, key="resume")
    st.markdown('<h3>📄 Resume Screening</h3><p>Get instant AI-powered resume feedback & certificates of authenticity.</p></div>', unsafe_allow_html=True)
with row1[1]:
    st.markdown('<div class="feature-card">', unsafe_allow_html=True)
    st_lottie(lottie_certificate, height=140, key="certificate")
    st.markdown('<h3>🏅 Verified Certificates</h3><p>Earn recognition for your skills with auto-generated certificates.</p></div>', unsafe_allow_html=True)
with row1[2]:
    st.markdown('<div class="feature-card">', unsafe_allow_html=True)
    st_lottie(lottie_team, height=140, key="team")
    st.markdown('<h3>👥 Team Collaboration</h3><p>Create or join teams, showcase group projects, and build together.</p></div>', unsafe_allow_html=True)

row2 = st.columns(3)
with row2[0]:
    st.markdown('<div class="feature-card">', unsafe_allow_html=True)
    st_lottie(lottie_jobs, height=140, key="jobs")
    st.markdown('<h3>💼 Apply to Jobs</h3><p>Discover opportunities and apply directly from your candidate profile.</p></div>', unsafe_allow_html=True)
with row2[1]:
    st.markdown('<div class="feature-card">', unsafe_allow_html=True)
    st_lottie(lottie_message, height=140, key="messages")
    st.markdown('<h3>💬 Smart Messaging</h3><p>Collaborate with recruiters and teammates with built-in chat.</p></div>', unsafe_allow_html=True)
with row2[2]:
    st.markdown('<div class="feature-card">', unsafe_allow_html=True)
    st_lottie(lottie_success, height=140, key="success")
    st.markdown('<h3>🌟 Earn Badges</h3><p>Unlock achievements as you grow your skills & career journey.</p></div>', unsafe_allow_html=True)

# ------------------- CTA Section -------------------
st.markdown("""
<div id="start" style="text-align:center; margin:100px 0;">
    <h2 style="font-size:2.5rem; font-weight:800; background: linear-gradient(90deg, #2563eb, #9333ea); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
        Ready to Build Your Future?
    </h2>
    <p style="color:#4b5563;">Join thousands of candidates showcasing their talent on ScreenerPro.</p>
    <a href="#" class="cta-btn">🚀 Create Your Profile</a>
</div>
""", unsafe_allow_html=True)

# ------------------- Footer -------------------
st.markdown('<div class="footer">© 2025 ScreenerPro. All rights reserved. | Built with ❤️ on Streamlit</div>', unsafe_allow_html=True)
