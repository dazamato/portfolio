from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Avg, Max, Min, Sum
import numpy as np
from .models import Course, Lecture, Review
from django.utils import timezone

def home(request):
    return render(request, 'courses/home.html')


@login_required(login_url="/accounts/signup")
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
    course_object=Course.objects.get(pk=course_id)
    rev2=Review.objects.filter(course=course_object).exclude(approved_review=False)
    rev3=rev2.aggregate(Avg('rating'))
    if list(rev3.values())[0] is None:
        rev=0
    else:
        rev=round(list(rev3.values())[0],1)

    reviews=Review.objects.filter(course=course_object).exclude(approved_review=False)
    reviews_not_appr=Review.objects.filter(course=course_object).exclude(approved_review=True)
    if request.user.is_authenticated:
        lecture=Lecture()
        review=Review()
        course=get_object_or_404(Course, pk=course_id)
        course_object=Course.objects.get(pk=course_id)
        lectures=Lecture.objects.filter(course=course_object)
        if course.instructor == request.user and request.method == 'POST':
            if request.POST['title'] and request.POST['chapter'] and request.FILES['video'] and request.FILES['attachments']:
                course_object=Course.objects.get(pk=course_id)
                lecture.course=course_object
                lecture.title=request.POST['title']
                lecture.chapter=request.POST['chapter']
                # course.isfree=request.POST.get('isfree', False)
                lecture.video=request.FILES['video']
                lecture.attachments=request.FILES['attachments']
                lecture.save()
                return redirect('/courses/'+str(course.id))

                # return HttpResponseRedirect(reverse('poll_results', kwargs={'object_id': p.id}))
            else:
                return render(request, 'courses/detail.html', { 'error': 'Все поля обязательны для заполнения'}, { 'course':course, 'lecture':lecture, 'rev':rev, 'reviews_not_appr':reviews_not_appr })

        elif request.method == 'POST':
            if request.POST['text'] and request.POST['rating']:
                course_object=Course.objects.get(pk=course_id)
                review.course=course_object
                review.text=request.POST['text']
                review.rating=request.POST['rating']
                review.author=request.user
                review.created_date=timezone.datetime.now()
                review.save()
                return redirect('/courses/'+str(course.id))
            else:
                return render(request, 'courses/detail.html', { 'error': 'Все поля обязательны для заполнения'}, { 'course':course, 'lectures':lectures, 'reviews':reviews, 'rev':rev})


        else:
            return render(request, 'courses/detail.html', {'course': course, 'lectures': lectures, 'reviews': reviews, 'rev':rev, 'reviews_not_appr':reviews_not_appr})
    else:
        lecture=Lecture()
        course=get_object_or_404(Course, pk=course_id)
        course_object=Course.objects.get(pk=course_id)
        lectures=Lecture.objects.filter(course=course_object)
        return render(request, 'courses/detail.html', {'course': course, 'lectures': lectures, 'reviews': reviews, 'rev':rev })

def reviewbutton(request, course_id):
    if request.method == 'POST':
        course_object=Course.objects.get(pk=course_id)
        review_obj=get_object_or_404(Review, course=course_object)
        review_obj.approve
        return redirect('/courses/'+str(course.id))
