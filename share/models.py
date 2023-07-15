from django.db import models


class Share(models.Model):
    form_name = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.form_name
