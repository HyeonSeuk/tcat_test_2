

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tcat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('location', models.CharField(blank=True, max_length=50, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='ticket_diarys/')),
                ('image_url', models.URLField(blank=True)),
                ('web_image', models.ImageField(blank=True, null=True, upload_to='ticket_diarys/')),
                ('web_image_url', models.CharField(blank=True, max_length=255, null=True)),
                ('review', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('categori', models.CharField(blank=True, max_length=50, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DynamicField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_title', models.CharField(max_length=255, null=True)),
                ('field_value', models.CharField(max_length=255, null=True)),
                ('tcat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dynamic_field', to='tcat.tcat')),
            ],
        ),
    ]
