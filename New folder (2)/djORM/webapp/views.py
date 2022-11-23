from django.shortcuts import render
from webapp.models import student
# Create your views here.
def display_views(request):
    stds=student.objects.filter(stdmarks__gte=5)
    print(type(stds))
    my_dict={'stds':stds}
    return render(request,'myapp/index.html',my_dict)