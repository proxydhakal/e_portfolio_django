from django.contrib import admin
from apps.blog.models import Blog,Category,Contact
# Register your models here.

admin.site.register(Category)
admin.site.register(Blog)
admin.site.register(Contact)