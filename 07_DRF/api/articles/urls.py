from django.urls import path
from . import views

app_name = 'articles'

urlpatterns=[
    # /articles/
    path('', views.article_index_create),
    # /articles/1/
    path('<int:article_pk>/', views.article_detail_update_delete),

    # POST/ articles/1/comments/
    path('<int:article_pk>/comments/', views.comment_create),
    path('<int:article_pk>/comments/<int:comment_pk>/', views.comment_update_delete)
]