from django.contrib import admin
from .models import Profile, Project, Review, Message, Messageroom, Skill, ApplyTeacherRequest

admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(Review)
admin.site.register(Message)
admin.site.register(Messageroom)
admin.site.register(Skill)
admin.site.register(ApplyTeacherRequest)