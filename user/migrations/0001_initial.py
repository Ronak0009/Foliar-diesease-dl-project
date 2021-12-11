# Generated by Django 4.0 on 2021-12-11 05:26

from django.db import migrations, models
import django.db.models.deletion
import user.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='model_data',
            fields=[
                ('model_id', models.CharField(default='', max_length=20, primary_key=True, serialize=False, verbose_name='Model Id')),
                ('name', models.CharField(default='', max_length=70, verbose_name='Model Name')),
                ('model_file', models.FileField(blank=True, upload_to='model_data', validators=[user.validators.validate_modelfile_extension], verbose_name='Model')),
            ],
        ),
        migrations.CreateModel(
            name='testing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(blank=True, upload_to='test_image', verbose_name='Image')),
                ('result', models.CharField(default='', max_length=100, verbose_name='Result')),
                ('accucracy', models.CharField(default='', max_length=20, verbose_name='Accuracy')),
                ('model_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.model_data')),
            ],
        ),
    ]
