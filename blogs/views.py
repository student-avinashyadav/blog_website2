from django.shortcuts import render , redirect , get_list_or_404
from django.http import HttpResponse 
from . models import Blogs , Category , Comment
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.http import HttpResponseRedirect
# Create your views here.
def posts_by_category(request,category_id):
    posts = Blogs.objects.filter(status='published',category = category_id)
    try:
     category = Category.objects.get(pk=category_id)
    except:
        return redirect('home')
    # category = get_list_or_404(Category,pk=category_id)
    context = {
        'posts':posts,
        'category':category
    }
    return render(request,'posts_by_category.html',context)



# blogs 

def blogs(request, slug):
   single_post = get_object_or_404(Blogs,slug=slug , status='published')
   #Comment
   if request.method=='POST':
      comment = Comment()
      comment.user = request.user
      comment.blog =  single_post
      comment.comment = request.POST['comment']
      comment.save()
      return HttpResponseRedirect(request.path_info)
   comments = Comment.objects.filter(blog = single_post)
   print('comments : ',comments)
   context = {
      'single_post':single_post,
      'comments':comments,
   }
   return render(request,'blogs.html',context)

def search(request):
   keyword = request.GET.get('keyword')
   #blogs = Blogs.objects.filter(title__icontains=keyword)
   blogs = Blogs.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword) , Q(status ='published'))
   print("value : ",blogs)
   context = {
      'blogs':blogs,
      'keyword':keyword,
   }

   return render(request, 'search.html',context)

