import streamlit as st

# Page Config
st.set_page_config(page_title="ScreenerPro - AI Hiring", layout="wide")

# Custom CSS
st.markdown("""
    <style>
        body {
            background: linear-gradient(135deg, #eef2ff, #fdf4ff, #ecfeff);
            font-family: 'Segoe UI', sans-serif;
        }
        .hero {
            text-align: center;
            padding: 120px 20px 80px 20px;
            background: linear-gradient(135deg, #2563eb, #9333ea);
            border-radius: 0 0 60px 60px;
            color: white;
        }
        .hero h1 {
            font-size: 3.8rem;
            font-weight: 900;
            margin-bottom: 20px;
        }
        .hero p {
            font-size: 1.3rem;
            margin-bottom: 40px;
        }
        .cta-btn {
            background: linear-gradient(90deg, #f43f5e, #9333ea, #2563eb);
            color: white;
            padding: 16px 42px;
            border-radius: 40px;
            font-size: 1.2rem;
            font-weight: 600;
            text-decoration: none;
            box-shadow: 0 8px 24px rgba(0,0,0,0.25);
            transition: all 0.3s ease-in-out;
        }
        .cta-btn:hover {
            transform: translateY(-4px) scale(1.05);
            box-shadow: 0 12px 30px rgba(0,0,0,0.4);
        }
        .feature-card {
            backdrop-filter: blur(12px);
            background: rgba(255, 255, 255, 0.75);
            padding: 40px;
            border-radius: 28px;
            box-shadow: 0 10px 32px rgba(0,0,0,0.15);
            text-align: center;
            transition: 0.3s;
        }
        .feature-card:hover {
            transform: translateY(-6px);
            box-shadow: 0 14px 36px rgba(0,0,0,0.25);
        }
        .feature-card h3 {
            font-size: 1.4rem;
            color: #2563eb;
            margin-top: 15px;
        }
        .footer {
            text-align: center;
            padding: 40px;
            margin-top: 80px;
            font-size: 0.95rem;
            color: #4b5563;
            border-top: 3px solid;
            border-image: linear-gradient(90deg,#2563eb,#9333ea,#f43f5e) 1;
        }
    </style>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
<div class="hero">
    <h1>Hire Smarter with ScreenerPro 🚀</h1>
    <p>AI-powered resume screening that saves time, ensures fairness, and helps you find top talent instantly.</p>
    <a href="#start" class="cta-btn">✨ Start Free Trial</a>
</div>
""", unsafe_allow_html=True)

# Wave Transition
st.markdown("""
<svg viewBox="0 0 1440 320"><path fill="#ffffff" fill-opacity="1" d="M0,224L48,192C96,160,192,96,288,74.7C384,53,480,75,576,117.3C672,160,768,224,864,250.7C960,277,1056,267,1152,224C1248,181,1344,107,1392,69.3L1440,32L1440,0L0,0Z"></path></svg>
""", unsafe_allow_html=True)

# Features Section
st.markdown("<h2 style='text-align:center; font-size:2.5rem;'>✨ Why Choose ScreenerPro?</h2>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-card">
        <lottie-player src="https://assets2.lottiefiles.com/packages/lf20_tno6cg2w.json" background="transparent" speed="1" style="width: 150px; height: 150px;" loop autoplay></lottie-player>
        <h3>⚡ Instant Screening</h3>
        <p>AI reviews resumes in seconds and ranks candidates automatically.</p>
    </div>
    <script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <lottie-player src="https://assets1.lottiefiles.com/packages/lf20_jcikwtux.json" background="transparent" speed="1" style="width: 150px; height: 150px;" loop autoplay></lottie-player>
        <h3>🤝 Unbiased Hiring</h3>
        <p>Data-driven assessments remove bias and improve diversity.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <lottie-player src="https://assets10.lottiefiles.com/packages/lf20_touohxv0.json" background="transparent" speed="1" style="width: 150px; height: 150px;" loop autoplay></lottie-player>
        <h3>📈 Scalable & Reliable</h3>
        <p>Trusted by startups and enterprises for volume hiring.</p>
    </div>
    """, unsafe_allow_html=True)

# How It Works
st.markdown("<h2 style='text-align:center; font-size:2.5rem; margin-top:80px;'>⚙️ How It Works</h2>", unsafe_allow_html=True)

step1, step2, step3 = st.columns(3)

with step1:
    st.markdown('<div class="feature-card">1️⃣ <h3>Upload Job Description</h3><p>Tell ScreenerPro what role you’re hiring for.</p></div>', unsafe_allow_html=True)

with step2:
    st.markdown('<div class="feature-card">2️⃣ <h3>AI Screens Resumes</h3><p>Smart algorithms scan, score & sort candidates.</p></div>', unsafe_allow_html=True)

with step3:
    st.markdown('<div class="feature-card">3️⃣ <h3>Get Ranked Shortlist</h3><p>Receive a ready-to-use shortlist instantly.</p></div>', unsafe_allow_html=True)

# Call To Action
st.markdown("""
<div id="start" style="text-align:center; margin:100px 0;">
    <h2 style="font-size:2.5rem; font-weight:800; background: linear-gradient(90deg, #2563eb, #9333ea, #f43f5e); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
        Ready to Transform Hiring?
    </h2>
    <p style="color:#4b5563;">Join 500+ HR teams already using ScreenerPro today.</p>
    <a href="#" class="cta-btn">🚀 Start Free Trial</a>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer">© 2025 ScreenerPro. All rights reserved. | Built with ❤️ on Streamlit</div>', unsafe_allow_html=True)
