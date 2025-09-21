import streamlit as st

# Page config
st.set_page_config(page_title="ScreenerPro - AI Hiring", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
        .hero {
            text-align: center;
            padding: 80px 20px;
        }
        .hero h1 {
            font-size: 3rem;
            font-weight: bold;
            color: #1e3a8a;
        }
        .hero p {
            font-size: 1.2rem;
            color: #4b5563;
        }
        .cta-btn {
            background: #2563eb;
            color: white;
            padding: 12px 30px;
            border-radius: 30px;
            font-size: 1.1rem;
            text-decoration: none;
        }
        .feature-card {
            background: white;
            padding: 25px;
            border-radius: 20px;
            box-shadow: 0 8px 24px rgba(0,0,0,0.05);
            text-align: center;
        }
        .footer {
            text-align: center;
            padding: 20px;
            color: gray;
            margin-top: 50px;
        }
    </style>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
<div class="hero">
    <h1>Revolutionize Your Hiring with <span style="color:#2563eb">ScreenerPro</span></h1>
    <p>AI-powered resume screening that delivers instant, accurate, and unbiased candidate assessments.</p>
    <a href="#start" class="cta-btn">🚀 Get Started Free</a>
</div>
""", unsafe_allow_html=True)

# Features Section
st.subheader("✨ Why ScreenerPro?")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="feature-card">⚡ **Instant Screening**<br/>AI reviews resumes in seconds.</div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="feature-card">🤝 **Unbiased Hiring**<br/>Data-driven candidate assessments.</div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="feature-card">📈 **Scalable & Reliable**<br/>For startups & enterprises alike.</div>', unsafe_allow_html=True)

# How It Works
st.subheader("⚙️ How It Works")
step1, step2, step3 = st.columns(3)

with step1:
    st.markdown('<div class="feature-card">1️⃣ Upload Job Description</div>', unsafe_allow_html=True)
with step2:
    st.markdown('<div class="feature-card">2️⃣ AI Screens Resumes</div>', unsafe_allow_html=True)
with step3:
    st.markdown('<div class="feature-card">3️⃣ Get Ranked Shortlist</div>', unsafe_allow_html=True)

# CTA Section
st.markdown("""
<div id="start" style="text-align:center; margin:60px 0;">
    <h2>Ready to Hire Smarter?</h2>
    <p>Join 500+ HR teams already using ScreenerPro.</p>
    <a href="#" class="cta-btn">Start Free Trial</a>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer">© 2025 ScreenerPro. All rights reserved.</div>', unsafe_allow_html=True)
