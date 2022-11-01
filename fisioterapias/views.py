from email import message
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Cita
from django.utils.timezone import localdate
from django.views.defaults import bad_request, server_error
from .forms import AddCita
from django.contrib import messages
# Create your views here.

def hello(request):
    citas = list(Cita.objects.values())
    return JsonResponse(citas, safe=False)
    #return HttpResponse("Hola")

#@login_required
def index(request):
    citas = Cita.objects.all()
    form_cita = AddCita()
    context = {
        "citas": citas,
        "hide_new_button": True,
        "priorities": "Event.priorities_list",
        "today": localdate(),
        "form_cita": form_cita
    }

    return render(request, "index.html", context)


def guardarCita(request):
    if request.POST:
        form = AddCita(request.POST)
        if form.is_valid:
            try:
                form.save()
            except:
                message(request, "Error al guardar cita")
                return redirect("index.html")
    return redirect("index.html")