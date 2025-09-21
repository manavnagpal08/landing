import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="ScreenerPro - Candidate Portal", layout="wide")

# ---------- Modern SaaS CSS ----------
st.markdown("""
    <style>
        body {
            font-family: 'Inter', sans-serif;
            background: #f8fafc;
            margin: 0;
            padding: 0;
        }

        /* Navbar */
        .navbar {
            position: sticky;
            top: 0;
            background: rgba(255, 255, 255, 0.75);
            backdrop-filter: blur(14px);
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 14px 40px;
            z-index: 999;
            border-bottom: 1px solid rgba(229,231,235,0.6);
        }
        .navbar a {
            margin: 0 16px;
            text-decoration: none;
            font-weight: 600;
            font-size: 0.95rem;
            color: #1e293b;
            transition: all 0.3s;
            position: relative;
        }
        .navbar a:hover {
            color: #6366f1;
        }
        .navbar a::after {
            content: "";
            display: block;
            height: 2px;
            width: 0;
            background: linear-gradient(90deg, #6366f1, #9333ea);
            transition: width 0.3s;
            margin-top: 4px;
        }
        .navbar a:hover::after {
            width: 100%;
        }

        /* Hero */
        .hero {
            text-align: center;
            padding: 140px 20px 120px 20px;
            background: linear-gradient(135deg, #6366f1, #9333ea, #ec4899);
            color: white;
            border-bottom-left-radius: 60% 8%;
            border-bottom-right-radius: 60% 8%;
        }
        .hero h1 {
            font-size: 4rem;
            font-weight: 900;
            margin-bottom: 20px;
            letter-spacing: -1px;
        }
        .hero p {
            font-size: 1.25rem;
            max-width: 720px;
            margin: auto;
            opacity: 0.95;
        }
        .cta-btn {
            display: inline-block;
            margin-top: 36px;
            background: linear-gradient(90deg, #6366f1, #9333ea, #ec4899);
            color: white;
            padding: 14px 38px;
            border-radius: 40px;
            font-size: 1.15rem;
            font-weight: 700;
            text-decoration: none;
            box-shadow: 0 8px 25px rgba(99, 102, 241, 0.45);
            transition: all 0.35s;
        }
        .cta-btn:hover {
            transform: translateY(-5px) scale(1.03);
            box-shadow: 0 14px 36px rgba(99, 102, 241, 0.7);
        }

        /* Section Titles */
        .section-title {
            font-size: 2.6rem;
            font-weight: 800;
            text-align: center;
            margin: 100px 0 50px 0;
            background: linear-gradient(90deg, #6366f1, #9333ea);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        /* Feature Cards */
        .feature-card {
            background: rgba(255,255,255,0.7);
            backdrop-filter: blur(12px);
            padding: 34px;
            border-radius: 28px;
            box-shadow: 0 6px 24px rgba(0,0,0,0.08);
            text-align: center;
            transition: all 0.35s;
        }
        .feature-card:hover {
            transform: translateY(-8px) scale(1.02);
            box-shadow: 0 12px 36px rgba(99,102,241,0.25);
        }
        .feature-card h3 {
            margin-top: 18px;
            font-size: 1.35rem;
            font-weight: 700;
            color: #111827;
        }
        .feature-card p {
            font-size: 1rem;
            color: #374151;
        }

        /* Footer */
        .footer {
            text-align: center;
            padding: 40px 20px;
            color: #6b7280;
            margin-top: 100px;
            font-size: 0.95rem;
            border-top: 1px solid #e5e7eb;
        }
    </style>
""", unsafe_allow_html=True)

# ---------- Helper: Lottie ----------
def lottie_player(url, height=200, width=200):
    components.html(f"""
        <lottie-player src="{url}" background="transparent" speed="1"
        style="width:{width}px; height:{height}px;" loop autoplay></lottie-player>
        <script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
    """, height=height+50, width=width+50)

# ---------- Navbar ----------
st.markdown("""
<div class="navbar">
    <div style="font-weight:900; font-size:1.3rem; color:#6366f1;">ScreenerPro</div>
    <div>
        <a href="#features">Features</a>
        <a href="#profile">Profile</a>
        <a href="#teams">Teams</a>
        <a href="#jobs">Jobs</a>
        <a href="#contact">Contact</a>
    </div>
</div>
""", unsafe_allow_html=True)

# ---------- Hero ----------
st.markdown("""
<div class="hero">
    <h1>🚀 ScreenerPro Candidate Portal</h1>
    <p>Showcase your skills, collaborate with teams, earn badges, and apply to jobs — all in one modern career hub.</p>
    <a href="#features" class="cta-btn">✨ Get Started</a>
</div>
""", unsafe_allow_html=True)

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
    lottie_player("https://assets9.lottiefiles.com/packages/lf20_xlkxtmul.json", 120, 120)
    st.markdown('<h3>🎓 Certificates</h3><p>Generate and share verified resume certificates.</p></div>', unsafe_allow_html=True)

with cols[2]:
    st.markdown('<div class="feature-card">', unsafe_allow_html=True)
    lottie_player("https://assets1.lottiefiles.com/packages/lf20_jcikwtux.json", 120, 120)
    st.markdown('<h3>🔍 Talent Finder</h3><p>Find collaborators and discover career matches.</p></div>', unsafe_allow_html=True)

with cols[3]:
    st.markdown('<div class="feature-card">', unsafe_allow_html=True)
    lottie_player("https://assets5.lottiefiles.com/packages/lf20_g2zjkhzt.json", 120, 120)
    st.markdown('<h3>🤝 Collaboration</h3><p>Chat, connect, and collaborate with peers.</p></div>', unsafe_allow_html=True)

# ---------- Profile + Teams ----------
st.markdown('<div id="profile"></div>', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">👤 Profile & Projects</h2>', unsafe_allow_html=True)
pcols = st.columns(3)
with pcols[0]:
    st.markdown('<div class="feature-card">', unsafe_allow_html=True)
    lottie_player("https://assets10.lottiefiles.com/private_files/lf30_editor_sflkwq.json", 140, 140)
    st.markdown('<h3>🌐 Profile</h3><p>Showcase your skills and personal brand.</p></div>', unsafe_allow_html=True)

with pcols[1]:
    st.markdown('<div class="feature-card">', unsafe_allow_html=True)
    lottie_player("https://assets6.lottiefiles.com/packages/lf20_ktwnwv5m.json", 140, 140)
    st.markdown('<h3>🚀 Projects</h3><p>Highlight your best work and achievements.</p></div>', unsafe_allow_html=True)

with pcols[2]:
    st.markdown('<div id="teams" class="feature-card">', unsafe_allow_html=True)
    lottie_player("https://assets4.lottiefiles.com/packages/lf20_tbrwjiv5.json", 140, 140)
    st.markdown('<h3>👥 Teams</h3><p>Create and join teams to collaborate efficiently.</p></div>', unsafe_allow_html=True)

# ---------- Badges & Jobs ----------
st.markdown('<div id="jobs"></div>', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">🏆 Achievements & Jobs</h2>', unsafe_allow_html=True)
ecols = st.columns(2)
with ecols[0]:
    st.markdown('<div class="feature-card">', unsafe_allow_html=True)
    lottie_player("https://assets1.lottiefiles.com/packages/lf20_9xcyfycw.json", 140, 140)
    st.markdown('<h3>🏅 Badges</h3><p>Earn recognition & climb the leaderboard.</p></div>', unsafe_allow_html=True)

with ecols[1]:
    st.markdown('<div class="feature-card">', unsafe_allow_html=True)
    lottie_player("https://assets8.lottiefiles.com/packages/lf20_3vbOcw.json", 140, 140)
    st.markdown('<h3>💼 Apply to Jobs</h3><p>One-click applications for top opportunities.</p></div>', unsafe_allow_html=True)

# ---------- Final CTA ----------
st.markdown("""
<div id="contact" style="text-align:center; margin:120px 0;">
    <h2 style="font-size:2.3rem; font-weight:800; color:#111827;">
        Ready to Supercharge Your Career?
    </h2>
    <p style="color:#374151; font-size:1.05rem;">Join thousands already growing with ScreenerPro.</p>
    <a href="#" class="cta-btn">🚀 Join Now</a>
</div>
""", unsafe_allow_html=True)

# ---------- Footer ----------
st.markdown('<div class="footer">© 2025 ScreenerPro Candidate Portal. All rights reserved.</div>', unsafe_allow_html=True)
