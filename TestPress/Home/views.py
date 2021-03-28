from datetime import datetime

from django.shortcuts import render

from Home.models import Contact

from django.contrib import messages

# Create your views here.
def index(request):
    # context = {
    #     "variable1": "Fzee is Good",
    #     "variable2": "at Programming"
    # }
    return render(request, 'index.html')
    # return HttpResponse("This is Home Page")


def about(request):
    return render(request, 'about.html')
    # return HttpResponse("This is About Page")


def service(request):
    return render(request, 'services.html')
    # return HttpResponse("This is Services Page")


def contacts(request):
    if request.method == "POST":
        # name = request.POST.get('name')
        # phone = request.POST.get('phone')
        # email = request.POST.get('email')
        # desc = request.POST.get('desc')
        # contact = Contact(name=name, phone=phone, email=email, desc=desc, date=datetime.today())
        contact = Contact(name=request.POST.get('name'), phone=request.POST.get('phone'),
                          email=request.POST.get('email'),
                          desc=request.POST.get('desc'), date=datetime.today())
        contact.save()
        messages.success(request, 'We have received your message successfully, we will get back to you soon.')

    return render(request, 'contact.html')
    # return HttpResponse("This is Contacts Page")
