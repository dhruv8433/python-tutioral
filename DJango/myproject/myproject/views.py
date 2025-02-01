# function based
# from django.http import HttpResponse 
from django.http import HttpResponseRedirect
from django.shortcuts import render

from news.models import news

from .forms import Calculation


def about_us(request):
    outputget=request.GET.get('output')
    # return HttpResponse("This is about page")
    data={
       "car":["Ford", "BMW", "Fiat"],
       "output":outputget
    }
    return render(request,'about.html',data)

def contact(request):
    if request.method =="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        msg=request.POST.get("msg")

        print("contact ")

        data={
            "name":name,
            "email":email,
            "msg":msg
        }
         # Encode the data as URL  
         # 
        url="/about/?output={}".format(data)
        return HttpResponseRedirect(url)
    else:
        return render(request,'contact.html')


def calc(request):
    if request.method == "POST":
        form = Calculation(request.POST)
        if form.is_valid():
            num1 = form.cleaned_data['num1']
            num2 = form.cleaned_data['num2']
            operator = form.cleaned_data['operator']
            if operator == "+":
                result = num1 + num2
            elif operator == "-":
                result = num1 - num2
            elif operator == "*":
                result = num1 * num2
            elif operator == "/":
                result = num1 / num2
            else:
                result = "Invalid operator"

            return render(request, 'calc.html', {'result': result})
    else:
        form = Calculation()
    return render(request, 'calc.html', {'form': form})
def check_number(request):

    status = ''

    if request.method == "POST":
        number = int(request.POST.get('num'))
        if (number % 2 == 0):
            status = 'Even'
        else:
            status = 'Odd'

    return render(request,'check_number.html',{"status":status})


def news_show(request):
    allNews= news.objects.all().order_by('title')
    return render(request,'news.html',{"allNews":allNews})

def news_author(request):
    allNews= news.objects.filter(author="rni").values()
    return render(request,'newsAuthor.html',{"allNews":allNews})