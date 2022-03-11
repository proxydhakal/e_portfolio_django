from django.shortcuts import render
from apps.blog.models import Blog,Category,Contact
from django.shortcuts import render,get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.http import require_http_methods

# Create your views here.
class BlogList(ListView):
    model = Blog
    queryset = Blog.objects.all()
    ordering =['-created_at']
    paginate_by = 3
    context_object_name = 'list_blog'
    template_name='index.html'

class BlogDetail(DetailView):
    model = Blog
    
    template_name='blog/single.html'
    context_object_name='single_blogs'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object.count = self.object.count + 1
        context["blogs"] = Blog.objects.filter(pk=self.object.pk)
        context['category']= Category.objects.all()
        self.object.save()
        return context


# def contact_form(request, *args, **kwargs):
#     if request.method  == 'POST':
#         message =request.POST['message']
#         subject =request.POST['subject']
#         email =request.POST['email']
#         send_mail(subject, message, email, ['shekhardhakal2015@gmail.com'])
        
   
  

#     return render(request, "index.html")
    


@require_http_methods(["POST"])
def contact_form(request, *args, **kwargs):
    request_data = request.POST
    print(request_data)
    message = request_data.get('message')
    subject = request_data.get('subject')
    email = request_data.get('email')
    name = request_data.get('name')
    phone = request_data.get('phone')
    comment_object = Contact(message=message, subject=subject, email=email,phone=phone,name=name)
    data = comment_object.save()
    print(data)
    
    return render(request, "index.html")

