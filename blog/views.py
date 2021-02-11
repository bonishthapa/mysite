from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic import CreateView,UpdateView,DetailView,DeleteView
from blog.forms import *
from blog.models import *

# Create your views here.

def home(request):
    posts = Post.objects.all()
    
    context = {
        'posts' : posts
    }
    return render(request,'blog/home.html',context)

'''class CreatePost(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = Post
    template_name='blog/createpost.html'
    fields = '__all__'
    success_url = reverse_lazy('home')'''

@login_required
def createPost(request):
    post = PostForm()
    
    if request.method == "POST":
        post = PostForm(request.POST)
        if post.is_valid():
            instance=post.save(commit=False)
            instance.user=request.user
            instance.save()
            return redirect('/')

    context = {
        'post' : post
    }       

    return render(request,'blog/createpost.html',context) 

@login_required
def updatePost(request,pk):
    posts= Post.objects.get(id = pk)
    post = PostForm(instance=posts)   
    if request.method == "POST":
        post = PostForm(request.POST,instance=posts)
        if post.is_valid():
            post.save()
            return redirect('/')

    context = {
        'post' : post
    }       

    return render(request,'blog/updatepost.html',context) 



'''class UpdatePost(UpdateView):
    model = Post
    template_name='blog/updatepost.html'
    fields = '__all__'
    success_url = reverse_lazy('home') '''

class DetailPost(DetailView):
    model = Post 
    template_name='blog/detailpost.html'  
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.form_class()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self,form):
        form.instance.post = self.object
        form.save()
        return super().form_valid(form)

    '''def get_queryset(self):
        qs = super().get_queryset()
        return self.qs.get(id=pk) ''' 

'''class DeletePost(DeleteView):
    model = Post
    success_url = reverse_lazy('/')'''
@login_required
def deletePost(request,pk):
    post = Post.objects.get( id = pk )
    post.delete()
    return redirect('home')    

def register(request):
    form = UserFormCreate()
    if request.method == "POST":
        form = UserFormCreate(request.POST)
        if form.is_valid:
            form.save()
            return redirect('userform')

    context = {
        'form' : form
    }
    return render(request,'registration/register.html',context)

@login_required
def userInfo_form(request):
    form = UserInfoForm()
    if request.method == "POST":
        form = UserInfoForm(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('home')

    context = {
        'form':form
    }
    return render(request,'registration/userdetail_form.html',context)         

def loginuser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username ,password= password)
        if user is not None:
            login(request,user)
            return redirect('home')

    return render(request,'registration/login.html')


def logoutuser(request):
    logout(request)
    return redirect('login')

@login_required
def mypost(request):
    posts = Post.objects.filter(user=request.user)
    context = {
        'posts' : posts
    }
    return render(request,'blog/mypost.html',context)


@login_required
def userDetail(request):
    posts = request.user
    post = UserInfo.objects.get(user = posts)
    context = {
        'post':post
    }    
    return render(request,'registration/userdetail.html',context)
