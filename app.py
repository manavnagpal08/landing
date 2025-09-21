import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="ScreenerPro - Candidate Portal", layout="wide")

# ---------- Custom Fonts and Styling (Futuristic Dark Theme) ----------
st.markdown("""
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700;800;900&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&display=swap');

        /* General page layout and dark background */
        html, body {
            font-family: 'Inter', sans-serif;
            background: #070e17;
            margin: 0;
            padding: 0;
            color: #ffffff;
        }
        .stApp { background-color: #070e17; }

        /* Navbar */
        .navbar {
            position: sticky;
            top: 0;
            background: rgba(10, 16, 26, 0.85);
            backdrop-filter: blur(10px);
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 1rem 2.5rem;
            z-index: 999;
            border-bottom: 1px solid rgba(255,255,255,0.08);
        }
        .navbar a {
            margin: 0 0.8rem;
            text-decoration: none;
            font-weight: 600;
            color: #ffffff;
            transition: color 0.3s ease-in-out;
        }
        .navbar a:hover { color: #818cf8; }
        .navbar div:first-child {
            font-weight: 900;
            font-size: 1.2rem;
            color: #818cf8;
            font-family: 'Poppins', sans-serif;
        }

        /* Hero */
        .hero {
            text-align: center;
            padding: 7rem 1.5rem 5rem;
            background: linear-gradient(135deg, #0e1627, #070e17);
            color: white;
            border-bottom-left-radius: 50% 5%;
            border-bottom-right-radius: 50% 5%;
            box-shadow: 0 10px 40px rgba(0,0,0,0.5);
        }
        .hero h1 {
            font-family: 'Poppins', sans-serif;
            font-size: clamp(2.5rem, 5vw, 4.5rem);
            font-weight: 800;
            background: linear-gradient(90deg, #c7d2fe, #a5b4fc, #818cf8);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .hero p {
            font-size: 1.2rem;
            max-width: 45rem;
            margin: auto;
            color: #e2e8f0;
        }
        .cta-btn {
            display: inline-block;
            margin-top: 2rem;
            background: linear-gradient(90deg, #6366f1, #8b5cf6);
            padding: 1rem 2.5rem;
            border-radius: 9999px;
            font-size: 1.1rem;
            font-weight: 700;
            color: white;
            text-decoration: none;
            box-shadow: 0 5px 25px rgba(99, 102, 241, 0.4);
            transition: all 0.3s ease;
        }
        .cta-btn:hover {
            transform: translateY(-0.25rem);
            box-shadow: 0 10px 35px rgba(99, 102, 241, 0.6);
        }

        /* Section Titles */
        .section-title {
            font-family: 'Poppins', sans-serif;
            font-size: clamp(2rem, 4vw, 3rem);
            font-weight: 800;
            text-align: center;
            margin: 6rem 0 3rem;
            color: #ffffff;
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

        /* Feature Cards */
        .feature-card {
            background: #0e1627;
            padding: 2rem;
            border-radius: 1.5rem;
            box-shadow: 0 8px 30px rgba(0,0,0,0.4);
            text-align: center;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            border: 1px solid rgba(255,255,255,0.06);
        }
        .feature-card:hover {
            transform: translateY(-0.75rem);
            box-shadow: 0 16px 50px rgba(0,0,0,0.6), 0 0 20px rgba(99, 102, 241, 0.25);
            border: 1px solid rgba(99, 102, 241, 0.6);
        }
        .feature-card h3 { color: #f9fafb; }
        .feature-card p { color: #cbd5e1; }

        /* Footer */
        .footer {
            text-align: center;
            padding: 2rem;
            color: #94a3b8;
            margin-top: 5rem;
            font-size: 0.875rem;
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
    <div style="font-weight:900; font-size:1.2rem; color:#818cf8; font-family:'Poppins', sans-serif;">ScreenerPro</div>
    <div>
        <a href="#features">Features</a>
        <a href="#profile">Profile</a>
        <a href="#teams">Teams</a>
        <a href="#jobs">Jobs</a>
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
st.markdown('<h2 class="section-title">👤 Your Profile</h2>', unsafe_allow_html=True)
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
    <h2>
        Ready to Supercharge Your Career?
    </h2>
    <p>Join thousands already growing with ScreenerPro.</p>
    <a href="#" class="cta-btn">🚀 Join Now</a>
</div>
""", unsafe_allow_html=True)

# ---------- Footer ----------
st.markdown('<div class="footer">© 2025 ScreenerPro Candidate Portal. All rights reserved.</div>', unsafe_allow_html=True)
