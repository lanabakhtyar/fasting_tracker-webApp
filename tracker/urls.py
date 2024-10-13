# tracker/urls.py

from django.urls import path
from . import views

urlpatterns = [
   path('index/', views.index, name='index'), 
    path('start/', views.start_fasting, name='start_fasting'),  # Start fasting
    path('end/', views.end_fasting, name='end_fasting'),        # End fasting
    path('login/', views.user_login, name='login'),             # Login page
             # Logout functionality
     path('track/', views.track_fasting, name='track_fasting'),
]
