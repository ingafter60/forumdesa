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

from django.shortcuts import render, get_object_or_404
from .models import Board


def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})


def board_topics(request, pk):
    board = Board.objects.get(pk=pk)
    return render(request, 'topics.html', {'board': board})    

