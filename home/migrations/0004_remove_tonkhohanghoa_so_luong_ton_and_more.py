# Generated by Django 4.2.21 on 2025-05-20 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_tonghopxuatnguyenlieu_ngay_xuat_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tonkhohanghoa',
            name='so_luong_ton',
        ),
        migrations.AddField(
            model_name='tonkhohanghoa',
            name='ton_cuoi_ngay',
            field=models.FloatField(default=0.0, help_text='Tồn cuối ngày'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tonkhohanghoa',
            name='ton_dau_ngay',
            field=models.FloatField(default=0.0, help_text='Tồn đầu ngày'),
        ),
    ]
