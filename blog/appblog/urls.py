
from django.urls import path

# importing views from appblog.
from . import views

# importing all functions from views

urlpatterns = [
    path('', views.home, name = 'home' ),
    path('about', views.about, name = 'about'),
    path('dashboard', views.dashboard, name = 'dashboard'),
    path('signup', views.user_signup, name = 'signup'),
    path('login', views.user_login, name = 'login'),
    path('logout', views.user_logout, name = 'logout'),
    path('addpost', views.add_post, name = 'addpost'),

# importing update& delete function with dynamic id included  
    path('updatepost/<int:id>/', views.update_post, name = 'updatepost'),
    path('deletepost/<int:id>/', views.delete_post, name = 'deletepost'),
]