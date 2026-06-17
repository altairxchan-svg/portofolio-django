from django.shortcuts import render

def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def skills(request):
    skills = [
        {'icon': 'fa-brands fa-html5',    'name': 'HTML5',          'level': 90},
        {'icon': 'fa-brands fa-css3-alt', 'name': 'CSS3 / SASS',    'level': 85},
        {'icon': 'fa-brands fa-js',       'name': 'JavaScript',      'level': 75},
        {'icon': 'fa-brands fa-python',   'name': 'Python / Django', 'level': 70},
        {'icon': 'fa-brands fa-php',      'name': 'PHP / Laravel',   'level': 65},
        {'icon': 'fa-solid fa-shield-halved', 'name': 'Cyber Security', 'level': 70},
    ]
    skill_cards = [
        {'icon': 'fa-brands fa-html5',    'name': 'HTML5',          'desc': 'Semantic markup, accessibility, dan struktur halaman yang solid.'},
        {'icon': 'fa-brands fa-css3-alt', 'name': 'CSS3 & SASS',    'desc': 'Responsive design, animasi, flexbox, grid, dan custom properties.'},
        {'icon': 'fa-brands fa-js',       'name': 'JavaScript',     'desc': 'ES6+, DOM manipulation, async/await, dan fetch API.'},
        {'icon': 'fa-brands fa-python',   'name': 'Python & Django','desc': 'Backend development, ORM, REST API, dan Django templates.'},
        {'icon': 'fa-brands fa-php',      'name': 'PHP & Laravel',  'desc': 'MVC pattern, Eloquent ORM, Blade templating, dan routing.'},
        {'icon': 'fa-solid fa-shield-halved','name':'Cyber Security','desc': 'Memahami keamanan aplikasi web, vulnerability assessment, penetration testing dasar, dan penerapan praktik keamanan yang baik.'},
        {'icon': 'fa-brands fa-react',    'name': 'React (Basic)',  'desc': 'Component-based UI, hooks, dan state management dasar.'},
        {'icon': 'fa-brands fa-git-alt',  'name': 'Git & GitHub',   'desc': 'Version control, branching, pull request, dan kolaborasi tim.'},
    ]
    return render(request, 'main/skills.html', {'skills': skills, 'skill_cards': skill_cards})

def services(request):
    services = [
        {'icon': 'fa-solid fa-code',       'title': 'Web Development',   'desc': 'Membangun website modern, cepat, dan responsif menggunakan HTML, CSS, JavaScript, Django, maupun Laravel sesuai kebutuhanmu.', 'items': ['Company Profile', 'Landing Page', 'Web Application']},
        {'icon': 'fa-solid fa-paintbrush', 'title': 'UI/UX Design',      'desc': 'Merancang tampilan antarmuka yang menarik, intuitif, dan memberikan pengalaman pengguna yang menyenangkan.',            'items': ['Wireframing', 'Mockup Design', 'Prototyping']},
        {'icon': 'fa-solid fa-mobile-screen','title': 'Responsive Design','desc': 'Memastikan website kamu tampil sempurna di semua perangkat, mulai dari desktop, tablet, hingga smartphone.',             'items': ['Mobile-first', 'Cross-browser', 'Performance Optimization']},
       {'icon': 'fa-solid fa-shield-halved', 'title': 'Cyber Security', 'desc': 'Membantu melindungi website dan aplikasi dari berbagai ancaman keamanan siber melalui analisis, pengujian, dan penerapan praktik keamanan terbaik.','items': [ 'Vulnerability Assessment',  'Security Audit', 'Web Application Security' ]},
        {'icon': 'fa-solid fa-magnifying-glass-chart','title': 'SEO Optimization','desc': 'Meningkatkan visibilitas websitemu di mesin pencari dengan teknik SEO on-page yang telah terbukti efektif.', 'items': ['Meta Optimization', 'Page Speed', 'Structured Data']},
        {'icon': 'fa-solid fa-headset',    'title': 'Tech Consulting',   'desc': 'Memberikan saran teknis strategis untuk membantu bisnismu memilih teknologi dan stack yang tepat.',                     'items': ['Tech Stack Advisory', 'Code Review', 'Project Planning']},
    ]
    return render(request, 'main/services.html', {'services': services})

def blogs(request):
    blogs = [
        {'category': 'webdev',      'icon': 'fa-brands fa-django',             'tag_label': 'Web Dev',    'title': 'Getting Started with Django REST Framework', 'excerpt': 'Panduan lengkap untuk membangun API yang powerful dengan Django dan DRF.', 'date': '15 Jan 2025', 'read_time': '8 min read'},
        {'category': 'css',         'icon': 'fa-brands fa-css3-alt',           'tag_label': 'CSS',        'title': 'Mastering CSS Scroll Snap',                   'excerpt': 'Cara membuat smooth full-page scrolling yang mulus tanpa JavaScript.',   'date': '3 Feb 2025',  'read_time': '5 min read'},
        {'category': 'javascript',  'icon': 'fa-brands fa-js',                 'tag_label': 'JavaScript', 'title': '10 JavaScript Tips Wajib Tahu',               'excerpt': 'Dari destructuring hingga optional chaining — tingkatkan skill JS kamu.', 'date': '20 Mar 2025', 'read_time': '6 min read'},
        {'category': 'python',      'icon': 'fa-brands fa-python',             'tag_label': 'Python',     'title': 'Django ORM: Tips & Tricks',                   'excerpt': 'Kumpulan tips menggunakan Django ORM secara efisien.',                  'date': '5 Apr 2025',  'read_time': '7 min read'},
        {'category': 'css',         'icon': 'fa-solid fa-wand-magic-sparkles', 'tag_label': 'CSS',        'title': 'CSS Animations yang Bikin Website Hidup',      'excerpt': 'Tutorial membuat animasi CSS yang smooth dan performant.',              'date': '18 Apr 2025', 'read_time': '6 min read'},
        {'category': 'Cyberscurity',      'icon': 'fa-solid fa-shield-halved',       'tag_label': 'Cyberscurity',    'title': 'Keamanan Web: Ancaman dan Cara Mencegahnya',   'excerpt': 'Pelajari ancaman keamanan web paling umum seperti XSS, CSRF, dan SQL Injection.', 'date': '25 Apr 2025', 'read_time': '9 min read'},
    ]
    return render(request, 'main/blogs.html', {'blogs': blogs})

from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')

        send_mail(
            subject=f'Portfolio Contact: {subject}',
            message=f'''
Nama: {name}
Email: {email}

Pesan:
{message}
''',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=['links7467@gmail.com'],
            fail_silently=False,
        )

        return render(
            request,
            'main/contact.html',
            {
                'success': True,
                'success_name': name
            }
        )

    return render(request, 'main/contact.html')


from django.http import HttpResponse
