# from django.shortcuts import render  # this line is added automatically
# from django.http import HttpResponse  # pass view information into the browser

# from polls.models import Person, Post

# person = Person.objects.filter(first_name="Maria", last_name="Fez").first()


# # takes a request, returns a response
# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")


# def display_info(request, name, age):
#     return HttpResponse(f"Hello {name}, your age after 5 years is {age + 5}")


# def about_website(request):
#     return HttpResponse('<h1> Welcome Users<h1>')


# def posts(request):
#     all_posts = Post.objects.filter(author__first_name=person.first_name, author__last_name=person.last_name)
#     context = {
#         "posts": all_posts
#     }
#     return render(request, 'posts/posts.html', context)
