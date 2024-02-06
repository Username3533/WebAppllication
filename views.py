from django.shortcuts import render, redirect

from .models import Topic
from .forms import TopicForm

# Create your views here.
def index(request):
    #Home page for learning log
    return render(request, 'learning_logs/index.html')

def topics(request):
    #Topics page
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    # Show topic and its entries
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

def new_topic(request):
    #add new topic
    if request.method != 'POST':
        #no data submited, creat blane form
        form = TopicForm()
    else:
        #post submitted data
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')
    #display blank or invaid form
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)