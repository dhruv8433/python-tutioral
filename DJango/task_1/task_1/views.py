import uuid
from django.shortcuts import render
from service.models import Service
def homepage(request):
    servicedata=Service.objects.all().order_by("-title")[:1]
    # for i in servicedata:
        
    #     print(i.title)
    data={"servicename":servicedata}
    return render(request, 'index.html',data)

def about(request):
    return render(request, 'about.html')

def skills(request):
    return render(request, 'skills.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Generate a unique contact ID
        contact_id = uuid.uuid4().hex[:8]  # Short UUID for simplicity

        # Render the thank you page with submitted data
        return render(request, 'thank_you.html', {
            'name': name,
            'email': email,
            'message': message,
            'contact_id': contact_id,
        })

    return render(request, 'contact.html')
