# Generated by Django 3.1.2 on 2020-10-28 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20201027_2207'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=100)),
                ('specs', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='sharpen',
            name='date',
            field=models.DateField(verbose_name='sharpen date'),
        ),
        migrations.AlterField(
            model_name='sharpen',
            name='sharp',
            field=models.CharField(choices=[('H', 'Hone'), ('S', 'Sharpen'), ('G', 'Grind')], default='H', max_length=1),
        ),
        migrations.AddField(
            model_name='cutlery',
            name='prep',
            field=models.ManyToManyField(to='main_app.Prep'),
        ),
    ]