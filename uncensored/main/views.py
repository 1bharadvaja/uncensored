from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Board, Thread, Reply
from .forms import ThreadForm, ReplyForm


# Create your views here.


def board_list(request):
    boards = Board.objects.all()
    return render(request, 'board_list.html', {'boards': boards})

def board_detail(request, slug):
    board = get_object_or_404(Board, slug=slug)
    threads = Thread.objects.filter(board=board)
    return render(request, 'board_detail.html', {'board': board, 'threads': threads})


def thread_detail(request, board_slug, thread_id):
    thread = get_object_or_404(Thread, id=thread_id, board__slug=board_slug)
    replies = thread.replies.all()
    if request.method == 'POST':
        form = ReplyForm(request.POST, request.FILES)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.thread = thread
            reply.save()
            thread.last_bump = timezone.now()
            thread.save()
            return redirect('thread_detail', board_slug=board_slug, thread_id=thread_id)
    else:
        form = ReplyForm()
    return render(request, 'main/thread_detail.html', {'thread': thread, 'replies': replies, 'form': form})

def thread_creation_page(request):
    return render(request, 'create_thread.html')

def create_thread(request, board_slug):
    board = get_object_or_404(Board, slug=board_slug)
    if request.method == 'POST':
        form = ThreadForm(request.POST, request.FILES)
        if form.is_valid():
            thread = form.save(commit=False)
            thread.board = board
            thread.save()
            return redirect('thread_detail', board_slug=board_slug, thread_id=thread.id)
    else:
        form = ThreadForm()
    return render(request, 'create_thread.html', {'form': form, 'board': board})

