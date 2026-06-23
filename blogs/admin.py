from django.contrib import admin
from . models import Category , Blogs ,Comment
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','category_name','create_at','update_at')

admin.site.register(Category,CategoryAdmin)

class BlogAdmin(admin.ModelAdmin):
    list_display = ('id','title','category','author','blog_image','status','is_feacherd','create_at','update_at')
    prepopulated_fields = {'slug':('title',)}
    search_fields = ('id','title','category__category_name','status')
    list_editable = ('is_feacherd',)
admin.site.register(Blogs,BlogAdmin)

admin.site.register(Comment)