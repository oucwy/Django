from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import StudentForm
from .models import Student

# markwy
# 2021.6.5 created.

# Create your views here.

def index(request):
    # students = Student.objects.all()  # 类名加方法，不需要实例化即可调用。
    students = Student.get_all()        # models.py中的get_all(),用类名直接调用，不用实例化。
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = StudentForm()

    context = {
        'students': students,
        'form': form,
    }
    return render(request, 'index.html', context=context)