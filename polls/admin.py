from django.contrib import admin

from .models import Choice, Question


admin.site.site_header = 'Мой сайт администрирования'
admin.site.site_title = 'Админка'
admin.site.index_title = 'Добро пожаловать в админку'


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)