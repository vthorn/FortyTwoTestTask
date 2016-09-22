# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PersonalData'
        db.create_table(u'hello_personaldata', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('date_of_birth', self.gf('django.db.models.fields.DateField')()),
            ('bio', self.gf('django.db.models.fields.TextField')(max_length=256, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=30)),
            ('jabber', self.gf('django.db.models.fields.EmailField')(max_length=30)),
            ('other_contacts', self.gf('django.db.models.fields.TextField')(max_length=256, null=True, blank=True)),
        ))
        db.send_create_signal(u'hello', ['PersonalData'])


    def backwards(self, orm):
        # Deleting model 'PersonalData'
        db.delete_table(u'hello_personaldata')


    models = {
        u'hello.personaldata': {
            'Meta': {'object_name': 'PersonalData'},
            'bio': ('django.db.models.fields.TextField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jabber': ('django.db.models.fields.EmailField', [], {'max_length': '30'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'other_contacts': ('django.db.models.fields.TextField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['hello']