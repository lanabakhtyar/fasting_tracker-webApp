from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone
from .models import FastingSession
# Create your views here

def user_login(request):
    if request.method== 'POST':
        username=request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('track_fasting')
    return render(request, 'login.html')


def index(request):
    return render(request, 'index.html')

def start_fasting(request):
    if request.user.is_authenticated:
        FastingSession.objects.create(user=request.user, start_time=timezone.now())
        return redirect('track_fasting')


def end_fasting(request):
    # End the current fasting session
    if request.user.is_authenticated:
        session = FastingSession.objects.filter(user=request.user, end_time__isnull=True).first()
        if session:
            session.end_time = timezone.now()
            session.save()
    return redirect('track_fasting')

def track_fasting(request):
    # Get the most recent fasting session and show duration if it has ended
    session = FastingSession.objects.filter(user=request.user).order_by('-start_time').first()
    duration = None
    if session and session.end_time:
        duration = session.get_fasting_duration()

    return render(request, 'track_fasting.html', {'session': session, 'duration': duration})


        