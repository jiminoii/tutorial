from django.shortcuts import render
from .models import Hospital

# Create your views here.
def show(request):
    hospital = Hospital.objects.all()
    return render(request,'show.html', {'list' : hospital})
    # html = ''
    # for c in curriculum:
    #     html += '%s번 %s<br>' %(c.id, c.name) 
    # return HttpResponse(html)

# Create your views here.


