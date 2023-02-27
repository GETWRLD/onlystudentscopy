from django.shortcuts import render
from .models import Subject

def subjects(request):
    subjects = Subject.objects.all()

    context = {
        'subjects': subjects
    }

    return render(request, 'projects/subjects.html', context)