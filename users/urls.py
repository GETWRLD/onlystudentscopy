from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('register/', views.registerUser, name='register'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('mentors/<str:pk>/', views.mentors, name='mentors'),
    path('profile/<str:pk>/', views.profile, name='profile'),
    path('projectform/<str:mentor>/', views.createrequest, name='projectform'),
    path('requests/<str:pk>/', views.projects, name='requests'),
    path('onerequest/<str:pk>/', views.oneproject, name='onerequest'),
    path('allmentors/', views.allmentors, name='allmentors'),
    path('requests-as-mentor/<str:pk>/', views.projects_as_mentor, name='projectsasmentor'),
    path('requests-as-student/<str:pk>/', views.projects_as_student, name='projectsasstudent'),
    path('completed-requests/<str:pk>/', views.completed_projects, name='completedprojects'),
    path('pending-requests/<str:pk>/', views.pending_projects, name='pendingprojects'),
    path('allrequests/', views.allprojects, name='allrequests'),
    path('request-review/<str:pk>/', views.projectreview, name='projectreview'),
    path('inbox/', views.inbox, name="inbox"),
    path('message/<str:pk>/', views.viewMessage, name="message"),
    path('create-message/<str:pk>/', views.createMessage, name="create-message"),
    path('create-messageroom/<str:pk>/', views.createmessageroom, name='createmessageroom'),
    path('messageroomslist/', views.messageroomslist, name='messageroomslist'),
    path('messageroom/<str:pk>/', views.messageroom, name='messageroom'),
    path('account/', views.account, name='account'),
    path('edit-account/', views.editaccount, name='edit-account'),
    path('apply-for-mentor/', views.applyformentor, name='applyformentor'),
    #path('apply-for-teacher/', views.applyforteacher, name='applyforteacher'),
    path('publicprojectform/<str:pk>/', views.createpublicrequest, name='createpublicrequest'),
    #path('students-list/', views.students_list, name='studentslist')
    path('confidentialpolicy/', views.confidential_policy, name='confidentialpolicy'),
    path('test/', views.test, name='test')
]