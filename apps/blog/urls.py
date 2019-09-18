from django.urls import path,include
from apps.blog.views import BlogDetail,BlogList,contact_form
urlpatterns = [
   
    path('', BlogList.as_view(), name='home'),
    path('contact_form', contact_form, name='contact_form'),
    path('<int:pk>/', BlogDetail.as_view(), name='blog_detail'),
    
   
]