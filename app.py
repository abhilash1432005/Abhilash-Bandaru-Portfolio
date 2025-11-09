from flask import Flask, render_template, url_for

app = Flask(__name__)


# Sample data - replace with your real content
PROJECTS = [
    {
        "title": "AutoMobile management system",
        "description": "A website based automobile garage management system Login&Registration page for users.Gallery of spare parts and tools.Appointment booking&Costs and billing page.Technology Used: Python, Django, HTML&CSS..",
        "github": "https://github.com/abhilash1432005/Auto-mobile-managementsystem",
        "live": "#"
    },
    {
        "title": "Driver Drowsiness Detection using Computer Vision",
        "description": "Detects driver fatigue in real time using facial landmarks and EAR– Python, OpenCV, dlib for real-time face landmark detection– Alerts user when drowsiness or yawning is detected.",
        "github": "https://github.com/abhilash1432005/driver-drowsiness-detector.git",
        "live": "#"
    }
]

SKILLS = [
    {"name": "Python", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg"},
    {"name": "C Language", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/c/c-original.svg"},
    {"name": "Java Basics", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/java/java-original.svg"},
    {"name": "DBMS", "icon": "https://cdn-icons-png.flaticon.com/512/2772/2772128.png"},
    {"name": "Cloud Fundamentals", "icon": "https://cdn-icons-png.flaticon.com/512/4144/4144727.png"},
    {"name": "HTML & CSS", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg"}
]

CERTIFICATIONS = [
    {
        "title": "AWS Cloud Practitioner",
        "provider": "Amazon Web Services (AWS)",
        "image": "images/AWS CP.png",        # your image file
        "pdf": "certifications/Abhi CP certificate.pdf"      # your PDF file
    },
    {
        "title": "Microsoft Certified: Azure Fundamentals (AZ-900)",
        "provider": "Microsoft",
        "image": "images/Azure.png",
        "pdf": "certifications/Microsoft Azure AZ-900.pdf"
    },
    {
        "title": "Salesforce Certified AI Associate",
        "provider": "Salesforce",
        "image": "images/Sales force .png",
        "pdf": "certifications/Sales force AI Associate .pdf"
    },
    {
        "title": "Essential RPA Professional",
        "provider": "Automation Anywhere",
        "image": "images/RPA.png",
        "pdf": "certifications/RPA Essential.pdf"
    }
]
EMAIL_ADDRESS = "bandaruabhilash2005@gmail.com"  # replace this

@app.route("/")
def index():
    return render_template(
        "index.html",
        projects=PROJECTS,
        skills=SKILLS,
        certifications=CERTIFICATIONS,
        email=EMAIL_ADDRESS
    )


if __name__ == "__main__":
    app.run(debug=True)
