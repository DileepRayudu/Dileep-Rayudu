from .models import AddCourse
from django import forms
from .models import Marks
class AddCourseForm(forms.ModelForm):
    class Meta:
        model = AddCourse
        fields = ['student','course','section']


    class Marksform(forms.ModelForm):
        class  Meta:
            model = Marks
            fields = ['student''course','marks']

