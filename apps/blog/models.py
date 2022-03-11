from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
   
    class Meta:
        verbose_name_plural = "categories"        
                                                

    def __str__(self):                          
        return self.name                         


class Blog(models.Model):
   
    title =models.CharField(max_length=255)
    description = RichTextUploadingField()
    count = models.IntegerField(default=0)
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    cover_image =models.ImageField(upload_to='media/blog',null=True)
    author = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"pk": self.pk})


class Contact(models.Model):
    name=models.CharField(max_length=255)
    phone=models.IntegerField()
    subject=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    message=models.TextField()


