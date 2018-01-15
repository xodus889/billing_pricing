from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<product>/run', views.run, name='run'),
    # ex: /polls/5/
    path('<product>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('/results', views.results, name='results'),
    path(r'^(?P<product>\d+)/vote/$', views.vote, name='vote'),

]