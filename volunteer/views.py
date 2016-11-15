from django.shortcuts import render,redirect,reverse
from .forms import VolunteerForm
from django.http import JsonResponse
from .models import State,City,Volunteer
from random import randint
from django.contrib import messages
from .messagingUtilties import sendMessage
# Create your views here.
def otpGenerator():
    return str(randint(1000,9999))

def getStates(request):
    states =State.objects.filter(country_id=101).values("id","state_name")
    d = []
    for state in states:
        d.append(state)
    return JsonResponse({"all_state": d})
def getCities(request):
    stateId = request.GET.get('id')
    cities = City.objects.filter(state_id=stateId).values('id','city_name')
    d = []
    for city in cities:
        d.append(city)
    return JsonResponse({'all_city':d})
def enterVolunteer(request):
    if(request.method == 'GET'):
        form = VolunteerForm()
        return render(request,'volunteerForm.html',{'form':form})
    else:
        form = VolunteerForm(request.POST)
        if(form.is_valid()):
            obj = form.save(commit=False)
            obj.city_id = request.POST.get('city')
            otp = otpGenerator()
            obj.otp = otp
            obj.save()
            sendMessage(obj.mobile,otp)
            return render(request,'verifyOTP.html',{'mobile':obj.mobile,'id':obj.id})
        return render(request,'volunteerForm.html',{'form':form})

def home(request):
    if (request.method == 'GET'):
        volunteers = Volunteer.objects.all()
        return render(request, 'home.html', {'volunteers': volunteers})
    else:
        state = request.POST.get('state')
        city = request.POST.get('city')
        if(state == None):
            volunteers = Volunteer.objects.all()
        else:
            if(city == None):
                volunteers = Volunteer.objects.filter(city__state_id=int(state))
            else:
                volunteers = Volunteer.objects.filter(city_id=int(city))

        return render(request, 'home.html', {'volunteers':volunteers})

def verifyOTP(request):
    if(request.method == 'POST'):
        mobile = request.POST.get('mobile')
        otp = request.POST.get('otp')
        voulunteer = Volunteer.objects.filter(id=mobile)
        print(request.POST)
        if(len(voulunteer) > 0):
            votp = voulunteer[0].otp
            print(votp,otp,votp==otp)
            if(votp == otp):
                print('aaya')
                voulunteer[0].mobile_verified = True
                voulunteer[0].save()
                messages.add_message(request, messages.SUCCESS,"Thanks for volunteering")
                return redirect(reverse('home'))
            else:
                messages.add_message(request,messages.WARNING,"Wrong OTP")
                return render(request, 'verifyOTP.html', {'mobile': mobile})
