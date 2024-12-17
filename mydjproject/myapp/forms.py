from django.forms import ModelForm
from .models import Student

class StudentForm(ModelForm):
    class Meta:
        model = Student
        field = ["sname","smobile","semail","spassword"]
        exclude = ['createdAt']
        #fields = '__all__'