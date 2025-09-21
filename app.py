import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="ScreenerPro - Candidate Portal", layout="wide")

# ---------- Custom Styling (Refined Futuristic SaaS Dark Theme) ----------
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700;800;900&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&display=swap');

        body {
            font-family: 'Inter', sans-serif;
            background: #050b14; /* Deep elegant dark */
            margin: 0;
            padding: 0;
            color: #e2e8f0;
        }
        .stApp {
            background-color: #050b14;
        }

        /* ✨ Glow animations */
        @keyframes glow {
            0% { box-shadow: 0 0 6px rgba(129,140,248,0.6), 0 0 10px rgba(139,92,246,0.5); }
            50% { box-shadow: 0 0 20px rgba(129,140,248,0.9), 0 0 35px rgba(236,72,153,0.7); }
            100% { box-shadow: 0 0 6px rgba(129,140,248,0.6), 0 0 10px rgba(139,92,246,0.5); }
        }

        /* 🌙 Navbar */
        .navbar {
            position: sticky;
            top: 0;
            background: rgba(10, 16, 26, 0.9);
            backdrop-filter: blur(14px);
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 1rem 2.8rem;
            z-index: 999;
            border-bottom: 1px solid rgba(255,255,255,0.08);
        }
        .navbar a {
            margin: 0 1rem;
            text-decoration: none;
            font-weight: 600;
            color: #cbd5e1;
            transition: color 0.3s ease;
        }
        .navbar a:hover {
            color: #818cf8;
        }
        .navbar div:first-child {
            font-weight: 900;
            font-size: 1.3rem;
            color: #a5b4fc;
            font-family: 'Poppins', sans-serif;
        }

        /* 🚀 Hero */
        .hero {
            text-align: center;
            padding: 8rem 1.5rem 6rem 1.5rem;
            background: radial-gradient(circle at 20% 30%, #111827, #050b14);
            color: white;
            border-bottom-left-radius: 50% 8%;
            border-bottom-right-radius: 50% 8%;
        }
        .hero h1 {
            font-family: 'Poppins', sans-serif;
            font-size: clamp(2.7rem, 6vw, 4.8rem);
            font-weight: 800;
            margin-bottom: 1rem;
            background: linear-gradient(90deg, #818cf8, #a78bfa, #ec4899);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .hero p {
            font-size: clamp(1rem, 2vw, 1.3rem);
            max-width: 46rem;
            margin: auto;
            opacity: 0.85;
            color: #d1d5db;
        }
        .cta-btn {
            display: inline-block;
            margin-top: 2.5rem;
            background: linear-gradient(90deg, #6366f1, #8b5cf6, #ec4899);
            color: white;
            padding: 1rem 2.8rem;
            border-radius: 9999px;
            font-size: 1.15rem;
            font-weight: 700;
            text-decoration: none;
            box-shadow: 0 6px 30px rgba(129,140,248,0.4);
            transition: all 0.3s ease;
        }
        .cta-btn:hover {
            transform: translateY(-0.3rem);
            animation: glow 1.5s infinite ease-in-out;
        }

        /* 🔥 Section Titles */
        .section-title {
            font-family: 'Poppins', sans-serif;
            font-size: clamp(2.2rem, 4vw, 3.2rem);
            font-weight: 800;
            text-align: center;
            margin: 6rem 0 3rem 0;
            background: linear-gradient(90deg, #a5b4fc, #ec4899);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        /* 🌌 Feature Cards */
        .feature-card {
            background: #0e1726;
            padding: 2rem;
            border-radius: 1.5rem;
            box-shadow: 0 8px 28px rgba(0,0,0,0.4);
            text-align: center;
            transition: all 0.4s ease;
            height: 100%;
            border: 1px solid rgba(255,255,255,0.05);
        }
        .feature-card:hover {
            transform: translateY(-0.7rem) scale(1.03);
            box-shadow: 0 14px 45px rgba(0,0,0,0.6), 0 0 30px rgba(129,140,248,0.3);
            border: 1px solid rgba(129,140,248,0.6);
        }
        .feature-card h3 {
            margin-top: 1rem;
            font-size: 1.35rem;
            font-weight: 700;
            color: #f1f5f9;
        }
        .feature-card p {
            font-size: 0.95rem;
            color: #94a3b8;
        }

        .lottie-container {
            width: 100%;
            height: 120px;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        /* 🎯 Final CTA */
        .final-cta {
            text-align: center;
            margin: 9rem 0;
        }
        .final-cta h2 {
            font-size: clamp(2.2rem, 4vw, 3.2rem);
            font-weight: 800;
            color: #f8fafc;
        }
        .final-cta p {
            color: #9ca3af;
            margin-bottom: 2rem;
        }

        /* ⚡ Footer */
        .footer {
            text-align: center;
            padding: 2rem;
            color: #6b7280;
            margin-top: 5rem;
            font-size: 0.9rem;
            border-top: 1px solid #1e293b;
        }
    </style>
""", unsafe_allow_html=True)

# ---------- Helper: Lottie Player ----------
def lottie_player(url, height=200, width=200):
    return components.html(f"""
        <div class="lottie-container">
            <lottie-player src="{url}" background="transparent" speed="1"
            style="width:{width}px; height:{height}px;" loop autoplay></lottie-player>
        </div>
        <script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
    """, height=height + 20, width=width)

# ---------- Navbar ----------
st.markdown("""
<div class="navbar">
    <div>ScreenerPro</div>
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
<div id="contact" class="final-cta">
    <h2>Ready to Supercharge Your Career?</h2>
    <p>Join thousands already growing with ScreenerPro.</p>
    <a href="#" class="cta-btn">🚀 Join Now</a>
</div>
""", unsafe_allow_html=True)

# ---------- Footer ----------
st.markdown('<div class="footer">© 2025 ScreenerPro Candidate Portal. All rights reserved.</div>', unsafe_allow_html=True)
