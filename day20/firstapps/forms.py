from django import forms 
from .models import Topics, Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topics
        fields = ['text']
        labels = {'text': ''}
        
class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields  = ['topic','text']
        labels  = {'text': 'Entry', 'topic':'Edit topic'}
        widgets = {'text': forms.Textarea(attrs={'cols':80})}
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args,**kwargs)
        if user:
            self.fields['topic'].queryset = Topics.objects.filter(owner=user.id)
