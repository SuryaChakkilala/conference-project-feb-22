from django.db import models
# Create your models here.

class Conference(models.Model):
    name = models.CharField(max_length=200)
    event_date = models.DateField(null=True, blank=True)
    event_start_time = models.TimeField(null=True, blank=True)
    event_end_time = models.TimeField(null=True, blank=True)
    description = models.TextField(default='-', blank=True)
    webex_link = models.URLField(null=True, blank=True)
    youtube_live_link = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name

class PaperPresentation(models.Model):
    name = models.CharField(max_length=200)
    event_date = models.DateField(null=True, blank=True)
    event_start_time = models.TimeField(null=True, blank=True)
    event_end_time = models.TimeField(null=True, blank=True)
    description = models.TextField(default='-', blank=True)
    webex_link = models.URLField(null=True, blank=True)
    youtube_live_link = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name