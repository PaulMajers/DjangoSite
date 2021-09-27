from django.shortcuts import render


# с помощью метода render, мы можем подгружать html-страницы и отображать их
def index(request):
    data = {
        'title': 'Главная страница серьезного сайта',
        'title_1': 'Главная страница',
    }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')


def contacts(request):
    return render(request, 'main/contacts.html')


def gratitude(request):
    return render(request, 'main/gratitude.html')






