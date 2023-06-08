from django.contrib import admin

from .models import ShortUrl, ShortUrlStats, ShortUrlView

# Register your models here.
admin.site.register(ShortUrl)
admin.site.register(ShortUrlStats)


@admin.register(ShortUrlView)
class ShortUrlViewAdmin(admin.ModelAdmin):
    list_display = ('date_created',
                    'username',
                    'full_url',
                    'shortcode',
                    'is_deleted',
                    'times_accessed',
                    'expiry_time')
