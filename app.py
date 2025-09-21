import streamlit as st

# ---------------------- PAGE CONFIG ----------------------
st.set_page_config(
    page_title="ScreenerPro",
    page_icon="✨",
    layout="wide"
)

# ---------------------- CUSTOM STYLES ----------------------
st.markdown("""
<style>
/* Background gradient */
.stApp {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    color: #f3f4f6;
}

/* Headings */
h1, h2, h3 {
    font-family: 'Segoe UI', sans-serif;
    font-weight: 700;
    color: #ffffff;
    text-align: center;
}

/* Sub text */
p {
    font-size: 16px;
    color: #d1d5db;
    line-height: 1.6;
}

/* Glassmorphism cards */
.feature-card {
    background: rgba(255, 255, 255, 0.08);
    border-radius: 18px;
    padding: 25px;
    text-align: center;
    backdrop-filter: blur(12px);
    box-shadow: 0 8px 25px rgba(0,0,0,0.2);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}
.feature-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 32px rgba(0,0,0,0.3);
}

/* Buttons */
.stButton>button {
    background: linear-gradient(90deg, #6366f1, #8b5cf6);
    color: white;
    font-weight: 600;
    padding: 10px 22px;
    border-radius: 12px;
    border: none;
    transition: all 0.3s ease;
}
.stButton>button:hover {
    background: linear-gradient(90deg, #4f46e5, #7c3aed);
    box-shadow: 0 4px 15px rgba(99,102,241,0.5);
    transform: scale(1.05);
}

/* Center elements */
.center {
    text-align: center;
    margin-top: 20px;
}
</style>
""", unsafe_allow_html=True)

# ---------------------- HERO SECTION ----------------------
st.markdown("<h1>🚀 Welcome to ScreenerPro</h1>", unsafe_allow_html=True)
st.markdown("<p class='center'>AI-powered Candidate Portal – Resumes, Certificates, Collaboration, and More.</p>", unsafe_allow_html=True)
st.markdown("<div class='center'>", unsafe_allow_html=True)
st.button("Get Started")
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")

# ---------------------- FEATURE GRID ----------------------
st.markdown("<h2>✨ Features for Candidates</h2>", unsafe_allow_html=True)
row1 = st.columns(3)

with row1[0]:
    st.markdown('<div class="feature-card">📄<h3>Resume Screening</h3><p>AI-powered resume screening against job descriptions in seconds.</p></div>', unsafe_allow_html=True)

with row1[1]:
    st.markdown('<div class="feature-card">🏅<h3>Certificates</h3><p>Generate and showcase verified certificates for your resumes.</p></div>', unsafe_allow_html=True)

with row1[2]:
    st.markdown('<div class="feature-card">🎯<h3>Talent Finder</h3><p>Find jobs that perfectly match your skills with our smart talent engine.</p></div>', unsafe_allow_html=True)

row2 = st.columns(3)

with row2[0]:
    st.markdown('<div class="feature-card">👥<h3>Collaboration</h3><p>Create or join teams, share projects, and build together.</p></div>', unsafe_allow_html=True)

with row2[1]:
    st.markdown('<div class="feature-card">👤<h3>Profile</h3><p>Showcase your projects, achievements, and earn profile badges.</p></div>', unsafe_allow_html=True)

with row2[2]:
    st.markdown('<div class="feature-card">💬<h3>Messaging</h3><p>Chat with team members, recruiters, and collaborate in real-time.</p></div>', unsafe_allow_html=True)

st.markdown("---")

# ---------------------- CTA ----------------------
st.markdown("<h2>🌟 Build Your Future with ScreenerPro</h2>", unsafe_allow_html=True)
st.markdown("<p class='center'>Start today and unlock the power of AI in your career journey.</p>", unsafe_allow_html=True)
st.markdown("<div class='center'>", unsafe_allow_html=True)
st.button("Sign Up Now")
st.markdown("</div>", unsafe_allow_html=True)
