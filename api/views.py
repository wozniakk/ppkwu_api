from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from api.models import Student

# Create your views here.

def student(request, student_id):
    student = Student.objects.get(id=student_id)
    return render_to_response('api/index.html',
        {'student': student},
        context_instance=RequestContext(request))
    