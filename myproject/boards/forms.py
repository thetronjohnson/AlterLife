from django import forms
from .models import Topic, Post

class  NewTopicForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(
            attrs = {'rows':5, 'placeholder':"What's on your mind?"}
        ), 
        max_length=4000,
        help_text="Max Length is 4000 letters"
    )

    class Meta:
        model = Topic
        fields = ['subject','message']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['message', ]