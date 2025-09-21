# app.py
import streamlit as st
import base64
import datetime
import json
import uuid

# ---------------------------
# ScreenerPro Candidate Portal
# Advanced Landing Page (Streamlit-only, no extra packages)
# Save as app.py and run: streamlit run app.py
# ---------------------------

st.set_page_config(page_title="ScreenerPro — Candidate Portal", layout="wide", initial_sidebar_state="collapsed")

# Initialize session state storage
if "profiles" not in st.session_state:
    st.session_state.profiles = []  # list of dicts
if "messages" not in st.session_state:
    st.session_state.messages = []  # list of (from, to, text, time)
if "applications" not in st.session_state:
    st.session_state.applications = []  # list of apps
if "badges" not in st.session_state:
    st.session_state.badges = {}  # user_id -> set(badges)
if "last_resume_score" not in st.session_state:
    st.session_state.last_resume_score = None

# Utility helpers
def make_download_link(text: str, filename: str, mime: str = "text/plain"):
    b = text.encode()
    b64 = base64.b64encode(b).decode()
    href = f"data:{mime};base64,{b64}"
    return href

def earn_badge(user_id: str, badge_name: str):
    badges = st.session_state.badges.setdefault(user_id, set())
    if badge_name not in badges:
        badges.add(badge_name)
        st.toast(f"🏅 Badge earned: {badge_name}")

def simulate_resume_screening(name, resume_text: str):
    # A toy scoring function — real model replaced by this demo
    words = resume_text.split()
    length_score = min(30, len(words))  # up to 30 points
    keyword_bonus = 0
    keywords = ["python","machine","learning","ai","sql","react","aws","docker","lead"]
    for kw in keywords:
        if kw in resume_text.lower():
            keyword_bonus += 5
    score = min(100, 40 + length_score + keyword_bonus)
    st.session_state.last_resume_score = score
    return score

# ---------------------------
# Page CSS & Lottie embed helper (no packages)
# ---------------------------
st.markdown("""
    <style>
        /* Page fonts & base */
        :root { --accent1: #2563eb; --accent2: #9333ea; --accent3: #f43f5e; --muted: #6b7280; }
        body { font-family: 'Segoe UI', Roboto, -apple-system, Arial; }
        .hero {
            padding: 80px 30px;
            color: white;
            border-radius: 0 0 40px 40px;
            background: linear-gradient(135deg, #2563eb, #7c3aed, #f43f5e);
            background-size: 300% 300%;
            animation: bgShift 10s ease infinite;
            box-shadow: 0 20px 60px rgba(37,99,235,0.12);
        }
        @keyframes bgShift {
            0% { background-position: 0% 50%;}
            50% { background-position: 100% 50%;}
            100% { background-position: 0% 50%;}
        }
        .hero h1 { font-size: 3.2rem; font-weight: 900; margin-bottom: 8px; }
        .hero p { font-size: 1.15rem; color: rgba(255,255,255,0.92); margin-bottom: 18px; }
        .cta {
            display:inline-block; padding: 14px 28px; border-radius: 999px;
            background: linear-gradient(90deg, #ff7a7a, #7c3aed); color:white; font-weight:700;
            box-shadow: 0 8px 28px rgba(124,58,237,0.25); text-decoration:none;
        }
        .card {
            background: linear-gradient(180deg, rgba(255,255,255,0.98), rgba(255,255,255,0.92));
            border-radius: 18px; padding: 22px; box-shadow: 0 10px 26px rgba(9,30,66,0.06);
        }
        .feature-title { font-weight:800; font-size:1.1rem; color:var(--accent1); }
        .muted { color:var(--muted); }
        .wave { margin-top:-40px; }
        .profile-avatar { border-radius:999px; width:72px; height:72px; object-fit:cover; }
        .badge { display:inline-block; padding:6px 10px; border-radius:999px; background:#f0f9ff; color:var(--accent1); font-weight:700; margin-right:6px; }
        .pricing { border-radius:18px; padding:20px; }
        .testimonial { border-radius:12px; padding:18px; }
        .small { font-size:0.9rem; color:var(--muted); }
    </style>
""", unsafe_allow_html=True)

# inject lottie-player script once
st.markdown("""
<script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
""", unsafe_allow_html=True)

# ---------------------------
# HERO
# ---------------------------
with st.container():
    st.markdown('<div class="hero">', unsafe_allow_html=True)
    c1, c2 = st.columns([2,1])
    with c1:
        st.markdown("<h1>ScreenerPro — Candidate Portal</h1>", unsafe_allow_html=True)
        st.markdown("<p>Create a standout profile, get your resume screened, earn certificates & badges, find jobs, apply, and collaborate with teams — all in one place.</p>", unsafe_allow_html=True)
        st.markdown('<a class="cta" href="#create-profile">Create Your Profile — It’s Free</a> &nbsp; <a class="cta" style="opacity:0.9" href="#talent-finder">Find Jobs</a>', unsafe_allow_html=True)
    with c2:
        # Lottie animation in hero
        st.markdown("""
        <div style="display:flex;justify-content:center;align-items:center;">
            <lottie-player src="https://assets7.lottiefiles.com/packages/lf20_jcikwtux.json"  background="transparent"  speed="1"  style="width:260px; height:260px;"  loop autoplay></lottie-player>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# wave divider
st.markdown("""
<div class="wave">
<svg viewBox="0 0 1440 120"><path fill="#ffffff" d="M0,96L48,112C96,128,192,160,288,149.3C384,139,480,85,576,64C672,43,768,53,864,69.3C960,85,1056,107,1152,112C1248,117,1344,107,1392,101.3L1440,96L1440,0L0,0Z"></path></svg>
</div>
""", unsafe_allow_html=True)

# ---------------------------
# FEATURES + QUICK ACTIONS
# ---------------------------
st.markdown("<h2 style='margin-top:10px'>What You Can Do</h2>", unsafe_allow_html=True)
f1, f2, f3, f4 = st.columns(4)
with f1:
    st.markdown('<div class="card" style="text-align:center;">')
    st.markdown('<div class="feature-title">Resume Screening</div>')
    st.markdown('<div class="small muted">Upload, scan, and get instant score & feedback.</div><br>')
    st.markdown('<lottie-player src="https://assets2.lottiefiles.com/packages/lf20_tno6cg2w.json"  background="transparent"  speed="1"  style="width:120px; height:120px;"  loop autoplay></lottie-player>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
with f2:
    st.markdown('<div class="card" style="text-align:center;">')
    st.markdown('<div class="feature-title">Certificates</div>')
    st.markdown('<div class="small muted">Generate verified resume certificates to showcase skills.</div><br>')
    st.markdown('<lottie-player src="https://assets10.lottiefiles.com/packages/lf20_touohxv0.json"  background="transparent"  speed="1"  style="width:120px; height:120px;"  loop autoplay></lottie-player>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
with f3:
    st.markdown('<div class="card" style="text-align:center;">')
    st.markdown('<div class="feature-title">Talent Finder</div>')
    st.markdown('<div class="small muted">Search jobs & get discovered by recruiters.</div><br>')
    st.markdown('<lottie-player src="https://assets8.lottiefiles.com/packages/lf20_7r8p2e5u.json"  background="transparent"  speed="1"  style="width:120px; height:120px;"  loop autoplay></lottie-player>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
with f4:
    st.markdown('<div class="card" style="text-align:center;">')
    st.markdown('<div class="feature-title">Team & Collaboration</div>')
    st.markdown('<div class="small muted">Connect, message, build teams & apply together.</div><br>')
    st.markdown('<lottie-player src="https://assets2.lottiefiles.com/packages/lf20_x62chJ.json"  background="transparent"  speed="1"  style="width:120px; height:120px;"  loop autoplay></lottie-player>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------
# HOW IT WORKS
# ---------------------------
st.markdown('<h2 class="small" style="margin-top:40px">How it works</h2>', unsafe_allow_html=True)
st.markdown("""
<div class="card" style="display:flex; gap:16px; align-items:center;">
    <div style="flex:1; text-align:center;">
        <div style="font-weight:800; font-size:1.1rem;">1. Create your profile</div>
        <div class="small muted">Showcase projects, skills & team preferences.</div>
    </div>
    <div style="flex:1; text-align:center;">
        <div style="font-weight:800; font-size:1.1rem;">2. Upload resume & screen</div>
        <div class="small muted">Get instant AI-based scoring & feedback.</div>
    </div>
    <div style="flex:1; text-align:center;">
        <div style="font-weight:800; font-size:1.1rem;">3. Get badges & certificates</div>
        <div class="small muted">Earn profile badges and downloadable certificates.</div>
    </div>
    <div style="flex:1; text-align:center;">
        <div style="font-weight:800; font-size:1.1rem;">4. Find jobs & collaborate</div>
        <div class="small muted">Apply, message teams and join projects.</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ---------------------------
# Create Profile (form)
# ---------------------------
st.markdown('<a id="create-profile"></a>')
st.markdown('<h2 style="margin-top:40px">Create Your Profile</h2>', unsafe_allow_html=True)
with st.form("create_profile", clear_on_submit=False):
    cols = st.columns([1,2])
    with cols[0]:
        avatar = st.file_uploader("Upload avatar (optional)", type=["png","jpg","jpeg"])
    with cols[1]:
        name = st.text_input("Full name", value="")
        title = st.text_input("Title / Role (e.g., Frontend Engineer)", value="")
        location = st.text_input("Location", value="")
        short_bio = st.text_area("Short Bio (1-2 lines)", value="", max_chars=300)
        skills = st.text_input("Skills (comma-separated)", value="Python, SQL, Machine Learning")
        projects_raw = st.text_area("Projects (one per line: Title | Short description | link(optional))", value="Personal Website | Built a portfolio site | https://example.com")
        team_pref = st.text_input("Preferred Team Roles (comma-separated)", value="Contributor,Lead")
    submitted = st.form_submit_button("Save Profile")
    if submitted:
        profile_id = str(uuid.uuid4())[:8]
        avatar_b64 = None
        if avatar:
            avatar_b64 = base64.b64encode(avatar.getvalue()).decode()
        projects = []
        for line in projects_raw.splitlines():
            parts = [p.strip() for p in line.split("|")]
            if len(parts) >= 2:
                projects.append({"title": parts[0], "desc": parts[1], "link": parts[2] if len(parts) > 2 else ""})
        profile = {
            "id": profile_id,
            "name": name or "Anonymous",
            "title": title,
            "location": location,
            "bio": short_bio,
            "skills": [s.strip() for s in skills.split(",") if s.strip()],
            "projects": projects,
            "avatar": avatar_b64,
            "team_pref": [t.strip() for t in team_pref.split(",") if t.strip()],
            "created_at": datetime.datetime.utcnow().isoformat()
        }
        st.session_state.profiles.insert(0, profile)
        earn_badge(profile_id, "Profile Created")
        st.success("✅ Profile saved. You earned the 'Profile Created' badge!")
        st.experimental_rerun()

# Show profiles
if st.session_state.profiles:
    st.markdown("<h3 style='margin-top:18px'>Your Profiles & Project Showcase</h3>", unsafe_allow_html=True)
    for p in st.session_state.profiles:
        cols = st.columns([0.8,2,1])
        with cols[0]:
            if p["avatar"]:
                st.image(base64.b64decode(p["avatar"]), width=96, caption=None)
            else:
                st.image("https://via.placeholder.com/96.png?text=Avatar", width=96)
        with cols[1]:
            st.markdown(f"**{p['name']}**  ·  {p['title']}  —  {p['location']}")
            st.markdown(f"<div class='small muted'>{p['bio']}</div>", unsafe_allow_html=True)
            st.markdown("<div style='margin-top:8px'><b>Skills:</b> " + ", ".join([f"<span class='badge'>{s}</span>" for s in p["skills"]]) + "</div>", unsafe_allow_html=True)
            if p["projects"]:
                st.markdown("<div style='margin-top:8px'><b>Projects</b></div>", unsafe_allow_html=True)
                for pr in p["projects"]:
                    link_html = f" (<a href='{pr['link']}' target='_blank'>link</a>)" if pr.get("link") else ""
                    st.markdown(f"- **{pr['title']}** — {pr['desc']}{link_html}", unsafe_allow_html=True)
        with cols[2]:
            st.markdown("<div style='text-align:right; margin-top:10px'>", unsafe_allow_html=True)
            if st.button(f"Claim badge: {p['name'][:6]}", key=f"badge_{p['id']}"):
                earn_badge(p['id'], "Claimant")
            st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------
# Resume Upload & Screening
# ---------------------------
st.markdown("<hr>")
st.markdown("<h2 id='resume' style='margin-top:18px'>Upload Resume & Screen</h2>", unsafe_allow_html=True)
with st.form("resume_form"):
    ru_cols = st.columns([2,1])
    with ru_cols[0]:
        resume_file = st.file_uploader("Upload your resume (PDF / txt). For demo, paste resume text below if no file.", type=["pdf","txt","docx"])
        resume_text = st.text_area("Or paste resume text for screening (recommended for demo)", height=160)
    with ru_cols[1]:
        candidate_for = st.text_input("Applying for (job title)", value="Data Scientist")
        submit_resume = st.form_submit_button("Run Resume Screening")
    if submit_resume:
        text_for_scoring = ""
        if resume_text.strip():
            text_for_scoring = resume_text
        elif resume_file:
            try:
                raw = resume_file.read()
                # fallback: interpret as text if possible
                text_for_scoring = raw.decode(errors="ignore")
            except Exception:
                text_for_scoring = ""
        else:
            st.error("Please upload or paste resume text.")
        if text_for_scoring:
            score = simulate_resume_screening("candidate", text_for_scoring)
            st.success(f"Resume screening complete — Score: {score}/100")
            # show some simple suggestions
            suggestions = []
            if score < 60:
                suggestions.append("Add measurable achievements (numbers & impact).")
                suggestions.append("Include keywords from the job description.")
            elif score < 85:
                suggestions.append("Good! Add a couple more project details to increase score.")
            else:
                suggestions.append("Excellent! Your resume is strong for initial screening.")
            for s in suggestions:
                st.markdown(f"- {s}")
            # badge for screening
            dummy_user = st.session_state.profiles[0]['id'] if st.session_state.profiles else "guest"
            if score >= 50:
                earn_badge(dummy_user, "Resume Screened")
            # allow certificate generation
            if st.button("Generate Resume Certificate (demo)"):
                cert_text = f"ScreenerPro Resume Certificate\n\nName: {candidate_for}\nScore: {score}/100\nDate: {datetime.datetime.utcnow().date().isoformat()}\nCertificate ID: CERT-{uuid.uuid4().hex[:10].upper()}\n\nThis certifies that the candidate's resume passed ScreenerPro screening (demo)."
                href = make_download_link(cert_text, f"certificate_{candidate_for.replace(' ','_')}.txt")
                st.markdown(f"[Download Certificate]({href})", unsafe_allow_html=True)
                earn_badge(dummy_user, "Certificate Generated")

# ---------------------------
# Talent Finder (demo search / filter)
# ---------------------------
st.markdown("<hr>")
st.markdown('<a id="talent-finder"></a>')
st.markdown("<h2 style='margin-top:18px'>Talent Finder — Jobs & Discoverability</h2>", unsafe_allow_html=True)

# demo job dataset
JOBS = [
    {"id":"J1","title":"Data Scientist","company":"Acme AI","location":"Remote","skills":["python","ml","sql"],"type":"Full-time"},
    {"id":"J2","title":"Frontend Engineer","company":"PixelLabs","location":"Bengaluru","skills":["react","css","js"],"type":"Full-time"},
    {"id":"J3","title":"ML Engineer","company":"NeuronX","location":"Remote","skills":["python","docker","aws"],"type":"Contract"},
    {"id":"J4","title":"Product Designer","company":"DesignPro","location":"Delhi","skills":["figma","ux"],"type":"Part-time"},
]

# search UI
c_search, c_filter = st.columns([3,1])
with c_search:
    query = st.text_input("Search by job title, company or skill", value="")
with c_filter:
    location_filter = st.selectbox("Location", ["All","Remote","Bengaluru","Delhi"], index=0)
    type_filter = st.selectbox("Job Type", ["All","Full-time","Part-time","Contract"], index=0)

# filtering
def job_matches(job, q, loc, typ):
    q = q.lower().strip()
    if loc != "All" and job["location"] != loc:
        return False
    if typ != "All" and job["type"] != typ:
        return False
    if not q:
        return True
    if q in job["title"].lower() or q in job["company"].lower():
        return True
    for s in job["skills"]:
        if q in s:
            return True
    return False

matches = [j for j in JOBS if job_matches(j, query, location_filter, type_filter)]
st.markdown(f"**{len(matches)}** jobs found")
for job in matches:
    cols = st.columns([3,1])
    with cols[0]:
        st.markdown(f"**{job['title']}**  ·  {job['company']}  —  <span class='small muted'>{job['location']}</span>", unsafe_allow_html=True)
        st.markdown(f"<div class='small muted'>Skills: {', '.join(job['skills'])}  •  Type: {job['type']}</div>", unsafe_allow_html=True)
    with cols[1]:
        if st.button(f"Apply {job['id']}", key=f"apply_{job['id']}"):
            st.session_state.applications.append({"job_id": job["id"], "job": job, "applied_at": datetime.datetime.utcnow().isoformat()})
            st.success(f"Applied to {job['title']} at {job['company']}")
            # optionally earn badge
            dummy_user = st.session_state.profiles[0]['id'] if st.session_state.profiles else "guest"
            earn_badge(dummy_user, "Applied to Job")

# ---------------------------
# Applications list (demo)
# ---------------------------
if st.session_state.applications:
    st.markdown("<h3 style='margin-top:20px'>Your Recent Applications (demo)</h3>", unsafe_allow_html=True)
    for app in reversed(st.session_state.applications[-5:]):
        st.markdown(f"- **{app['job']['title']}** at {app['job']['company']} — <span class='small muted'>applied {app['applied_at']}</span>", unsafe_allow_html=True)

# ---------------------------
# Messaging / Collaboration (simple mock)
# ---------------------------
st.markdown("<hr>")
st.markdown("<h2 style='margin-top:18px'>Messaging & Collaboration (Demo)</h2>", unsafe_allow_html=True)
chat_cols = st.columns([3,1])
with chat_cols[0]:
    for m in st.session_state.messages[-10:]:
        time = m.get("time","")
        st.markdown(f"**{m['from']} → {m['to']}** <span class='small muted'>{time}</span>", unsafe_allow_html=True)
        st.markdown(f"> {m['text']}", unsafe_allow_html=True)
    st.markdown("---")
    with st.form("send_message"):
        from_name = st.text_input("Your name", value="You")
        to_name = st.text_input("To (person/team)", value="Team")
        msg_text = st.text_area("Message", height=80)
        sent = st.form_submit_button("Send Message")
        if sent:
            st.session_state.messages.append({"from": from_name, "to": to_name, "text": msg_text, "time": datetime.datetime.utcnow().isoformat()})
            st.success("Message sent (demo).")
            earn_badge(from_name, "First Message")
with chat_cols[1]:
    st.markdown("<div class='card'><b>Collaboration Tips</b><ul class='small muted'><li>Start with a clear goal</li><li>Share project links</li><li>Invite 2-3 members</li></ul></div>", unsafe_allow_html=True)

# ---------------------------
# Badges & Certificates showcase
# ---------------------------
st.markdown("<hr>")
st.markdown("<h2 style='margin-top:18px'>Badges & Certificates</h2>", unsafe_allow_html=True)
if st.session_state.badges:
    for user_id, badge_set in st.session_state.badges.items():
        st.markdown(f"<div class='card'><b>Profile:</b> {user_id} <br>Badges: " + ", ".join([f"<span class='badge'>{b}</span>" for b in badge_set]) + "</div>", unsafe_allow_html=True)
else:
    st.markdown("<div class='small muted'>No badges yet — create a profile & screen a resume to earn badges.</div>", unsafe_allow_html=True)

# ---------------------------
# Testimonials & Social Proof
# ---------------------------
st.markdown("<hr>")
st.markdown("<h2 style='margin-top:18px'>Trusted by Candidates & Recruiters</h2>", unsafe_allow_html=True)
t1, t2, t3 = st.columns(3)
with t1:
    st.markdown('<div class="testimonial"><b>“ScreenerPro helped me get interviews faster!”</b><br><span class="small muted">— Rahul, Data Engineer</span></div>', unsafe_allow_html=True)
with t2:
    st.markdown('<div class="testimonial"><b>“Great for showcasing projects and getting discovered.”</b><br><span class="small muted">— Meera, Product Designer</span></div>', unsafe_allow_html=True)
with t3:
    st.markdown('<div class="testimonial"><b>“The resume score gave me clear steps to improve.”</b><br><span class="small muted">— Karan, ML Intern</span></div>', unsafe_allow_html=True)

# ---------------------------
# FAQ + Footer
# ---------------------------
st.markdown("<hr>")
st.markdown("<h2 style='margin-top:18px'>FAQ</h2>", unsafe_allow_html=True)
st.markdown("<div class='card'><b>Q: Are certificates verified?</b><br><div class='small muted'>Demo certificates are downloadable text here — production would have cryptographic verification and issuer metadata.</div></div>", unsafe_allow_html=True)
st.markdown("<div class='card' style='margin-top:12px'><b>Q: Can I import from LinkedIn?</b><br><div class='small muted'>Yes — we plan resume imports and LinkedIn connect integrations in production.</div></div>", unsafe_allow_html=True)

st.markdown("""
<div style="margin-top:24px; padding:20px; border-radius:12px; text-align:center; background:linear-gradient(90deg,#ffffff,#f8fafc);">
    <b>© 2025 ScreenerPro</b> — Candidate Portal Demo · Built with ❤️ on Streamlit
</div>
""", unsafe_allow_html=True)
