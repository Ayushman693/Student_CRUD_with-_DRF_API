from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User

# This method is used to add and display the data.
def add_show(request):
    if request.method == "POST":
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            n = fm.cleaned_data['name'] 
            e = fm.cleaned_data['email']
            p = fm.cleaned_data['password']
            reg = User(name=n, email=e, password=p)
            reg.save()
            #fm.save()
            fm = StudentRegistration()
    else: 
        fm = StudentRegistration()
    stud = User.objects.all()
    return render(request, 'enroll/Addandshow.html', {'form': fm, 'stu':stud})

# This function will update and edit.
def update_data(request, id):
    if request.method == "POST":
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
    return render(request, 'enroll/updatestudent.html', {'form':fm})

 
# This method is used to delete the data.
def delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
