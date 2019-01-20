from django.contrib import admin

from .models import Course, Review, Lecture

admin.site.register(Course)
admin.site.register(Review)
admin.site.register(Lecture)
