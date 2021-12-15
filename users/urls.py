from django.urls import path,include

from . import views

app_name = 'users'
urlpatterns = [
    #users page / django defaults
    path('', include('django.contrib.auth.urls')),
    
    # USer registration.
    path('register/', views.register, name='register'),
]