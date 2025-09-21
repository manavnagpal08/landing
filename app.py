import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="ScreenerPro - Candidate Portal", layout="wide")

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

        /* Navbar - a more refined look */
        .navbar {
            position: sticky;
            top: 0;
            background: rgba(10, 16, 26, 0.8);
            backdrop-filter: blur(10px);
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 1rem 2.5rem;
            z-index: 999;
            box-shadow: 0 4px 15px rgba(0,0,0,0.3);
            border-bottom: 1px solid rgba(255,255,255,0.1);
        }
        .navbar a {
            margin: 0 0.8rem;
            text-decoration: none;
            font-weight: 600;
            color: #ffffff;
            transition: color 0.3s ease-in-out;
        }
        .navbar a:hover {
            color: #818cf8;
        }
        .navbar div:first-child {
            font-weight: 900;
            font-size: 1.2rem;
            color: #818cf8;
            font-family: 'Poppins', sans-serif;
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
    # New, stable Lottie animation for Collaboration
    lottie_player("https://raw.githubusercontent.com/manavnagpal08/landing/refs/heads/main/Collaboration.json", 120, 120)
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
    lottie_player("https://assets7.lottiefiles.com/packages/lf20_1r9y3p.json", 140, 140)
    st.markdown('<h3>🏅 Badges</h3><p>Earn recognition & climb the leaderboard.</p></div>', unsafe_allow_html=True)

with ecols[1]:
    st.markdown('<div class="feature-card">', unsafe_allow_html=True)
    lottie_player("https://assets8.lottiefiles.com/packages/lf20_v3g2a9.json", 140, 140)
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
