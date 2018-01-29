from django.conf.urls import url
from snippets import views

urlpatterns = [
    url(r'^snippets/$', views.SnippetList.as_view()),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
        url(r'^meals/$', views.MealList.as_view()),
    url(r'^meals/(?P<pk>[0-9]+)/$', views.MealDetail.as_view())
]