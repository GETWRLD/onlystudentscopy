from django.shortcuts import render
from .models import Subject

def subjects(request):
    subjects = Subject.objects.all()
    announcement = """!Уважаемые пользователи! Платформа находится на стадии разработки и имеет большое количество багов.\n
    Пожалуйста, при возникновении проблем, не покидайте платформу, а сообщите нам о проблеме.\n
    Наша почта: onlystudentsapp@gmail.com\n
    Мы сразу устраним неполадку.\n
    Хорошего пользования, команда OnlyStudents
    """

    context = {
        'subjects': subjects,
        'announcement': announcement
    }

    return render(request, 'projects/subjects.html', context)