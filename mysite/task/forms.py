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

    origin_ranking = forms.IntegerField()

    class Meta:
        model = Task
        fields = (
            'ranking',
            'title',
            'description',
            'origin_ranking',
        )
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control',
                                                 'cols': 40,
                                                 'rows': 10}),
        }

    def __init__(self, *args, **kwargs):
        super(TaskEditModelForm, self).__init__(*args, **kwargs)
        self.fields['ranking'] = forms.ChoiceField(
            choices=self.get_my_choice(),
        )
        self.fields['origin_ranking'] = forms.IntegerField(
            widget=forms.HiddenInput(attrs={'value': self.instance.ranking})
        )

    def get_my_choice(self):
        return ((str(x), x) for x in range(1, self.instance.mission.ranking))

    def save(self, commit=True):
        super(TaskEditModelForm, self).save(commit=False)
        self.instance.sort_ranking(self.cleaned_data['origin_ranking'])
        self.instance.save()
        return self.instance
