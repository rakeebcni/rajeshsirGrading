from django import forms
from myApp.models import *

class StudentCreationForm(forms.ModelForm):

    class Meta:

        model=studentModel
        fields=['StudentName','Age','Gender','Subjects']
        
class SubjectCreationForm(forms.ModelForm):

    class Meta:

        model=SubjectModel
        fields=['SubjectName','SubjectCode','Credit']

class MarkCreationForm(forms.ModelForm):
    class Meta:
        model = MarkModel
        fields = ['student', 'subject', 'marks']

        
        


    
