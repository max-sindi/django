from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=20)
    body = models.CharField(max_length=100)

    class Meta:
        app_label = 'todosbackend'
        ordering = ('title',)