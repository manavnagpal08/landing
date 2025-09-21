import streamlit as st

# Page Config
st.set_page_config(page_title="ScreenerPro - AI Hiring Platform", layout="wide")

# Custom CSS for Styling & Animations
st.markdown("""
    <style>
        body {
            font-family: 'Segoe UI', sans-serif;
        }
        .hero {
            text-align: center;
            padding: 120px 20px 100px 20px;
            background: linear-gradient(-45deg, #2563eb, #9333ea, #f43f5e, #14b8a6);
            background-size: 400% 400%;
            animation: gradientBG 12s ease infinite;
            border-radius: 0 0 60px 60px;
            color: white;
        }
        @keyframes gradientBG {
            0% {background-position: 0% 50%;}
            50% {background-position: 100% 50%;}
            100% {background-position: 0% 50%;}
        }
        .hero h1 {
            font-size: 4rem;
            font-weight: 900;
            margin-bottom: 20px;
            animation: fadeInDown 1s ease;
        }
        .hero p {
            font-size: 1.3rem;
            margin-bottom: 40px;
            animation: fadeInUp 1.2s ease;
        }
        .cta-btn {
            background: linear-gradient(90deg, #f43f5e, #9333ea, #2563eb);
            color: white;
            padding: 16px 46px;
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
        .section-title {
            text-align: center;
            font-size: 2.5rem;
            font-weight: 800;
            margin: 60px 0 40px 0;
            background: linear-gradient(90deg, #2563eb, #9333ea, #f43f5e);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .feature-card {
            backdrop-filter: blur(12px);
            background: rgba(255, 255, 255, 0.8);
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
        .pricing-card {
            background: white;
            padding: 50px 40px;
            border-radius: 30px;
            box-shadow: 0 10px 36px rgba(0,0,0,0.15);
            text-align: center;
            transition: 0.4s;
        }
        .pricing-card:hover {
            transform: scale(1.05);
            box-shadow: 0 14px 40px rgba(0,0,0,0.3);
        }
        .pricing-card h3 {
            font-size: 1.6rem;
            margin-bottom: 10px;
            color: #2563eb;
        }
        .pricing-card h2 {
            font-size: 2.2rem;
            margin-bottom: 20px;
        }
        .testimonial {
            background: rgba(255,255,255,0.9);
            padding: 30px;
            border-radius: 20px;
            box-shadow: 0 6px 20px rgba(0,0,0,0.1);
            margin: 15px;
            text-align: center;
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
    <p>AI-powered recruitment that saves time, reduces bias, and helps you find the best talent instantly.</p>
    <a href="#start" class="cta-btn">✨ Start Free Trial</a>
</div>
""", unsafe_allow_html=True)

# Features Section
st.markdown('<h2 class="section-title">✨ Key Features</h2>', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""
    <div class="feature-card">
        <lottie-player src="https://assets2.lottiefiles.com/packages/lf20_tno6cg2w.json"  background="transparent"  speed="1" style="width:150px; height:150px;"  loop autoplay></lottie-player>
        <h3>⚡ Instant Resume Screening</h3>
        <p>Screen 1000s of resumes in seconds with AI ranking.</p>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div class="feature-card">
        <lottie-player src="https://assets1.lottiefiles.com/packages/lf20_jcikwtux.json"  background="transparent"  speed="1" style="width:150px; height:150px;"  loop autoplay></lottie-player>
        <h3>🤝 Fair & Unbiased</h3>
        <p>Remove unconscious bias and hire more diverse teams.</p>
    </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown("""
    <div class="feature-card">
        <lottie-player src="https://assets10.lottiefiles.com/packages/lf20_touohxv0.json"  background="transparent"  speed="1" style="width:150px; height:150px;"  loop autoplay></lottie-player>
        <h3>📈 Scalable Hiring</h3>
        <p>From startups to enterprises, ScreenerPro adapts to your needs.</p>
    </div>
    """, unsafe_allow_html=True)

# How it Works
st.markdown('<h2 class="section-title">⚙️ How It Works</h2>', unsafe_allow_html=True)
step1, step2, step3 = st.columns(3)
with step1:
    st.markdown('<div class="feature-card">1️⃣ <h3>Upload Job Description</h3><p>Tell us what role you’re hiring for.</p></div>', unsafe_allow_html=True)
with step2:
    st.markdown('<div class="feature-card">2️⃣ <h3>AI Screens Resumes</h3><p>Smart AI scans, scores & sorts resumes.</p></div>', unsafe_allow_html=True)
with step3:
    st.markdown('<div class="feature-card">3️⃣ <h3>Get Shortlist</h3><p>Receive a ranked list of top candidates instantly.</p></div>', unsafe_allow_html=True)

# Pricing Plans
st.markdown('<h2 class="section-title">💰 Pricing Plans</h2>', unsafe_allow_html=True)
p1, p2, p3 = st.columns(3)
with p1:
    st.markdown('<div class="pricing-card"><h3>Starter</h3><h2>Free</h2><p>✔️ 100 resumes / month<br>✔️ Basic AI screening<br>❌ No integrations</p><a href="#start" class="cta-btn">Get Started</a></div>', unsafe_allow_html=True)
with p2:
    st.markdown('<div class="pricing-card"><h3>Pro</h3><h2>$49/mo</h2><p>✔️ 5,000 resumes<br>✔️ Advanced AI scoring<br>✔️ Email support</p><a href="#start" class="cta-btn">Choose Pro</a></div>', unsafe_allow_html=True)
with p3:
    st.markdown('<div class="pricing-card"><h3>Enterprise</h3><h2>Custom</h2><p>✔️ Unlimited resumes<br>✔️ API & Integrations<br>✔️ Dedicated manager</p><a href="#start" class="cta-btn">Contact Us</a></div>', unsafe_allow_html=True)

# Testimonials
st.markdown('<h2 class="section-title">💬 What Our Users Say</h2>', unsafe_allow_html=True)
t1, t2, t3 = st.columns(3)
with t1:
    st.markdown('<div class="testimonial">“ScreenerPro cut our hiring time in half. Amazing tool!”<br><br><b>- Priya, HR Manager</b></div>', unsafe_allow_html=True)
with t2:
    st.markdown('<div class="testimonial">“We love how unbiased the shortlisting is. Game changer!”<br><br><b>- John, Recruiter</b></div>', unsafe_allow_html=True)
with t3:
    st.markdown('<div class="testimonial">“Simple, scalable, and reliable. Perfect for our needs.”<br><br><b>- Ayesha, Talent Head</b></div>', unsafe_allow_html=True)

# Call To Action
st.markdown("""
<div id="start" style="text-align:center; margin:100px 0;">
    <h2 style="font-size:2.8rem; font-weight:800; background: linear-gradient(90deg, #2563eb, #9333ea, #f43f5e); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
        Ready to Hire Smarter?
    </h2>
    <p style="color:#4b5563;">Join 500+ HR teams already using ScreenerPro today.</p>
    <a href="#" class="cta-btn">🚀 Start Free Trial</a>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer">© 2025 ScreenerPro. All rights reserved. | Built with ❤️ on Streamlit</div>', unsafe_allow_html=True)
