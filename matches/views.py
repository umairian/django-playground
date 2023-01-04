from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    matches = [
        'Hashir VS Waleed',
        'Owais VS Hamza'
    ]
    return render(request, 'matches/index.html', {
        'matches': matches
    })