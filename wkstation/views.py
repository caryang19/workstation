from django.shortcuts import render, redirect
import csv
from .models import Workstation
import socket
import getpass
from uuid import getnode as get_mac
from django.http import HttpResponse
import datetime



hostname = socket.gethostname()
system_user = getpass.getuser()
mac = get_mac()
ip_address = socket.gethostbyname(hostname)
system_details = {'system_user': system_user, 'ip_address': ip_address, 'mac': mac, 'hostname': hostname, 'system_brand': " ",}

#Print Database data ouut
def workstation(request):
    #workstation_list = Workstation.objects.all()
    return render(request, 'workstation.html')
   # {'workstation_list': {'system_brand': " ", 'system_user': system_user, 'ip_address': ip_address, 'mac': mac, 'hostname': hostname}})
        
# Create your views here.
def index(request):
    if request.method == "POST":
        workstation=Workstation()
        system_user=request.POST.get('system_user')
        hostname=request.POST.get('hostname')
        mac=request.POST.get('mac')
        ip_address=request.POST.get('ip_address')
        system_brand=request.POST.get('system_brand')
        system_type = request.POST.get('system_type')
        system_model=request.POST.get('system_model')
        location=request.POST.get('location')
        workstation.mac=mac
        workstation.hostname=hostname
        workstation.system_user=system_user
        workstation.ip_address=ip_address
        workstation.system_brand=system_brand
        workstation.system_type=system_type
        workstation.system_model=system_model
        workstation.location=location
        
        workstation.save()
        
        return HttpResponse("<h3>Thank You, Update Successfully Submitted.</h3>")

        
    return render(request, 'index.html', system_details)



def export_csv(request):
    
    response = HttpResponse(content_type='text/csv')
    

    writer=csv.writer(response)
    writer.writerow(['System User', 'Hostname', 'Mac Address', 'IP Address', 'System Brand', 'System Type', 'System Model', 'location'])

    workstation=Workstation.objects.filter(system_user=request.user)

    for member in Workstation.objects.all().values_list('system_user', 'hostname', 'mac', 'ip_address', 'system_brand', 'system_type', 'system_model', 'location'):
        writer.writerow(member)

    response['content-Disposition'] = 'attachment; filename=workstations'+str(datetime.datetime.now())+'.csv'
        
    return response

    