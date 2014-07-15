# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Post.pub_date'
        db.add_column(u'blog_post', 'pub_date',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 6, 30, 0, 0)),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Post.pub_date'
        db.delete_column(u'blog_post', 'pub_date')


    models = {
        u'blog.author': {
            'Meta': {'object_name': 'Author'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True'})
        },
        u'blog.comment': {
            'Meta': {'object_name': 'Comment'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'comment': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'comments'", 'to': u"orm['blog.Post']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'comment_authors'", 'to': u"orm['blog.User']"})
        },
        u'blog.post': {
            'Meta': {'object_name': 'Post'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'posts'", 'to': u"orm['blog.Author']"}),
            'body': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '120'})
        },
        u'blog.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'posts': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'tags'", 'symmetrical': 'False', 'to': u"orm['blog.Post']"})
        },
        u'blog.user': {
            'Meta': {'object_name': 'User'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'vote': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_votes'", 'symmetrical': 'False', 'to': u"orm['blog.Post']"})
        }
    }

    complete_apps = ['blog']