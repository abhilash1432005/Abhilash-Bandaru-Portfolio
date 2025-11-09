from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt


def home(request):
    # -------------------------
    # PROJECTS
    # -------------------------
    projects = [
        {
            'title': 'Automobile Management System',
            'description': (
                'Developed a web-based application to streamline garage management and services. '
                'Built using Python (Django), HTML, CSS, and MySQL for efficient data handling. '
            ),
            'github': 'https://github.com/abhilash1432005/Auto-mobile-managementsystem.git'
        },
        {
            'title': 'Driver Drowsiness Detection System',
            'description': (
                'Implemented an AI-powered system using Deep Learning to monitor driver facial features '
                'in real time and detect signs of fatigue or drowsiness. '
                'The system triggers an alert to prevent accidents, enhancing road safety through automation.'
            ),
            'github': 'https://github.com/abhilash1432005/driver-drowsiness-detector.git'
        },
        {
            'title': 'Personal Portfolio Website',
            'description': (
                'Designed and developed this responsive personal portfolio using Django, Bootstrap. '
                'Integrated contact form email functionality and optimized static asset delivery for performance.'
            ),
            'github': 'https://github.com/abhilash1432005/portfolio'
        }
    ]

    # -------------------------
    # SKILLS (using image files from static/images)
    # -------------------------
    skills = [
        {'name': 'Python', 'icon': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg'},
        {'name': 'C Language', 'icon': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/c/c-original.svg'},
        {'name': 'Java Basics', 'icon': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/java/java-original.svg'},
        {'name': 'DBMS', 'icon': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mysql/mysql-original.svg'},
        {'name': 'Cloud Fundamentals',
         'icon': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/googlecloud/googlecloud-original.svg'},
        {'name': 'HTML & CSS', 'icon': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg'},
    ]

    # -------------------------
    # CERTIFICATIONS (use folder “Certifications”)
    # -------------------------
    certifications = [
        {
            'title': 'AWS Cloud Practitioner',
            'provider': 'Amazon Web Services',
            'image': 'images/AWS CP.png',
            'pdf': 'Certifications/Abhi CP certificate.pdf'
        },
        {
            'title': 'Microsoft Azure AZ-900',
            'provider': 'Microsoft',
            'image': 'images/Azure.png',
            'pdf': 'Certifications/Microsoft Azure AZ-900.pdf'
        },
        {
            'title': 'Salesforce AI Associate',
            'provider': 'Salesforce',
            'image': 'images/Sales force .png',
            'pdf': 'Certifications/Sales force AI Associate .pdf'
        },
        {
            'title': 'RPA Essential',
            'provider': 'Automation Anywhere',
            'image': 'images/RPA.png',
            'pdf': 'Certifications/RPA Essential.pdf'
        }
    ]

    return render(request, 'index.html', {
        'projects': projects,
        'skills': skills,
        'certifications': certifications,
        'email': 'bandaruabhilash2005@gmail.com',
        'title': 'Portfolio - Abhilash Bandaru'
    })


@csrf_exempt
def contact_api(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if not (name and email and message):
            return JsonResponse({'success': False, 'message': '⚠️ All fields are required.'})

        try:
            subject = f"New message from {name}"
            body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

            send_mail(
                subject,
                body,
                'bandaruabhilash2005@gmail.com',
                ['bandaruabhilash2005@gmail.com'],
                fail_silently=False,
            )
            return JsonResponse({'success': True, 'message': '✅ Message sent successfully!'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': f'❌ Failed to send: {e}'})

    return JsonResponse({'success': False, 'message': 'Invalid request method.'})
