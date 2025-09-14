import streamlit as st
from fpdf import FPDF
from PIL import Image
import os

# --- PDF Class ---
class PDF(FPDF):
    def header(self):
        pass

    def footer(self):
        pass


# --- Streamlit Page Config ---
st.set_page_config(page_title="📄 CV Creator", layout="centered")
st.title("📄 Automatic CV Creator")
st.write("Fill in the details below to generate your CV")

# --- Personal Info ---
st.header("👤 Personal Information")
name = st.text_input("Full Name")
birth_date = st.date_input("Birth Date")
email = st.text_input("Email")
phone = st.text_input("Phone Number")
address = st.text_area("Address")
photo = st.file_uploader("Upload a Profile Photo", type=["jpg", "jpeg", "png"])

# --- Profile ---
st.header("📌 Profile Summary")
profile_summary = st.text_area("Write a short profile/introduction")

# --- Skills ---
st.header("🛠 Skills")
num_skills = st.number_input("How many skills do you want to add?", min_value=0, max_value=20, value=3)
skills = [st.text_input(f"Skill #{i+1}") for i in range(num_skills)]

# --- Experiences ---
st.header("💼 Experiences")
num_exp = st.number_input("How many experiences do you want to add?", min_value=0, max_value=10, value=2)
experiences = [st.text_area(f"Experience #{i+1}") for i in range(num_exp)]

# --- Education ---
st.header("🎓 Education")
num_edu = st.number_input("How many education details do you want to add?", min_value=0, max_value=10, value=2)
education = [st.text_area(f"Education #{i+1}") for i in range(num_edu)]

# --- Generate CV ---
if st.button("📄 Generate CV"):
    pdf = PDF("P", "mm", "A4")
    pdf.add_page()

    # --- Background ---
    pdf.set_fill_color(30, 30, 30)  # Dark gray
    pdf.rect(0, 0, 210, 297, "F")  # Fill whole page

    # --- Title ---
    pdf.set_text_color(255, 215, 0)  # Gold/yellow
    pdf.set_font("Helvetica", "B", 24)
    pdf.cell(0, 20, name, ln=True, align="C")

    # --- Add Photo ---
    if photo is not None:
        img = Image.open(photo)
        img_path = "temp_photo.png"
        img.save(img_path)
        pdf.image(img_path, x=170, y=10, w=30, h=30)
        os.remove(img_path)

    # --- Contact Info ---
    pdf.set_font("Helvetica", "", 12)
    pdf.set_text_color(255, 255, 255)
    pdf.ln(5)
    pdf.multi_cell(0, 8, f"📅 {birth_date}\n📧 {email}\n📞 {phone}\n📍 {address}")

    # --- Section: Profile ---
    pdf.ln(5)
    pdf.set_text_color(255, 215, 0)
    pdf.set_font("Helvetica", "B", 16)
    pdf.cell(0, 10, "📌 Profile", ln=True)
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("Helvetica", "", 12)
    pdf.multi_cell(0, 8, profile_summary)

    # --- Section: Skills ---
    if skills:
        pdf.ln(3)
        pdf.set_text_color(255, 215, 0)
        pdf.set_font("Helvetica", "B", 16)
        pdf.cell(0, 10, "🛠 Skills", ln=True)
        pdf.set_text_color(255, 255, 255)
        pdf.set_font("Helvetica", "", 12)
        for skill in skills:
            if skill:
                pdf.cell(0, 8, f"• {skill}", ln=True)

    # --- Section: Experience ---
    if experiences:
        pdf.ln(3)
        pdf.set_text_color(255, 215, 0)
        pdf.set_font("Helvetica", "B", 16)
        pdf.cell(0, 10, "💼 Experience", ln=True)
        pdf.set_text_color(255, 255, 255)
        pdf.set_font("Helvetica", "", 12)
        for exp in experiences:
            if exp:
                pdf.multi_cell(0, 8, f"• {exp}")
                pdf.ln(1)

    # --- Section: Education ---
    if education:
        pdf.ln(3)
        pdf.set_text_color(255, 215, 0)
        pdf.set_font("Helvetica", "B", 16)
        pdf.cell(0, 10, "🎓 Education", ln=True)
        pdf.set_text_color(255, 255, 255)
        pdf.set_font("Helvetica", "", 12)
        for edu in education:
            if edu:
                pdf.multi_cell(0, 8, f"• {edu}")
                pdf.ln(1)

    # --- Save PDF ---
    pdf_path = "Generated_CV.pdf"
    pdf.output(pdf_path)

    with open(pdf_path, "rb") as f:
        st.download_button("⬇️ Download CV", f, file_name="My_CV.pdf", mime="application/pdf")

    st.success("✅ Your CV has been generated successfully!")
