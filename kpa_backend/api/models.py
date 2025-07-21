from django.db import models



from django.db import models

class KPAForm(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15, null=True, blank=True)

    email = models.EmailField()
    document = models.FileField(upload_to='documents/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


