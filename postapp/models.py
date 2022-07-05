from django.db import models
from django.contrib.auth.models import AbstractUser
from django.shortcuts import redirect
# Create your models here.
class Register_Model(AbstractUser):
    first_name=models.CharField(max_length=100)
    username=models.CharField(max_length=100,unique=True)
    email=models.EmailField()
    password=models.CharField(max_length=20)

    def __str__(self):
        return self.username
    


class Category(models.Model):
    title=models.CharField(max_length=150)
    body=models.TextField()
    image=models.ImageField(upload_to='category_image')

    def __str__(self):
        return self.title

class Post(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='posts')
    title=models.CharField(max_length=150)
    anons=models.CharField(max_length=250)
    body=models.TextField()
    image=models.ImageField(upload_to='post_image')
    author=models.ForeignKey(Register_Model,on_delete=models.CASCADE,related_name='posts')
    created_date=models.DateTimeField(auto_now_add=True)
    update_date=models.DateTimeField(auto_now=True)
    views=models.PositiveIntegerField(default=0)

    def ImageUrl(self):
        if self.image:
            return self.image.url


        else:
            return ''

    def __str__(self):
        return self.title

    @property
    def like(self):
        return self.reaction.filter(like='like').count()
    @property
    def dislike(self):
        return self.reaction.filter(like='dislike').count()
    

    def setreaction(self,react,person):
        corrent_react=self.reaction.filter(author=person)
        corrent_reaction=corrent_react[0] if corrent_react else None 
        if not corrent_reaction:
            reaction=Like.objects.create(
                post=self,
                author=person,
                like=react
            )
        elif corrent_reaction.like==react:
            corrent_react.delete()

    
            


class Like(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='reaction',null=True,blank=True)
    author=models.ForeignKey(Register_Model,on_delete=models.CASCADE,related_name='likes',null=True,blank=True)
    like=models.CharField(max_length=8)

    def __str__(self):
        return f'{self.author} reaction {self.like}'

    

class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='postcomment',null=True,blank=True)
    author=models.ForeignKey(Register_Model,on_delete=models.CASCADE,related_name='authorcomment',null=True,blank=True)
    parent_com=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='parentcomment',null=True,blank=True)
    body=models.TextField()

    def __str__(self):
        return f"{self.author}s comment for {self.body}"


        









