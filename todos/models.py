from django.db import models

# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)


# Feat => Feature
# Fix => Bug fix
# Chore