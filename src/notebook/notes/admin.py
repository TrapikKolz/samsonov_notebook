from django.contrib import admin
from django import forms

from .models import Note, Category


class NoteAdminForm(forms.ModelForm):
    labels = 'Описание'

    class Meta:
        model = Note
        fields = '__all__'


class NoteAdmin (admin.ModelAdmin):
    form = NoteAdminForm
    list_display = ('id', 'title', 'author', 'category', 'created', 'updated', 'views')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_filter = ('category', 'title', 'author')
    fields = ('title', 'category', 'text', 'author')
    readonly_fields = ('views', 'created', 'author')
    save_on_top = True


class CategoryAdmin (admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(Note, NoteAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.site_title = 'Управление записями'
admin.site.site_header = 'Управление записями'
