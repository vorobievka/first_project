from django.http import HttpResponse
from django.shortcuts import render, reverse
from datetime import datetime
import os


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    # обратите внимание – здесь HTML шаблона нет, 
    # возвращается просто текст
    # current_time = None
    current_time = datetime.today()
    # msg = f'Текущее время: {current_time.hour}:{current_time.minute}'
    msg = f'Текущее время: {"{:02d}".format(current_time.hour)}:{"{:02d}".format(current_time.minute)}'
    return HttpResponse(msg)


def workdir_view(request):
    # по аналогии с `time_view`, напишите код,
    # который возвращает список файлов в рабочей 
    # директории
    # raise NotImplemented
    msg = ''
    rez = os.listdir(path='.')
    for n, item in enumerate(rez):
        # print(n+1, item)
        msg += f'{n+1}. {item} ' + '\r\n'
    print(msg)
    return HttpResponse(msg)
