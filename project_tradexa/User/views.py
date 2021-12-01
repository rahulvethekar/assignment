from django.shortcuts import redirect, render
from .forms import PostForm,UserForm
from django.contrib.auth import login,logout,authenticate
from .models import Post
from django.contrib.auth.decorators import login_required

# Create your views here.
def user_view(request):
    form  = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {'form':form}
    template_name = 'user/user.html'
    return render(request,template_name,context)


@login_required(login_url='login')
def post_view(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_post')
    context = {'form':form}
    template_name = 'user/post.html'
    return render(request,template_name,context)

def all_post(request):
    obj = Post.objects.using('User_db').all()
    context = {'posts':obj}
    template_name = 'user/all_post.html'
    return render(request,template_name,context)

def post_update(request,uid):
    obj = Post.objects.using('User_db').get(id = uid)
    form = PostForm(instance = obj)
    if request.method == 'POST':
        form  = PostForm(request.POST,instance = obj)
        if form.is_valid():
            form.save()
            return redirect('all_post')
    context = {'form':form}
    template_name = 'user/post.html'
    return render(request,template_name,context) 


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username , password = password)
        if user is not None:
            login(request,user)
            return redirect('all_post')
    template_name = 'user/login.html'
    return render(request,template_name)

def logout_view(request):
    logout(request)
    return redirect('login')






