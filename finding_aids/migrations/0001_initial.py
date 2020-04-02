# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-26 12:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_date_extensions.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('controlled_list', '0001_initial'),
        ('archival_unit', '0001_initial'),
        ('container', '0001_initial'),
        ('authority', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FindingAidsEntity',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('uuid', models.UUIDField(default=uuid.uuid4)),
                ('legacy_id', models.CharField(blank=True, max_length=200, null=True)),
                ('archival_reference_code', models.CharField(blank=True, max_length=50, null=True)),
                ('old_id', models.CharField(blank=True, max_length=12, null=True)),
                ('catalog_id', models.CharField(blank=True, max_length=12, null=True)),
                ('description_level', models.CharField(choices=[('L1', 'Level 1'), ('L2', 'Level 2')], default='L1', max_length=2)),
                ('level', models.CharField(choices=[('F', 'Folder'), ('I', 'Item')], default='F', max_length=1)),
                ('is_template', models.BooleanField(default=False)),
                ('template_name', models.CharField(blank=True, max_length=100, null=True)),
                ('folder_no', models.IntegerField(default=0)),
                ('sequence_no', models.IntegerField(blank=True, default=0, null=True)),
                ('title', models.CharField(blank=True, max_length=300, null=True)),
                ('title_given', models.BooleanField(default=False)),
                ('title_original', models.CharField(blank=True, max_length=300, null=True)),
                ('date_from', django_date_extensions.fields.ApproximateDateField(blank=True)),
                ('date_to', django_date_extensions.fields.ApproximateDateField(blank=True)),
                ('date_ca_span', models.IntegerField(blank=True, default=0)),
                ('contents_summary', models.TextField(blank=True, null=True)),
                ('contents_summary_original', models.TextField(blank=True, null=True)),
                ('administrative_history', models.TextField(blank=True, null=True)),
                ('administrative_history_original', models.TextField(blank=True, null=True)),
                ('language_statement', models.CharField(blank=True, max_length=300, null=True)),
                ('language_statement_original', models.CharField(blank=True, max_length=300, null=True)),
                ('physical_description', models.CharField(blank=True, max_length=300, null=True)),
                ('physical_description_original', models.CharField(blank=True, max_length=300, null=True)),
                ('physical_condition', models.CharField(blank=True, max_length=200, null=True)),
                ('time_start', models.DurationField(blank=True, null=True)),
                ('time_end', models.DurationField(blank=True, null=True)),
                ('duration', models.DurationField(blank=True, null=True)),
                ('dimensions', models.TextField(blank=True, max_length=200, null=True)),
                ('note', models.CharField(blank=True, max_length=500, null=True)),
                ('note_original', models.CharField(blank=True, max_length=500, null=True)),
                ('internal_note', models.CharField(blank=True, max_length=500, null=True)),
                ('published', models.BooleanField(default=False)),
                ('confidential_display_text', models.CharField(blank=True, max_length=300, null=True)),
                ('confidential', models.BooleanField(default=False)),
                ('user_published', models.CharField(blank=True, max_length=100)),
                ('date_published', models.DateTimeField(blank=True, null=True)),
                ('user_created', models.CharField(blank=True, max_length=100)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('user_updated', models.CharField(blank=True, max_length=100)),
                ('date_updated', models.DateTimeField(blank=True, null=True)),
                ('archival_unit', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='archival_unit.ArchivalUnit')),
                ('container', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='container.Container')),
                ('genre', models.ManyToManyField(blank=True, to='authority.Genre')),
                ('original_locale', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='controlled_list.Locale')),
                ('primary_type', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='controlled_list.PrimaryType')),
                ('spatial_coverage_country', models.ManyToManyField(blank=True, related_name='spatial_coverage_countries', to='authority.Country')),
                ('spatial_coverage_place', models.ManyToManyField(blank=True, related_name='spatial_coverage_places', to='authority.Place')),
                ('subject_corporation', models.ManyToManyField(blank=True, related_name='subject_corporations', to='authority.Corporation')),
                ('subject_heading', models.ManyToManyField(blank=True, to='authority.Subject')),
                ('subject_keyword', models.ManyToManyField(blank=True, to='controlled_list.Keyword')),
                ('subject_person', models.ManyToManyField(blank=True, related_name='subject_poeple', to='authority.Person')),
            ],
            options={
                'db_table': 'finding_aids_entities',
            },
        ),
        migrations.CreateModel(
            name='FindingAidsEntityAlternativeTitle',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('alternative_title', models.CharField(max_length=300)),
                ('title_given', models.BooleanField(default=False)),
                ('fa_entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finding_aids.FindingAidsEntity')),
            ],
            options={
                'db_table': 'finding_aids_alternative_titles',
            },
        ),
        migrations.CreateModel(
            name='FindingAidsEntityAssociatedCorporation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('associated_corporation', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='authority.Corporation')),
                ('fa_entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finding_aids.FindingAidsEntity')),
                ('role', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='controlled_list.CorporationRole')),
            ],
            options={
                'db_table': 'finding_aids_associated_corporations',
            },
        ),
        migrations.CreateModel(
            name='FindingAidsEntityAssociatedCountry',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('associated_country', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='authority.Country')),
                ('fa_entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finding_aids.FindingAidsEntity')),
                ('role', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='controlled_list.GeoRole')),
            ],
            options={
                'db_table': 'finding_aids_associated_countries',
            },
        ),
        migrations.CreateModel(
            name='FindingAidsEntityAssociatedPerson',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('associated_person', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='authority.Person')),
                ('fa_entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finding_aids.FindingAidsEntity')),
                ('role', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='controlled_list.PersonRole')),
            ],
            options={
                'db_table': 'finding_aids_associated_people',
            },
        ),
        migrations.CreateModel(
            name='FindingAidsEntityAssociatedPlace',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('associated_place', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='authority.Place')),
                ('fa_entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finding_aids.FindingAidsEntity')),
                ('role', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='controlled_list.GeoRole')),
            ],
            options={
                'db_table': 'finding_aids_associated_places',
            },
        ),
        migrations.CreateModel(
            name='FindingAidsEntityCreator',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('creator', models.CharField(max_length=300)),
                ('role', models.CharField(choices=[('COL', 'Collector'), ('CRE', 'Creator')], default='CRE', max_length=3)),
                ('fa_entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finding_aids.FindingAidsEntity')),
            ],
            options={
                'db_table': 'finding_aids_creators',
            },
        ),
        migrations.CreateModel(
            name='FindingAidsEntityDate',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date_from', django_date_extensions.fields.ApproximateDateField()),
                ('date_to', django_date_extensions.fields.ApproximateDateField(blank=True)),
                ('date_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='controlled_list.DateType')),
                ('fa_entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finding_aids.FindingAidsEntity')),
            ],
        ),
        migrations.CreateModel(
            name='FindingAidsEntityExtent',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('extent_number', models.IntegerField(blank=True, null=True)),
                ('extent_unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='controlled_list.ExtentUnit')),
                ('fa_entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finding_aids.FindingAidsEntity')),
            ],
            options={
                'db_table': 'finding_aids_extents',
            },
        ),
        migrations.CreateModel(
            name='FindingAidsEntityLanguage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fa_entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finding_aids.FindingAidsEntity')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='authority.Language')),
                ('language_usage', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='controlled_list.LanguageUsage')),
            ],
            options={
                'db_table': 'finding_aids_languages',
            },
        ),
        migrations.CreateModel(
            name='FindingAidsEntityPlaceOfCreation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('place', models.CharField(max_length=200)),
                ('fa_entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finding_aids.FindingAidsEntity')),
            ],
            options={
                'db_table': 'finding_aids_places_of_creation',
            },
        ),
        migrations.CreateModel(
            name='FindingAidsEntitySubject',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('subject', models.CharField(max_length=200)),
                ('fa_entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finding_aids.FindingAidsEntity')),
            ],
            options={
                'db_table': 'finding_aids_subjects',
            },
        ),
    ]
