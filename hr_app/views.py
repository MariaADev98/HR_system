from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from django.template.loader import render_to_string

menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить статью', 'url_name': 'addpage'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        {'title': 'Войти', 'url_name': 'login'},
        ]

data_db = [
    {'id': 1, 'title': 'кандидат 1', 'content': 'Биография Кандидата 1', 'is_published': True},
    {'id': 2, 'title': 'кандидат 2', 'content': 'Биография Кандидата 2', 'is_published': True},
    {'id': 3, 'title': 'кандидат 3', 'content': 'Биография Кандидата 3', 'is_published': True},
]


def index(request):
    # t = render_to_string('hr_app/index.html')
    # return HttpResponse(t)
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': data_db,
    }
    return render(request, 'hr_app/index.html', context=data)


def about(request):
    return render(request, 'hr_app/about.html', {'title': 'О сайте', 'menu': menu})


def tasks(request):
    return render(request, 'hr_app/tasks.html', {'title': 'Задачи'})


def forms(request):
    return render(request, 'hr_app/forms.html', {'title': 'Анкеты'})


def create_form(request):
    return render(request, 'hr_app/create_form.html', {'title': 'Создание анкеты'})


def categories(request, cat_id):
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>id:{cat_id}</p>')


def categories_by_slug(request, cat_slug):
    if request.POST:
        print(request.POST)
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>id:{cat_slug}</p>')


def archive(request, year):
    if year > 2023:
        return redirect('home')

    return HttpResponse(f'<h1>Архив по годам</h1><p>{year}</p>')


def show_post(request, post_id):
    return HttpResponse(f'Отображение статьи с id = {post_id}')


def addpage(request):
    return HttpResponse('Добавление статьи')


def contact(request):
    return HttpResponse('Обратная связь')


def login(request):
    return HttpResponse('Авторизация')


def page_not_found(request, exeption):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
