from django.shortcuts import render
from .update_autoru_catalog import update_autoru_catalog


from .models import Mark, ModelAuto


def index(request):
    if request.method == 'POST':
        name = request.POST['mark']
        mark_key = Mark.objects.get(name=name).id
        auto_models = ModelAuto.objects.values_list('name', flat=True).filter(mark_id=mark_key)
    else:
        auto_models = []
        name = 'Марка не выбрана'
    context = {
        'title': 'Каталог авто.ру',
        'marks': Mark.objects.values_list('name', flat=True),
        'auto_models': auto_models,
        'name': name

    }
    return render(request, 'index.html', context)


