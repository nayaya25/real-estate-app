from django.shortcuts import render, redirect
from .models import Contact
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.
def contact(request):
    if request.method == 'POST':
            listing_id = request.POST['listing_id']
            listing = request.POST['listing']
            name = request.POST['name']
            email = request.POST['email']
            phone = request.POST['phone']
            message = request.POST['message']
            user_id = request.POST['user_id']
            realtor_email = request.POST['realtor_email']

            if request.user.is_authenticated:
                    user_id = request.user.id
                    has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
                    if has_contacted:
                            messages.error(request, 'Opps! You have made an enquiry about this property already. the realtor will contact you real soon.')
                            return redirect('/listings/' + listing_id)

            
            contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id)
            contact.save()

            send_mail(
                    'Property Listing Enquiry',
                    'There has been an enquiry for ' + listing + ". Sign in to your admin dashboard for more info.",
                    'nayayaibrahim21@gmail.com',
                    [realtor_email, nayayaibrahim @ gmail.com],
                    fail_silently=True
            )
            messages.success(request, 'Your request has been submitted successfully. a realtor will get back to you soon!')
            return redirect('/listings/'+ listing_id)