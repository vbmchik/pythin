from django.shortcuts import render
from .models import Topics, Entry

# Create your views here.
def index(request):
    """Home page of application"""
    return render(request, "firstapps/index.html")


def topics(request):
    topics = Topics.objects.order_by("data_added")
    content = {"topics": topics}
    return render(request, "firstapps/topics.html", content)


def topic(request, topic_id):
    topic = Topics.objects.get(id=topic_id)
    entries = topic.entry_set.order_by("date_added")
    context = {"topic": topic, "entries": entries}
    return render(request, "firstapps/topic.html", context)
