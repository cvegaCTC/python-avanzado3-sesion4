import datetime

from django.shortcuts import render

from api.models import Mascota


def index(request):
    fechaHoraActual = datetime.datetime.now()
    horaActual = fechaHoraActual.hour

    if horaActual < 12:
        saludo = "Buenos días"
    elif horaActual < 19:
        saludo = "Buenas tardes"
    else:
        saludo = "Buenas noches"

    mascotas = Mascota.objects.all()

    context = {"saludo": saludo, "mascotas": mascotas}

    return render(request, 'api/index.html', context)
