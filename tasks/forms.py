from django import forms
from .models import Task
from .models import TaskTemplate

class TaskForm(forms.ModelForm):
    template = forms.ModelChoiceField(
        queryset=TaskTemplate.objects.all(),
        required=False,
        label='Choose a Template (optional)',
        empty_label='---Create custom task---'
    )

    class Meta:
        model = Task
        fields = ['title', 'description', 'completed']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'completed': forms.CheckboxInput(attrs={'class': 'form-check-control'}),

        }