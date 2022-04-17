from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [
    path('', views.login_user ,name='login'),
    path('register/' ,views.register,name='register'),
    path('albums/',views.detail,name='detail'),
    path('news/' ,views.news , name='news'),
    path('contact/',views.contact, name='contact'),
    path('home/',views.index, name='index')

]
