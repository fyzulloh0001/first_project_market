from unicodedata import category
from django.urls import path
from .views import createview, deleteview, detailview, home,category,reaction, logoutview, registerview, regular,singleblog,contact,loginview, updateview

urlpatterns = [
    path('',home,name='home'),
    path('category/',category,name='category'),
    path('singleblog/',singleblog,name='singleblog'),
    path('regular/',regular,name='regular'),
    path('contact/',contact,name='contact'),
    path('detail/<int:id>/',detailview,name='detail'),
# ___________________________________________________________
    path('login/',loginview,name='login'),
    path('logout/',logoutview,name='logout'),
    path('register/',registerview,name='register'),
    path('create/',createview,name='create'),
    path('update/<int:id>/',updateview,name='update'),
    path('delete/<int:id>/',deleteview,name='delete'),
    path('reaction/<int:id>/<str:react>/',reaction,name='reaction'),
    

]