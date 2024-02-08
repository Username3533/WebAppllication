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
    # Page for adding new entries
    path('new_entry/<int:topic_id>', views.new_entry, name='new_entry'),
    # Page for editing entries
    path('edit_entry/<int:entry_id>', views.edit_entry, name='edit_entry'),
]