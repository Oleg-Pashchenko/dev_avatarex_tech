from django.db import models


class Task(models.Model):
    text = models.CharField(max_length=200, null=False)
    status = models.TextField(null=False)
    owner_host = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.owner_host}: {self.status}'
