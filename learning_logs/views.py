from django.shortcuts import render
from .models import Topic


def index(request):
    """Página principal do Learning_log"""
    return render(request, 'learning_logs/index.html')


def topics(request):
    """Mostra todos os assuntos"""
    topics = Topic.objects.order_by('data_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)
