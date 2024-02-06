""" Defines url patters for learning_logs """

from django.urls import path

from . import views

app_name = 'learning_logs'

urlpatterns = [
    #Home Page
    path('', views.index, name='index'),
    #Page that shows all topics
    path('topics/', views.topics, name='topics'),
    # Details about single topics
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # Page for adding new topics
    path('new_topic/', views.new_topic, name='new_topic'),
]