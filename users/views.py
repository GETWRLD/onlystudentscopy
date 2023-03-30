from django.shortcuts import render, redirect
from .models import Profile, Project, Review, Messageroom, Skill, Teacher
from .forms import CustomUserCreationForm, ProjectForm, MessageForm, MessageroomForm, ActiveProjectForm, StudentAccountForm, MentorApplyForm, TeacherApplyForm, MentorAccountForm, TeacherAccountForm, ProjectReviewForm, ApplyTeacherRequest
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from projects.models import Subject
from .utils import searchprofiles
from django.core.mail import send_mail
from django.conf import settings

#import cloudinary.uploader



def error_404(request, exception):
    return render(request, '404.html')


def error_500(request):
    return render(request, '404.html')


def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'User account was created!')
            return redirect('subjects')
        
        else:
            messages.success(request, 'An error has occured during registration!')

    context = {
        'page':page,
        'form':form
    }

    return render(request, 'users/login_register.html', context)


def loginUser(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect("subjects")

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        username = username.lower()

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')

        user = authenticate(request, username=username, password=password)

        if user != None:
            login(request, user)
            return redirect("subjects")
        else:
            messages.error(request, 'Username OR password is incorrect')

    context = {
      'page': page
    }
    
    return render(request, 'users/login_register.html', context)
      
def logoutUser(request):
  logout(request)
  messages.info(request, "User was logged out")
  return redirect('login')


def mentors(request, pk):
    subject = Subject.objects.get(title=pk)
    profiles = Profile.objects.filter(subjects=subject)
    profiles_search = searchprofiles(request)
    page = 'mentors'

    context = {
        'profiles': profiles,
        'subject': subject,
        'page': page,
        'profiles_search': profiles_search
    }

    return render(request, 'users/subject_mentors.html', context)


def profile(request, pk):
    profile = Profile.objects.get(username=pk)

    context = {
        'profile': profile
    }

    return render(request, 'users/profile.html', context)


def createrequest(request, mentor):
    form = ProjectForm()
    mentor = Profile.objects.get(username=mentor)
    student = request.user.profile

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.student = student
            project.mentor = mentor
            project.save()
            send_mail(
            f'Вам пришел запрос "{project.title}" от {project.student}',
            f"""Запрос "{project.title}" от {project.student} находится во вкладке личных запросов.\n
            Вы можете принять его, зайдя в меню личных запросов (через навигационную панель наверху страницы).\n 
            OnlyStudents""",
            settings.EMAIL_HOST_USER,
            [mentor.email],
            fail_silently=False,
            )
        
            send_mail(
                f'Ваш запрос "{project.title}" был успешно отправлен ментору {project.mentor}',
                f"""Запрос "{project.title}" был успешно отправлен ментору {project.mentor}\n
                Ожидайте, пока ментор примет его, или подайте публичную заявку, которую примет первый свободный ментор.\n 
                OnlyStudents""",
                settings.EMAIL_HOST_USER,
                [student.email],
                fail_silently=False,
                )

            return redirect('profile', pk=mentor.username)
        
    context = {
        'form': form
    }

    return render(request, 'users/projectform.html', context)


def createpublicrequest(request, pk):
    form = ProjectForm()
    student = request.user.profile

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.student = student
            project.private = False
            project.save()
            return redirect('allrequests')

    context = {
        'form': form
    }

    return render(request, 'users/projectform.html', context)


def projects(request, pk):
    mentor = Profile.objects.get(id=pk)
    projects = Project.objects.filter(mentor=mentor)

    context = {
        'projects': projects
    }

    return render(request, 'users/requests.html', context)

def projects_as_mentor(request, pk):
    page = 'mentor'
    mentor = Profile.objects.get(id=pk)
    projects = Project.objects.filter(mentor=mentor)
    suitable_projects = []
    for project in projects:
        if project.is_completed == False and project.is_accepted == True:
            suitable_projects.append(project)

    context = {
        'projects': suitable_projects,
        'page': page
    }

    return render(request, 'users/requests.html', context)


def projects_as_student(request, pk):
    page = 'student'
    mentor = Profile.objects.get(id=pk)
    projects = Project.objects.filter(student=mentor)
    suitable_projects = []
    for project in projects:
        if project.is_completed == False and project.is_accepted == True:
            suitable_projects.append(project)

    context = {
        'projects': suitable_projects,
        'page': page
    }

    return render(request, 'users/requests.html', context)


def completed_projects(request, pk):
    page = 'completed'
    mentor = Profile.objects.get(id=pk)
    projects_mentor = Project.objects.filter(mentor=mentor)
    projects_student = Project.objects.filter(student=mentor)
    suitable_projects = []
    for project in projects_mentor:
        if project.is_completed == True and project.is_accepted == True:
            suitable_projects.append(project)
    for project in projects_student:
        if project.is_completed == True and project.is_accepted == True:
            suitable_projects.append(project)
            
    context = {
        'projects': suitable_projects,
        'page': page
    }

    return render(request, 'users/requests.html', context)


def pending_projects(request, pk):
    page = 'pending'
    mentor = Profile.objects.get(id=pk)
    projects_mentor = Project.objects.filter(mentor=mentor)
    projects_student = Project.objects.filter(student=mentor)
    suitable_projects = []
    for project in projects_mentor:
        if project.is_completed == False and project.is_accepted == False:
            suitable_projects.append(project)
    for project in projects_student:
        if project.is_completed == False and project.is_accepted == False:
            suitable_projects.append(project)

    context = {
        'projects': suitable_projects,
        'page': page
    }

    return render(request, 'users/requests.html', context)


def oneproject(request, pk):
    onerequest = Project.objects.get(id=pk)
    active_project_form = ActiveProjectForm(instance=onerequest)
    mentor = onerequest.mentor
    student = onerequest.student
    reviewed = False
    if onerequest.review_set.all():
        reviewed = True

    if request.method == 'POST':
        if 'accept_request'  in request.POST:
            onerequest.mentor = request.user.profile
            onerequest.is_accepted = True
            onerequest.save()
            send_mail(
            f'Ваш запрос "{onerequest.title}" был принят ментором {mentor}',
            f"""Запрос "{onerequest.title}" был принят ментором. Поспешите проверить его. \n 
            OnlyStudents""",
            settings.EMAIL_HOST_USER,
            [student.email],
            fail_silently=False,
            )

        if 'finish_project' in request.POST:
            onerequest.is_completed = True
            onerequest.save()
            request.user.profile.requests_number

            send_mail(
            f'Ваш запрос "{onerequest.title}" был завершен',
            f"""Запрос "{onerequest.title}", где вы были ментором был завершен \n 
            Хорошего пользования, команда OnlyStudents""",
            settings.EMAIL_HOST_USER,
            [mentor.email],
            fail_silently=False,
            )

            send_mail(
            f'Ваш запрос "{onerequest.title}" был завершен',
            f"""Ваш запрос "{onerequest.title}" был завершен \n
            Не забудьте поставить ментору отзыв.\n 
            Хорошего пользования, команда OnlyStudents""",
            settings.EMAIL_HOST_USER,
            [student.email],
            fail_silently=False,
            )

        if 'save-edit-project' in request.POST:
            form = ActiveProjectForm(request.POST, instance=Project.objects.get(id=pk))
            if form.is_valid():
                onerequest = form.save(commit=False)
                onerequest.save()
                return redirect('onerequest', pk=onerequest.id)


    context = {
        'onerequest': onerequest,
        'active_project_form': active_project_form,
        'reviewed': reviewed
    }

    return render(request, 'users/onerequest.html', context)


def projectreview(request, pk):
    onerequest = Project.objects.get(id=pk)
    review_form = ProjectReviewForm()
    profile = onerequest.mentor
    reviewed = False
    if onerequest.review_set.all():
        reviewed = True

    if request.method == 'POST':
        review_form = ProjectReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.owner = request.user.profile
            review.project = onerequest
            review.save()
            profile.reviews_ratio
            profile.requests_number
            

        return redirect('subjects')

    context = {
        'review_form': review_form
    }

    return render(request, 'users/projectreview.html', context)



def allmentors(request):
    profiles = Profile.objects.all()
    page = 'allmentors'
    profiles_search = searchprofiles(request)

    context = {
        'profiles': profiles,
        'page': page,
        'profiles_search': profiles_search
    }

    return render(request, 'users/allmentors.html', context)


def allprojects(request):
    projects = Project.objects.filter(private=False)

    context = {
        'projects': projects
    }

    return render(request, 'users/allrequests.html', context)
    

def inbox(request):
  profile = request.user.profile
  messageRequests = profile.messages.all()
  unreadCount = messageRequests.filter(is_read=False).count()
  context = {
    'messageRequests': messageRequests,
    'unreadCount': unreadCount,
  }
  return render(request, 'users/inbox.html', context) 


def viewMessage(request, pk):
  profile = request.user.profile
  message = profile.messages.get(id=pk)
  if message.is_read == False:
    message.is_read = True
    message.save()
  context = {
    'message': message,
  }
  return render(request, 'users/message.html', context)


def createMessage(request, pk):
  recipient = Profile.objects.get(username=pk)
  form = MessageForm()

  try:
    sender = request.user.profile
  except:
    sender = None

  if request.method == 'POST':

    form = MessageForm(request.POST)
    if form.is_valid():
      message = form.save(commit=False)
      message.sender = sender
      message.recepient = Profile.objects.get(username=pk)

      if sender:
        message.name = sender.name
        message.email = sender.email
      
      message.save()

      messages.success(request, 'Your message was successfully sent!')
      return redirect('profile', pk=recipient.username)

  context = {
    'recepient': recipient,
    'form': form,
  }
  return render(request, 'users/message_form.html', context)


def createmessageroom(request, pk):
    user2 = Profile.objects.get(username=pk)
    form = MessageroomForm
    user1 = request.user.profile

    if request.method == 'POST':
        form = MessageroomForm(request.POST)
        if form.is_valid():
            messagerooms = Messageroom.objects.all()
            messageroom = form.save(commit=False)
            messageroom.user1 = user1
            messageroom.user2 = Profile.objects.get(username=pk)
            messageroom.name = f"{user2.username}+{user1.username}"
            for messageroom1 in messagerooms:
                if messageroom1.user2 == messageroom.user2:
                    if messageroom1.user1 == messageroom.user1:
                        return redirect('subjects')
                else:
                    send_mail(
                    f'Чат с "{user2}" был создан',
                    f"""Чат с "{user2}", был создан. Не забывайте проверять его почаще! \n 
                    OnlyStudents""",
                    settings.EMAIL_HOST_USER,
                    [user1.email],
                    fail_silently=False,
                    )

                    send_mail(
                    f'Чат с "{user1}" был создан',
                    f"""Чат с "{user1}", был создан. Не забывайте проверять его почаще! \n 
                    OnlyStudents""",
                    settings.EMAIL_HOST_USER,
                    [user2.email],
                    fail_silently=False,
                    )
                    messageroom.save()
                    return redirect('subjects')

            messages.success(request, 'Your message was successfully sent!')
            
            return redirect('profile', pk=user2.username)


    context = {
    'user2': user2,
    'form': form,
    }
    return render(request, 'users/messageroom_form.html', context)



def messageroomslist(request):
    user = request.user.profile

    messagerooms1 = Messageroom.objects.filter(user1=user)
    messagerooms2 = Messageroom.objects.filter(user2=user)

    messagerooms = messagerooms1 | messagerooms2

    context = {
        'messagerooms': messagerooms
    }

    return render(request, 'users/messageroomslist.html', context)


def messageroom(request, pk):
    messageroom = Messageroom.objects.get(id=pk)
    form = MessageForm()
    sender = request.user.profile
    if messageroom.user1 == request.user.profile:
        recepient = messageroom.user2
    elif messageroom.user2 == request.user.profile:
        recepient = messageroom.user1

    messages = messageroom.message_set.all()

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = sender
            message.messageroom = messageroom
            message.save()

            return redirect('messageroom', pk=messageroom.id)

    context = {
        'messages': messages,
        'form': form,
        'sender': sender,
        'recepient': recepient
    }

    return render(request, 'users/messageroom.html', context)


def account(request):
    account = request.user.profile

    context = {
        'account': account
    }

    return render(request, 'users/account.html', context)


def editaccount(request):
    account = request.user.profile
    if request.user.profile.role == 'student':
        form = StudentAccountForm(instance=account)

        if request.method == 'POST':
            form = StudentAccountForm(request.POST, request.FILES, instance=account)
            if form.is_valid():
                form.save()
                return redirect('account')

    if request.user.profile.role == 'mentor':
       form = MentorAccountForm(instance=account)

       if request.method == 'POST':
           form = MentorAccountForm(request.POST, request.FILES, instance=account)
           if form.is_valid():
               #upload_result = cloudinary.uploader.upload(request.FILES['profile_image'])
               form.save()
               return redirect('account')

    if request.user.profile.role == 'teacher':
       form = TeacherAccountForm(instance=account)

       if request.method == 'POST':
           form = TeacherAccountForm(request.POST, request.FILES, instance=account)
           if form.is_valid():
               form.save()
               return redirect('account')

    context = {
        'account': account,
        'form': form
    }

    return render(request, 'users/account_form.html', context)


def mentorsstats(request):
    mentors = Profile.objects.filter(role='mentor')

    context = {
        'mentors': mentors
    }

    return render(request, 'users/mentorsstats.html', context)


def applyformentor(request):
    page = 'mentor'
    mentorform = MentorApplyForm()
    user = request.user.profile

    if request.method == 'POST':
        mentorform = MentorApplyForm(request.POST, instance=user)
        if mentorform.is_valid():
            mentor = mentorform.save(commit=False)
            user.role = 'mentor'
            mentor.save()

            return redirect('subjects')

    context = {
        'user': user,
        'mentorform': mentorform,
        'page': page
    }

    return render(request, 'users/applyforrole.html', context)


def applyforteacher(request):
    page = 'teacher'
    user = request.user.profile
    form = TeacherApplyForm

    if request.method == 'POST':
        form = TeacherApplyForm(request.POST)
        if form.is_valid():
            teacher = ApplyTeacherRequest.objects.create(owner=user)
            

    context = {
        'user': user,
        'page': page,
        'form': form
    }

    return render(request, 'users/applyforrole.html', context)


def students_list(request):
    teacherr = request.user.teacher
    students = teacherr.students.all()
    context = {
        'students': students
    }

    return render(request, 'users/students_list.html', context)


def confidential_policy(request):

    return render(request, 'users/confidential_policy.html')


