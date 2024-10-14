from django.contrib import admin
from .models import Tag, Scope, Article
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        count_topic = 0
        for form in self.forms:
            # print(form)
            # print(self.forms)

            print(form.cleaned_data)
            if form.cleaned_data.get('is_main'):
                count_topic += 1
            else:
                continue
        if count_topic == 0:
            raise ValidationError('Выберите основной раздел')
        elif count_topic > 1:
            raise ValidationError('Основной раздел уже выбран')

        return super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    extre = 0
    formset = ScopeInlineFormset


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    tage_name = ['id', 'name']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]
