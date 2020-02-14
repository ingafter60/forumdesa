# PART 1: Hello world
# from django.http import HttpResponse

# def home(request):
#     return HttpResponse('Hello, World!')


# # PART 2 (1/2): Retrieve and display

# from django.http import HttpResponse
# from .models import Board

# def home(request):
#     boards = Board.objects.all()
#     boards_names = list()

#     for board in boards:
#         boards_names.append(board.name)

#     response_html = '<br>'.join(boards_names)

#     return HttpResponse(response_html)    



# PART 2 (2/2): Retrieve and display

# from django.shortcuts import render
# from .models import Board

# def home(request):
#     boards = Board.objects.all()
#     return render(request, 'home.html', {'boards': boards})


# PART 3 (1): Using the URLs API

# from django.shortcuts import render, get_object_or_404
# from .models import Board


# def home(request):
#     boards = Board.objects.all()
#     return render(request, 'home.html', {'boards': boards})


# def board_topics(request, pk):
#     board = Board.objects.get(pk=pk)
#     return render(request, 'topics.html', {'board': board})    


# PART 3 (2): Forms

# from django.shortcuts import render, get_object_or_404
# from .models import Board


# def home(request):
#     boards = Board.objects.all()
#     return render(request, 'home.html', {'boards': boards})


# def board_topics(request, pk):
#     board = Board.objects.get(pk=pk)
#     return render(request, 'topics.html', {'board': board})  


# def new_topic(request, pk):
#     board = get_object_or_404(Board, pk=pk)
#     return render(request, 'new_topic.html', {'board': board})  



# PART 3 (3): Creating Forms The Right Way

# from django.contrib.auth.models import User
# from django.shortcuts import render, redirect, get_object_or_404
# from .forms import NewTopicForm
# from .models import Board, Topic, Post


# def home(request):
#     boards = Board.objects.all()
#     return render(request, 'home.html', {'boards': boards})


# def board_topics(request, pk):
#     board = Board.objects.get(pk=pk)
#     return render(request, 'topics.html', {'board': board})  


# # def new_topic(request, pk):
# #     board = get_object_or_404(Board, pk=pk)
# #     return render(request, 'new_topic.html', {'board': board})     


# def new_topic(request, pk):
#     board = get_object_or_404(Board, pk=pk)
#     user = User.objects.first()  # TODO: get the currently logged in user
#     if request.method == 'POST':
#         form = NewTopicForm(request.POST)
#         if form.is_valid():
#             topic = form.save(commit=False)
#             topic.board = board
#             topic.starter = user
#             topic.save()
#             post = Post.objects.create(
#                 message=form.cleaned_data.get('message'),
#                 topic=topic,
#                 created_by=user
#             )
#             return redirect('board_topics', pk=board.pk)  # TODO: redirect to the created topic page
#     else:
#         form = NewTopicForm()
#     return render(request, 'new_topic.html', {'board': board, 'form': form})


# PART 5 (1): Protecting Views

# from django.contrib.auth.models import User
# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth.decorators import login_required

# from .forms import NewTopicForm
# from .models import Board, Topic, Post


# def home(request):
#     boards = Board.objects.all()
#     return render(request, 'home.html', {'boards': boards})


# def board_topics(request, pk):
#     board = Board.objects.get(pk=pk)
#     return render(request, 'topics.html', {'board': board})  


# @login_required
# def new_topic(request, pk):
#     board = get_object_or_404(Board, pk=pk)
#     user = User.objects.first()  # TODO: get the currently logged in user
#     if request.method == 'POST':
#         form = NewTopicForm(request.POST)
#         if form.is_valid():
#             topic = form.save(commit=False)
#             topic.board = board
#             topic.starter = user
#             topic.save()
#             post = Post.objects.create(
#                 message=form.cleaned_data.get('message'),
#                 topic=topic,
#                 created_by=user
#             )
#             return redirect('board_topics', pk=board.pk)  # TODO: redirect to the created topic page
#     else:
#         form = NewTopicForm()
#     return render(request, 'new_topic.html', {'board': board, 'form': form})



# PART 5 (2): Accessing the Authenticated User

# from django.contrib.auth.decorators import login_required
# from django.shortcuts import get_object_or_404, redirect, render

# from .forms import NewTopicForm
# from .models import Board, Post


# def home(request):
#     boards = Board.objects.all()
#     return render(request, 'home.html', {'boards': boards})


# def board_topics(request, pk):
#     board = get_object_or_404(Board, pk=pk)
#     return render(request, 'topics.html', {'board': board})


# @login_required
# def new_topic(request, pk):
#     board = get_object_or_404(Board, pk=pk)
#     if request.method == 'POST':
#         form = NewTopicForm(request.POST)
#         if form.is_valid():
#             topic = form.save(commit=False)
#             topic.board = board
#             topic.starter = request.user
#             topic.save()
#             Post.objects.create(
#                 message=form.cleaned_data.get('message'),
#                 topic=topic,
#                 created_by=request.user
#             )
#             return redirect('board_topics', pk=board.pk)  # TODO: redirect to the created topic page
#     else:
#         form = NewTopicForm()
#     return render(request, 'new_topic.html', {'board': board, 'form': form})


# PART 5 (3): Topic Posts View

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import NewTopicForm
from .models import Board, Post, Topic


def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})


def board_topics(request, pk):
    board = get_object_or_404(Board, pk=pk)
    return render(request, 'topics.html', {'board': board})


@login_required
def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)
    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.starter = request.user
            topic.save()
            Post.objects.create(
                message=form.cleaned_data.get('message'),
                topic=topic,
                created_by=request.user
            )
            return redirect('board_topics', pk=board.pk)  # TODO: redirect to the created topic page
    else:
        form = NewTopicForm()
    return render(request, 'new_topic.html', {'board': board, 'form': form})


def topic_posts(request, pk, topic_pk):
    topic = get_object_or_404(Topic, board__pk=pk, pk=topic_pk)
    return render(request, 'topic_posts.html', {'topic': topic})

