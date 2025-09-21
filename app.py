import streamlit as st

st.set_page_config(page_title="Candidate Portal - ScreenerPro", layout="wide")

# Hero Section
st.markdown("""
<div style="text-align:center; padding:100px 20px; background:linear-gradient(135deg,#2563eb,#9333ea,#f43f5e); border-radius:0 0 50px 50px; color:white;">
    <h1 style="font-size:3.5rem; font-weight:900;">Your Career, Powered by AI 🚀</h1>
    <p style="font-size:1.3rem; max-width:800px; margin:auto;">
        Build your profile, showcase projects, get resume certificates, apply for jobs, 
        collaborate with peers, and grow your career — all in one smart platform.
    </p>
    <br>
    <a href="#" style="background:#fff; color:#2563eb; padding:15px 40px; border-radius:40px; font-weight:700; text-decoration:none; margin-right:15px;">✨ Create Profile</a>
    <a href="#" style="background:transparent; border:2px solid white; color:white; padding:15px 40px; border-radius:40px; font-weight:700; text-decoration:none;">🔍 Explore Jobs</a>
</div>
""", unsafe_allow_html=True)

# Features Section
st.markdown("<h2 style='text-align:center; margin:60px 0 30px;'>🌟 Platform Features</h2>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""<div style="background:#fff; padding:30px; border-radius:20px; text-align:center; box-shadow:0 8px 24px rgba(0,0,0,0.1);">
        <h3>📄 Resume Screening</h3>
        <p>AI-powered resume scoring with instant certification.</p>
    </div>""", unsafe_allow_html=True)

with col2:
    st.markdown("""<div style="background:#fff; padding:30px; border-radius:20px; text-align:center; box-shadow:0 8px 24px rgba(0,0,0,0.1);">
        <h3>👥 Talent Finder</h3>
        <p>Discover opportunities that match your skills.</p>
    </div>""", unsafe_allow_html=True)

with col3:
    st.markdown("""<div style="background:#fff; padding:30px; border-radius:20px; text-align:center; box-shadow:0 8px 24px rgba(0,0,0,0.1);">
        <h3>💬 Collaboration</h3>
        <p>Chat, build teams, and work on projects together.</p>
    </div>""", unsafe_allow_html=True)

col4, col5 = st.columns(2)
with col4:
    st.markdown("""<div style="background:#fff; padding:30px; border-radius:20px; text-align:center; margin-top:20px; box-shadow:0 8px 24px rgba(0,0,0,0.1);">
        <h3>🏆 Profile & Badges</h3>
        <p>Showcase skills, earn credibility with badges.</p>
    </div>""", unsafe_allow_html=True)

with col5:
    st.markdown("""<div style="background:#fff; padding:30px; border-radius:20px; text-align:center; margin-top:20px; box-shadow:0 8px 24px rgba(0,0,0,0.1);">
        <h3>💼 Apply to Jobs</h3>
        <p>Directly apply to partnered companies through the portal.</p>
    </div>""", unsafe_allow_html=True)

# How It Works
st.markdown("<h2 style='text-align:center; margin:80px 0 40px;'>⚙️ How It Works</h2>", unsafe_allow_html=True)
steps = ["📝 Create your profile", "📂 Upload resume & projects", "🚀 Apply & Collaborate"]
for i, step in enumerate(steps, 1):
    st.markdown(f"<div style='text-align:center; margin:20px; font-size:1.2rem;'> <b>{i}. {step}</b></div>", unsafe_allow_html=True)

# CTA
st.markdown("""
<div style="text-align:center; margin:100px 0;">
    <h2 style="font-size:2.5rem; font-weight:800; color:#2563eb;">Start Your Journey with ScreenerPro</h2>
    <p>Join thousands of candidates building their future here.</p>
    <a href="#" style="background:#2563eb; color:white; padding:15px 40px; border-radius:40px; font-weight:700; text-decoration:none;">🚀 Get Started</a>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
<div style="text-align:center; padding:40px; color:#555; border-top:2px solid #eee;">
    © 2025 ScreenerPro Candidate Portal. All rights reserved.
</div>
""", unsafe_allow_html=True)
