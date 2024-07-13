from django.db import models # type: ignore
from django.contrib.auth.models import User # type: ignore
from datetime import datetime
class Todo(models.Model):
    title = models.TextField()
    is_completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_line=models.DateTimeField(null=True)