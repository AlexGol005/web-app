from django.shortcuts import render
from django.http import HttpResponse
def index(reqest):
    return HttpResponse("<h4>Проверка работы</h4>")


def about(reqest):
    return HttpResponse("<h4>Про нас</h4>")

def course(reqest):
    return HttpResponse("<h3>Страница курсов</h3><p>Это страница курсов!</p>")

