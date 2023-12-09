from django import forms
from .models import Comment
from .models import Post

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["name","email","body"]

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["body"]

class YourForm(forms.Form):
    your_text = forms.CharField(widget=forms.Textarea)