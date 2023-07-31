from django.shortcuts import render
from .models import Destination
# Create your views here.


def index(request):
    # dest1 = Destination()
    # dest1.name = 'Yangon'
    # dest1.desc = ' The city that never sleeps '
    # dest1.img = 'destination_1.jpg'
    # dest1.price = 700
    # dest1.offer = False
    
    # dest2 = Destination()
    # dest2.name = 'Mandalay'
    # dest2.desc = ' The ancient city in my country'
    # dest2.img = 'destination_2.jpg'
    # dest2.price = 689
    # dest2.offer = False
    
    # dest3 = Destination()
    # dest3.name = 'Magway'
    # dest3.desc = ' The city that I never forget'
    # dest3.img = 'destination_3.jpg'
    # dest3.price = 690
    # dest3.offer = True
    
    # dests = [dest1, dest2 , dest3 ]
    dests = Destination.objects.all()
    
    return render(request,'index.html',{'dests': dests})