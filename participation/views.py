from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from participation.forms import QueryForm
from participation.models import Student

def index(request):
    if request.method == 'POST':
        form = QueryForm(request.POST) 
        if form.is_valid(): 
            return HttpResponseRedirect('id/%s/' % form.cleaned_data['student_id'])
    else:
        form = QueryForm()

    return render(request, 'index.html', {
        'form': form,
    })

def query(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    return render(request, 'query.html', {'student': student})
