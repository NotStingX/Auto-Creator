import streamlit as st
from fpdf import FPDF
from PIL import Image
import os

# Custom PDF class
class PDF(FPDF):
    def header(self):
        pass

    def footer(self):
        pass


# Streamlit app
st.set_page_config(page_title="CV Creator", layout="centered")
st.title("📄 Automatic CV Creator")

st.header("Personal Information")
name = st.text_input("Full Name")
birthdate = st.text_input("Birthdate (DD/MM/YYYY)")
email = st.text_input("Email")
phone = st.text_input("Phone")
address = st.text_input("Address")
photo = st.file_uploader("Upload Profile Photo", type=["jpg", "jpeg", "png"])

st.header("Profile")
profile = st.text_area("Short Profile Introduction")

st.header("Skills")
num_skills = st.number_input("How many skills do you want to add?", min_value=0, max_value=20, step=1)
skills = []
for i in range(int(num_skills)):
    skills.append(st.text_input(f"Skill #{i+1}"))

st.header("Experience")
num_experiences = st.number_input("How many experiences do you want to add?", min_value=0, max_value=10, step=1)
experiences = []
for i in range(int(num_experiences)):
    exp_title = st.text_input(f"Experience #{i+1} - Job Title")
    exp_desc = st.text_area(f"Experience #{i+1} - Description")
    experiences.append((exp_title, exp_desc))

st.header("Education")
num_edu = st.number_input("How many education entries do you want to add?", min_value=0, max_value=10, step=1)
education = []
for i in range(int(num_edu)):
    edu_title = st.text_input(f"Education #{i+1} - Degree/Program")
    edu_school = st.text_input(f"Education #{i+1} - School/Institution")
    education.append((edu_title, edu_school))


# Generate PDF
if st.button("Generate CV"):
    pdf = PDF()
    pdf.add_page()

    # Set background black/gray
    pdf.set_fill_color(30, 30, 30)  # dark gray
    pdf.rect(0, 0, 210, 297, 'F')   # A4 size background

    # Add profile photo if uploaded
    if photo:
        img = Image.open(photo)
        img_path = "temp_photo.png"
        img.save(img_path)
        pdf.image(img_path, 160, 10, 35, 35)
        os.remove(img_path)

    # Title (name)
    pdf.set_text_color(255, 255, 0)  # yellow
    pdf.set_font("Arial", 'B', 20)
    pdf.cell(0, 10, name, ln=True, align="L")

    pdf.set_font("Arial", '', 12)
    pdf.set_text_color(255, 255, 255)  # white for text
    pdf.cell(0, 10, f"Birthdate: {birthdate}", ln=True)
    pdf.cell(0, 10, f"Email: {email}", ln=True)
    pdf.cell(0, 10, f"Phone: {phone}", ln=True)
    pdf.cell(0, 10, f"Address: {address}", ln=True)

    pdf.ln(5)

    # Profile
    pdf.set_font("Arial", 'B', 16)
    pdf.set_text_color(255, 255, 0)  # yellow heading
    pdf.cell(0, 10, "PROFILE", ln=True)

    pdf.set_font("Arial", '', 12)
    pdf.set_text_color(255, 255, 255)
    pdf.multi_cell(0, 10, profile)

    pdf.ln(5)

    # Skills
    if skills:
        pdf.set_font("Arial", 'B', 16)
        pdf.set_text_color(255, 255, 0)
        pdf.cell(0, 10, "SKILLS", ln=True)

        pdf.set_font("Arial", '', 12)
        pdf.set_text_color(255, 255, 255)
        for skill in skills:
            pdf.cell(0, 10, f"- {skill}", ln=True)

        pdf.ln(5)

    # Experience
    if experiences:
        pdf.set_font("Arial", 'B', 16)
        pdf.set_text_color(255, 255, 0)
        pdf.cell(0, 10, "EXPERIENCE", ln=True)

        pdf.set_font("Arial", '', 12)
        pdf.set_text_color(255, 255, 255)
        for title, desc in experiences:
            pdf.set_font("Arial", 'B', 12)
            pdf.cell(0, 10, title, ln=True)
            pdf.set_font("Arial", '', 12)
            pdf.multi_cell(0, 10, desc)
            pdf.ln(3)

        pdf.ln(5)

    # Education
    if education:
        pdf.set_font("Arial", 'B', 16)
        pdf.set_text_color(255, 255, 0)
        pdf.cell(0, 10, "EDUCATION", ln=True)

        pdf.set_font("Arial", '', 12)
        pdf.set_text_color(255, 255, 255)
        for degree, school in education:
            pdf.cell(0, 10, f"{degree} - {school}", ln=True)

    # Save PDF
    pdf_output = "cv_output.pdf"
    pdf.output(pdf_output)

    # Show download link
    with open(pdf_output, "rb") as f:
        st.download_button("📥 Download CV", f, file_name="My_CV.pdf")
