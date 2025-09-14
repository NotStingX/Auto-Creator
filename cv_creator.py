import streamlit as st
from fpdf import FPDF
from PIL import Image
import os

# PDF Class
class PDF(FPDF):
    def header(self):
        pass
    def footer(self):
        pass

# Streamlit Config
st.set_page_config(page_title="Automatic CV Creator", layout="centered")

st.markdown("<h1 style='text-align:center; color:gold;'>📄 Automatic CV Creator</h1>", unsafe_allow_html=True)
st.write("<p style='text-align:center;'>Fill in your details and generate a professional CV instantly.</p>", unsafe_allow_html=True)

# --- Personal Info ---
with st.expander("👤 Personal Information", expanded=True):
    name = st.text_input("Full Name")
    age = st.number_input("Age", min_value=10, max_value=100, step=1)
    birthdate = st.text_input("Birthdate (YYYY/MM/DD)")
    email = st.text_input("Email")
    phone = st.text_input("Phone Number")
    address = st.text_input("Address")
    photo = st.file_uploader("Upload Profile Photo", type=["jpg", "jpeg", "png"])

# --- Profile ---
with st.expander("📝 Profile", expanded=True):
    profile = st.text_area("Write a short profile introduction")

# --- Skills ---
with st.expander("💡 Skills", expanded=False):
    num_skills = st.number_input("How many skills do you want to add?", min_value=0, max_value=20, step=1)
    skills = []
    for i in range(int(num_skills)):
        skills.append(st.text_input(f"Skill #{i+1}"))

# --- Languages ---
with st.expander("🌐 Languages", expanded=False):
    num_langs = st.number_input("How many languages do you speak?", min_value=0, max_value=10, step=1)
    languages = []
    for i in range(int(num_langs)):
        languages.append(st.text_input(f"Language #{i+1} (Format: Language - Level)"))

# --- Work Experience ---
with st.expander("🧰 Work Experiences", expanded=False):
    num_experiences = st.number_input("How many work experiences?", min_value=0, max_value=10, step=1)
    experiences = []
    for i in range(int(num_experiences)):
        st.subheader(f"Experience #{i+1}")
        job = st.text_input(f"Job Title #{i+1}")
        company = st.text_input(f"Company #{i+1}")
        years = st.text_input(f"Years (e.g., 2020-2023) #{i+1}")
        description = st.text_area(f"Description #{i+1}")
        experiences.append({"Job": job, "Company": company, "Years": years, "Description": description})

# --- Education ---
with st.expander("🎓 Education", expanded=False):
    num_edu = st.number_input("How many education entries?", min_value=0, max_value=10, step=1)
    education = []
    for i in range(int(num_edu)):
        st.subheader(f"Education #{i+1}")
        degree = st.text_input(f"Degree/Level #{i+1}")
        subject = st.text_input(f"Subject #{i+1}")
        education.append(f"{degree} for {subject}")

# --- Hobbies ---
with st.expander("🎯 Hobbies", expanded=False):
    num_hobbies = st.number_input("How many hobbies?", min_value=0, max_value=10, step=1)
    hobbies = []
    for i in range(int(num_hobbies)):
        hobbies.append(st.text_input(f"Hobby #{i+1}"))

# --- Certifications ---
with st.expander("📜 Certifications", expanded=False):
    num_certs = st.number_input("How many certifications?", min_value=0, max_value=10, step=1)
    certifications = []
    for i in range(int(num_certs)):
        st.subheader(f"Certification #{i+1}")
        cert_title = st.text_input(f"Certification Title #{i+1}")
        issuer = st.text_input(f"Issued by #{i+1}")
        certifications.append({"Title": cert_title, "Issuer": issuer})


# --- PDF Generation ---
if st.button("🚀 Generate My CV"):
    pdf = PDF()
    pdf.add_page()

    # Background
    pdf.set_fill_color(30, 30, 30)
    pdf.rect(0, 0, 210, 297, 'F')

    # Profile Photo
    if photo:
        img = Image.open(photo)
        img_path = "temp_photo.png"
        img.save(img_path)
        pdf.image(img_path, 160, 10, 35, 35)
        os.remove(img_path)

    # Header - Name
    pdf.set_text_color(255, 215, 0)  # gold
    pdf.set_font("Arial", 'B', 20)
    pdf.cell(0, 10, name, ln=True)

    pdf.set_font("Arial", '', 12)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(0, 10, f"Age: {age}", ln=True)
    pdf.cell(0, 10, f"Birthdate: {birthdate}", ln=True)
    pdf.cell(0, 10, f"Email: {email}", ln=True)
    pdf.cell(0, 10, f"Phone: {phone}", ln=True)
    pdf.cell(0, 10, f"Address: {address}", ln=True)
    pdf.ln(5)

    # Section helper
    def section(title):
        pdf.set_font("Arial", 'B', 16)
        pdf.set_text_color(255, 215, 0)
        pdf.cell(0, 10, title, ln=True)
        pdf.set_text_color(255, 255, 255)
        pdf.set_font("Arial", '', 12)

    # Profile
    if profile:
        section("PROFILE")
        pdf.multi_cell(0, 10, profile)
        pdf.ln(5)

    # Skills
    if skills:
        section("SKILLS")
        for s in skills:
            pdf.cell(0, 10, f"- {s}", ln=True)
        pdf.ln(5)

    # Languages
    if languages:
        section("LANGUAGES")
        for l in languages:
            pdf.cell(0, 10, f"- {l}", ln=True)
        pdf.ln(5)

    # Work Experience
    if experiences:
        section("EXPERIENCE")
        for exp in experiences:
            pdf.set_font("Arial", 'B', 12)
            pdf.cell(0, 10, f"{exp['Job']} at {exp['Company']} ({exp['Years']})", ln=True)
            pdf.set_font("Arial", '', 12)
            pdf.multi_cell(0, 10, exp['Description'])
            pdf.ln(3)
        pdf.ln(5)

    # Education
    if education:
        section("EDUCATION")
        for edu in education:
            pdf.cell(0, 10, edu, ln=True)
        pdf.ln(5)

    # Hobbies
    if hobbies:
        section("HOBBIES")
        for hob in hobbies:
            pdf.cell(0, 10, hob, ln=True)
        pdf.ln(5)

    # Certifications
    if certifications:
        section("CERTIFICATIONS")
        for cert in certifications:
            pdf.cell(0, 10, f"{cert['Title']} (Issued by {cert['Issuer']})", ln=True)
        pdf.ln(5)

    # Save PDF
    pdf_output = "cv_output.pdf"
    pdf.output(pdf_output)

    with open(pdf_output, "rb") as f:
        st.download_button("📥 Download My CV", f, file_name="My_CV.pdf")
