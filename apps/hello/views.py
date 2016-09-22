from django.shortcuts import render

from apps.hello.models import PersonalData


def contact_data(request):
    pers_data = PersonalData.objects.first()
    return render(request, 'home.html', {'data': pers_data})
