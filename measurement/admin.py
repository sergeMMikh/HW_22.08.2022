from django.contrib import admin
from django.forms import BaseInlineFormSet
from .models import Sensor, Measurement

# class ArticleChapterInLine(admin.TabularInline):
#     model = ArticleChapter
#     extra = 3
#     formset = ArticleChapterInlineFormset

@admin.register(Sensor)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']


@admin.register(Measurement)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ['detector_id', 'temperature', 'date']
