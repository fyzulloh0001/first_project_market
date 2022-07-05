from django.forms import ModelForm
from .models import Like, Post
from .models import Comment
class PostForm(ModelForm):
    class Meta:
        model=Post
        fields='__all__'

class CommentForm(ModelForm):
    class Meta:
        model=Comment
        fields=['body']

class LikesForm(ModelForm):
    class Meta:
        model=Like
        fields=['like']

