from email import message
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Cita, Aula, User, Paciente, ProgramaEducativo, Procedencia
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

def citas(request):
    #citas = list(Cita.objects.values())
    #return JsonResponse(citas, safe=False)
    #return HttpResponse("Hola")
    citas = Cita.objects.all().order_by('-id')
    aulas = Aula.objects.all()
    programaseducativos = ProgramaEducativo.objects.all()
    procedencias = Procedencia.objects.all()
    responsables = User.objects.all()
    pacientes = Paciente.objects.all()

    context = {
        "citas": citas,
        "aulas": aulas,
        "responsables": responsables,
        "pacientes": pacientes,
        "programaseducativos": programaseducativos,
        "procedencias": procedencias
    }
    return render(request, "citas.html", context)

def reportes(request):
    #citas = list(Cita.objects.values())
    #return JsonResponse(citas, safe=False)
    #return HttpResponse("Hola")
    aulas = Aula.objects.all()
    context = {
        "aulas": aulas,
    }
    return render(request, "reportes.html", context)    

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
        cita.paciente_id = request.POST.get('id_paciente')
        cita.aula_id = request.POST.get('id_aula')
        cita.motivo = request.POST.get('motivo')    
        cita.fecha = request.POST.get('fecha')    
        cita.hora_inicio = request.POST.get('hora_inicio')    
        cita.hora_cierre = request.POST.get('hora_cierre')    
        cita.cumplio = request.POST.get('cumplio')    
        cita.costo = request.POST.get('costo')    
        cita.comentarios = request.POST.get('comentarios')    
        cita.responsable_id = request.POST.get('responsable')    

        cita.save()
        #return JsonResponse({'status','Guardado'}, safe=False)
        citas = list(Cita.objects.values())
        return JsonResponse(["Listo"], safe=False)        
    else:
        return JsonResponse(["No valido"], safe=False)


def guardarPaciente(request):
    if request.method == 'POST':
        paciente= Paciente()
        paciente.nombre = request.POST.get('nombre')
        paciente.expediente = request.POST.get('expediente')
        paciente.procedencia_id = request.POST.get('paciente_procedencia')
        paciente.programaeducativo_id = request.POST.get('paciente_programaeducativo')   

        paciente.save()
        #return JsonResponse({'status','Guardado'}, safe=False)
        paciente = list(Paciente.objects.values())
        return JsonResponse(paciente, safe=False)        
    else:
        return JsonResponse(["No valido"], safe=False)
# def postuserinfo(request):
#     if request.method == 'POST':
#         userinfo= UserInfo()
#         userinfo.firstname= request.POST.get('firstnamevalue')
#         userinfo.lastname= request.POST.get('lastnamevalue')    
#         userinfo.save()

# 	return render(request,'accounts/userinfoform.html')