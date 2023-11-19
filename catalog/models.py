from django.db import models


class Mark(models.Model):
    name = models.CharField(max_length=64, null=False)


class ModelAuto(models.Model):
    name = models.CharField(max_length=64, null=False)
    mark_id = models.ForeignKey(to=Mark, on_delete=models.CASCADE)






