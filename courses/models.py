from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



class Course(models.Model):
    title = models.CharField(max_length=100)
    isfree = models.BooleanField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='images/')
    instructor = models.ForeignKey(User, on_delete=models.CASCADE)
    discription = models.CharField(max_length=300)
    mission = models.CharField(max_length=300)
    outcomes = models.CharField(max_length=300)
    rating = models.IntegerField(default=1)
    pub_date = models.DateTimeField()
    # class Category_choice(models.Model):
    #     DataScience = 'DS'
    #     WebDevelopment = 'WD'
    #     PythonProgramming = 'PP'
    #     Course_Category_CHOICES = (
    #         (DataScience, 'DataScience'),
    #         (WebDevelopment, 'Веб разработка'),
    #         (PythonProgramming, 'Курсы по Python')
    # )
    # category_course = models.CharField(
    #     max_length=2,
    #     choices=Course_Category_CHOICES,
    #     default=DataScience,
    # )

    def __str__(self):
        return self.title
    def pub_date_pretty(self):
        return self.pub_date.strftime('%d %m %Y')

class Review(models.Model):
    course = models.ForeignKey('courses.Course', on_delete=models.CASCADE, related_name='review')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_review = models.BooleanField(default=False)

    def approve(self):
        self.approved_review = True
        self.save()

    def __str__(self):
        return self.text


# class Curriculum(models.Model):
#     course = models.ForeignKey('courses.Course', on_delete=models.CASCADE, related_name='Curriculum')
#     title = models.CharField(max_length=100)
#     attachment =
#     embeded_video =
#     timeinminute =
#     # class Category_title_choice(models.Model):
#     #     Chapter = 'CH'
#     #     lecture = 'LE'
#     #     circulum_category_choices = (
#     #             (Chapter, 'Глава'),
#     #             (lecture, 'Лекция'),
#     #     )
#     # cirruculum_category= models.CharField(
#     #     max_length=2,
#     #     choices=Category_title_choice,
#     #     default='Chapter',
#     # )
#     lecture
