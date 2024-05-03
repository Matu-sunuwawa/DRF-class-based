from django.db import models

# Create your models here.

class NoteApp(models.Model):
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.title