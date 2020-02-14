# PART 1: Hello world
# from django.http import HttpResponse

# def home(request):
#     return HttpResponse('Hello, World!')


# PART 2: Retrieve and display

from django.http import HttpResponse
from .models import Board

def home(request):
    boards = Board.objects.all()
    boards_names = list()

    for board in boards:
        boards_names.append(board.name)

    response_html = '<br>'.join(boards_names)

    return HttpResponse(response_html)    