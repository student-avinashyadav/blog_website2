from django.shortcuts import render ,redirect
from blogs.models import Category,Blogs
from django.contrib.auth.decorators import login_required
from dashbords.forms import CategoryForm , BlogForm
from django.shortcuts import get_object_or_404 
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from . forms import AddUserForm,EditUserForm
# Create your views here.
@login_required(login_url='login')
def dashboard(request):
    category_counts = Category.objects.all().count()
    blogs_counts = Blogs.objects.all().count()

    context = {
        'category_counts': category_counts,
        'blogs_counts': blogs_counts,
    }

    #print("Category_count : ",category_counts , " blog_counts : " , blogs_counts)
    return render(request,'dashboard/dashboard.html',context)

def categories(request):
    return render(request,'dashboard/categories.html')

def add_categories(request):
    if request.method=='POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    else:
        form = CategoryForm()
    context = {
        'form':form,
    }
    return render(request,'dashboard/add_categories.html',context)

def edit_category(request,pk):
    category = get_object_or_404(Category,pk=pk)
    if request.method=='POST':
        form = CategoryForm(request.POST , instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form = CategoryForm(instance=category)
    context = {
        'form':form,
        'category':category,
    }
    return render(request,'dashboard/edit_category.html',context)

def delete_category(request,pk):
    category = get_object_or_404(Category,pk=pk)
    category.delete()
    return redirect('categories')

def posts(request):
    posts = Blogs.objects.all()
    context = {
        'posts':posts
    }
    return render(request,'dashboard/posts.html',context)

def add_post(request):
    if request.method=='POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
          
            title = form.cleaned_data['title']
            post.slug = slugify(title)
            post.save()
            print('success')
            return redirect('posts')
        else:
            print(form.errors)
    else:
        form = BlogForm()
    context = {
        'form':form
    }
    return render(request,'dashboard/add_post.html',context)

def delete_post(request,pk):
    post = get_object_or_404(Blogs,pk=pk)
    post.delete()
    return redirect('posts')
  
def edit_post(request,pk):
    blog = get_object_or_404(Blogs,pk=pk)
    if request.method=='POST':
        form = BlogForm(request.POST , instance=blog)
        if form.is_valid():
            form.save()
            return redirect('posts')
    else:
        form = BlogForm(instance=blog)
    context = {
        'form':form,
        'blog':blog,
    }
    return render(request,'dashboard/edit_post.html',context)

def users(request):
    users = User.objects.all()
    context = {
        'users':users,
    }
    return render(request,'dashboard/users.html',context)

def add_user(request):
    if request.method=='POST':
        form = AddUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')
        
    form = AddUserForm()
    context = {
        'form':form,
    }
    return render(request,'dashboard/add_user.html',context)

def edit_user(request,pk):
    user = get_object_or_404(User,pk=pk)
    if request.method=='POST':
        form = EditUserForm(request.POST ,instance=user)
        if form.is_valid():
            form.save()
            return redirect('users')
    form = EditUserForm(instance=user)
    context = {
        'form':form,
        'user':user
    }
    return render(request,'dashboard/edit_user.html',context)

def delete_user(request,pk):
    user = get_object_or_404(User,pk=pk)
    user.delete()
    return redirect('users')