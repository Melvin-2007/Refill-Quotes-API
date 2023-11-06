# urls.py
from django.urls import path
from . import views

urlpatterns = [
    # URL pattern for the home page (GET)
    path('', views.Home, name='Home'),

    # URL pattern for the topics page (GET)
    path('Topics/', views.topics, name='Topics'),

    # URL pattern for the authors page (GET)
    path('Authors/', views.authors, name='Authors'),

    # URL pattern for the collections page (GET)
    path('Collections/', views.collections, name='Collections'),

    # URL pattern for individual topics (GET)
    path('Topics/<str:topic_name>/', views.Topicsdata, name='Topics_data'),

    # URL pattern for individual authors (GET)
    path('Authors/<str:author_name>/', views.Authorsdata, name='Authors_data'),

    # URL pattern for individual collections (GET)
    path('Collections/<str:collection_name>/', views.Collectionsdata, name='Collections_data'),

    path('quote/', views.quote, name='more quotes'),

]
