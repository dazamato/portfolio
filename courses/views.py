from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Course, Lecture
from django.utils import timezone

def home(request):
    return render(request, 'courses/home.html')
@login_required
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['discription'] and request.POST['mission'] and request.POST['outcomes'] and request.POST['price']  and request.FILES['image']:
            course=Course()
            course.title=request.POST['title']
            course.discription=request.POST['discription']
            course.mission=request.POST['mission']
            course.outcomes=request.POST['outcomes']
            # if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
            #     course.url=request.POST['url']
            # else:
            #     course.url='http://' + request.POST['url']
            course.price=request.POST['price']
            # course.isfree=request.POST.get('isfree', False)
            course.image=request.FILES['image']
            course.pub_date=timezone.datetime.now()
            course.instructor=request.user
            course.save()
            return redirect('/courses/'+str(course.id))
        else:
            return render(request, 'courses/create.html', { 'error': 'Все поля обязательны для заполнения'})

    else:
        return render(request, 'courses/create.html')

def detail(request, course_id):
    course=get_object_or_404(Course, pk=course_id)
    return render(request, 'courses/detail.html', {'course':course})

def addlecture(request, course_id):
    lecture=Lecture()
    course=get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        if request.POST['title'] and request.POST['discription'] and request.FILES['video'] and request.FILES['attachments']:
            course_object=Course.objects.get(pk=course_id)
            lecture.course=course_object
            lecture.title=request.POST['title']
            lecture.discription=request.POST['discription']
            # course.isfree=request.POST.get('isfree', False)
            lecture.video=request.FILES['video']
            lecture.attachments=request.FILES['attachments']
            lecture.save()
            return redirect('/courses/'+str(course.id))

            # return HttpResponseRedirect(reverse('poll_results', kwargs={'object_id': p.id}))
        else:
            return render(request, 'courses/addlecture.html', { 'error': 'Все поля обязательны для заполнения'}, {'course': course })

    else:

        return render(request, 'courses/addlecture.html', {'course': course })
