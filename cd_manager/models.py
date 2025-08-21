from django.db import models
from django.urls import reverse


class Package(models.Model):
    BuildStatus = models.TextChoices(
        'BuildStatus', 'SUCCESS FAILURE NOT_BUILT BUILDING PREPARING WAITING')

    name = models.CharField(max_length=100, primary_key=True)
    repo_url = models.CharField(max_length=100)
    makepkg_extra_args = models.CharField(max_length=255, blank=True)
    clean_build = models.BooleanField(default=False)
    build_status = models.CharField(choices=BuildStatus.choices,
                                    default='NOT_BUILT', max_length=10)
    build_date = models.DateTimeField(null=True, blank=True)
    build_output = models.TextField(null=True, blank=True)
    repo_push = models.BooleanField(default=False)
    repo_release_push = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})
