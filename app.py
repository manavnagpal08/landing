import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="ScreenerPro - Candidate Portal", layout="wide")

# ---------- Font and General Styling ----------
# Note: Using Tailwind-inspired styling for a clean, modern look.
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&display=swap');

        /* General page layout and background */
        body {
            font-family: 'Inter', sans-serif;
            background: #f0f2f5;
            margin: 0;
            padding: 0;
        }

        /* Streamlit main content container */
        .st-emotion-cache-1cypq83 {
            background-color: #f0f2f5;
        }
        
        .stApp {
            background-color: #f0f2f5;
        }

        /* Navbar - a little more subtle and clean */
        .navbar {
            position: sticky;
            top: 0;
            background: rgba(255, 255, 255, 0.9);
            backdrop-filter: blur(10px);
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 1rem 2.5rem;
            z-index: 999;
            box-shadow: 0 4px 15px rgba(0,0,0,0.05);
            border-bottom: 1px solid rgba(0,0,0,0.05);
        }
        .navbar a {
            margin: 0 0.8rem;
            text-decoration: none;
            font-weight: 600;
            color: #334155;
            transition: color 0.3s ease-in-out;
        }
        .navbar a:hover {
            color: #4f46e5;
        }

        /* Hero section - using a smoother, more elegant gradient */
        .hero {
            text-align: center;
            padding: 7rem 1.5rem 5rem 1.5rem;
            background: linear-gradient(135deg, #6b21a8, #4f46e5);
            color: white;
            border-bottom-left-radius: 50% 5%;
            border-bottom-right-radius: 50% 5%;
        }
        .hero h1 {
            font-family: 'Poppins', sans-serif;
            font-size: clamp(2rem, 5vw, 4rem);
            font-weight: 800;
            margin-bottom: 1.25rem;
        }
        .hero p {
            font-size: clamp(1rem, 2vw, 1.25rem);
            max-width: 45rem;
            margin: auto;
            opacity: 0.95;
        }
        .cta-btn {
            display: inline-block;
            margin-top: 1.5rem;
            background: #ffffff;
            color: #4f46e5;
            padding: 0.75rem 2.25rem;
            border-radius: 9999px;
            font-size: 1.1rem;
            font-weight: 700;
            text-decoration: none;
            box-shadow: 0 5px 20px rgba(79, 70, 229, 0.3);
            transition: all 0.3s ease-in-out;
        }
        .cta-btn:hover {
            transform: translateY(-0.25rem);
            box-shadow: 0 10px 30px rgba(79, 70, 229, 0.4);
        }

        /* Section Titles - using a more professional font */
        .section-title {
            font-family: 'Poppins', sans-serif;
            font-size: clamp(1.8rem, 4vw, 2.5rem);
            font-weight: 800;
            text-align: center;
            margin: 5rem 0 2.5rem 0;
            color: #1f2937;
        }

        /* Feature Cards - with a lift-on-hover effect */
        .feature-card {
            background: white;
            padding: 2rem;
            border-radius: 1.5rem;
            box-shadow: 0 8px 24px rgba(0,0,0,0.05);
            text-align: center;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            height: 100%; /* Ensure all cards have same height */
            display: flex;
            flex-direction: column;
            justify-content: flex-start;
            align-items: center;
        }
        .feature-card:hover {
            transform: translateY(-0.5rem);
            box-shadow: 0 16px 40px rgba(0,0,0,0.1);
        }
        .feature-card h3 {
            margin-top: 1rem;
            font-size: 1.25rem;
            font-weight: 700;
            color: #1f2937;
        }
        .feature-card p {
            font-size: 0.95rem;
            color: #64748b;
            flex-grow: 1; /* Pushes content to the top */
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
            margin: 6rem 0;
        }
        .final-cta h2 {
            font-size: clamp(1.8rem, 4vw, 2.5rem);
            font-weight: 800;
            color: #1f2937;
        }
        .final-cta p {
            color: #64748b;
            margin-bottom: 2rem;
        }

        /* Footer */
        .footer {
            text-align: center;
            padding: 2rem;
            color: #94a3b8;
            margin-top: 5rem;
            font-size: 0.875rem;
            border-top: 1px solid #e2e8f0;
        }
    </style>
""", unsafe_allow_html=True)

# ---------- Helper: Lottie Player ----------
def lottie_player(url, height=200, width=200):
    components.html(f"""
        <div class="lottie-container">
            <lottie-player src="{url}" background="transparent" speed="1"
            style="width:{width}px; height:{height}px;" loop autoplay></lottie-player>
        </div>
        <script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
    """, height=height + 20, width=width)

# ---------- Navbar ----------
st.markdown("""
<div class="navbar">
    <div style="font-weight:900; font-size:1.2rem; color:#4f46e5; font-family:'Poppins', sans-serif;">ScreenerPro</div>
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
    <h2>
        Ready to Supercharge Your Career?
    </h2>
    <p>Join thousands already growing with ScreenerPro.</p>
    <a href="#" class="cta-btn">🚀 Join Now</a>
</div>
""", unsafe_allow_html=True)

# ---------- Footer ----------
st.markdown('<div class="footer">© 2025 ScreenerPro Candidate Portal. All rights reserved.</div>', unsafe_allow_html=True)
