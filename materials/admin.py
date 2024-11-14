from django.contrib import admin

from materials.models import Course, Lesson


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'pk', 'preview', 'description', 'owner')
    list_filter = ('title',)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'pk', 'preview', 'description', 'linc_to_video', 'course')
    list_filter = ('title', 'course',)