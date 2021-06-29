from django.shortcuts import render

posts = [
    {
        'author': 'John Doe',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'June 27, 2021'
    },
    {
        'author': 'Jane Doe',
        'title': 'How I posted from future',
        'content': 'Second post content',
        'date_posted': 'June 27, 2031'
    }
]


def home(request):
    context = {
        'posts': posts,
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': "Blogs"})

