import streamlit as st

# Page config
st.set_page_config(page_title="ScreenerPro - AI Hiring", layout="wide")

# Custom CSS
st.markdown("""
    <style>
        body {
            background: linear-gradient(135deg, #f0f9ff, #e0e7ff, #ede9fe);
        }
        .hero {
            text-align: center;
            padding: 100px 20px 70px 20px;
        }
        .hero h1 {
            font-size: 3.2rem;
            font-weight: 800;
            background: linear-gradient(90deg, #2563eb, #7c3aed);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .hero p {
            font-size: 1.2rem;
            color: #374151;
            margin-bottom: 30px;
        }
        .cta-btn {
            background: linear-gradient(90deg, #2563eb, #7c3aed);
            color: white;
            padding: 14px 36px;
            border-radius: 40px;
            font-size: 1.2rem;
            text-decoration: none;
            font-weight: 500;
            box-shadow: 0 6px 16px rgba(124, 58, 237, 0.4);
            transition: 0.3s;
        }
        .cta-btn:hover {
            box-shadow: 0 8px 22px rgba(124, 58, 237, 0.6);
            transform: translateY(-3px);
        }
        .feature-card {
            background: white;
            padding: 30px;
            border-radius: 24px;
            box-shadow: 0 6px 20px rgba(0,0,0,0.08);
            text-align: center;
            transition: 0.3s;
        }
        .feature-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 28px rgba(0,0,0,0.12);
        }
        .feature-card h3 {
            font-size: 1.3rem;
            color: #2563eb;
        }
        .footer {
            text-align: center;
            padding: 30px;
            color: gray;
            margin-top: 50px;
            font-size: 0.9rem;
        }
    </style>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
<div class="hero">
    <h1>Hire Smarter with <span>ScreenerPro</span></h1>
    <p>AI-powered resume screening that saves time, ensures fairness, and finds the best talent instantly.</p>
    <a href="#start" class="cta-btn">🚀 Start Free Trial</a>
</div>
""", unsafe_allow_html=True)

# Features Section
st.subheader("✨ Why Choose ScreenerPro?")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="feature-card">⚡ <h3>Instant Screening</h3><p>AI reviews resumes in seconds and ranks candidates automatically.</p></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="feature-card">🤝 <h3>Unbiased Hiring</h3><p>Data-driven assessments remove bias and improve diversity.</p></div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="feature-card">📈 <h3>Scalable & Reliable</h3><p>Trusted by startups and enterprises for volume hiring.</p></div>', unsafe_allow_html=True)

# How It Works
st.subheader("⚙️ How It Works")
step1, step2, step3 = st.columns(3)

with step1:
    st.markdown('<div class="feature-card">1️⃣ <h3>Upload Job Description</h3><p>Tell ScreenerPro what role you’re hiring for.</p></div>', unsafe_allow_html=True)
with step2:
    st.markdown('<div class="feature-card">2️⃣ <h3>AI Screens Resumes</h3><p>Smart algorithms scan, score & sort candidates.</p></div>', unsafe_allow_html=True)
with step3:
    st.markdown('<div class="feature-card">3️⃣ <h3>Get Ranked Shortlist</h3><p>Receive a ready-to-use shortlist instantly.</p></div>', unsafe_allow_html=True)

# CTA Section
st.markdown("""
<div id="start" style="text-align:center; margin:80px 0;">
    <h2 style="font-size:2.2rem; font-weight:700; color:#1e3a8a;">Ready to Hire Smarter?</h2>
    <p style="color:#4b5563;">Join 500+ HR teams already using ScreenerPro today.</p>
    <a href="#" class="cta-btn">✨ Start Free Trial</a>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer">© 2025 ScreenerPro. All rights reserved.</div>', unsafe_allow_html=True)
