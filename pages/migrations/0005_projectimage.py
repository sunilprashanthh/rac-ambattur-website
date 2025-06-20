# Generated by Django 5.2.1 on 2025-05-25 01:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_project_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(help_text='Upload an image for the project gallery.', upload_to='project_gallery/')),
                ('caption', models.CharField(blank=True, help_text='Optional caption for the image.', max_length=200, null=True)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery_images', to='pages.project')),
            ],
            options={
                'ordering': ['uploaded_at'],
            },
        ),
    ]
