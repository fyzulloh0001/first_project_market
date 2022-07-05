import random
from django.shortcuts import redirect, render

from postapp.forms import LikesForm, PostForm,CommentForm
from .models import Category, Like, Post
from django.contrib.auth import login,logout,authenticate
from .models import Register_Model
# Create your views here.



def home(request):
    category_6=Category.objects.all()[:6]
    category_7=Category.objects.all()[6:]
    post=Post.objects.all()[1:3]
    post_update_date=Post.objects.all().order_by('-update_date')[:2]
    post_footer=list(Post.objects.all())
    post_footer=random.shuffle(post_footer)
  
    
    
    # category destance
 

    # end range

    if request.method=='POST':
        form=LikesForm(request.POST)
        if form.is_valid():
            form.save()
            
    else:
        form=LikesForm()

    context={'Post':post,
            'form':form,
            'category_6':category_6,
            'category_7':category_7,
            'Post':post_update_date,
            'post_footer':post_footer,
            }


    return render(request=request,template_name='home.html',context=context)

def category(request):


    return render(request=request,template_name='category/category.html')

def singleblog(request):
    return render(request=request,template_name='category/singleblog.html')

def regular(request):
    return render(request=request,template_name='category/regular.html')

def contact(request):
    return render(request=request,template_name='category/contact.html')

def detailview(request,id):
    post=Post.objects.get(id=id)
  
  
    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.post=post
            form.save()
            return redirect('.')
    else:
        form=CommentForm()
            

 
    context={'post':post,
               'form':form,
              
                }
    return render(request=request,template_name='detail.html',context=context)

def reaction(request,id,react):
    post=Post.objects.get(id=id)
    person=Register_Model.objects.get(username=request.user.username)
    post.setreaction(
        react=react,
        person=person,
    )
    
    return redirect('detail',id)
       
# ___________________________________________




def loginview(request):
    pass_user=''
    if request.method=='POST':
        print('--',request.POST)
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('home')
        else:
            pass_user='password or username is error'
    return render(request=request,template_name='account/login.html',context={'error':pass_user})

def logoutview(request):

    logout(request)
    return redirect('login')

def registerview(request):
    password_error=''
    user=Register_Model()
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        password1=request.POST.get('password1')

        if password == password1:
            user=Register_Model.objects.create(username=username,email=email,password=password)
            user.set_password(password)
            user.save()
            return redirect('login')
        else:
            password_error='you inter password it is deffirent'
    else:
        Register_Model()

    return render(request=request,template_name='account/register.html',context={'password_error':password_error})

def createview(request):


    form =PostForm()
    print('----',request.POST)
    if request.method=="POST":
        form=PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=PostForm()

    return render(request=request,template_name='create.html',context={'form':form})

def updateview(request,id):
    object=Post.objects.get(id=id)

   

    if request.method=='POST':
        form=PostForm(request.POST or None,instance=object)
        
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=PostForm(instance=object)

    return render(request=request,template_name='update.html',context={'form':form})

def deleteview(request,id):
    post=Post.objects.get(id=id)
    post.delete()
    return redirect('home')

def likesview(request):
    if request.method=='POST':
        form=LikesForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=LikesForm()

      
    context={'form':form}
    return render(request=request,template_name='home.html',context=context)


# ____________________________________________
# def homecategory(request):
#     category=Category.objects.all()
#     context={'category':category}
#     return render(request=request,template_name='homecategory.html',context=context)
