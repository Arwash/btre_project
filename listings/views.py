from django.shortcuts import get_object_or_404, render
from .models import listing
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import bedroom_choices, state_choices, price_choices


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
    Listing = get_object_or_404(listing, pk=listing_id) #the urgument Listing is the model, we do get object or 404 because if a user entered the link for an object thatdoes not exiist we want ot show it
    context = {'listing': Listing}
    return render(request, 'listings/listing.html', context)

def search(request):
    #first, start a queryset list
    queryset_list = listing.objects.order_by('-list_date')
    
    # Keyword
    #Second, keywords. We make a GET request from the form. The below code checks if the keywords (name attribute) does exist in our form
    if 'keywords' in request.GET:
        #Third, getting the actual form value of keyword (the value entered by the user)
        keywords = request.GET['keywords']
        # Fourth, make sure it's not an empty string. like if keywords does exist with a a value.
        # if a value exists, then we do the filtering to get the desired result based on the given keyword
        if keywords:
            queryset_list = queryset_list.filter(description__icontains = keywords)
    # City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact = city)

     # State
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact = state)

  # bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte = bedrooms) # lte is less than or equal. To bring the offers up to 4 bedrooms

  # price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte = price)



    context = {'state_choices' : state_choices,
                'bedroom_choices' : bedroom_choices,
                'price_choices' : price_choices,
                'listings' : queryset_list,
                'values' : request.GET} # the last dictionary item is to make the search value stays in the form it will store it like this e.g. for city: city.value which is the value of the city
    return render(request, 'listings/search.html', context)