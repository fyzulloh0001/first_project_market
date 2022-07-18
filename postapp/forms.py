from django.forms import ModelForm
from .models import  Like, Post, Register_Model
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


class Register_ModelForm(ModelForm):
    class Meta:
        model=Register_Model
        fields=['first_name','email','last_name','username','password','image','age','country','phone_number','job','body','unevirsite']

