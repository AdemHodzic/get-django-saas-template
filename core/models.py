from django.db import models

class SimpleModel(models.Model):
    id = models.UUIDField(primary_key=True)
    created_at = models.DateTimeField(editable=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
