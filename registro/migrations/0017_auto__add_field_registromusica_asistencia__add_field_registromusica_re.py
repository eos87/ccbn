# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'RegistroMusica.asistencia'
        db.add_column('registro_registromusica', 'asistencia',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'RegistroMusica.rezon_no_continuar'
        db.add_column('registro_registromusica', 'rezon_no_continuar',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'RegistroMusica.calificacion'
        db.add_column('registro_registromusica', 'calificacion',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'RegistroMusica.valores_ccbn'
        db.add_column('registro_registromusica', 'valores_ccbn',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'RegistroMusica.genero'
        db.add_column('registro_registromusica', 'genero',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'RegistroMusica.mejora_capacidad'
        db.add_column('registro_registromusica', 'mejora_capacidad',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'RegistroMusica.utilidad_para_vida'
        db.add_column('registro_registromusica', 'utilidad_para_vida',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'RegistroMusica.calidad_creativa'
        db.add_column('registro_registromusica', 'calidad_creativa',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'RegistroMusica.metodologia'
        db.add_column('registro_registromusica', 'metodologia',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'RegistroMusica.perspectiva'
        db.add_column('registro_registromusica', 'perspectiva',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'RegistroMusica.grupo'
        db.add_column('registro_registromusica', 'grupo',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['promocion.Musica']),
                      keep_default=False)

        # Adding field 'RegistroTeatro.asistencia'
        db.add_column('registro_registroteatro', 'asistencia',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'RegistroTeatro.rezon_no_continuar'
        db.add_column('registro_registroteatro', 'rezon_no_continuar',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'RegistroTeatro.calificacion'
        db.add_column('registro_registroteatro', 'calificacion',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'RegistroTeatro.valores_ccbn'
        db.add_column('registro_registroteatro', 'valores_ccbn',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'RegistroTeatro.genero'
        db.add_column('registro_registroteatro', 'genero',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'RegistroTeatro.mejora_capacidad'
        db.add_column('registro_registroteatro', 'mejora_capacidad',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'RegistroTeatro.utilidad_para_vida'
        db.add_column('registro_registroteatro', 'utilidad_para_vida',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'RegistroTeatro.calidad_creativa'
        db.add_column('registro_registroteatro', 'calidad_creativa',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'RegistroTeatro.metodologia'
        db.add_column('registro_registroteatro', 'metodologia',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'RegistroTeatro.perspectiva'
        db.add_column('registro_registroteatro', 'perspectiva',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'RegistroTeatro.grupo'
        db.add_column('registro_registroteatro', 'grupo',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['promocion.Teatro']),
                      keep_default=False)

        # Adding field 'RegistroPintura.asistencia'
        db.add_column('registro_registropintura', 'asistencia',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'RegistroPintura.rezon_no_continuar'
        db.add_column('registro_registropintura', 'rezon_no_continuar',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'RegistroPintura.calificacion'
        db.add_column('registro_registropintura', 'calificacion',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'RegistroPintura.valores_ccbn'
        db.add_column('registro_registropintura', 'valores_ccbn',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'RegistroPintura.genero'
        db.add_column('registro_registropintura', 'genero',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'RegistroPintura.mejora_capacidad'
        db.add_column('registro_registropintura', 'mejora_capacidad',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'RegistroPintura.utilidad_para_vida'
        db.add_column('registro_registropintura', 'utilidad_para_vida',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'RegistroPintura.calidad_creativa'
        db.add_column('registro_registropintura', 'calidad_creativa',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'RegistroPintura.metodologia'
        db.add_column('registro_registropintura', 'metodologia',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'RegistroPintura.perspectiva'
        db.add_column('registro_registropintura', 'perspectiva',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'RegistroPintura.grupo'
        db.add_column('registro_registropintura', 'grupo',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['promocion.Pintura']),
                      keep_default=False)

        # Adding field 'RegistroCoro.asistencia'
        db.add_column('registro_registrocoro', 'asistencia',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'RegistroCoro.rezon_no_continuar'
        db.add_column('registro_registrocoro', 'rezon_no_continuar',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'RegistroCoro.calificacion'
        db.add_column('registro_registrocoro', 'calificacion',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'RegistroCoro.valores_ccbn'
        db.add_column('registro_registrocoro', 'valores_ccbn',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'RegistroCoro.genero'
        db.add_column('registro_registrocoro', 'genero',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'RegistroCoro.mejora_capacidad'
        db.add_column('registro_registrocoro', 'mejora_capacidad',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'RegistroCoro.utilidad_para_vida'
        db.add_column('registro_registrocoro', 'utilidad_para_vida',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'RegistroCoro.calidad_creativa'
        db.add_column('registro_registrocoro', 'calidad_creativa',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'RegistroCoro.metodologia'
        db.add_column('registro_registrocoro', 'metodologia',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'RegistroCoro.perspectiva'
        db.add_column('registro_registrocoro', 'perspectiva',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'RegistroCoro.grupo'
        db.add_column('registro_registrocoro', 'grupo',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['promocion.Coro']),
                      keep_default=False)

        # Adding field 'RegistroDanza.asistencia'
        db.add_column('registro_registrodanza', 'asistencia',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'RegistroDanza.rezon_no_continuar'
        db.add_column('registro_registrodanza', 'rezon_no_continuar',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'RegistroDanza.calificacion'
        db.add_column('registro_registrodanza', 'calificacion',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'RegistroDanza.valores_ccbn'
        db.add_column('registro_registrodanza', 'valores_ccbn',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'RegistroDanza.genero'
        db.add_column('registro_registrodanza', 'genero',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'RegistroDanza.mejora_capacidad'
        db.add_column('registro_registrodanza', 'mejora_capacidad',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'RegistroDanza.utilidad_para_vida'
        db.add_column('registro_registrodanza', 'utilidad_para_vida',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'RegistroDanza.calidad_creativa'
        db.add_column('registro_registrodanza', 'calidad_creativa',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'RegistroDanza.metodologia'
        db.add_column('registro_registrodanza', 'metodologia',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'RegistroDanza.perspectiva'
        db.add_column('registro_registrodanza', 'perspectiva',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'RegistroDanza.grupo'
        db.add_column('registro_registrodanza', 'grupo',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['promocion.Danza']),
                      keep_default=False)

    def backwards(self, orm):
        # Deleting field 'RegistroMusica.asistencia'
        db.delete_column('registro_registromusica', 'asistencia')

        # Deleting field 'RegistroMusica.rezon_no_continuar'
        db.delete_column('registro_registromusica', 'rezon_no_continuar')

        # Deleting field 'RegistroMusica.calificacion'
        db.delete_column('registro_registromusica', 'calificacion')

        # Deleting field 'RegistroMusica.valores_ccbn'
        db.delete_column('registro_registromusica', 'valores_ccbn')

        # Deleting field 'RegistroMusica.genero'
        db.delete_column('registro_registromusica', 'genero')

        # Deleting field 'RegistroMusica.mejora_capacidad'
        db.delete_column('registro_registromusica', 'mejora_capacidad')

        # Deleting field 'RegistroMusica.utilidad_para_vida'
        db.delete_column('registro_registromusica', 'utilidad_para_vida')

        # Deleting field 'RegistroMusica.calidad_creativa'
        db.delete_column('registro_registromusica', 'calidad_creativa')

        # Deleting field 'RegistroMusica.metodologia'
        db.delete_column('registro_registromusica', 'metodologia')

        # Deleting field 'RegistroMusica.perspectiva'
        db.delete_column('registro_registromusica', 'perspectiva')

        # Deleting field 'RegistroMusica.grupo'
        db.delete_column('registro_registromusica', 'grupo_id')

        # Deleting field 'RegistroTeatro.asistencia'
        db.delete_column('registro_registroteatro', 'asistencia')

        # Deleting field 'RegistroTeatro.rezon_no_continuar'
        db.delete_column('registro_registroteatro', 'rezon_no_continuar')

        # Deleting field 'RegistroTeatro.calificacion'
        db.delete_column('registro_registroteatro', 'calificacion')

        # Deleting field 'RegistroTeatro.valores_ccbn'
        db.delete_column('registro_registroteatro', 'valores_ccbn')

        # Deleting field 'RegistroTeatro.genero'
        db.delete_column('registro_registroteatro', 'genero')

        # Deleting field 'RegistroTeatro.mejora_capacidad'
        db.delete_column('registro_registroteatro', 'mejora_capacidad')

        # Deleting field 'RegistroTeatro.utilidad_para_vida'
        db.delete_column('registro_registroteatro', 'utilidad_para_vida')

        # Deleting field 'RegistroTeatro.calidad_creativa'
        db.delete_column('registro_registroteatro', 'calidad_creativa')

        # Deleting field 'RegistroTeatro.metodologia'
        db.delete_column('registro_registroteatro', 'metodologia')

        # Deleting field 'RegistroTeatro.perspectiva'
        db.delete_column('registro_registroteatro', 'perspectiva')

        # Deleting field 'RegistroTeatro.grupo'
        db.delete_column('registro_registroteatro', 'grupo_id')

        # Deleting field 'RegistroPintura.asistencia'
        db.delete_column('registro_registropintura', 'asistencia')

        # Deleting field 'RegistroPintura.rezon_no_continuar'
        db.delete_column('registro_registropintura', 'rezon_no_continuar')

        # Deleting field 'RegistroPintura.calificacion'
        db.delete_column('registro_registropintura', 'calificacion')

        # Deleting field 'RegistroPintura.valores_ccbn'
        db.delete_column('registro_registropintura', 'valores_ccbn')

        # Deleting field 'RegistroPintura.genero'
        db.delete_column('registro_registropintura', 'genero')

        # Deleting field 'RegistroPintura.mejora_capacidad'
        db.delete_column('registro_registropintura', 'mejora_capacidad')

        # Deleting field 'RegistroPintura.utilidad_para_vida'
        db.delete_column('registro_registropintura', 'utilidad_para_vida')

        # Deleting field 'RegistroPintura.calidad_creativa'
        db.delete_column('registro_registropintura', 'calidad_creativa')

        # Deleting field 'RegistroPintura.metodologia'
        db.delete_column('registro_registropintura', 'metodologia')

        # Deleting field 'RegistroPintura.perspectiva'
        db.delete_column('registro_registropintura', 'perspectiva')

        # Deleting field 'RegistroPintura.grupo'
        db.delete_column('registro_registropintura', 'grupo_id')

        # Deleting field 'RegistroCoro.asistencia'
        db.delete_column('registro_registrocoro', 'asistencia')

        # Deleting field 'RegistroCoro.rezon_no_continuar'
        db.delete_column('registro_registrocoro', 'rezon_no_continuar')

        # Deleting field 'RegistroCoro.calificacion'
        db.delete_column('registro_registrocoro', 'calificacion')

        # Deleting field 'RegistroCoro.valores_ccbn'
        db.delete_column('registro_registrocoro', 'valores_ccbn')

        # Deleting field 'RegistroCoro.genero'
        db.delete_column('registro_registrocoro', 'genero')

        # Deleting field 'RegistroCoro.mejora_capacidad'
        db.delete_column('registro_registrocoro', 'mejora_capacidad')

        # Deleting field 'RegistroCoro.utilidad_para_vida'
        db.delete_column('registro_registrocoro', 'utilidad_para_vida')

        # Deleting field 'RegistroCoro.calidad_creativa'
        db.delete_column('registro_registrocoro', 'calidad_creativa')

        # Deleting field 'RegistroCoro.metodologia'
        db.delete_column('registro_registrocoro', 'metodologia')

        # Deleting field 'RegistroCoro.perspectiva'
        db.delete_column('registro_registrocoro', 'perspectiva')

        # Deleting field 'RegistroCoro.grupo'
        db.delete_column('registro_registrocoro', 'grupo_id')

        # Deleting field 'RegistroDanza.asistencia'
        db.delete_column('registro_registrodanza', 'asistencia')

        # Deleting field 'RegistroDanza.rezon_no_continuar'
        db.delete_column('registro_registrodanza', 'rezon_no_continuar')

        # Deleting field 'RegistroDanza.calificacion'
        db.delete_column('registro_registrodanza', 'calificacion')

        # Deleting field 'RegistroDanza.valores_ccbn'
        db.delete_column('registro_registrodanza', 'valores_ccbn')

        # Deleting field 'RegistroDanza.genero'
        db.delete_column('registro_registrodanza', 'genero')

        # Deleting field 'RegistroDanza.mejora_capacidad'
        db.delete_column('registro_registrodanza', 'mejora_capacidad')

        # Deleting field 'RegistroDanza.utilidad_para_vida'
        db.delete_column('registro_registrodanza', 'utilidad_para_vida')

        # Deleting field 'RegistroDanza.calidad_creativa'
        db.delete_column('registro_registrodanza', 'calidad_creativa')

        # Deleting field 'RegistroDanza.metodologia'
        db.delete_column('registro_registrodanza', 'metodologia')

        # Deleting field 'RegistroDanza.perspectiva'
        db.delete_column('registro_registrodanza', 'perspectiva')

        # Deleting field 'RegistroDanza.grupo'
        db.delete_column('registro_registrodanza', 'grupo_id')

    models = {
        'atencionintegral.becaprimaria': {
            'Meta': {'object_name': 'BecaPrimaria'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'atencionintegral.becasecundaria': {
            'Meta': {'object_name': 'BecaSecundaria'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'atencionintegral.becauniversitaria': {
            'Meta': {'object_name': 'BecaUniversitaria'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'formacion.curso': {
            'Meta': {'object_name': 'Curso'},
            'fecha_fin': ('django.db.models.fields.DateField', [], {}),
            'fecha_inicio': ('django.db.models.fields.DateField', [], {}),
            'frecuencia': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['formacion.Frecuencia']"}),
            'horario': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'submodulo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sistema.SubModulo']"})
        },
        'formacion.frecuencia': {
            'Meta': {'object_name': 'Frecuencia'},
            'cantidad': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
        'lugar.barrio': {
            'Meta': {'object_name': 'Barrio'},
            'ciudad': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Ciudad']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'tipo': ('django.db.models.fields.IntegerField', [], {})
        },
        'lugar.ciudad': {
            'Meta': {'object_name': 'Ciudad'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'municipio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Municipio']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'tipo': ('django.db.models.fields.IntegerField', [], {})
        },
        'lugar.departamento': {
            'Meta': {'object_name': 'Departamento'},
            'extension': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True', 'null': 'True'})
        },
        'lugar.municipio': {
            'Meta': {'ordering': "['departamento__nombre']", 'object_name': 'Municipio'},
            'departamento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Departamento']"}),
            'extension': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'latitud': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'longitud': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True', 'null': 'True'})
        },
        'promocion.coro': {
            'Meta': {'object_name': 'Coro'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'semestre': ('django.db.models.fields.IntegerField', [], {}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'promocion.danza': {
            'Meta': {'object_name': 'Danza'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'semestre': ('django.db.models.fields.IntegerField', [], {}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'promocion.musica': {
            'Meta': {'object_name': 'Musica'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'semestre': ('django.db.models.fields.IntegerField', [], {}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'promocion.pintura': {
            'Meta': {'object_name': 'Pintura'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'semestre': ('django.db.models.fields.IntegerField', [], {}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'promocion.teatro': {
            'Meta': {'object_name': 'Teatro'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'semestre': ('django.db.models.fields.IntegerField', [], {}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'registro.colegio': {
            'Meta': {'object_name': 'Colegio'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'registro.inscripcioncurso': {
            'Meta': {'object_name': 'InscripcionCurso'},
            'becado': ('django.db.models.fields.IntegerField', [], {}),
            'calidad_contenido': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'calificacion': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'curso': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['formacion.Curso']"}),
            'date_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'estado': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'fecha': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 4, 30, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mejora_autoestima': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'mejora_vida': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'metodologia': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'persona': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['registro.Persona']"}),
            'xq_no_termino': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'registro.modulopersona': {
            'Meta': {'object_name': 'ModuloPersona'},
            'atencion_integral': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'atencion_integral'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['sistema.SubModulo']"}),
            'biblioteca': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'biblioteca'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['sistema.SubModulo']"}),
            'formacion': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'formacion'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['sistema.SubModulo']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'persona': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['registro.Persona']", 'unique': 'True'}),
            'promocion_artistica': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'promocion_artistica'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['sistema.SubModulo']"}),
            'pv_externa': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'pv_externa'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['sistema.SubModulo']"}),
            'pv_interna': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'pv_interna'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['sistema.SubModulo']"})
        },
        'registro.oficio': {
            'Meta': {'object_name': 'Oficio'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'})
        },
        'registro.pariente': {
            'Meta': {'object_name': 'Pariente'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        'registro.persona': {
            'Meta': {'object_name': 'Persona'},
            'barrio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Barrio']"}),
            'cedula': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20', 'blank': 'True'}),
            'celular': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '12', 'blank': 'True'}),
            'centro_actual': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['registro.Colegio']", 'null': 'True', 'blank': 'True'}),
            'ciudad': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Ciudad']"}),
            'codigo': ('django.db.models.fields.IntegerField', [], {}),
            'con_quien_vive': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['registro.Pariente']", 'symmetrical': 'False'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'distrito': ('django.db.models.fields.IntegerField', [], {}),
            'docente_ccbn': ('django.db.models.fields.IntegerField', [], {}),
            'fecha_nacimiento': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'j_oficio': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'oficio_jefe'", 'null': 'True', 'to': "orm['registro.Oficio']"}),
            'j_primer_apellido': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'j_primer_nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'j_segundo_apellido': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'blank': 'True'}),
            'j_segundo_nombre': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'blank': 'True'}),
            'jefe_familia': ('django.db.models.fields.IntegerField', [], {}),
            'municipio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Municipio']"}),
            'nivel_academico': ('django.db.models.fields.IntegerField', [], {}),
            'nivel_estudio': ('django.db.models.fields.IntegerField', [], {}),
            'oficio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['registro.Oficio']", 'null': 'True', 'blank': 'True'}),
            'personal_ccbn': ('django.db.models.fields.IntegerField', [], {}),
            'primer_apellido': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'primer_nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'segundo_apellido': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'blank': 'True'}),
            'segundo_nombre': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'blank': 'True'}),
            'sexo': ('django.db.models.fields.IntegerField', [], {}),
            'telefono': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '12', 'blank': 'True'}),
            'tipo_familia': ('django.db.models.fields.IntegerField', [], {})
        },
        'registro.registrobecaprimaria': {
            'Meta': {'object_name': 'RegistroBecaPrimaria'},
            'beca': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['atencionintegral.BecaPrimaria']"}),
            'fecha': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 4, 30, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mejoro_habilidades': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'perc_derecho': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'persona': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['registro.Persona']"}),
            'recibio_atencion_psicologica': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'recibio_suplemento': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'reconoce_capacidad': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rendimiento_academico': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tutoria': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'registro.registrobecasecundaria': {
            'Meta': {'object_name': 'RegistroBecaSecundaria'},
            'beca': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['atencionintegral.BecaSecundaria']"}),
            'esp_propos': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'fecha': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 4, 30, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'persona': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['registro.Persona']"}),
            'promotor': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'servicio_social': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'solidario_centro': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'solidario_comunidad': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'solidario_famila': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'solidario_sociedad': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'registro.registrobecauniversitaria': {
            'Meta': {'object_name': 'RegistroBecaUniversitaria'},
            'beca': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['atencionintegral.BecaUniversitaria']"}),
            'esp_propos': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'fecha': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 4, 30, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'persona': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['registro.Persona']"}),
            'promotor': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'servicio_social': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'solidario_centro': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'solidario_comunidad': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'solidario_famila': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'solidario_sociedad': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'registro.registrobiblioteca': {
            'Meta': {'object_name': 'RegistroBiblioteca'},
            'fecha': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 4, 30, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'persona': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['registro.Persona']", 'unique': 'True'})
        },
        'registro.registrocoro': {
            'Meta': {'object_name': 'RegistroCoro'},
            'asistencia': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'calidad_creativa': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'calificacion': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'fecha': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 4, 30, 0, 0)'}),
            'genero': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'grupo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['promocion.Coro']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mejora_capacidad': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'metodologia': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'persona': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['registro.Persona']"}),
            'perspectiva': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rezon_no_continuar': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'utilidad_para_vida': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'valores_ccbn': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'registro.registrodanza': {
            'Meta': {'object_name': 'RegistroDanza'},
            'asistencia': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'calidad_creativa': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'calificacion': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'fecha': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 4, 30, 0, 0)'}),
            'genero': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'grupo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['promocion.Danza']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mejora_capacidad': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'metodologia': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'persona': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['registro.Persona']"}),
            'perspectiva': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rezon_no_continuar': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'utilidad_para_vida': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'valores_ccbn': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'registro.registromusica': {
            'Meta': {'object_name': 'RegistroMusica'},
            'asistencia': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'calidad_creativa': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'calificacion': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'fecha': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 4, 30, 0, 0)'}),
            'genero': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'grupo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['promocion.Musica']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mejora_capacidad': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'metodologia': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'persona': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['registro.Persona']"}),
            'perspectiva': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rezon_no_continuar': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'utilidad_para_vida': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'valores_ccbn': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'registro.registropintura': {
            'Meta': {'object_name': 'RegistroPintura'},
            'asistencia': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'calidad_creativa': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'calificacion': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'fecha': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 4, 30, 0, 0)'}),
            'genero': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'grupo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['promocion.Pintura']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mejora_capacidad': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'metodologia': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'persona': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['registro.Persona']"}),
            'perspectiva': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rezon_no_continuar': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'utilidad_para_vida': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'valores_ccbn': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'registro.registroteatro': {
            'Meta': {'object_name': 'RegistroTeatro'},
            'asistencia': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'calidad_creativa': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'calificacion': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'fecha': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 4, 30, 0, 0)'}),
            'genero': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'grupo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['promocion.Teatro']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mejora_capacidad': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'metodologia': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'persona': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['registro.Persona']"}),
            'perspectiva': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rezon_no_continuar': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'utilidad_para_vida': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'valores_ccbn': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'registro.relacion': {
            'Meta': {'object_name': 'Relacion'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'owner'", 'to': "orm['registro.Persona']"}),
            'parentesco': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'persona': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'persona'", 'to': "orm['registro.Persona']"})
        },
        'sistema.modulo': {
            'Meta': {'object_name': 'Modulo'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'sistema.submodulo': {
            'Meta': {'object_name': 'SubModulo'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inline': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'parent_module': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sistema.Modulo']"})
        }
    }

    complete_apps = ['registro']