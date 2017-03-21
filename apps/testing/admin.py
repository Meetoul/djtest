from django.contrib import admin
from nested_inline.admin import NestedStackedInline, NestedTabularInline, NestedModelAdmin
from .models import *


class ChoiceInline(NestedTabularInline):
    model = Choice
    extra = 4


class QuestionInline(NestedStackedInline):
    model = Question
    extra = 3
    inlines = [ChoiceInline]


class TestAdmin(NestedModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'description', 'result_text']}),
    ]
    inlines = [QuestionInline]


admin.site.register(Test, TestAdmin)
