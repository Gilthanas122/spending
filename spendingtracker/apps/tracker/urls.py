from django.urls import path
from . import views
urlpatterns = [
    path("", views.index),
    path("template", views.render_page),
    path("<int:num_page>/", views.number_page_view),
    path("<str:topic>/", views.news_view, name="topic-page"),
    path("<int:num1>/<int:num2>", views.add_view),
]

