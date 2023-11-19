from django.shortcuts import render
from .forms import ChoiceMark


from .models import Mark, ModelAuto


def index(request):
    if request.method == 'POST':
        name = request.POST['mark']
        mark_key = Mark.objects.get(name=name).id
        auto_models = ModelAuto.objects.values_list('name', flat=True).filter(mark_id=mark_key)
    else:
        auto_models = []
    context = {
        'marks': Mark.objects.values_list('name', flat=True),
        'auto_models': auto_models

    }
    return render(request, 'index.html', context)


