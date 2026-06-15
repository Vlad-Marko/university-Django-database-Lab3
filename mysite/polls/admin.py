# from django.contrib import admin

# # Register your models here.
# from django.contrib import admin
# from .models import Question, Choice

# admin.site.register(Question)
# admin.site.register(Choice)

from django.contrib import admin
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text", "question_type"]}), 
        ("Information about date", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]
    list_display = ["question_text", "pub_date", "was_published_recently", "question_type","countAbsoluteVotes"]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('choice_text', 'question', 'votes', 'is_correct', 'is_popular')


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
