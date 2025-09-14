import re

print("\033[1;93mHello,👋 Welcome to the Automatic CV Creator. This application was created by - Avin Regmi.")
print("\033[1;93mTo start making the CV we might require some information.\n")
print("\033[1;93mNote: None of this information is being stored. So, let's begin!.\n")

# Collecting user input
Name = input(f"\033[1;97mWhat is your name?:\033[1;93m ")
Howmuchyear = int(input(f"\033[1;97mWhat is your current age?:\033[1;93m "))
Field = input(f"\033[1;97mWhat is your field? (Science, Maths, Design, Arts, etc):\033[1;93m ")

while True:
    BornStatement = input(f"\033[1;97mWhat was your birth date (YYYY/MM/DD)?: ")
    if re.match(r"^\d{4}/\d{2}/\d{2}$", BornStatement):
        break
    else:
        print("❌ Please enter in correct format: YYYY/MM/DD")

PhoneNumber = input(f"\033[1;97mWhat is your business email or phone number?: ")
LivingSpace = input(f"\033[1;97mWhere do you live?: ")

# ------------------- EDUCATION -------------------
educations = []
Education = int(input(f"\033[1;97mHow many education levels do you have? "))
for i in range(Education):
    while True:
        education = input(f"Education #{i + 1} (Format: Level for Subject): ")
        if re.match(r"^[A-Za-z ]+ for [A-Za-z ]+$", education):
            educations.append(education)
            break
        else:
            print("❌ Please enter in correct format: (Education_level) for (Subject)")

# ------------------- SKILLS -------------------
skills = []
Skills = int(input(f"\033[1;97mHow many skills do you have?: "))
for i in range(Skills):
    skill = input(f"Skill #{i+1}: ")
    skills.append(skill)

# ------------------- HOBBIES -------------------
Hobbies = []
HobbiesNumber = int(input(f"\033[1;97mHow many hobbies do you have? [Write in Number]: "))
for i in range(HobbiesNumber):
    hob = input(f"Hobby #{i+1}: ")
    Hobbies.append(hob)
print(" ")

# ------------------- LANGUAGES -------------------
languages = []
NumberOfLang = int(input(f"\033[1;97m🌐 How many languages can you speak?: "))
for i in range(NumberOfLang):
    while True:
        Language = input(f"Language #{i+1} (Format: Language - Level): ")
        if re.match(r"^[A-Za-z ]+\s*-\s*[A-Za-z ]+$", Language):
            languages.append(Language)
            break
        else:
            print("❌ Please enter in correct format: [Language_name] - [Language_Level]")
print(" ")

# ------------------- WORK EXPERIENCES -------------------
experiences = []
num_exp = int(input(f"\033[1;97m🧰 How many work experiences do you have (Ex: 2,3,4,etc.)?: "))
for i in range(num_exp):
    print(f"\033[1;97m🧰 Work Experience #{i+1}")
    Job = input("Job Title: ")
    Company = input("Company Name: ")
    Years = input("Years (e.g., 2020-2023): ")
    Description = input("Brief Description: ")
    experiences.append({
        "Job": Job,
        "Company": Company,
        "Years": Years,
        "Description": Description
    })

# ------------------- CERTIFICATIONS -------------------
certifications = []
num_certs = int(input(f"\033[1;97m📜 How many certifications do you want to add?: "))
for i in range(num_certs):
    print(f"\033[1;97m📄 Certification #{i+1}")
    cert_title = input("Certification Title: ")
    issuer = input("Issued by: ")
    certifications.append({
        "Title": cert_title,
        "Issuer": issuer
    })

# ------------------- PROCESSING -------------------
print("\nProcessing your data...")
for dots in range(1, 5):
    print("." * dots)

# ------------------- OUTPUT -------------------
print(f"\n\033[1;93mAbout Me:\033[0m")
print(f"\033[1;97mI am a dedicated and adaptable individual with a strong passion for growth and learning.")
print(f"My name is {Name}, and I am {Howmuchyear} years old.")
print(f"I aim to grow in the field of {Field} while contributing value to teams and organizations.\033[0m\n")

print(f"\033[1;93mContacts:\033[0m")
print(f"\033[1;97m📞 {PhoneNumber}")
print(f"📍 {LivingSpace}")
print(f"🎂 Born in: {BornStatement}\033[0m\n")

print(f"\033[1;93mSkills:\033[0m")
for i, skil in enumerate(skills, 1):
    print(f"\033[1;97m{i}. {skil}\033[0m")

print(f"\n\033[1;93mLanguages:\033[0m")
for i, lang in enumerate(languages, 1):
    print(f"\033[1;97m{i}. {lang}\033[0m")

print(f"\n\033[1;93mWork Experiences:\033[0m")
for i, exp in enumerate(experiences, 1):
    print(f"\033[1;97m{i}. {exp['Job']} at {exp['Company']} ({exp['Years']})")
    print(f"   → {exp['Description']}\033[0m")

print(f"\n\033[1;93mEducation:\033[0m")
for i, edu in enumerate(educations, 1):
    print(f"\033[1;97m{i}. {edu}\033[0m")

print(f"\n\033[1;93mHobbies:\033[0m")
for i, hob in enumerate(Hobbies, 1):
    print(f"\033[1;97m{i}. {hob}\033[0m")

print(f"\n\033[1;93mCertifications:\033[0m")
for i, cert in enumerate(certifications, 1):
    print(f"\033[1;97m{i}. {cert['Title']} (Issued by: {cert['Issuer']})\033[0m")
