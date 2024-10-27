from django import forms
from .models import Thread, Reply

class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ['subject', 'content', 'image']

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['content', 'image']


