from django.db import models
from django.contrib.auth.models import User
import uuid
from projects.models import Subject
    

class Teacher(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
  name = models.CharField(max_length=200, blank=True, null=True)
  email = models.EmailField(max_length=500, blank=True, null=True)
  created = models.DateTimeField(auto_now_add=True)
  id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
  students = models.ManyToManyField('Profile', blank=True)

  def __str__(self):
      return str(self.name)


class Profile(models.Model):
  ROLE_TYPE = (
    ('mentor', 'Mentor'),
    ('student', 'Student'),
    ('teacher', 'Teacher')
  )
  user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
  email = models.EmailField(max_length=500, blank=True, null=True)
  username = models.CharField(max_length=200, blank=True, null=True)
  location = models.CharField(max_length=200, blank=True, null=True)
  short_intro = models.CharField(max_length=200, blank=True, null=True)
  bio = models.TextField(blank=True, null=True)
  profile_image = models.ImageField(null=True, blank=True, upload_to='images/profiles/', default="images/user.png")
  social_instagram = models.CharField(max_length=200, blank=True, null=True)
  social_twitter = models.CharField(max_length=200, blank=True, null=True)
  social_linkedin = models.CharField(max_length=200, blank=True, null=True)
  social_youtube = models.CharField(max_length=200, blank=True, null=True)
  social_website = models.CharField(max_length=200, blank=True, null=True)
  social_vk = models.CharField(max_length=200, blank=True, null=True)
  social_telegram = models.CharField(max_length=200, blank=True, null=True)
  created = models.DateTimeField(auto_now_add=True)
  id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
  subjects = models.ManyToManyField(Subject, blank=True)
  classs = models.IntegerField(blank=True, null=True)
  vote_total = models.IntegerField(default=0, null=True, blank=True)
  vote_ratio = models.IntegerField(default=0, null=True, blank=True)
  role = models.CharField(max_length=200, choices=ROLE_TYPE, default='student')
  skill = models.ManyToManyField('Skill', blank=True)
  teachers = models.ManyToManyField(Teacher, blank=True)

  def __str__(self):
      return str(self.username)
  
      class Meta:
        ordering = ['created']

  @property
  def imageURL(self):
    try:
      url = self.profile_image.url
    except:
      url = ""
    return url

  @property
  def reviews_ratio(self):
    projects_queryset = self.project_set.all()
    all_reviews_sum = 0
    reviews = 0
    for project in projects_queryset:
      review = Review.objects.get(project=project)
      all_reviews_sum = all_reviews_sum + int(review.value)
      reviews = reviews + 1
    ratio = (all_reviews_sum/reviews)*10
    #self.vote_total = reviews
    self.vote_ratio = ratio
    self.save()

  @property
  def requests_number(self):
    projects_queryset = self.project_set.all()
    all_projects_sum = 0
    for project in projects_queryset:
      all_projects_sum = all_projects_sum + 1
      self.vote_total = all_projects_sum
      self.save()


class Project(models.Model):
  mentor = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL)
  student = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL, related_name='student')
  title = models.CharField(max_length=200)
  description = models.TextField(null=True, blank=True, default="")
  featured_image = models.ImageField(null=True, blank=True, default="default.jpg")
  demo_link = models.CharField(max_length=2000, null=True, blank=True, default="Demo Link")
  source_link = models.CharField(max_length=2000, null=True, blank=True, default="Source Link")
  subject = models.ForeignKey(Subject, blank=True, on_delete=models.CASCADE)
  created = models.DateTimeField(auto_now_add=True)
  id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
  is_completed = models.BooleanField(default=False, null=True)
  is_accepted = models.BooleanField(default=False, null=True)
  private = models.BooleanField(default=True, null=True)
  body = models.TextField(null=True, blank=True, default="Объяснение")
  meeting_link = models.CharField(max_length=500, blank=True, null=True, default="Ссылка на встречу")
  documents_link = models.TextField(null=True, blank=True, default="Ссылка на гугл докс")
  meeting_time = models.CharField(max_length=500, blank=True, null=True, default="Время встречи")


  def __str__(self):
    return self.title


class Review(models.Model):
  VOTE_TYPE = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10'),
  )
  owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
  project = models.ForeignKey(Project, on_delete=models.CASCADE)
  body = models.TextField(null=True, blank=True)
  value = models.CharField(max_length=200, choices=VOTE_TYPE, blank=False, default=None)
  created = models.DateTimeField(auto_now_add=True)
  id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

  class Meta:
    unique_together = [['owner', 'project']]

  def __str__(self):
    return self.body


class Messageroom(models.Model):
  name = models.CharField(max_length=200, null=True, blank=True)
  created = models.DateTimeField(auto_now_add=True)
  id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
  user2 = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True, related_name='user1')
  user1 = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True, related_name='user2')

  def __str__(self):
    return self.name
  
class Message(models.Model):
  sender = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True, related_name='sender')
  recepient = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True, related_name='recepient')
  #name = models.CharField(max_length=200, null=True, blank=True)
  #email = models.CharField(max_length=200, null=True, blank=True)
  #subject = models.CharField(max_length=200, null=True, blank=True)
  body = models.TextField()
  is_read = models.BooleanField(default=False, null=True)
  created = models.DateTimeField(auto_now_add=True)
  id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
  messageroom = models.ForeignKey(Messageroom, on_delete=models.SET_NULL, null=True, blank=True)

  def __str__(self):
    return self.body

  class Meta:
    ordering = ['-created']


class Skill(models.Model):
  name = models.CharField(max_length=200, blank=True, null=True)
  description = models.TextField(null=True, blank=True)
  created = models.DateTimeField(auto_now_add=True)
  id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

  def __str__(self):
    return str(self.name)



class ApplyTeacherRequest(models.Model):
  owner = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)
  id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
  created = models.DateTimeField(auto_now_add=True)
  school = models.CharField(max_length=500, blank=True, null=True)
  email = models.CharField(max_length=500, blank=True, null=True)

  def __str__(self):
    return str(self.owner)










