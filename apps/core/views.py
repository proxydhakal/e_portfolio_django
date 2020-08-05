from django.shortcuts import render
from apps.core.models import Home,Skill,Project,About
from django.shortcuts import render,get_object_or_404
from django.views.generic.list import ListView
from django.conf import settings

# Create your views here.
class HomeList(ListView):
    model = Home
    queryset = Home.objects.all()
    context_object_name = 'list_slider'
    template_name='partials/homeslider.html'

class SkillList(ListView):
    model = Skill
    queryset = Skill.objects.all()
    context_object_name = 'list_skill'
    template_name='partials/skill.html'

class ProjectList(ListView):
    model = Project
    queryset = Project.objects.all()
    context_object_name = 'list_project'
    template_name='partials/project.html'

class AboutList(ListView):
    model = About
    queryset = About.objects.all()
    context_object_name = 'about'
    template_name='partials/about.html'


# Create your views here.
def home(request):
    template_name='index.html'
    return render(request, template_name)


