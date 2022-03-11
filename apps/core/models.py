from django.db import models

# Create your models here.

class Home(models.Model):
   
    caption =models.CharField(max_length=255)
    video_link = models.CharField(max_length=255)
    slider_image =models.ImageField(upload_to='media/home',null=True)

class About(models.Model):
   
    total_project =models.CharField(max_length=255)
    about_description = models.TextField()
    about_image =models.ImageField(upload_to='media/about',null=True)

class Skill(models.Model):
   
    skill_title =models.CharField(max_length=255)
    skill_progress = models.CharField(max_length=255)

class Project(models.Model):
   
    spam_text =models.CharField(max_length=255)
    project_titel = models.CharField(max_length=255)
    project_image =models.ImageField(upload_to='media/projects',null=True)
