from django.shortcuts import render
from .models import courses,enquiry,lessons,section
# Create your views here.
def index(request):
    course_list = courses.objects.all()

    context = {
        'courses': course_list
    }
    return render(request,'home.html',context)

def about(request):
    return render(request,'about.html')

def course(request):
    course_list=courses.objects.all()

    context = {
        'courses':course_list
    }
    return render(request,'courses.html',context)

def course_details(request,num):
    course=courses.objects.get(id=num)
    sections = section.objects.filter(course=course)
    lesson=lessons.objects.filter(course=course)

    context = {
        'course_id': num,
        'course_obj':course,
        'lessons':lesson,
        'section':sections
    }
    return render(request, 'course_details.html',context)




def contact(request):
    if request.method == 'POST':
        name_r =request.POST.get('cname')
        email_r = request.POST.get('email')
        number_r = request.POST.get('mob')
        message_r = request.POST.get('msg')

        info=enquiry(name=name_r,number=number_r,email=email_r,message=message_r)
        info.save()
        form = True
        context ={
            'submitted':form
        }
        return render(request,'contact.html',context)
    else:
        return render(request, 'contact.html')


