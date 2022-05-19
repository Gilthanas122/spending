from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

articles = {
    "sports": "Sports page",
    "finance": "Finance page",
    "politics": "Politics page"
}

def index(request):
    return  HttpResponse("Finally reached index")

# without dynamic routing
"""
def sport_view(request):
    return  HttpResponse(articles["sports"])

def finance_view(request):
    return  HttpResponse(articles["politics"])
"""

#with dynamic routing

def news_view(request, topic):
    try:
        return HttpResponse(articles[topic])
    except:
        # result = "No page found"
        # return  HttpResponseNotFound(result) ## easier implementation, but not generic
        raise  Http404("404 Generic error") # edit settings file to make this work

def add_view(request, num1, num2):
    #result = num1 + num2
    add_result = num1 + num2
    result = f"{num1} + {num2} = {add_result}" # formatting string
    return HttpResponse(str(result))

def number_page_view(request, num_page):
    topics_list = list(articles.keys())
    topic = topics_list[num_page]
    return HttpResponseRedirect(reverse("topic-page", args=[topic]))

def render_page(request):
    return render(request, "tracker/index.html")