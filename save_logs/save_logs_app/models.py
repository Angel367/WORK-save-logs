from django.db import models

# Create your models here.


class SearchLog(models.Model):
    search_query = models.CharField(max_length=255, null=True, blank=True)
    search_date = models.DateTimeField(auto_now_add=True)
    search_ip = models.GenericIPAddressField(null=True, blank=True)
    path = models.CharField(max_length=255, null=True, blank=True)
    status_code = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.search_query
