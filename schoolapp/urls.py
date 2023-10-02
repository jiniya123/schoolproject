from django.urls import path
from .import views
from .views import confirmation_view

from django.contrib.auth import views as auth_views
app_name='school'
urlpatterns=[
    path('', views.home, name='home'),
    path('department/<int:department_id>/', views.redirect_to_wikipedia, name='department'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('another_page/', views.another_page_view, name='another_page'),
    path('form/', views.form_page, name='form_page'),
    path('logout/', views.logout_view, name='logout'),
]

