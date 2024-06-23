from django.urls import path  # path function
from . import views  # . is shorthand for the current directory

# one urlpattern per line
urlpatterns = [
    path('', views.index, name='index'),
    path('sayHi/<name>/<int:age>', views.display_info, name='say_hi'),
    path('about', views.about_website, name='about'),
    path('posts', views.posts, name='posts'),
]
