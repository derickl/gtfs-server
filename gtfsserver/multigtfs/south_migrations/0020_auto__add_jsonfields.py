# -*- coding: utf-8 -*-
# flake8: noqa
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Trip.extra_data'
        db.add_column(u'trip', 'extra_data',
                      self.gf('jsonfield.fields.JSONField')(default={}),
                      keep_default=False)

        # Adding field 'Zone.extra_data'
        db.add_column(u'zone', 'extra_data',
                      self.gf('jsonfield.fields.JSONField')(default={}),
                      keep_default=False)

        # Adding field 'FeedInfo.extra_data'
        db.add_column(u'feed_info', 'extra_data',
                      self.gf('jsonfield.fields.JSONField')(default={}),
                      keep_default=False)

        # Adding field 'Agency.extra_data'
        db.add_column(u'agency', 'extra_data',
                      self.gf('jsonfield.fields.JSONField')(default={}),
                      keep_default=False)

        # Adding field 'Block.extra_data'
        db.add_column(u'block', 'extra_data',
                      self.gf('jsonfield.fields.JSONField')(default={}),
                      keep_default=False)

        # Adding field 'ShapePoint.extra_data'
        db.add_column(u'shape_point', 'extra_data',
                      self.gf('jsonfield.fields.JSONField')(default={}),
                      keep_default=False)

        # Adding field 'Shape.extra_data'
        db.add_column(u'shape', 'extra_data',
                      self.gf('jsonfield.fields.JSONField')(default={}),
                      keep_default=False)

        # Adding field 'Transfer.extra_data'
        db.add_column(u'transfer', 'extra_data',
                      self.gf('jsonfield.fields.JSONField')(default={}),
                      keep_default=False)

        # Adding field 'Fare.extra_data'
        db.add_column(u'fare', 'extra_data',
                      self.gf('jsonfield.fields.JSONField')(default={}),
                      keep_default=False)

        # Adding field 'ServiceDate.extra_data'
        db.add_column(u'service_date', 'extra_data',
                      self.gf('jsonfield.fields.JSONField')(default={}),
                      keep_default=False)

        # Adding field 'Feed.meta'
        db.add_column(u'feed', 'meta',
                      self.gf('jsonfield.fields.JSONField')(default={}),
                      keep_default=False)

        # Adding field 'Frequency.extra_data'
        db.add_column(u'frequency', 'extra_data',
                      self.gf('jsonfield.fields.JSONField')(default={}),
                      keep_default=False)

        # Adding field 'Stop.extra_data'
        db.add_column(u'stop', 'extra_data',
                      self.gf('jsonfield.fields.JSONField')(default={}),
                      keep_default=False)

        # Adding field 'FareRule.extra_data'
        db.add_column(u'fare_rules', 'extra_data',
                      self.gf('jsonfield.fields.JSONField')(default={}),
                      keep_default=False)

        # Adding field 'Service.extra_data'
        db.add_column(u'service', 'extra_data',
                      self.gf('jsonfield.fields.JSONField')(default={}),
                      keep_default=False)

        # Adding field 'StopTime.extra_data'
        db.add_column(u'stop_time', 'extra_data',
                      self.gf('jsonfield.fields.JSONField')(default={}),
                      keep_default=False)

        # Adding field 'Route.extra_data'
        db.add_column(u'route', 'extra_data',
                      self.gf('jsonfield.fields.JSONField')(default={}),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Trip.extra_data'
        db.delete_column(u'trip', 'extra_data')

        # Deleting field 'Zone.extra_data'
        db.delete_column(u'zone', 'extra_data')

        # Deleting field 'FeedInfo.extra_data'
        db.delete_column(u'feed_info', 'extra_data')

        # Deleting field 'Agency.extra_data'
        db.delete_column(u'agency', 'extra_data')

        # Deleting field 'Block.extra_data'
        db.delete_column(u'block', 'extra_data')

        # Deleting field 'ShapePoint.extra_data'
        db.delete_column(u'shape_point', 'extra_data')

        # Deleting field 'Shape.extra_data'
        db.delete_column(u'shape', 'extra_data')

        # Deleting field 'Transfer.extra_data'
        db.delete_column(u'transfer', 'extra_data')

        # Deleting field 'Fare.extra_data'
        db.delete_column(u'fare', 'extra_data')

        # Deleting field 'ServiceDate.extra_data'
        db.delete_column(u'service_date', 'extra_data')

        # Deleting field 'Feed.meta'
        db.delete_column(u'feed', 'meta')

        # Deleting field 'Frequency.extra_data'
        db.delete_column(u'frequency', 'extra_data')

        # Deleting field 'Stop.extra_data'
        db.delete_column(u'stop', 'extra_data')

        # Deleting field 'FareRule.extra_data'
        db.delete_column(u'fare_rules', 'extra_data')

        # Deleting field 'Service.extra_data'
        db.delete_column(u'service', 'extra_data')

        # Deleting field 'StopTime.extra_data'
        db.delete_column(u'stop_time', 'extra_data')

        # Deleting field 'Route.extra_data'
        db.delete_column(u'route', 'extra_data')


    models = {
        u'multigtfs.agency': {
            'Meta': {'object_name': 'Agency', 'db_table': "u'agency'"},
            'agency_id': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255', 'blank': 'True'}),
            'extra_data': ('jsonfield.fields.JSONField', [], {'default': '{}'}),
            'fare_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'feed': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['multigtfs.Feed']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lang': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'timezone': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'multigtfs.block': {
            'Meta': {'object_name': 'Block', 'db_table': "u'block'"},
            'block_id': ('django.db.models.fields.CharField', [], {'max_length': '10', 'db_index': 'True'}),
            'extra_data': ('jsonfield.fields.JSONField', [], {'default': '{}'}),
            'feed': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['multigtfs.Feed']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'multigtfs.fare': {
            'Meta': {'object_name': 'Fare', 'db_table': "u'fare'"},
            'currency_type': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'extra_data': ('jsonfield.fields.JSONField', [], {'default': '{}'}),
            'fare_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'feed': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['multigtfs.Feed']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'payment_method': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '17', 'decimal_places': '4'}),
            'transfer_duration': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'transfers': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'})
        },
        u'multigtfs.farerule': {
            'Meta': {'object_name': 'FareRule', 'db_table': "u'fare_rules'"},
            'contains': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'fare_contains'", 'null': 'True', 'to': u"orm['multigtfs.Zone']"}),
            'destination': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'fare_destinations'", 'null': 'True', 'to': u"orm['multigtfs.Zone']"}),
            'extra_data': ('jsonfield.fields.JSONField', [], {'default': '{}'}),
            'fare': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['multigtfs.Fare']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'origin': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'fare_origins'", 'null': 'True', 'to': u"orm['multigtfs.Zone']"}),
            'route': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['multigtfs.Route']", 'null': 'True', 'blank': 'True'})
        },
        u'multigtfs.feed': {
            'Meta': {'object_name': 'Feed', 'db_table': "u'feed'"},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meta': ('jsonfield.fields.JSONField', [], {'default': '{}'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'multigtfs.feedinfo': {
            'Meta': {'object_name': 'FeedInfo', 'db_table': "u'feed_info'"},
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'extra_data': ('jsonfield.fields.JSONField', [], {'default': '{}'}),
            'feed': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['multigtfs.Feed']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lang': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'publisher_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'publisher_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'multigtfs.frequency': {
            'Meta': {'object_name': 'Frequency', 'db_table': "u'frequency'"},
            'end_time': ('multigtfs.models.fields.seconds.SecondsField', [], {}),
            'exact_times': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'extra_data': ('jsonfield.fields.JSONField', [], {'default': '{}'}),
            'headway_secs': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_time': ('multigtfs.models.fields.seconds.SecondsField', [], {}),
            'trip': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['multigtfs.Trip']"})
        },
        u'multigtfs.route': {
            'Meta': {'object_name': 'Route', 'db_table': "u'route'"},
            'agency': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['multigtfs.Agency']", 'null': 'True', 'blank': 'True'}),
            'color': ('django.db.models.fields.CharField', [], {'max_length': '6', 'blank': 'True'}),
            'desc': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'extra_data': ('jsonfield.fields.JSONField', [], {'default': '{}'}),
            'feed': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['multigtfs.Feed']"}),
            'geometry': ('django.contrib.gis.db.models.fields.MultiLineStringField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'long_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'route_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'rtype': ('django.db.models.fields.IntegerField', [], {}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '63'}),
            'text_color': ('django.db.models.fields.CharField', [], {'max_length': '6', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'multigtfs.service': {
            'Meta': {'object_name': 'Service', 'db_table': "u'service'"},
            'end_date': ('django.db.models.fields.DateField', [], {}),
            'extra_data': ('jsonfield.fields.JSONField', [], {'default': '{}'}),
            'feed': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['multigtfs.Feed']"}),
            'friday': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monday': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'saturday': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'service_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'sunday': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'thursday': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'tuesday': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'wednesday': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'multigtfs.servicedate': {
            'Meta': {'object_name': 'ServiceDate', 'db_table': "u'service_date'"},
            'date': ('django.db.models.fields.DateField', [], {}),
            'exception_type': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'extra_data': ('jsonfield.fields.JSONField', [], {'default': '{}'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'service': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['multigtfs.Service']"})
        },
        u'multigtfs.shape': {
            'Meta': {'object_name': 'Shape', 'db_table': "u'shape'"},
            'extra_data': ('jsonfield.fields.JSONField', [], {'default': '{}'}),
            'feed': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['multigtfs.Feed']"}),
            'geometry': ('django.contrib.gis.db.models.fields.LineStringField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'shape_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'})
        },
        u'multigtfs.shapepoint': {
            'Meta': {'object_name': 'ShapePoint', 'db_table': "u'shape_point'"},
            'extra_data': ('jsonfield.fields.JSONField', [], {'default': '{}'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'point': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            'sequence': ('django.db.models.fields.IntegerField', [], {}),
            'shape': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'points'", 'to': u"orm['multigtfs.Shape']"}),
            'traveled': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        u'multigtfs.stop': {
            'Meta': {'object_name': 'Stop', 'db_table': "u'stop'"},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'desc': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'extra_data': ('jsonfield.fields.JSONField', [], {'default': '{}'}),
            'feed': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['multigtfs.Feed']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location_type': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'parent_station': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['multigtfs.Stop']", 'null': 'True', 'blank': 'True'}),
            'point': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            'stop_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'timezone': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'wheelchair_boarding': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'zone': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['multigtfs.Zone']", 'null': 'True', 'blank': 'True'})
        },
        u'multigtfs.stoptime': {
            'Meta': {'object_name': 'StopTime', 'db_table': "u'stop_time'"},
            'arrival_time': ('multigtfs.models.fields.seconds.SecondsField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'departure_time': ('multigtfs.models.fields.seconds.SecondsField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'drop_off_type': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'extra_data': ('jsonfield.fields.JSONField', [], {'default': '{}'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pickup_type': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'shape_dist_traveled': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'stop': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['multigtfs.Stop']"}),
            'stop_headsign': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'stop_sequence': ('django.db.models.fields.IntegerField', [], {}),
            'trip': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['multigtfs.Trip']"})
        },
        u'multigtfs.transfer': {
            'Meta': {'object_name': 'Transfer', 'db_table': "u'transfer'"},
            'extra_data': ('jsonfield.fields.JSONField', [], {'default': '{}'}),
            'from_stop': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'transfer_from_stop'", 'to': u"orm['multigtfs.Stop']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'min_transfer_time': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'to_stop': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'transfer_to_stop'", 'to': u"orm['multigtfs.Stop']"}),
            'transfer_type': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'})
        },
        u'multigtfs.trip': {
            'Meta': {'object_name': 'Trip', 'db_table': "u'trip'"},
            'bikes_allowed': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'block': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['multigtfs.Block']", 'null': 'True', 'blank': 'True'}),
            'direction': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'extra_data': ('jsonfield.fields.JSONField', [], {'default': '{}'}),
            'geometry': ('django.contrib.gis.db.models.fields.LineStringField', [], {'null': 'True', 'blank': 'True'}),
            'headsign': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'route': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['multigtfs.Route']"}),
            'service': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['multigtfs.Service']", 'null': 'True', 'blank': 'True'}),
            'shape': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['multigtfs.Shape']", 'null': 'True', 'blank': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'trip_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'wheelchair_accessible': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'})
        },
        u'multigtfs.zone': {
            'Meta': {'object_name': 'Zone', 'db_table': "u'zone'"},
            'extra_data': ('jsonfield.fields.JSONField', [], {'default': '{}'}),
            'feed': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['multigtfs.Feed']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'zone_id': ('django.db.models.fields.CharField', [], {'max_length': '10', 'db_index': 'True'})
        }
    }

    complete_apps = ['multigtfs']
