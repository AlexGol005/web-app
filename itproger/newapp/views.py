from django.http import HttpResponse


def mainstr(reqest):
    return HttpResponse("<h3>Это главная страница сайта!</h3>")
