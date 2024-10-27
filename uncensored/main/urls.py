from django.urls import path
from . import views

urlpatterns = [
    path('', views.board_list, name='board_list'),
    path('board/<slug:slug>/', views.board_detail, name='board_detail'),
    path('create_thread.html/', views.thread_creation_page, name='create_thread'),
    path('board/<slug:board_slug>/thread/<uuid:thread_id>/', views.thread_detail, name='thread_detail', ),
]

