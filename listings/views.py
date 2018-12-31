from django.shortcuts import render

def listing(request):
    return render(request, 'listings/listing.html')


def index(request):
    return render(request, 'listings/listings.html')


def search(request):
    return render(request, 'listings/search.html')
