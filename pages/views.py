from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Q
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse
from django.urls import reverse_lazy
from .models import Movie, Review
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import movie_quality, movie_genre, movie_rating
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
) 

# Create your views here.
def index(request):
    movies = Movie.objects.all()

    query = request.GET.get("q")
    if query:
        movies = movies.filter(movie_name__icontains=query)

    context = {
        'movies': movies
    }

    return render(request, 'movie/index.html', context)

def movie_list(request):
    movies = Movie.objects.order_by('-movie_year')

    #keywords
    query = request.GET.get("q")
    if query:
        movies = movies.filter(movie_name__icontains=query)

    #Quality
    ql = request.GET.get("ql")
    if ql:
        movies = movies.filter(movie_quality__quality__iexact=ql)

    #Genre
    gen = request.GET.get("gen")
    if gen:
        movies = movies.filter(movie_category__cat_name_one__iexact=gen)

    #Rating
    rt = request.GET.get("rt")
    if rt:
        movies = movies.filter(movie_rating__rating__iexact=rt)

    paginator = Paginator(movies, 8)
    page = request.GET.get('page')
    paged_lists = paginator.get_page(page)

    context = {
        'movies': paged_lists,
        'movie_quality': movie_quality,
        'movie_genre': movie_genre,
        'movie_rating': movie_rating,
        'values': request.GET
    }

    return render (request, 'browse/browse.html', context)

class MovieListView(ListView):
    model = Movie
    template_name = 'browse/browse.html'
    context_object_name = 'movies'

class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movie/movie_lists.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movies'] = Movie.objects.all()
        context['reviews'] = Review.objects.order_by('-movie_date')
        return context
        
class PostCreateView(CreateView):
    model = Review
    template_name = 'reviews/post_form.html'
    fields = ['movie_title_content', 'movie_content', 'movie_date', 'movie_rating']

    def form_valid(self, form):
        movie_name = Movie.objects.get(pk=self.kwargs['pk'])
        form.instance.author = self.request.user
        form.instance.movie_name = movie_name
        return super().form_valid(form)

class ReviewDetailView(DetailView):
    model = Review
    template_name = 'reviews/post_detail.html'

class PostUpdateView(UserPassesTestMixin, UpdateView):
    model = Review
    template_name = 'reviews/post_form.html'
    fields = ['movie_title_content', 'movie_content', 'movie_date', 'movie_rating']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    def get_success_url(self):
        movie = self.object.movie_name
        return reverse_lazy( 'movie-detail', kwargs={'pk': movie.id})
    
class PostDeleteView(UserPassesTestMixin, DeleteView):
    model = Review
    template_name = 'reviews/post_confirmed_delete.html'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    def get_success_url(self):
        movie = self.object.movie_name
        return reverse_lazy( 'movie-detail', kwargs={'pk': movie.id})
