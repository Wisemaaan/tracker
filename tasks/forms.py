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
        fields = ['title', 'description', 'completed']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'id': 'titleInput'}), 
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'completed': forms.CheckboxInput(attrs={'class': 'form-check-control'}),
        }


class TaskCreateForm(TaskForm):
    pass  

class TaskEditForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'completed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }