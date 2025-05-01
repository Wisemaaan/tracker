from django import forms
from .models import Task
from .models import TaskTemplate

class TaskForm(forms.ModelForm):
    template = forms.ModelChoiceField(
    queryset=TaskTemplate.objects.all(),
    required=False,
    label='Choose a Template (optional)',
    empty_label="--- Create custom task ---",
    widget=forms.Select(attrs={'class': 'form-control', 'id': 'templateSelect'})
)

    class Meta:
        model = Task
        fields = ['template', 'title', 'description', 'due_date', 'completed']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'id': 'titleInput'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'due_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'completed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class TaskCreateForm(forms.ModelForm):
    template = forms.ModelChoiceField(
        queryset=TaskTemplate.objects.none(),
        required=False,
        label='Choose a Template (optional)',
        empty_label="--- Create custom task ---",
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'templateSelect'})
    )

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  
        super().__init__(*args, **kwargs)
        self.fields['title'].required = False  

        if user:
            self.fields['template'].queryset = TaskTemplate.objects.filter(user=user)

    class Meta:
        model = Task
        fields = ['template', 'title', 'description', 'due_date', 'completed']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'id': 'titleInput'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'due_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'completed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class TaskEditForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'due_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'completed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

