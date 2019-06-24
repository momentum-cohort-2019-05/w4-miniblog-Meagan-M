from django.shortcuts import render
from blog.models import BlogPost, BlogAuthor, Comment
from django.views import generic
# Create your views here.


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_blog_post = BlogPost.objects.all().count()
    num_blog_author = BlogAuthor.objects.all().count()
    num_comment = Comment.objects.all().count()
    
    # # Available books (status = 'a')
    # num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    
    # # The 'all()' is implied by default.    
    # num_authors = Author.objects.count()
    
    context = {
        'num_blog_post': num_blog_post,
        'num_blog_author': num_blog_author,
        'num_comment': num_comment,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class BlogPostListView(generic.ListView):
    model = BlogPost
    