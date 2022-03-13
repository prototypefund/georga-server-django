# Generated by Django 4.0.3 on 2022-03-03 19:38

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActionCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'verbose_name': 'Einsatzkategorie',
                'verbose_name_plural': 'Einsatzkategorien',
            },
        ),
        migrations.CreateModel(
            name='EquipmentProvided',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'verbose_name': 'Ausstattung durch HiOrg',
                'verbose_name_plural': 'Ausstattungen durch HiOrg',
            },
        ),
        migrations.CreateModel(
            name='EquipmentSelf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'verbose_name': 'Ausstattung mitzubringen',
                'verbose_name_plural': 'Ausstattungen mitzubringen',
            },
        ),
        migrations.CreateModel(
            name='GeneralWorkAvailability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weekday', models.IntegerField(choices=[(1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday'), (7, 'Sunday')])),
                ('forenoon', models.BooleanField()),
                ('afternoon', models.BooleanField()),
                ('evening', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='HelpOperation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'verbose_name': 'Hilfstätigkeit',
                'verbose_name_plural': 'Hilfstätigkeit',
            },
        ),
        migrations.CreateModel(
            name='OpeningTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weekday', models.IntegerField(choices=[(1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday'), (7, 'Sunday')])),
                ('from_hour', models.TimeField()),
                ('to_hour', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='PublicationCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=30, null=True)),
                ('slug', models.CharField(max_length=30, unique=True)),
            ],
            options={
                'verbose_name': 'Artikelkategorie',
                'verbose_name_plural': 'Artikelkategorien',
            },
        ),
        migrations.CreateModel(
            name='QualificationAdministrative',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'verbose_name': 'Qualifikation Verwaltung',
                'verbose_name_plural': 'Qualifikationen Verwaltung',
            },
        ),
        migrations.CreateModel(
            name='QualificationHealth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'verbose_name': 'Qualifikation Gesundheitswesen',
                'verbose_name_plural': 'Qualifikationen Gesundheitswesen',
            },
        ),
        migrations.CreateModel(
            name='QualificationLanguage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'verbose_name': 'Sprachkenntnis',
                'verbose_name_plural': 'Sprachkenntnisse',
            },
        ),
        migrations.CreateModel(
            name='QualificationLicense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'verbose_name': 'Führerschein',
                'verbose_name_plural': 'Führerscheine',
            },
        ),
        migrations.CreateModel(
            name='QualificationTechnical',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'verbose_name': 'Technische Qualifikation',
                'verbose_name_plural': 'Technische Qualifikationen',
            },
        ),
        migrations.CreateModel(
            name='Restriction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'verbose_name': 'Einschränkung',
                'verbose_name_plural': 'Einschränkungen',
            },
        ),
        migrations.CreateModel(
            name='SinglePersonUptime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weekday', models.IntegerField(choices=[(1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday'), (7, 'Sunday')], unique=True)),
                ('daytime', models.CharField(blank=True, choices=[('vormittags', 'Vormittags'), ('nachmittags', 'Nachmittags'), ('abends', 'Abends')], max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('title', models.CharField(choices=[('herr', 'Herr'), ('frau', 'Frau'), ('divers', 'Divers'), ('none', 'Keine')], default='none', max_length=6)),
                ('qualification_specific', models.CharField(blank=True, max_length=60, null=True, verbose_name='Qualif. Details')),
                ('restriction_specific', models.CharField(blank=True, max_length=60, null=True, verbose_name='Einschränkung Details')),
                ('occupation', models.CharField(blank=True, max_length=50, null=True, verbose_name='Beruf')),
                ('company', models.CharField(blank=True, max_length=50, null=True, verbose_name='Firma')),
                ('position_in_company', models.CharField(blank=True, max_length=50, null=True, verbose_name='Position im Unternehmen')),
                ('company_phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Geschäftsnummer Festnetz')),
                ('company_phone_mobile', models.CharField(blank=True, max_length=20, null=True, verbose_name='Geschäftsnummer Mobil')),
                ('emergency_phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Notfall-Rufnummer')),
                ('help_description', models.TextField(blank=True, max_length=300, null=True)),
                ('street', models.CharField(blank=True, max_length=50, null=True, verbose_name='Straße')),
                ('number', models.CharField(blank=True, max_length=8, null=True, verbose_name='Hausnr.')),
                ('postal_code', models.CharField(blank=True, max_length=5, null=True, verbose_name='PLZ')),
                ('city', models.CharField(blank=True, max_length=50, null=True, verbose_name='Ort')),
                ('private_phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Festnetznummer')),
                ('mobile_phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Mobilnummer')),
                ('expiration_date', models.DateField(blank=True, default=None, null=True, verbose_name='Registriert bleiben bis')),
                ('remark', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Anmerkungen')),
                ('drk_honorary', models.BooleanField(blank=True, null=True, verbose_name='DRK Ehrenamt')),
                ('drk_employee', models.BooleanField(blank=True, null=True, verbose_name='DRK Hauptamt')),
                ('drk_home', models.CharField(blank=True, max_length=50, null=True, verbose_name='DRK-Zugehörigkeit')),
                ('available_for_cleaning', models.CharField(blank=True, choices=[('undefiniert', 'undefiniert'), ('unbedingt', 'unbedingt'), ('eventuell', 'eventuell'), ('nein', 'nein')], max_length=11, null=True, verbose_name='Aufräumarbeiten nach Hochwasser')),
                ('only_job_related_topics', models.CharField(blank=True, choices=[('undefiniert', 'undefiniert'), ('unbedingt', 'unbedingt'), ('nicht nur', 'nicht nur')], max_length=11, null=True, verbose_name='Einsatz nur für eigene Fachtätigkeiten')),
                ('is_active', models.BooleanField(blank=True, null=True)),
                ('password1', models.CharField(blank=True, max_length=40, null=True)),
                ('password2', models.CharField(blank=True, max_length=40, null=True)),
                ('poll_uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('emergency_opening_times', models.ManyToManyField(blank=True, null=True, related_name='emergency_opening_times', to='georga.openingtime', verbose_name='Geschäftliche Notdienstzeiten')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('help_operations', models.ManyToManyField(blank=True, null=True, to='georga.helpoperation')),
                ('opening_times', models.ManyToManyField(blank=True, null=True, related_name='opening_times', to='georga.openingtime', verbose_name='Geschäftszeiten')),
                ('possible_work_times', models.ManyToManyField(blank=True, null=True, related_name='general_work_availability', to='georga.generalworkavailability', verbose_name='Verfügbarkeitszeiten für Hilfe')),
                ('qualifications_administrative', models.ManyToManyField(blank=True, to='georga.qualificationadministrative', verbose_name='Qualifikationen Verwaltung')),
                ('qualifications_health', models.ManyToManyField(blank=True, to='georga.qualificationhealth', verbose_name='Qualifikationen Gesundheitswesen')),
                ('qualifications_language', models.ManyToManyField(blank=True, to='georga.qualificationlanguage', verbose_name='Sprachkenntnisse')),
                ('qualifications_license', models.ManyToManyField(blank=True, to='georga.qualificationlicense', verbose_name='Führerscheine')),
                ('qualifications_technical', models.ManyToManyField(blank=True, to='georga.qualificationtechnical', verbose_name='Qualifikationen Technisch')),
                ('restrictions', models.ManyToManyField(blank=True, to='georga.restriction', verbose_name='Einschränkung')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Registrierter Helfer',
                'verbose_name_plural': 'Registrierte Helfer',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]