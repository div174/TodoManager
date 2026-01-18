from django import forms
from todolistapp.models import *

class TaskForm(forms.ModelForm):
    class Meta:
        model=Task
        fields = ["task", "is_completed"]