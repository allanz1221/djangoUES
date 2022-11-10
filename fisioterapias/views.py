from email import message
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Cita, Aula
from django.utils.timezone import localdate
from django.views.defaults import bad_request, server_error
#from .forms import AddCita
from django.contrib import messages

def index(request):
    #citas = list(Cita.objects.values())
    #return JsonResponse(citas, safe=False)
    #return HttpResponse("Hola")
    aulas = Aula.objects.all()
    context = {
        "aulas": aulas,
    }
    return render(request, "index.html", context)

#@login_required
def aula(request, id):
    aula = None
    if id == 1:
        aula = 1
    else:
        aula = 2
    citas = Cita.objects.filter(aula=aula)
    aulas = Aula.objects.filter(id=aula)
    context = {
        "citas": citas,
        "hide_new_button": True,
        "priorities": "Event.priorities_list",
        "today": localdate(),
        "aulas": aulas
    }
    return render(request, "aula.html", context)

def guardarCita(request):
    if request.method == 'POST':
        cita= Cita()
        cita.motivo = request.POST.get('motivo')    
        cita.cumplio = request.POST.get('cumplio')    
        cita.fecha = request.POST.get('fecha')    
        cita.costo = request.POST.get('costo')    
        cita.aula_id = 1
        cita.cliente_id = 1
        cita.fecha = localdate()  
        cita.save()
        #return JsonResponse({'status','Guardado'}, safe=False)
        citas = list(Cita.objects.values())
        return JsonResponse(["Listo"], safe=False)        
    else:
        return JsonResponse(["No valido"], safe=False)

# def postuserinfo(request):
#     if request.method == 'POST':
#         userinfo= UserInfo()
#         userinfo.firstname= request.POST.get('firstnamevalue')
#         userinfo.lastname= request.POST.get('lastnamevalue')    
#         userinfo.save()

# 	return render(request,'accounts/userinfoform.html')