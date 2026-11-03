from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def About(request):
    return render(request, 'about.html')

def Contact(request):
    return render(request, 'contact.html')

def Home(request):
    return render(request, 'index.html')

def Admin_Dashboard(request):
    if not request.user.is_staff:
        return redirect('login')           ###
    doctors = Doctor.objects.all()
    patients = Patient.objects.all()
    appointments = Appointment.objects.all()

    d = 0
    p = 0
    ap = 0

    for i in doctors:
        d+=1

    for i in patients:
        p+=1

    for i in appointments:
        ap+=1

    d1 = {'d':d,'p':p,'ap':ap}

    return render(request, 'admin_dashboard.html', d1)

def Login(request):
    error=""
    if request.method == "POST":
        u_name = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username= u_name, password= p)
        try:
            if user.is_staff:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'login.html', d)

def Logout_admin(request):
    if not request.user.is_staff:
        return redirect('login')
    logout(request)
    return redirect('login')

def View_Doctor(request):
    if not request.user.is_staff:
        return redirect('login')      ###
    doc = Doctor.objects.all()
    d = {'doc':doc}
    return render(request, 'view_doctor.html', d)

def View_Patient(request):
    if not request.user.is_staff:
        return redirect('login')      ###
    patient = Patient.objects.all()
    p = {'patient':patient}
    return render(request, 'view_patient.html', p)

def View_Appointment(request):
    if not request.user.is_staff:
        return redirect('login')      ###
    appoint = Appointment.objects.all()
    ap = {'appoint':appoint}
    return render(request, 'view_appointment.html', ap)

def Add_Doctor(request):
    error=""
    if not request.user.is_staff:
        return redirect('login')      ###
    if request.method == "POST":
        d_name = request.POST['dname']
        c = request.POST['contact']
        sp = request.POST['spec']
        try:
            Doctor.objects.create(name=d_name ,mobile=c ,speciality=sp)
            error = "no"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'add_doctor.html', d)

def Add_Patient(request):
    error=""
    if not request.user.is_staff:
        return redirect('login')       ###
    if request.method == "POST":
        p_name = request.POST['pname']
        g = request.POST['gender']
        mo = request.POST['mob']
        ads = request.POST['address']
        try:
            Patient.objects.create(name=p_name, gender=g ,mobile=mo ,address=ads)
            error = "no"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'add_patient.html', d)

def Add_Appointment(request):
    error=""
    if not request.user.is_staff:
        return redirect('login')

    doctor1 = Doctor.objects.all()                                     # fetch data from Doctor model
    patient1 = Patient.objects.all()                                   # fetch data from Patient model

    if request.method == "POST":
        d = request.POST['doctor']
        p = request.POST['patient']
        d1 = request.POST['date']
        t1 = request.POST['time']
        doctor = Doctor.objects.filter(name=d).first()
        patient = Patient.objects.filter(name=p).first()
        try:
            Appointment.objects.create(doctor=doctor, patient=patient ,date1=d1 ,time1=t1)
            error = "no"
        except:
            error = "yes"
    d = {'doctor': doctor1, 'patient': patient1, 'error': error}
    return render(request, 'add_appointment.html', d)


def Delete_Doctor(request, pid):
    if not request.user.is_staff:
        return redirect('login')      ###
    doctor = Doctor.objects.get(id=pid)
    doctor.delete()
    return redirect('view_doctor')

def Delete_Patient(request, pid):
    if not request.user.is_staff:
        return redirect('login')      ###
    patient = Patient.objects.get(id=pid)
    patient.delete()
    return redirect('view_patient')

def Delete_Appointment(request, pid):
    if not request.user.is_staff:
        return redirect('login')      ###
    appointment = Appointment.objects.get(id=pid)
    appointment.delete()
    return redirect('view_appointment')




