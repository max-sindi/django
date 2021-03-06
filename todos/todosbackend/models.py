from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=20)
    body = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    isDone = models.BooleanField(default=False)

    class Meta:
        app_label = 'todosbackend'
        ordering = ('created',)