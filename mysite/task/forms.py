from django import forms
from .models import Task, ToDoList


class TaskModelForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = (
            'title',
            'description',
        )
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control',
                                                 'cols': 40,
                                                 'rows': 10}),
        }


class TaskEditModelForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(TaskEditModelForm, self).__init__(*args, **kwargs)
        self.fields['ranking'] = forms.ChoiceField(
            choices=self.get_my_choice(),
        )

    def get_my_choice(self):
        return ((str(x), x) for x in range(1, self.instance.mission.ranking))

    class Meta:
        model = Task
        fields = (
            'ranking',
            'title',
            'description',
        )
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control',
                                                 'cols': 40,
                                                 'rows': 10}),
        }
