from django.shortcuts import get_object_or_404, render
from .models import listing
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# Create your views here.
def index(request):
    #it was listings = listing.objects.all() but we change it to the current method to fetch the objects ordered descently by time
    # the filter is to view the objects that are marked in the admin area as published
    listings = listing.objects.order_by('-list_date').filter(is_published=True)  
    
    #Pagination code
    paginator = Paginator(listings, 6) #The number is number of items per page
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {'listings' : paged_listings}    
    return render(request, 'listings/listings.html', context)

def Listing(request, listing_id):
    listing = get_object_or_404(listing, pk=listing_id) #the urgument Listing is the model, we do get object or 404 because if a user entered the link for an object thatdoes not exiist we want ot show it

    context = {'listing':listing}

    return render(request, 'listings/listing.html', context)

def search(request):
    return render(request, 'listings/search.html')