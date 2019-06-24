from django.db import models
from datetime import date
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
from django.conf import settings


class BlogPost(models.Model):
    title = models.CharField(max_length=200, help_text="Enter title of blog post")
    blog_post = models.TextField(max_length=3000, help_text='Type your blog post here')
    post_date = models.DateField(default=date.today)
    
    def __str__(self):
        """String for representing the Model object."""
        return self.title
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this blog."""
        return reverse('blog-detail', args=[str(self.id)])
    
    class Meta:
        ordering = ['post_date']


class BlogAuthor(models.Model):
    """Model representing an author."""
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    bio = models.CharField(max_length=200, help_text="Enter a short bio for yourself")

    class Meta:
        ordering = ['first_name', 'last_name']

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'


class Comment(models.Model):
    comment = models.TextField(max_length=500, help_text='Type your comment here')
    post_date = models.DateField(default=date.today)
    target_blog_post = models.ForeignKey('BlogPost', on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)

    class Meta:
       ordering = ['-post_date']

    def __str__(self):
       
       return f'{self.comment}'

    '''makes creating a comment accessible to only logged-in users from a link at the bottom of the blog post detail pages'''

    '''redirects back to the associated blog post page after a comment has been created'''

    '''directs logged out users to the log in page, to log in before they can add comments. Redirects the user back to the blog page they wanted to comment on after logging in'''

    '''adds a name/link info to the blogpost being commented on'''


# # class UserAuth:
# #     '''makes log-in/out accessible via sidebar links. Standard Django authentication pages for logging in/out and setting a password.'''

# #     '''lists logged in user in the sidebar'''
# #     pass

# # class Admin:
    # pass