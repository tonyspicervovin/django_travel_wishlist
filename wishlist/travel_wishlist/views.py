from django.shortcuts import render, redirect, get_object_or_404
from .models import Place
from .forms import NewPlaceForm

# Create your views here.

def place_list(request):

    if request.method == 'POST':
        form = NewPlaceForm(request.POST)
        place = form.save() #creating new place from form
        if form.is_valid(): #checks form is valid, right fields
            place.save() #saves to database
            return redirect('place_list')

    #if not post or form is not valid renders page with form to add new place
    places = Place.objects.filter(visited=False).order_by('name')
    new_place_form = NewPlaceForm()
    return render(request, 'travel_wishlist/wishlist.html', { 'places': places, 'new_place_form': new_place_form })


def places_visited(request):

    visited = Place.objects.filter(visited=True)
    return render(request, 'travel_wishlist/visited.html', { 'visited': visited })


def place_was_visited(request):

    if request.method == 'POST':
        pk = request.POST.get('pk')
        place = get_object_or_404(Place, pk=pk)
        place.visited = True
        place.save()

    return redirect('place_list')