from django.shortcuts import render
from .models import moviel

def filldetails(request):
    return render(request, 'Movielist/Updatelist.html')

def Movie(request):
    movielist = moviel.objects.all()
    return render(request, 'Movielist/Movieslist.html', {'moviel': movielist})


def InsertData(request):
    MovieName = request.POST.get('MovieName')
    Budget= request.POST.get('Budget')
    IMDBrating = request.POST.get('IMDBrating')
    Movieinfo = request.POST.get('Movieinfo')
    link=request.POST.get('link')
    image=request.POST.get('image')
    movie_list=moviel(MovieName=MovieName,Budget=Budget,IMDBrating=IMDBrating,Movieinfo=Movieinfo,link=link,image=image)
    movie_list.save()
    return render(request, 'Movielist/Updatelist.html')

def search(request):
    query=request.GET.get('search')
    allPost=moviel.objects.filter(MovieName__icontains=query)
    params={'moviel': allPost, 'query': query}
    return render(request, 'Movielist/Search.html', params)



