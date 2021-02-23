from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def index(request):
    tasks = Task.objects.order_by('-id')  # .order_by('поле для сортировки')


   # num_tasks = Task.objects.filter(title__contains='moloko')
    return render(request, 'main/index.html', {'title': 'Главная страница нашего сайта', 'tasks': tasks})


    #return render(request, 'main/index.html')
    # request и html-шаблон


def about(request):
    return render(request, 'main/about.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    form = TaskForm()
    context = {
        'form': form,
        'error': error

    }

    return render(request, 'main/create.html', context)


def register(request):
    # Массив для передачи данных шаблонны
    data = {}
    # Проверка что есть запрос POST
    if request.method == 'POST':
        # Создаём форму
        form = UserCreationForm(request.POST)
        # Валидация данных из формы
        if form.is_valid():
            # Сохраняем пользователя
            form.save()
            # Передача формы к рендару
            data['form'] = form
            # Передача надписи, если прошло всё успешно
            data['res'] = "Всё прошло успешно"
            # Рендаринг страницы
            return render(request, 'main/register.html', data)
    else:  # Иначе
        # Создаём форму
        form = UserCreationForm()
        # Передаём форму для рендеринга
        data['form'] = form
        # Рендаринг страницы
        return render(request, 'main/register.html', data)
