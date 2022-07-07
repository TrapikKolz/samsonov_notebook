from django.db.models import Model, CharField, TextField, DateTimeField, IntegerField, ForeignKey, PROTECT
from django.conf import settings
from django.urls import reverse

User = settings.AUTH_USER_MODEL


class Note(Model):
    author = ForeignKey(User, null=True, blank=False, on_delete=PROTECT, verbose_name='Автор')
    title = CharField(max_length=255, verbose_name='Заголовок')
    text = TextField(blank=True, verbose_name='Текст')
    created = DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = DateTimeField(auto_now=True, verbose_name='Дата обновления')
    category = ForeignKey('Category', on_delete=PROTECT, verbose_name='Категория')
    views = IntegerField(default=0, verbose_name='Просмотры')

    def get_absolute_url(self):
        return reverse('user_note_list', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
        ordering = ['updated']


class Category(Model):
    title = CharField(max_length=255)

    def get_absolute_url(self):
        return reverse('user_note_category', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']
