import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="ScreenerPro - AI Hiring", layout="wide")

# Custom CSS
st.markdown("""
    <style>
        body {
            background: linear-gradient(135deg, #eef2ff, #fdf4ff, #ecfeff);
        }
        .hero {
            text-align: center;
            padding: 120px 20px 80px 20px;
        }
        .hero h1 {
            font-size: 3.5rem;
            font-weight: 900;
            background: linear-gradient(90deg, #2563eb, #9333ea, #f43f5e);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 20px;
        }
        .hero p {
            font-size: 1.25rem;
            color: #374151;
            margin-bottom: 40px;
        }
        .cta-btn {
            background: linear-gradient(90deg, #2563eb, #9333ea);
            color: white;
            padding: 16px 40px;
            border-radius: 40px;
            font-size: 1.2rem;
            font-weight: 600;
            text-decoration: none;
            box-shadow: 0 6px 20px rgba(124, 58, 237, 0.5);
            transition: all 0.3s ease-in-out;
        }
        .cta-btn:hover {
            transform: translateY(-4px) scale(1.05);
            box-shadow: 0 10px 28px rgba(124, 58, 237, 0.7);
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
            transform: translateY(-6px);
            box-shadow: 0 14px 36px rgba(0,0,0,0.15);
        }
        .feature-card h3 {
            font-size: 1.4rem;
            color: #2563eb;
            margin-top: 15px;
        }
        .footer {
            text-align: center;
            padding: 40px;
            color: gray;
            margin-top: 80px;
            font-size: 0.9rem;
        }
    </style>
""", unsafe_allow_html=True)

# Function to insert lottie animation (via HTML)
def lottie_player(url, height=200, width=200):
    components.html(f"""
        <lottie-player src="{url}"  background="transparent"  speed="1"  
        style="width:{width}px; height:{height}px;"  loop autoplay></lottie-player>
        <script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
    """, height=height+50, width=width+50)

# Hero Section
st.markdown("""
<div class="hero">
    <h1>Hire Smarter with ScreenerPro 🚀</h1>
    <p>AI-powered resume screening that saves time, ensures fairness, and helps you find top talent instantly.</p>
    <a href="#start" class="cta-btn">✨ Start Free Trial</a>
</div>
""", unsafe_allow_html=True)

# Features Section
st.subheader("✨ Why Choose ScreenerPro?")
row1 = st.columns(3)

with row1[0]:
    st.markdown('<div class="feature-card">', unsafe_allow_html=True)
    lottie_player("https://assets2.lottiefiles.com/packages/lf20_tno6cg2w.json", height=140, width=140)
    st.markdown('<h3>⚡ Instant Screening</h3><p>AI reviews resumes in seconds and ranks candidates automatically.</p></div>', unsafe_allow_html=True)

with row1[1]:
    st.markdown('<div class="feature-card">', unsafe_allow_html=True)
    lottie_player("https://assets1.lottiefiles.com/packages/lf20_jcikwtux.json", height=140, width=140)
    st.markdown('<h3>📄 Resume Screening</h3><p>Get instant AI-powered resume evaluation.</p></div>', unsafe_allow_html=True)

with row1[2]:
    st.markdown('<div class="feature-card">', unsafe_allow_html=True)
    lottie_player("https://assets10.lottiefiles.com/packages/lf20_touohxv0.json", height=140, width=140)
    st.markdown('<h3>📈 Scalable & Reliable</h3><p>Trusted by startups and enterprises for volume hiring.</p></div>', unsafe_allow_html=True)

# How It Works
st.markdown("<h2 style='text-align:center; font-size:2.5rem;'>⚙️ How It Works</h2>", unsafe_allow_html=True)
steps = st.columns(3)

with steps[0]:
    st.markdown('<div class="feature-card">1️⃣ <h3>Upload Job Description</h3><p>Tell ScreenerPro what role you’re hiring for.</p></div>', unsafe_allow_html=True)
with steps[1]:
    st.markdown('<div class="feature-card">2️⃣ <h3>AI Screens Resumes</h3><p>Smart algorithms scan, score & sort candidates.</p></div>', unsafe_allow_html=True)
with steps[2]:
    st.markdown('<div class="feature-card">3️⃣ <h3>Get Ranked Shortlist</h3><p>Receive a ready-to-use shortlist instantly.</p></div>', unsafe_allow_html=True)

# CTA Section
st.markdown("""
<div id="start" style="text-align:center; margin:100px 0;">
    <h2 style="font-size:2.5rem; font-weight:800; background: linear-gradient(90deg, #2563eb, #9333ea); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
        Ready to Transform Hiring?
    </h2>
    <p style="color:#4b5563;">Join 500+ HR teams already using ScreenerPro today.</p>
    <a href="#" class="cta-btn">🚀 Start Free Trial</a>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer">© 2025 ScreenerPro. All rights reserved. | Built with ❤️ on Streamlit</div>', unsafe_allow_html=True)
