from email import message
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Cita, Aula
from django.utils.timezone import localdate
from django.views.defaults import bad_request, server_error
from .forms import AddCita
from django.contrib import messages
# Create your views here.

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
    Aula = None
    if id == 1:
        Aula = 1
    else:
        Aula = 2
    citas = Cita.objects.filter(aula=Aula)
    form_cita = AddCita()
    context = {
        "citas": citas,
        "hide_new_button": True,
        "priorities": "Event.priorities_list",
        "today": localdate(),
        "form_cita": form_cita
    }
    return render(request, "aula.html", context)


def guardarCita(request):
    if request.POST:
        form = AddCita(request.POST)
        if form.is_valid:
            try:
                form.save()
            except:
                message(request, "Error al guardar cita")
                return redirect("index.html")
                
    Aula = request.POST.get('aula')
    citas = Cita.objects.filter(aula=Aula)
    form_cita = AddCita()
    context = {
        "citas": citas,
        "hide_new_button": True,
        "priorities": "Event.priorities_list",
        "today": localdate(),
        "form_cita": form_cita
    }                
    return redirect(request,'aula.html', context)

# def postuserinfo(request):
#     if request.method == 'POST':
#         userinfo= UserInfo()
#         userinfo.firstname= request.POST.get('firstnamevalue')
#         userinfo.lastname= request.POST.get('lastnamevalue')    
#         userinfo.save()

# 	return render(request,'accounts/userinfoform.html')