from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    # post views
    path('', views.post_list, name='post_list'),
    path('<int:post_id>/share', views.post_share, name='post_share'),
    path(
        '<int:year>/<int:month>/<int:day>/<str:slug>',
        views.post_detail,
        name='post_detail',
    ),
]
