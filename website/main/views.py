from django.shortcuts import render
from main.models import ContactMessage
from shop.models import Category

# This function renders the "About Us" page
def about(request):
    return render(request, 'about.html')

# This function handles the "Contact Us" page
# If the request method is POST, it processes the contact form submission
# Otherwise, it simply displays the contact form
def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        text = request.POST['text']
        ContactMessage.objects.create(
            name=name,
            email=email,
            text=text,
        )
        message = "Your message is submited"
    else:
        message = None

    return render(request, 'contact.html', {'message':message})

# This function renders the FAQ (Frequently Asked Questions) page
def faq(request):
    return render(request, 'faq.html')

# This function renders the homepage
def home(request):
    categories = Category.objects.all()
    return render(request, 'home.html',{'categories':categories})

# This function renders the Terms and Conditions page
def terms(request):
    return render(request, 'terms.html')
    