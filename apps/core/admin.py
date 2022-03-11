from django.contrib import admin
from apps.core.models import Home, Skill,Project, About
# Register your models here.

admin.site.register(Home)
admin.site.register(Skill)
admin.site.register(About)
admin.site.register(Project)