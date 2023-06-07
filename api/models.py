from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User


# Create your models here.
class ShortUrl (models.Model):
    # Not explicitly needed, but it shuts up PyCharm CE
    objects = models.Manager()

    # Django already provides an auth_user table, so just use it as foreign key
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    full_url = models.TextField(db_comment="Full URL")
    # MVP: randomly-generated code (4 chars) / Later: custom codes
    shortcode = models.CharField(primary_key=True, max_length=16,
                                 db_comment="Short code used for the shortened link. "
                                            "Auto-generated ones are 4 characters long.")
    date_created = models.DateTimeField(default=timezone.now,
                                        db_comment="Date/time when the short URL was created.")
    is_deleted = models.BooleanField(default=False,
                                     db_comment="If True, the link is considered soft-deleted.")
    expiry_time = models.DateTimeField(default=None, null=True,
                                       db_comment="When the short URL expires (optional).")


class ShortUrlStats (models.Model):
    # Not explicitly needed, but it shuts up PyCharm CE
    objects = models.Manager()

    shortcode = models.OneToOneField(ShortUrl, primary_key=True, on_delete=models.CASCADE)
    times_accessed = models.IntegerField(db_comment="Number of times the URL was accessed.")
