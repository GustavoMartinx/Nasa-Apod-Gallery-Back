from django.db import models
from django.contrib.auth.models import User

class SavedCollections(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    # date_list = models.JSONField()

    user = models.ForeignKey(User, on_delete=models.CASCADE)