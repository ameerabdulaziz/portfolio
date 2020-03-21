from django.shortcuts import render

from resume.models import Certificate, Experience, Field, Skill, Project


def index_view(request):
    experiences = Experience.objects.all().order_by('-start_date')
    certificates = Certificate.objects.all().order_by('-date')
    fields = Field.objects.all()
    skills = Skill.objects.all()
    projects = Project.objects.all()
    context = {
        'first_name': 'Ameer',
        'last_name': 'Abdulaziz',
        'address': 'Nasr city - Cairo, Egypt',
        'phone': '+20 111 326 4340',
        'email': 'ameer.abdulaziz93@gmail.com',
        'about': 'I am experienced in leveraging agile frameworks to provide a robust synopsis for high level '
                 'overviews. Iterative approaches to corporate strategy foster collaborative thinking to further '
                 'the overall value proposition.',
        'social': {
            'linkedin': 'https://www.linkedin.com/in/ameerabdulaziz/',
            'github': 'http://github.com/ameerabdulaziz/',
            'twitter': 'https://twitter.com/ameerabdulaziz_',
            'instagram': 'https://www.instagram.com/ameerabdulaziz_/',
        },
        'education': {
            'university': 'Modern Academy For Engineering & Technology',
            'department': 'Computer Engineering & Information Technology',
            'project_degree': 'A+',
            'gpa': '2.1',
            'start_date': 'September 2014',
            'end_date': 'June 2020'
        },
        'experiences': experiences,
        'certificates': certificates,
        'fields': fields,
        'skills': skills,
        'projects': projects,
    }
    return render(request, 'resume/base.html', context)
