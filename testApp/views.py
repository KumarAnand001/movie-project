from django.shortcuts import render
from testApp.forms import MovieForm
from testApp.models import Movie

# Create your views here.
def indexView(request):

    return render(request, 'testApp/index.html')

def addMovieView(request):

    form = MovieForm()
    if request.method == "POST":

        form = MovieForm(request.POST)
        if form.is_valid():

            form.save()
            return indexView(request)

    return render(request, 'testApp/addMovie.html', {'form':form})

def listMovieView(request):

    movie_list = Movie.objects.all()
    return render(request, 'testApp/listMovie.html', {'movie_list':movie_list})
