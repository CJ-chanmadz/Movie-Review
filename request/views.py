from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Request
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView


def request(request): 
    if request.method == 'POST':
        #Request
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        movie_title = request.POST['movie_title']  
        message = request.POST['message']

        if Request.objects.filter(movie_title=movie_title, email=email).exists():
            messages.error(request, 'You request it already!')
            return redirect('request')
        else:
            request_movie = Request(first_name=first_name, last_name=last_name, email=email, movie_title=movie_title, message=message)
            request_movie.save()
            messages.success(request, 'Your request submitted successfully!')
            return redirect('request')
        
    else:
        return render (request, 'request/request.html')

