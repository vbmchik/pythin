from django.shortcuts import render, redirect
from .models import Topics, Entry
from .forms import TopicForm, EntryForm

# Create your views here.
def index(request):
    """Home page of application"""
    return render(request, "firstapps/index.html")

def topics(request):
    topics = Topics.objects.order_by('data_added')
    content = {"topics": topics}
    return render(request, 'firstapps/topics.html', content)

def topic(request, topic_id):
    topic = Topics.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('date_added')
    context = {"topic":topic, "entries": entries}
    return render(request, 'firstapps/topic.html', context)

def new_topic(request):
    if request.method != 'POST':
        # No data in request
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('firstapps:topics')

    mapper = {"Form": form}
    return render(request,"firstapps/new_topic.html", mapper)

def new_entry(request,topic_id):
    topic = Topics.objects.get(id=topic_id)
    if request.method != 'POST':
        # No data in request
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('firstapps:topic', topic_id=topic_id)
    mapper = {"topic":topic,"Form": form}
    return render(request, "firstapps/new_entry.html", mapper)


def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if request.method != 'POST':
        # Current record state
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('firstapps:topic', topic_id=topic.id)
    mapper = {"entry":entry,"topic": topic, "Form": form}
    return render(request, "firstapps/edit_entry.html", mapper)
