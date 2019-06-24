from django.contrib import admin

# Register your models here.
from blog.models import BlogPost, BlogAuthor, Comment

'''insert the names of each model into these to register them, add more as needed'''
admin.site.register(BlogPost)
admin.site.register(BlogAuthor)
admin.site.register(Comment)
# admin.site.register(BloggerList)
# admin.site.register(CommentForm)