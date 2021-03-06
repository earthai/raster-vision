# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rv2/protos/project.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from rv2.protos import raster_source_pb2 as rv2_dot_protos_dot_raster__source__pb2
from rv2.protos import annotation_source_pb2 as rv2_dot_protos_dot_annotation__source__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='rv2/protos/project.proto',
  package='rv.protos',
  syntax='proto2',
  serialized_pb=_b('\n\x18rv2/protos/project.proto\x12\trv.protos\x1a\x1erv2/protos/raster_source.proto\x1a\"rv2/protos/annotation_source.proto\"\xc1\x01\n\x07Project\x12.\n\rraster_source\x18\x01 \x01(\x0b\x32\x17.rv.protos.RasterSource\x12\x43\n\x1eground_truth_annotation_source\x18\x02 \x01(\x0b\x32\x1b.rv.protos.AnnotationSource\x12\x41\n\x1cprediction_annotation_source\x18\x03 \x01(\x0b\x32\x1b.rv.protos.AnnotationSource')
  ,
  dependencies=[rv2_dot_protos_dot_raster__source__pb2.DESCRIPTOR,rv2_dot_protos_dot_annotation__source__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PROJECT = _descriptor.Descriptor(
  name='Project',
  full_name='rv.protos.Project',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='raster_source', full_name='rv.protos.Project.raster_source', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ground_truth_annotation_source', full_name='rv.protos.Project.ground_truth_annotation_source', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='prediction_annotation_source', full_name='rv.protos.Project.prediction_annotation_source', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=108,
  serialized_end=301,
)

_PROJECT.fields_by_name['raster_source'].message_type = rv2_dot_protos_dot_raster__source__pb2._RASTERSOURCE
_PROJECT.fields_by_name['ground_truth_annotation_source'].message_type = rv2_dot_protos_dot_annotation__source__pb2._ANNOTATIONSOURCE
_PROJECT.fields_by_name['prediction_annotation_source'].message_type = rv2_dot_protos_dot_annotation__source__pb2._ANNOTATIONSOURCE
DESCRIPTOR.message_types_by_name['Project'] = _PROJECT

Project = _reflection.GeneratedProtocolMessageType('Project', (_message.Message,), dict(
  DESCRIPTOR = _PROJECT,
  __module__ = 'rv2.protos.project_pb2'
  # @@protoc_insertion_point(class_scope:rv.protos.Project)
  ))
_sym_db.RegisterMessage(Project)


# @@protoc_insertion_point(module_scope)
