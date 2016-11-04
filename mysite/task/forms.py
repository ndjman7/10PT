from django import forms
from .models import Task


class TaskModelForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = (
            'task1',
            'task2',
            'task3',
            'task4',
            'task5',
            'task6',
            'task7',
            'task8',
            'task9',
            'task10',
        )
        widgets = {
            'task1': forms.TextInput(),
            'task2': forms.TextInput(),
            'task3': forms.TextInput(),
            'task4': forms.TextInput(),
            'task5': forms.TextInput(),
            'task6': forms.TextInput(),
            'task7': forms.TextInput(),
            'task8': forms.TextInput(),
            'task9': forms.TextInput(),
            'task10': forms.TextInput(),
        }
