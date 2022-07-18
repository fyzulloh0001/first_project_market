from django.contrib import admin

from postapp.models import  Category, Like, Post,Comment,Register_Model,MemberThink

# Register your models here.
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(Register_Model)
admin.site.register(MemberThink)
# admin.site.register(AboutAdmin)