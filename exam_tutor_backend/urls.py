"""
URL configuration for exam_tutor_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from rest_framework.authtoken.views import ObtainAuthToken
from accounts.views import TutorSignUpView,TutorRetreieveUpdateView
from assesment_management.views import AssesmentListCreateView,AssesmentRetreiveUpdateDeleteView
from question_management.views import QuestionCreateView,QuestionRetreiveUpdateDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),

    # register accounts
    path('tutor/signup/', TutorSignUpView.as_view()),
    path('tutor/profile/', TutorRetreieveUpdateView.as_view()),


    # token
    path('token/', ObtainAuthToken.as_view()),

    #assesment
     path('tutor/assesments/',AssesmentListCreateView.as_view()),

     path('tutor/assesments/<int:pk>/',AssesmentRetreiveUpdateDeleteView.as_view()),

     #questions
    path('questions/<int:pk>/questions/',QuestionCreateView.as_view()),
    path('questions/<int:pk>/',QuestionRetreiveUpdateDeleteView.as_view()),

]
