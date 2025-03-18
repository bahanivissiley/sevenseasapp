"""
URL configuration for sevenSeasApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from main.views import index, contact, about, questionnaire, therapist, join_therapist, contact_view, questionnaire_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('questionnaire/', questionnaire, name='questionnaire'),
    path('therapist/', therapist, name='therapist'),
    path('join-therapist/', join_therapist, name='join_therapist'),
    path("contact_submit/", contact_view, name="contact_submit"),
path('questionnaire_submit/', questionnaire_view, name='questionnaire_submit'),
]
