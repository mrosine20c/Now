
from django.urls import path

from accounts.views import  ChangePasswordView, InstructorRegisterView, Instructortonlyview, LoginView, LogoutView, StudentRegisterView , Studentonlyview


urlpatterns = [
  path('register/instructor/',InstructorRegisterView.as_view(), name="insructorregister"),
  path('register/student/',StudentRegisterView.as_view(), name="studentregister"),
  path('login/',LoginView.as_view(),name="login"),
  path('logout/',LogoutView.as_view(),name="logout"),
  path('student/dashboard/',Studentonlyview.as_view()),
  path('instructor/dashboard/',Instructortonlyview.as_view()),
  path('change_password/', ChangePasswordView.as_view()),

]
