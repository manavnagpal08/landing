import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="ScreenerPro - Candidate Portal", layout="wide")

# ---------- CSS ----------
st.markdown("""
    <style>
        /* Moving gradient background */
        body {
            background: linear-gradient(-45deg, #ff9a9e, #fad0c4, #fbc2eb, #a18cd1, #fbc2eb, #fad0c4);
            background-size: 400% 400%;
            animation: gradientBG 15s ease infinite;
        }
        @keyframes gradientBG {
            0% {background-position: 0% 50%;}
            50% {background-position: 100% 50%;}
            100% {background-position: 0% 50%;}
        }

        .hero {
            text-align: center;
            padding: 140px 20px 100px 20px;
        }
        .hero h1 {
            font-size: 4rem;
            font-weight: 900;
            color: white;
            margin-bottom: 20px;
            text-shadow: 0px 4px 20px rgba(0,0,0,0.3);
        }
        .hero p {
            font-size: 1.3rem;
            color: #f0f0f0;
            margin-bottom: 40px;
        }
        .cta-btn {
            background: linear-gradient(90deg, #2563eb, #9333ea, #f43f5e);
            color: white;
            padding: 16px 42px;
            border-radius: 40px;
            font-size: 1.3rem;
            font-weight: 700;
            text-decoration: none;
            box-shadow: 0 6px 20px rgba(124, 58, 237, 0.6);
            transition: all 0.3s ease-in-out;
        }
        .cta-btn:hover {
            transform: translateY(-5px) scale(1.05);
            box-shadow: 0 12px 32px rgba(124, 58, 237, 0.8);
        }

        .section-title {
            font-size: 2.6rem;
            font-weight: 800;
            text-align: center;
            margin: 80px 0 40px 0;
            background: linear-gradient(90deg, #2563eb, #9333ea, #f43f5e);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
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
            transform: translateY(-8px);
            box-shadow: 0 16px 40px rgba(0,0,0,0.2);
        }
        .feature-card h3 {
            font-size: 1.4rem;
            color: #2563eb;
            margin-top: 15px;
        }

        .footer {
            text-align: center;
            padding: 40px;
            color: white;
            margin-top: 80px;
            font-size: 1rem;
            background: rgba(0,0,0,0.2);
        }
    </style>
""", unsafe_allow_html=True)

# ---------- Helper: Lottie player ----------
def lottie_player(url, height=200, width=200):
    components.html(f"""
        <lottie-player src="{url}"  background="transparent"  speed="1"
        style="width:{width}px; height:{height}px;"  loop autoplay></lottie-player>
        <script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
    """, height=height+50, width=width+50)

# ---------- Hero ----------
st.markdown("""
<div class="hero">
    <h1>Welcome to ScreenerPro Candidate Portal 🚀</h1>
    <p>Showcase your profile, collaborate with teams, earn badges, apply to jobs & unlock career opportunities.</p>
    <a href="#features" class="cta-btn">✨ Get Started</a>
</div>
""", unsafe_allow_html=True)

# ---------- Features ----------
st.markdown('<div id="features"></div>', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">🌟 Portal Features</h2>', unsafe_allow_html=True)

features = st.columns(4)

with features[0]:
    st.markdown('<div class="feature-card">', unsafe_allow_html=True)
    lottie_player("https://assets2.lottiefiles.com/packages/lf20_tno6cg2w.json", 120, 120)
    st.markdown('<h3>📄 Resume Screening</h3><p>Get instant AI-powered resume evaluations.</p></div>', unsafe_allow_html=True)

with features[1]:
    st.markdown('<div class="feature-card">', unsafe_allow_html=True)
    lottie_player("https://assets9.lottiefiles.com/packages/lf20_xlkxtmul.json", 120, 120)
    st.markdown('<h3>🎓 Certificates</h3><p>Generate verified resume certificates instantly.</p></div>', unsafe_allow_html=True)

with features[2]:
    st.markdown('<div class="feature-card">', unsafe_allow_html=True)
    lottie_player("https://assets1.lottiefiles.com/packages/lf20_jcikwtux.json", 120, 120)
    st.markdown('<h3>🔍 Talent Finder</h3><p>Discover and connect with the right people for projects.</p></div>', unsafe_allow_html=True)

with features[3]:
    st.markdown('<div class="feature-card">', unsafe_allow_html=True)
    lottie_player("https://assets5.lottiefiles.com/packages/lf20_g2zjkhzt.json", 120, 120)
    st.markdown('<h3>🤝 Collaboration</h3><p>Chat, collaborate, and build teams in real time.</p></div>', unsafe_allow_html=True)

# ---------- Profile & Team ----------
st.markdown('<h2 class="section-title">👤 Your Profile & Teams</h2>', unsafe_allow_html=True)
profile = st.columns(3)

with profile[0]:
    st.markdown('<div class="feature-card">', unsafe_allow_html=True)
    lottie_player("https://assets10.lottiefiles.com/private_files/lf30_editor_sflkwq.json", 140, 140)
    st.markdown('<h3>🌐 Profile</h3><p>Create your profile, showcase skills, and stand out.</p></div>', unsafe_allow_html=True)

with profile[1]:
    st.markdown('<div class="feature-card">', unsafe_allow_html=True)
    lottie_player("https://assets6.lottiefiles.com/packages/lf20_ktwnwv5m.json", 140, 140)
    st.markdown('<h3>🚀 Projects</h3><p>Showcase projects to highlight your achievements.</p></div>', unsafe_allow_html=True)

with profile[2]:
    st.markdown('<div class="feature-card">', unsafe_allow_html=True)
    lottie_player("https://assets4.lottiefiles.com/packages/lf20_tbrwjiv5.json", 140, 140)
    st.markdown('<h3>👥 Teams</h3><p>Create or join teams and work together effectively.</p></div>', unsafe_allow_html=True)

# ---------- Badges & Jobs ----------
st.markdown('<h2 class="section-title">🏆 Achievements & Opportunities</h2>', unsafe_allow_html=True)
extras = st.columns(2)

with extras[0]:
    st.markdown('<div class="feature-card">', unsafe_allow_html=True)
    lottie_player("https://assets1.lottiefiles.com/packages/lf20_9xcyfycw.json", 140, 140)
    st.markdown('<h3>🏅 Badges</h3><p>Earn recognition & unlock levels with badges.</p></div>', unsafe_allow_html=True)

with extras[1]:
    st.markdown('<div class="feature-card">', unsafe_allow_html=True)
    lottie_player("https://assets8.lottiefiles.com/packages/lf20_3vbOcw.json", 140, 140)
    st.markdown('<h3>💼 Apply to Jobs</h3><p>Apply directly to jobs that match your skills.</p></div>', unsafe_allow_html=True)

# ---------- Messages ----------
st.markdown('<h2 class="section-title">💬 Stay Connected</h2>', unsafe_allow_html=True)
st.markdown('<div class="feature-card">', unsafe_allow_html=True)
lottie_player("https://assets4.lottiefiles.com/packages/lf20_p9ziqf.json", 200, 200)
st.markdown('<h3>📩 Messaging</h3><p>Collaborate, chat & grow your network within ScreenerPro.</p></div>', unsafe_allow_html=True)

# ---------- Final CTA ----------
st.markdown("""
<div id="start" style="text-align:center; margin:100px 0;">
    <h2 style="font-size:2.5rem; font-weight:800; color:white; text-shadow:0px 4px 20px rgba(0,0,0,0.4);">
        Ready to Build Your Future?
    </h2>
    <p style="color:#f0f0f0;">Join thousands of candidates already transforming their careers with ScreenerPro.</p>
    <a href="#" class="cta-btn">🚀 Join Now</a>
</div>
""", unsafe_allow_html=True)

# ---------- Footer ----------
st.markdown('<div class="footer">© 2025 ScreenerPro Candidate Portal. All rights reserved. | Built with ❤️ on Streamlit</div>', unsafe_allow_html=True)
