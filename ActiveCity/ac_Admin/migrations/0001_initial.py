# Generated by Django 2.1.7 on 2019-03-16 08:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ac_Login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('dept_name', models.CharField(max_length=25, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Officer',
            fields=[
                ('officer_idno', models.AutoField(primary_key=True, serialize=False)),
                ('officer_name', models.CharField(max_length=20)),
                ('officer_contact', models.IntegerField()),
                ('officer_image', models.ImageField(upload_to='officer/')),
                ('officer_department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ac_Admin.Department')),
                ('officer_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ac_Login.Login_Details')),
            ],
        ),
    ]
