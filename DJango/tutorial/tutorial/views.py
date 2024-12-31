from django.http import HttpResponse
from django.shortcuts import render
def about_us(request):
    return HttpResponse("Hi this is about page") # type: ignorey


def about_page(request):
    return render(request,"about.html")

# dynamic url
def course(request,courseId):
    return HttpResponse("Hi this is <b>" +courseId+ "now happy")

def course_detail(request):
    data={
        "name":"dhruv",
        "hobby":["coding","music"],
        "number":[10,30,60],
        "students":[{"name":"rni","age":30},{"name":"dhruv","age":30}]
    }
    return render(request,"about.html",data)