from django.urls import path
from . import views
from .views import (
    MovieListView,
    MovieDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    ReviewDetailView
)

urlpatterns = [
    path('', views.index, name='index'),
    path('movies/', views.movie_list, name='movie-list'),
    path('movies/', MovieListView.as_view(), name='movie-list'),
    path('movie/<int:pk>/', MovieDetailView.as_view(), name='movie-detail'),
    path('movie/<int:pk>/review', PostCreateView.as_view(), name='post-create'),
    path('review/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]