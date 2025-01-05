# all pages view 

from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from project.models import project
from contactInquiry.models import contactInquiry
from resort.models import resort
from django.core.paginator import Paginator
from resort_meals.models import resort_meals

def homePage(request):
    return render(request, 'index.html')

def projectPage(request):

    projectData = project.objects.all() # fetch all project
    data = {
        'projectData': projectData
    }

    return render(request, 'projects.html', data)

def contactPage(request):
        if request.method == 'POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            message = request.POST.get('message')

            try:
                data = contactInquiry(name=name, email=email, phone=phone, message=message)
                data.save()
                print(f"Contact saved: data",data)
                return redirect('/thank-you')
            except Exception as e:
                print(f"Error saving contact: {e}")
                return HttpResponse("An error occurred. Please try again later.")
        return render(request, 'contact.html')

def thanksPage(request):
    return HttpResponse('Thank you for contact us')

def aboutPage(request):
    return render(request, 'about.html')

def resortsPage(request):
    # Get all resorts
    resorts = resort.objects.all()

    # Filter based on search parameters
    city = request.GET.get('city')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    if city:
        resorts = resorts.filter(location__icontains=city)
    if min_price:
        resorts = resorts.filter(price__gte=min_price)
    if max_price:
        resorts = resorts.filter(price__lte=max_price)

     # Pagination
    pagination = Paginator(resorts, 3) # 3 resorts per page
    page = request.GET.get('page') # Get the page number
    resorts = pagination.get_page(page) # Get the resorts for the page

    data = {
        'resorts': resorts
    }

    return render(request, 'resorts.html', data)

def resort_detail(request, id, category=None):
    # Fetch the resort object
    singleResort = resort.objects.get(id=id)
    
    # Pass the resort object to the template
    data = {
        'resort': singleResort,
        'category': category
    }

    return render(request, 'resort-details.html', data)

def resortMeals(request, id, category):
    # Fetch the resort object
    singleResort = resort.objects.get(id=id)
    meals = resort_meals.objects.filter(refrence_resort=id)

    print("cat" ,category)
    
    # Pass the resort object to the template
    data = {
        'resort': singleResort,
        'meals': meals
    }

    return render(request, 'resort-meals.html', data)