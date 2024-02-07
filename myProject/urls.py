
from django.contrib import admin
from django.urls import path
from myProject.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboardPage,name='dashboardPage'),
    path('createStudenPage/', createStudenPage,name='createStudenPage'),
    path('viewStudentPage/', viewStudentPage,name='viewStudentPage'),
    path('createSubjectPage/', createSubjectPage,name='createSubjectPage'),
    path('viewSubjectPage/', viewSubjectPage,name='viewSubjectPage'),
    path('inputMarksPage/<str:student_id>', inputMarksPage,name='inputMarksPage'),
    path('viewMarksPage/<str:student_id>', viewMarksPage,name='viewMarksPage'),
]
