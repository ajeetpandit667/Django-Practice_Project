"""
URL configuration for practice_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from practice_project import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homePage,name='home'),
    path('about/', views.aboutPage,name='about'),
    path('submitform/', views.submitForm,name='submitform'),
    path('contact/', views.contactPage,name='contact'),
    path('services/', views.servicePage,name='service'),
    path("user-form/", views.userformPage, name="userform"),
    path("calculator/", views.calculator, name="calculator"),
    path("marksheet/", views.marksheet),
    path("news/", views.NewsList, name='news'),
    path("news-details/<int:newsId>/", views.NewsDetails, name='news-details')
]
