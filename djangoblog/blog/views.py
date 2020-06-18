from django.shortcuts import render

posts = [
    {
        'author': 'Cowboy Marlboro',
        'title': 'Blog Post 1',
        'content': 'How to find a cow',
        'date_posted': 'June 10, 2020'
    },
    {
        'author': 'Donald Duck',
        'title': 'Blog Post 2',
        'content': 'No time to play games',
        'date_posted': 'June 11, 2020'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
