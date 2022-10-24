from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from . models import Cita
from django.utils.timezone import localdate
from django.views.defaults import bad_request, server_error
# Create your views here.

def hello(request):
    citas = list(Cita.objects.values())
    return JsonResponse(citas, safe=False)
    #return HttpResponse("Hola")

#@login_required
def index(request):
    context = {
        "hide_new_button": True,
        "priorities": "Event.priorities_list",
        "today": localdate(),
    }

    return render(request, "index.html", context)