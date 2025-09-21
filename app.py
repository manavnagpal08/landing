import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="ScreenerPro - Candidate Portal", layout="wide")

# ---------- Modern Dark SaaS CSS ----------
st.markdown("""
    <style>
        body {
            font-family: 'Inter', sans-serif;
            background: #0f0f11;
            margin: 0;
            padding: 0;
            color: white;
        }

        /* Navbar */
        .navbar {
            position: sticky;
            top: 0;
            background: rgba(15, 15, 17, 0.85);
            backdrop-filter: blur(12px);
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 18px 40px;
            z-index: 999;
            border-bottom: 1px solid rgba(255,255,255,0.1);
        }
        .navbar a {
            margin: 0 18px;
            text-decoration: none;
            font-weight: 500;
            font-size: 0.95rem;
            color: #d1d5db;
            transition: color 0.3s;
        }
        .navbar a:hover {
            color: #60a5fa;
        }

        /* Hero */
        .hero {
            text-align: center;
            padding: 150px 20px 120px 20px;
            background: radial-gradient(circle at top left, #1e1b4b, #0f0f11);
            color: white;
        }
        .hero h1 {
            font-size: 3.5rem;
            font-weight: 900;
            margin-bottom: 20px;
            background: linear-gradient(90deg, #60a5fa, #a855f7, #ec4899);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .hero p {
            font-size: 1.2rem;
            max-width: 750px;
            margin: auto;
            opacity: 0.9;
        }
        .cta-btn {
            display: inline-block;
            margin-top: 35px;
            background: linear-gradient(90deg, #6366f1, #a855f7, #ec4899);
            color: white;
            padding: 14px 38px;
            border-radius: 50px;
            font-size: 1.15rem;
            font-weight: 700;
            text-decoration: none;
            box-shadow: 0 8px 28px rgba(99, 102, 241, 0.5);
            transition: all 0.3s;
        }
        .cta-btn:hover {
            transform: translateY(-5px);
            box-shadow: 0 12px 36px rgba(168, 85, 247, 0.7);
        }

        /* Section Titles */
        .section-title {
            font-size: 2.3rem;
            font-weight: 800;
            text-align: center;
            margin: 90px 0 40px 0;
            background: linear-gradient(90deg, #60a5fa, #a855f7, #ec4899);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        /* Feature Cards */
        .feature-card {
            background: rgba(255, 255, 255, 0.05);
            padding: 32px;
            border-radius: 20px;
            text-align: center;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255,255,255,0.1);
            transition: all 0.3s;
        }
        .feature-card:hover {
            transform: translateY(-6px);
            box-shadow: 0 12px 32px rgba(96,165,250,0.3);
            border-color: rgba(96,165,250,0.5);
        }
        .feature-card h3 {
            margin-top: 15px;
            font-size: 1.2rem;
            font-weight: 700;
            color: #f3f4f6;
        }
        .feature-card p {
            font-size: 0.95rem;
            color: #cbd5e1;
        }

        /* Footer */
        .footer {
            text-align: center;
            padding: 35px;
            color: #9ca3af;
            margin-top: 90px;
            font-size: 0.9rem;
            border-top: 1px solid rgba(255,255,255,0.1);
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
    <div style="font-weight:900; font-size:1.3rem; background: linear-gradient(90deg,#60a5fa,#a855f7); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">ScreenerPro</div>
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
    <h1>🚀 Your Career. Upgraded.</h1>
    <p>ScreenerPro empowers candidates with AI-driven resume screening, verified certificates, collaboration tools, team creation, badges, and job applications — all in one futuristic portal.</p>
    <a href="#features" class="cta-btn">✨ Get Started</a>
</div>
""", unsafe_allow_html=True)

# ---------- Features ----------
st.markdown('<div id="features"></div>', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">🌟 Features that Empower You</h2>', unsafe_allow_html=True)

cols = st.columns(4)
with cols[0]:
    st.markdown('<div class="feature-card">', unsafe_allow_html=True)
    lottie_player("https://assets2.lottiefiles.com/packages/lf20_tno6cg2w.json", 120, 120)
    st.markdown('<h3>📄 Resume Screening</h3><p>AI-powered instant resume review.</p></div>', unsafe_allow_html=True)

with cols[1]:
    st.markdown('<div class="feature-card">', unsafe_allow_html=True)
    lottie_player("https://assets9.lottiefiles.com/packages/lf20_xlkxtmul.json", 120, 120)
    st.markdown('<h3>🎓 Certificates</h3><p>Generate verified resume certificates.</p></div>', unsafe_allow_html=True)

with cols[2]:
    st.markdown('<div class="feature-card">', unsafe_allow_html=True)
    lottie_player("https://assets1.lottiefiles.com/packages/lf20_jcikwtux.json", 120, 120)
    st.markdown('<h3>🔍 Talent Finder</h3><p>Discover peers and new opportunities.</p></div>', unsafe_allow_html=True)

with cols[3]:
    st.markdown('<div class="feature-card">', unsafe_allow_html=True)
    lottie_player("https://assets5.lottiefiles.com/packages/lf20_g2zjkhzt.json", 120, 120)
    st.markdown('<h3>🤝 Collaboration</h3><p>Work together with chat & messaging.</p></div>', unsafe_allow_html=True)

# ---------- Profile & Teams ----------
st.markdown('<div id="profile"></div>', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">👤 Profiles, Projects & Teams</h2>', unsafe_allow_html=True)

pcols = st.columns(3)
with pcols[0]:
    st.markdown('<div class="feature-card">', unsafe_allow_html=True)
    lottie_player("https://assets10.lottiefiles.com/private_files/lf30_editor_sflkwq.json", 140, 140)
    st.markdown('<h3>🌐 Profile</h3><p>Create a stunning candidate profile.</p></div>', unsafe_allow_html=True)

with pcols[1]:
    st.markdown('<div class="feature-card">', unsafe_allow_html=True)
    lottie_player("https://assets6.lottiefiles.com/packages/lf20_ktwnwv5m.json", 140, 140)
    st.markdown('<h3>🚀 Projects</h3><p>Showcase your portfolio to employers.</p></div>', unsafe_allow_html=True)

with pcols[2]:
    st.markdown('<div id="teams" class="feature-card">', unsafe_allow_html=True)
    lottie_player("https://assets4.lottiefiles.com/packages/lf20_tbrwjiv5.json", 140, 140)
    st.markdown('<h3>👥 Teams</h3><p>Build and join teams with shared goals.</p></div>', unsafe_allow_html=True)

# ---------- Badges & Jobs ----------
st.markdown('<div id="jobs"></div>', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">🏆 Achievements & Careers</h2>', unsafe_allow_html=True)

ecols = st.columns(2)
with ecols[0]:
    st.markdown('<div class="feature-card">', unsafe_allow_html=True)
    lottie_player("https://assets1.lottiefiles.com/packages/lf20_9xcyfycw.json", 140, 140)
    st.markdown('<h3>🏅 Badges</h3><p>Earn achievements that showcase skills.</p></div>', unsafe_allow_html=True)

with ecols[1]:
    st.markdown('<div class="feature-card">', unsafe_allow_html=True)
    lottie_player("https://assets8.lottiefiles.com/packages/lf20_3vbOcw.json", 140, 140)
    st.markdown('<h3>💼 Apply to Jobs</h3><p>Apply to curated jobs with one click.</p></div>', unsafe_allow_html=True)

# ---------- CTA ----------
st.markdown("""
<div id="contact" style="text-align:center; margin:100px 0;">
    <h2 style="font-size:2rem; font-weight:800; color:white;">Ready to Supercharge Your Career?</h2>
    <p style="color:#cbd5e1;">Join thousands already growing with ScreenerPro.</p>
    <a href="#" class="cta-btn">🚀 Join Now</a>
</div>
""", unsafe_allow_html=True)

# ---------- Footer ----------
st.markdown('<div class="footer">© 2025 ScreenerPro Candidate Portal. All rights reserved.</div>', unsafe_allow_html=True)
