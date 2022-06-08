from django.shortcuts import render,redirect
from .models import Appointment,AppointmentForm
     

def add_appointment(request):
    if request.method=="POST":
        form=AppointmentForm(request.POST)
        context={'form':form}
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request,"addappointment.html",context)
    else:
        form=AppointmentForm()
        context={'form':form}
        return render(request,'addappointment.html',context)

def appointmentapp_list(request):
        appoint =Appointment.objects.all()
        context={'appoint':appoint}
        return render(request,'appointmentapplist.html',context)

def delete_appointment(request,id):
    appoint = Appointment.objects.get(id=id)
    appoint.delete()
    return redirect('/')

def edit_appointment(request,id):
    appoint = Appointment.objects.get(id=id)
    if request.method == 'POST':
        appoint = AppointmentForm(request.POST,instance=appoint)
        appoint.save()
        return redirect('/')
    else:
        appoint = AppointmentForm(instance = appoint)
        context = {'form':appoint}
        return render(request,'addappointment.html',context)


