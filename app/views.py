from django.shortcuts import render, redirect
from .models import *
from django.http import JsonResponse


# Create your views here.
def Index(request):
    return render(request, 'app/index.html')

def LoginPage(request):
    return render(request, 'app/login.html')

def Signuppage(request):
    return render(request, 'app/signup.html')

def login(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')

        if UserMaster.objects.filter(phone_number=phone).exists():
            user = UserMaster.objects.get(phone_number=phone)
            request.session['user_id'] = user.id
            return render(request, 'app/detail_form.html')
        else:
            message = "User does not exist"
            return render(request, 'app/signup.html', {'msg': message})
    else:
        return redirect('loginpage')


def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST['phone']

        new_user = UserMaster.objects.create(name=name, phone_number=phone)
        message = 'Signup Successfull!!'
        return render(request, 'app/login.html', {'msg':message})
    else:
        return redirect('signuppage')
   

def Detail_form(request):
    all_location = User.objects.all()
    print(all_location) 
    return render(request, 'app/detail_form.html', {'all_location': all_location})


def location_grid(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        location = request.POST.get('location')
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')

        if city and location:
            locations = User.objects.filter(city=city, location=location)
        elif latitude and longitude:
            locations = Location.objects.filter(latitude=latitude, longitude=longitude)
        else:
            locations = []

        return render(request, 'app/location_form.html', {'locations': locations})

    return render(request, 'app/location_form.html')


