# Generated by Django 4.2.2 on 2023-06-07 18:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ShortUrl',
            fields=[
                ('full_url', models.TextField(db_comment='Full URL')),
                ('shortcode', models.CharField(db_comment='Short code used for the shortened link. Auto-generated ones are 4 characters long.', max_length=16, primary_key=True, serialize=False)),
                ('date_created', models.DateTimeField(db_comment='Date/time when the short URL was created.', default=django.utils.timezone.now)),
                ('is_deleted', models.BooleanField(db_comment='If True, the link is considered soft-deleted.', default=False)),
                ('expiry_time', models.DateTimeField(db_comment='When the short URL expires (optional).', default=None, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ShortUrlStats',
            fields=[
                ('shortcode', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='api.shorturl')),
                ('times_accessed', models.IntegerField(db_comment='Number of times the URL was accessed.')),
            ],
        ),
        migrations.RunSQL("""
            ALTER TABLE api_shorturl ALTER COLUMN date_created SET DEFAULT now();
            ALTER TABLE api_shorturl ALTER COLUMN is_deleted SET DEFAULT FALSE;
        """, reverse_sql='')
    ]