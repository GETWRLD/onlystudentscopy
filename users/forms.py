from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Project, Message, Messageroom, ApplyTeacherRequest, Review
from django import forms
from django.utils.safestring import mark_safe

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']
        labels = {
        }

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
    
        #self.fields['title'].widget.attrs.update({'class':'input', 'placeholder':'Add Title'})
    
        for name, field in self.fields.items():
          field.widget.attrs.update({'class':'input'})


class ProjectForm(ModelForm):
    class Meta:
      model = Project

      fields = ["title", 'description', 'subject']
      widgets = {
        'title': forms.TextInput,
        'description': forms.TextInput,
      }
      
    def __init__(self, *args, **kwargs):
      super(ProjectForm, self).__init__(*args, **kwargs)
  
      for name, field in self.fields.items():
        self.fields['title'].widget.attrs.update({'class':'project-form-input', 'required':'', 'type':'text', 'name':'text', 'autocomplete':'off'})
        self.fields['description'].widget.attrs.update({'class':'project-form-input', 'required':'', 'type':'text', 'name':'text', 'autocomplete':'off'})
        self.fields['subject'].widget.attrs.update({'class':'project-form-subject', 'required':''})


class MessageForm(ModelForm):
  class Meta:
    model = Message
    fields = ['body']
    widgets = {
      'body': forms.TextInput
    }

  def __init__(self, *args, **kwargs):
    super(MessageForm, self).__init__(*args, **kwargs)

    for name, field in self.fields.items():
      field.widget.attrs.update({'class':'message-input', 'required':'', 'type':'text', 'name':'text', 'autocomplete':'off'})


class MessageroomForm(ModelForm):
  class Meta:
    model = Messageroom
    fields = ['name']


class ActiveProjectForm(ModelForm):
  class Meta:
    model = Project
    fields = ['title','description', 'body', 'meeting_link', 'documents_link', 'meeting_time']
    widgets = {
      'title': forms.Textarea,
      'description': forms.Textarea,
      'body': forms.Textarea,
      'meeting_link': forms.Textarea,
      'documents_link': forms.Textarea,
      'meeting_time': forms.Textarea
    }

  def __init__(self, *args, **kwargs):
    super(ActiveProjectForm, self).__init__(*args, **kwargs)
    self.fields['title'].required = False
    self.fields['description'].required = False
    self.fields['body'].required = False
    self.fields['meeting_link'].required = False
    self.fields['documents_link'].required = False
    self.fields['meeting_time'].required = False

    for name, field in self.fields.items():
      self.fields['title'].widget.attrs.update({'class':'edit-project-input', 'required':'False', 'type':'text', 'name':'text', 'autocomplete':'off'})
      self.fields['description'].widget.attrs.update({'class':'edit-project-input', 'required':'False', 'type':'text', 'name':'text', 'autocomplete':'off'})
      self.fields['body'].widget.attrs.update({'class':'edit-project-input', 'required':'False', 'type':'text', 'name':'text', 'autocomplete':'off'})
      self.fields['meeting_link'].widget.attrs.update({'class':'edit-project-input', 'required':'False', 'type':'text', 'name':'text', 'autocomplete':'off'})
      self.fields['documents_link'].widget.attrs.update({'class':'edit-project-input', 'required':'False', 'type':'text', 'name':'text', 'autocomplete':'off'})
      self.fields['meeting_time'].widget.attrs.update({'class':'edit-project-input', 'required':'False', 'type':'text', 'name':'text', 'autocomplete':'off'})



class StudentAccountForm(ModelForm):
  class Meta:
    model = Profile
    fields = ['username', 'short_intro', 'bio',
    'social_instagram', 'social_twitter', 'social_linkedin', 'social_youtube', 
    'social_website', 'social_vk', 'social_telegram', 'classs']

    widgets = {
      'subjects': forms.CheckboxSelectMultiple,
      'username': forms.TextInput,
      'short_intro': forms.TextInput,
      'bio': forms.TextInput,
      'social_instagram': forms.TextInput,
      'social_twitter': forms.TextInput,
      'social_linkedin': forms.TextInput,
      'social_youtube': forms.TextInput,
      'social_website': forms.TextInput,
      'social_vk': forms.TextInput,
      'social_telegram': forms.TextInput
    }

  def __init__(self, *args, **kwargs):
    super(StudentAccountForm, self).__init__(*args, **kwargs)

    for name, field in self.fields.items():
      self.fields['username'].widget.attrs.update({'class':'account-input', 'required':'', 'type':'text', 'name':'text', 'autocomplete':'off'})
      #self.fields['location'].widget.attrs.update({'class':'account-input', 'required':'', 'type':'text', 'name':'text', 'autocomplete':'off'})
      self.fields['short_intro'].widget.attrs.update({'class':'account-input', 'required':'', 'type':'text', 'name':'text', 'autocomplete':'off'})
      self.fields['bio'].widget.attrs.update({'class':'account-input', 'required':'', 'type':'text', 'name':'text', 'autocomplete':'off'})
      self.fields['social_instagram'].widget.attrs.update({'class':'account-input', 'required':'', 'type':'text', 'name':'text', 'autocomplete':'off'})
      self.fields['social_twitter'].widget.attrs.update({'class':'account-input', 'required':'', 'type':'text', 'name':'text', 'autocomplete':'off'})
      self.fields['social_linkedin'].widget.attrs.update({'class':'account-input', 'required':'', 'type':'text', 'name':'text', 'autocomplete':'off'})
      self.fields['social_youtube'].widget.attrs.update({'class':'account-input', 'required':'', 'type':'text', 'name':'text', 'autocomplete':'off'})
      self.fields['social_website'].widget.attrs.update({'class':'account-input', 'required':'', 'type':'text', 'name':'text', 'autocomplete':'off'})
      self.fields['social_vk'].widget.attrs.update({'class':'account-input', 'required':'', 'type':'text', 'name':'text', 'autocomplete':'off'})
      self.fields['social_telegram'].widget.attrs.update({'class':'account-input', 'required':'', 'type':'text', 'name':'text', 'autocomplete':'off'})
      #self.fields['profile_image'].widget.attrs.update({'class':'account-image-input'})
      self.fields['classs'].widget.attrs.update({'class':'account-classs-input'})


class MentorAccountForm(ModelForm):
  class Meta:
    model = Profile
    fields = ['username', 'short_intro', 'bio', 
    'social_instagram', 'social_twitter', 'social_linkedin', 'social_youtube', 
    'social_website', 'social_vk', 'social_telegram', 'subjects', 'classs']

    widgets = {
      'subjects': forms.CheckboxSelectMultiple,
      'username': forms.TextInput,
      'short_intro': forms.TextInput,
      'bio': forms.TextInput,
      'social_instagram': forms.TextInput,
      'social_twitter': forms.TextInput,
      'social_linkedin': forms.TextInput,
      'social_youtube': forms.TextInput,
      'social_website': forms.TextInput,
      'social_vk': forms.TextInput,
      'social_telegram': forms.TextInput
    }

  def __init__(self, *args, **kwargs):
    super(MentorAccountForm, self).__init__(*args, **kwargs)

    for name, field in self.fields.items():
      self.fields['username'].widget.attrs.update({'class':'account-input', 'required':'', 'type':'text', 'name':'text', 'autocomplete':'off'})
      #self.fields['location'].widget.attrs.update({'class':'account-input', 'required':'', 'type':'text', 'name':'text', 'autocomplete':'off'})
      self.fields['short_intro'].widget.attrs.update({'class':'account-input', 'required':'', 'type':'text', 'name':'text', 'autocomplete':'off'})
      self.fields['bio'].widget.attrs.update({'class':'account-input', 'required':'', 'type':'text', 'name':'text', 'autocomplete':'off'})
      self.fields['social_instagram'].widget.attrs.update({'class':'account-input', 'required':'', 'type':'text', 'name':'text', 'autocomplete':'off'})
      self.fields['social_twitter'].widget.attrs.update({'class':'account-input', 'required':'', 'type':'text', 'name':'text', 'autocomplete':'off'})
      self.fields['social_linkedin'].widget.attrs.update({'class':'account-input', 'required':'', 'type':'text', 'name':'text', 'autocomplete':'off'})
      self.fields['social_youtube'].widget.attrs.update({'class':'account-input', 'required':'', 'type':'text', 'name':'text', 'autocomplete':'off'})
      self.fields['social_website'].widget.attrs.update({'class':'account-input', 'required':'', 'type':'text', 'name':'text', 'autocomplete':'off'})
      self.fields['social_vk'].widget.attrs.update({'class':'account-input', 'required':'', 'type':'text', 'name':'text', 'autocomplete':'off'})
      self.fields['social_telegram'].widget.attrs.update({'class':'account-input', 'required':'', 'type':'text', 'name':'text', 'autocomplete':'off'})
      #self.fields['profile_image'].widget.attrs.update({'class':'account-image-input'})
      self.fields['subjects'].widget.attrs.update({'class':'account-subjects-input'})
      self.fields['classs'].widget.attrs.update({'class':'account-classs-input'})



class TeacherAccountForm(ModelForm):
  class Meta:
    model = Profile
    fields = ['username', 'short_intro', 'bio', 'profile_image', 'subjects']

    widgets = {
      'subjects': forms.CheckboxSelectMultiple
    }

    def __init__(self, *args, **kwargs):
      super(TeacherAccountForm, self).__init__(*args, **kwargs)

      for name, field in self.fields.items():
        field.widget.attrs.update({'class':'input'})


class MentorApplyForm(ModelForm):
  class Meta:
    model = Profile
    fields = ['subjects']


class TeacherApplyForm(ModelForm):
  class Meta:
    model = ApplyTeacherRequest
    fields = ['school', 'email']


class ProjectReviewForm(ModelForm):
  class Meta:
    model = Review
    fields = ['value', 'body']
    widgets = {
      'value': forms.RadioSelect,
      'body': forms.TextInput
    }

  def __init__(self, *args, **kwargs):
    super(ProjectReviewForm, self).__init__(*args, **kwargs)
    
    for name, field in self.fields.items():
      self.fields['body'].widget.attrs.update({'class':'review-input', 'required':'', 'type':'text', 'name':'text', 'autocomplete':'off'})
      self.fields['value'].widget.attrs.update({'class':'value-button'})
        
