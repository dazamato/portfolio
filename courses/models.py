from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import magic




class Course(models.Model):
    title = models.CharField(max_length=100)
    # isfree = models.BooleanField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='images/')
    instructor = models.ForeignKey(User, on_delete=models.CASCADE)
    discription = models.TextField(max_length=300)
    mission = models.TextField(max_length=300)
    outcomes = models.TextField(max_length=300)
    rating = models.IntegerField(default=5)
    pub_date = models.DateTimeField()
    # url = models.CharField(max_length=100)
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
    rating = models.IntegerField(default=5)

    def approve(self):
        self.approved_review = True
        self.save()

    def __str__(self):
        return self.text


class Lecture(models.Model):
    course = models.ForeignKey('courses.Course', on_delete=models.CASCADE, related_name='lecture')
    chapter = models.CharField(max_length=100, default="Новый раздел")
    title = models.CharField(max_length=100)
    video = models.FileField(upload_to='videos/', null=True, verbose_name="video")
    attachments = models.FileField(upload_to='attachments/', null=True, verbose_name="attachments")

    # def clean_file(video):
    #     file = video.cleaned_data.get("file", False)
    #     filetype = magic.from_buffer(file.read())
    #     if not "MPEG-4" in filetype:
    #         raise ValidationError("Файл не имеет формат MPEG-4")
    #     return file

    def __str__(self):
        return self.title + ": " + str(self.video)

    # attachment =
    # embeded_video =
    # timeinminute =
    # class Category_title_choice(models.Model):
    #     Chapter = 'CH'
    #     lecture = 'LE'
    #     circulum_category_choices = (
    #             (Chapter, 'Глава'),
    #             (lecture, 'Лекция'),
    #     )
    # cirruculum_category= models.CharField(
    #     max_length=2,
    #     choices=Category_title_choice,
    #     default='Chapter',
    # )
