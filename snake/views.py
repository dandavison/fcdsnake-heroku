from django.shortcuts import render

from snake.models import Score


def scores(request):
    context = {
        'scores': Score.objects.order_by('date'),
    }
    return render(request, 'snake/scores.html', context)
