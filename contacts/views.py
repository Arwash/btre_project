from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact

# Create your views here.

# Handling the submission
def contact (request):
    if request.method == 'POST': #fetching the data from the form and store it in variables
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        # Check if a user has made inquiry already        
        if request.user.is_authenticated:
            user_id = request.user.id
            # bringing all the objects of the contact model(all the inquiry items and check if there is an object/inquiry
            # contain the same list_id and user_id. if this is true then this means the user has already made an inquiry:
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id) 
            if has_contacted:
                messages.error(request, 'You have already made inquiry for this listing')
                return redirect ('/listings/' + listing_id)


        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id)

        contact.save()

        # Send email
        send_mail(
            'Property Listing Inquiry', # email title
            'There has been an inquiry for ' + listing +'. sign into the admin panel for more info', # email body. Listing is the listig title
            'web.arwa@gmail.com', # The sending email adress
            [realtor_email, 'optimist4ever90@gmail.com'], # the emails that will receive the email message
            fail_silently = False         
        )


 # Send email
    # send_mail(
    #   'Property Listing Inquiry',
    #   'There has been an inquiry for ' + listing + '. Sign into the admin panel for more info',
    #   'traversy.brad@gmail.com',
    #   [realtor_email, 'techguyinfo@gmail.com'],
    #   fail_silently=False
    # )


        messages.success(request,'Your request has been submitted, a realtor will get back to you soon')

        return redirect ('/listings/' + listing_id)