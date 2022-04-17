from django.shortcuts import render ,redirect
from .models  import Album , Song
from django.contrib.auth import authenticate , login
from django.views.generic import View
from .forms import UserForm

from django.http import HttpResponse

# Create your views here.
def index(request ):
    albump1 = Album.objects.get(pk=1)
    song1= albump1.song_set.get(pk=1)
    albump2 = Album.objects.get(pk=2)
    song2 = albump2.song_set.get(pk=6)
    songs = Song.objects.all()
    albums = Album.objects.all()
    context = {'albums':albums, 'songs':songs ,'albump1':albump1,'song1':song1 , 'song3':song2,'albump2':albump2}
    return render(request, 'music/index2.html',context)

def detail(request):

    albums = Album.objects.all()
    songs = Song.objects.all()
    albums2=Album.objects.get(pk=1)
    context = { 'songs':songs ,'albums2':albums2,'albums':albums}
    return render(request, 'music/albums-store2.html', context)

def news(request):
    return render(request,'music/blog2.html')

def contact(request):
    return render(request,'music/contact2.html')



def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request,user)

                albums = Album.objects.all()
                return render(request, 'music/register.html', {'albums': albums})
    context = {"form": form}
    return render(request, 'music/register.html', context)

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                albums = Album.objects.all()


                return render(request, 'music/index2.html', {'albums': albums})
            else:
                return render(request, 'music/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'music/login.html', {'error_message': 'Invalid login'})
    return render(request, 'music/login.html')



