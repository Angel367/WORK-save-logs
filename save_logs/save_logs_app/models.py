from django.db import models

# Create your models here.


class SearchLog(models.Model):
    search_query = models.CharField(max_length=255)
    search_date = models.DateTimeField(auto_now_add=True)
    search_ip = models.GenericIPAddressField()
    path = models.CharField(max_length=255)
    status_code = models.IntegerField()

    def __str__(self):
        return self.search_query
