from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.loginUser,name='login'),
    path('logout/',views.logoutUser,name='logout'),
    path('register/', views.registerUser, name='register'),  
    path('update_profile/', views.update_profile, name='update_profile'),  
    path('profile/<uuid:profile_id>/',views.profile_detail, name='profile_detail'),
    path('coursebase/', views.coursebase, name='coursebase')
]
