# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: porerefiner/protocols/porerefiner/rpc/porerefiner.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='porerefiner/protocols/porerefiner/rpc/porerefiner.proto',
  package='porerefiner.rpc',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n7porerefiner/protocols/porerefiner/rpc/porerefiner.proto\x12\x0fporerefiner.rpc\"\xcc\x04\n\x03Run\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x15\n\rmnemonic_name\x18\x03 \x01(\t\x12\x12\n\nlibrary_id\x18\x04 \x01(\t\x12\x0e\n\x06status\x18\x05 \x01(\t\x12\x0c\n\x04path\x18\x06 \x01(\t\x12\x15\n\rflowcell_type\x18\x07 \x01(\t\x12\x13\n\x0b\x66lowcell_id\x18\x08 \x01(\t\x12\x19\n\x11\x62\x61secalling_model\x18\t \x01(\t\x12\x16\n\x0esequencing_kit\x18\n \x01(\t\x12,\n\x07samples\x18\x14 \x03(\x0b\x32\x1b.porerefiner.rpc.Run.Sample\x12\x0c\n\x04tags\x18\x1e \x03(\t\x1a\xc6\x02\n\x06Sample\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x11\n\taccession\x18\x03 \x01(\t\x12\x12\n\nbarcode_id\x18\x04 \x01(\t\x12\x13\n\x0b\x62\x61rcode_seq\x18\x05 \x01(\t\x12\x10\n\x08organism\x18\x06 \x01(\t\x12\x16\n\x0e\x65xtraction_kit\x18\x07 \x01(\t\x12\x0f\n\x07\x63omment\x18\x08 \x01(\t\x12\x0c\n\x04user\x18\t \x01(\t\x12/\n\x05\x66iles\x18\x14 \x03(\x0b\x32 .porerefiner.rpc.Run.Sample.File\x12\x0c\n\x04tags\x18\x1e \x03(\t\x1a^\n\x04\x46ile\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04path\x18\x02 \x01(\t\x12\x0f\n\x07spot_id\x18\x05 \x01(\t\x12\x0c\n\x04size\x18\x08 \x01(\x04\x12\r\n\x05ready\x18\n \x01(\x08\x12\x0c\n\x04tags\x18\x1e \x03(\t\"E\n\x05\x45rror\x12\x0e\n\x04\x63ode\x18\x01 \x01(\x05H\x00\x12\x0e\n\x04type\x18\x02 \x01(\tH\x00\x12\x13\n\x0b\x65rr_message\x18\x03 \x01(\tB\x07\n\x05\x65rror\"d\n\x0bRunResponse\x12#\n\x03run\x18\x01 \x01(\x0b\x32\x14.porerefiner.rpc.RunH\x00\x12\'\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x16.porerefiner.rpc.ErrorH\x00\x42\x07\n\x05reply\"+\n\x0eRunListRequest\x12\x0b\n\x03\x61ll\x18\x01 \x01(\x08\x12\x0c\n\x04tags\x18\x14 \x03(\t\"-\n\x07RunList\x12\"\n\x04runs\x18\x01 \x03(\x0b\x32\x14.porerefiner.rpc.Run\"m\n\x0fRunListResponse\x12(\n\x04runs\x18\x01 \x01(\x0b\x32\x18.porerefiner.rpc.RunListH\x00\x12\'\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x16.porerefiner.rpc.ErrorH\x00\x42\x07\n\x05reply\"2\n\nRunRequest\x12\x0c\n\x02id\x18\x01 \x01(\rH\x00\x12\x0e\n\x04name\x18\x02 \x01(\tH\x00\x42\x06\n\x04term\"E\n\x0fRunRsyncRequest\x12\x0c\n\x02id\x18\x01 \x01(\rH\x00\x12\x0e\n\x04name\x18\x02 \x01(\tH\x00\x12\x0c\n\x04\x64\x65st\x18\x03 \x01(\tB\x06\n\x04term\"9\n\x10RunRsyncResponse\x12%\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x16.porerefiner.rpc.Error\"a\n\x10RunAttachRequest\x12\x0c\n\x02id\x18\x01 \x01(\rH\x00\x12\x0e\n\x04name\x18\x02 \x01(\tH\x00\x12\x0e\n\x04path\x18\x03 \x01(\tH\x01\x12\x0e\n\x04\x66ile\x18\x04 \x01(\x0cH\x01\x42\x06\n\x04termB\x07\n\x05sheet\":\n\x11RunAttachResponse\x12%\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x16.porerefiner.rpc.Error2\xd2\x02\n\x0bPoreRefiner\x12L\n\x07GetRuns\x12\x1f.porerefiner.rpc.RunListRequest\x1a .porerefiner.rpc.RunListResponse\x12G\n\nGetRunInfo\x12\x1b.porerefiner.rpc.RunRequest\x1a\x1c.porerefiner.rpc.RunResponse\x12Y\n\x10\x41ttachSheetToRun\x12!.porerefiner.rpc.RunAttachRequest\x1a\".porerefiner.rpc.RunAttachResponse\x12Q\n\nRsyncRunTo\x12 .porerefiner.rpc.RunRsyncRequest\x1a!.porerefiner.rpc.RunRsyncResponseb\x06proto3')
)




_RUN_SAMPLE_FILE = _descriptor.Descriptor(
  name='File',
  full_name='porerefiner.rpc.Run.Sample.File',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='porerefiner.rpc.Run.Sample.File.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='path', full_name='porerefiner.rpc.Run.Sample.File.path', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='spot_id', full_name='porerefiner.rpc.Run.Sample.File.spot_id', index=2,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='size', full_name='porerefiner.rpc.Run.Sample.File.size', index=3,
      number=8, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ready', full_name='porerefiner.rpc.Run.Sample.File.ready', index=4,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tags', full_name='porerefiner.rpc.Run.Sample.File.tags', index=5,
      number=30, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=571,
  serialized_end=665,
)

_RUN_SAMPLE = _descriptor.Descriptor(
  name='Sample',
  full_name='porerefiner.rpc.Run.Sample',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='porerefiner.rpc.Run.Sample.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='porerefiner.rpc.Run.Sample.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='accession', full_name='porerefiner.rpc.Run.Sample.accession', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='barcode_id', full_name='porerefiner.rpc.Run.Sample.barcode_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='barcode_seq', full_name='porerefiner.rpc.Run.Sample.barcode_seq', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='organism', full_name='porerefiner.rpc.Run.Sample.organism', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='extraction_kit', full_name='porerefiner.rpc.Run.Sample.extraction_kit', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='comment', full_name='porerefiner.rpc.Run.Sample.comment', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user', full_name='porerefiner.rpc.Run.Sample.user', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='files', full_name='porerefiner.rpc.Run.Sample.files', index=9,
      number=20, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tags', full_name='porerefiner.rpc.Run.Sample.tags', index=10,
      number=30, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_RUN_SAMPLE_FILE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=339,
  serialized_end=665,
)

_RUN = _descriptor.Descriptor(
  name='Run',
  full_name='porerefiner.rpc.Run',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='porerefiner.rpc.Run.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='porerefiner.rpc.Run.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mnemonic_name', full_name='porerefiner.rpc.Run.mnemonic_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='library_id', full_name='porerefiner.rpc.Run.library_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='porerefiner.rpc.Run.status', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='path', full_name='porerefiner.rpc.Run.path', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='flowcell_type', full_name='porerefiner.rpc.Run.flowcell_type', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='flowcell_id', full_name='porerefiner.rpc.Run.flowcell_id', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='basecalling_model', full_name='porerefiner.rpc.Run.basecalling_model', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sequencing_kit', full_name='porerefiner.rpc.Run.sequencing_kit', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='samples', full_name='porerefiner.rpc.Run.samples', index=10,
      number=20, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tags', full_name='porerefiner.rpc.Run.tags', index=11,
      number=30, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_RUN_SAMPLE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=77,
  serialized_end=665,
)


_ERROR = _descriptor.Descriptor(
  name='Error',
  full_name='porerefiner.rpc.Error',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='porerefiner.rpc.Error.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='porerefiner.rpc.Error.type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='err_message', full_name='porerefiner.rpc.Error.err_message', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='error', full_name='porerefiner.rpc.Error.error',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=667,
  serialized_end=736,
)


_RUNRESPONSE = _descriptor.Descriptor(
  name='RunResponse',
  full_name='porerefiner.rpc.RunResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='run', full_name='porerefiner.rpc.RunResponse.run', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='porerefiner.rpc.RunResponse.error', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='reply', full_name='porerefiner.rpc.RunResponse.reply',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=738,
  serialized_end=838,
)


_RUNLISTREQUEST = _descriptor.Descriptor(
  name='RunListRequest',
  full_name='porerefiner.rpc.RunListRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='all', full_name='porerefiner.rpc.RunListRequest.all', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tags', full_name='porerefiner.rpc.RunListRequest.tags', index=1,
      number=20, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=840,
  serialized_end=883,
)


_RUNLIST = _descriptor.Descriptor(
  name='RunList',
  full_name='porerefiner.rpc.RunList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='runs', full_name='porerefiner.rpc.RunList.runs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=885,
  serialized_end=930,
)


_RUNLISTRESPONSE = _descriptor.Descriptor(
  name='RunListResponse',
  full_name='porerefiner.rpc.RunListResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='runs', full_name='porerefiner.rpc.RunListResponse.runs', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='porerefiner.rpc.RunListResponse.error', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='reply', full_name='porerefiner.rpc.RunListResponse.reply',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=932,
  serialized_end=1041,
)


_RUNREQUEST = _descriptor.Descriptor(
  name='RunRequest',
  full_name='porerefiner.rpc.RunRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='porerefiner.rpc.RunRequest.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='porerefiner.rpc.RunRequest.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='term', full_name='porerefiner.rpc.RunRequest.term',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=1043,
  serialized_end=1093,
)


_RUNRSYNCREQUEST = _descriptor.Descriptor(
  name='RunRsyncRequest',
  full_name='porerefiner.rpc.RunRsyncRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='porerefiner.rpc.RunRsyncRequest.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='porerefiner.rpc.RunRsyncRequest.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dest', full_name='porerefiner.rpc.RunRsyncRequest.dest', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='term', full_name='porerefiner.rpc.RunRsyncRequest.term',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=1095,
  serialized_end=1164,
)


_RUNRSYNCRESPONSE = _descriptor.Descriptor(
  name='RunRsyncResponse',
  full_name='porerefiner.rpc.RunRsyncResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='error', full_name='porerefiner.rpc.RunRsyncResponse.error', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1166,
  serialized_end=1223,
)


_RUNATTACHREQUEST = _descriptor.Descriptor(
  name='RunAttachRequest',
  full_name='porerefiner.rpc.RunAttachRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='porerefiner.rpc.RunAttachRequest.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='porerefiner.rpc.RunAttachRequest.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='path', full_name='porerefiner.rpc.RunAttachRequest.path', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='file', full_name='porerefiner.rpc.RunAttachRequest.file', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='term', full_name='porerefiner.rpc.RunAttachRequest.term',
      index=0, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='sheet', full_name='porerefiner.rpc.RunAttachRequest.sheet',
      index=1, containing_type=None, fields=[]),
  ],
  serialized_start=1225,
  serialized_end=1322,
)


_RUNATTACHRESPONSE = _descriptor.Descriptor(
  name='RunAttachResponse',
  full_name='porerefiner.rpc.RunAttachResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='error', full_name='porerefiner.rpc.RunAttachResponse.error', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1324,
  serialized_end=1382,
)

_RUN_SAMPLE_FILE.containing_type = _RUN_SAMPLE
_RUN_SAMPLE.fields_by_name['files'].message_type = _RUN_SAMPLE_FILE
_RUN_SAMPLE.containing_type = _RUN
_RUN.fields_by_name['samples'].message_type = _RUN_SAMPLE
_ERROR.oneofs_by_name['error'].fields.append(
  _ERROR.fields_by_name['code'])
_ERROR.fields_by_name['code'].containing_oneof = _ERROR.oneofs_by_name['error']
_ERROR.oneofs_by_name['error'].fields.append(
  _ERROR.fields_by_name['type'])
_ERROR.fields_by_name['type'].containing_oneof = _ERROR.oneofs_by_name['error']
_RUNRESPONSE.fields_by_name['run'].message_type = _RUN
_RUNRESPONSE.fields_by_name['error'].message_type = _ERROR
_RUNRESPONSE.oneofs_by_name['reply'].fields.append(
  _RUNRESPONSE.fields_by_name['run'])
_RUNRESPONSE.fields_by_name['run'].containing_oneof = _RUNRESPONSE.oneofs_by_name['reply']
_RUNRESPONSE.oneofs_by_name['reply'].fields.append(
  _RUNRESPONSE.fields_by_name['error'])
_RUNRESPONSE.fields_by_name['error'].containing_oneof = _RUNRESPONSE.oneofs_by_name['reply']
_RUNLIST.fields_by_name['runs'].message_type = _RUN
_RUNLISTRESPONSE.fields_by_name['runs'].message_type = _RUNLIST
_RUNLISTRESPONSE.fields_by_name['error'].message_type = _ERROR
_RUNLISTRESPONSE.oneofs_by_name['reply'].fields.append(
  _RUNLISTRESPONSE.fields_by_name['runs'])
_RUNLISTRESPONSE.fields_by_name['runs'].containing_oneof = _RUNLISTRESPONSE.oneofs_by_name['reply']
_RUNLISTRESPONSE.oneofs_by_name['reply'].fields.append(
  _RUNLISTRESPONSE.fields_by_name['error'])
_RUNLISTRESPONSE.fields_by_name['error'].containing_oneof = _RUNLISTRESPONSE.oneofs_by_name['reply']
_RUNREQUEST.oneofs_by_name['term'].fields.append(
  _RUNREQUEST.fields_by_name['id'])
_RUNREQUEST.fields_by_name['id'].containing_oneof = _RUNREQUEST.oneofs_by_name['term']
_RUNREQUEST.oneofs_by_name['term'].fields.append(
  _RUNREQUEST.fields_by_name['name'])
_RUNREQUEST.fields_by_name['name'].containing_oneof = _RUNREQUEST.oneofs_by_name['term']
_RUNRSYNCREQUEST.oneofs_by_name['term'].fields.append(
  _RUNRSYNCREQUEST.fields_by_name['id'])
_RUNRSYNCREQUEST.fields_by_name['id'].containing_oneof = _RUNRSYNCREQUEST.oneofs_by_name['term']
_RUNRSYNCREQUEST.oneofs_by_name['term'].fields.append(
  _RUNRSYNCREQUEST.fields_by_name['name'])
_RUNRSYNCREQUEST.fields_by_name['name'].containing_oneof = _RUNRSYNCREQUEST.oneofs_by_name['term']
_RUNRSYNCRESPONSE.fields_by_name['error'].message_type = _ERROR
_RUNATTACHREQUEST.oneofs_by_name['term'].fields.append(
  _RUNATTACHREQUEST.fields_by_name['id'])
_RUNATTACHREQUEST.fields_by_name['id'].containing_oneof = _RUNATTACHREQUEST.oneofs_by_name['term']
_RUNATTACHREQUEST.oneofs_by_name['term'].fields.append(
  _RUNATTACHREQUEST.fields_by_name['name'])
_RUNATTACHREQUEST.fields_by_name['name'].containing_oneof = _RUNATTACHREQUEST.oneofs_by_name['term']
_RUNATTACHREQUEST.oneofs_by_name['sheet'].fields.append(
  _RUNATTACHREQUEST.fields_by_name['path'])
_RUNATTACHREQUEST.fields_by_name['path'].containing_oneof = _RUNATTACHREQUEST.oneofs_by_name['sheet']
_RUNATTACHREQUEST.oneofs_by_name['sheet'].fields.append(
  _RUNATTACHREQUEST.fields_by_name['file'])
_RUNATTACHREQUEST.fields_by_name['file'].containing_oneof = _RUNATTACHREQUEST.oneofs_by_name['sheet']
_RUNATTACHRESPONSE.fields_by_name['error'].message_type = _ERROR
DESCRIPTOR.message_types_by_name['Run'] = _RUN
DESCRIPTOR.message_types_by_name['Error'] = _ERROR
DESCRIPTOR.message_types_by_name['RunResponse'] = _RUNRESPONSE
DESCRIPTOR.message_types_by_name['RunListRequest'] = _RUNLISTREQUEST
DESCRIPTOR.message_types_by_name['RunList'] = _RUNLIST
DESCRIPTOR.message_types_by_name['RunListResponse'] = _RUNLISTRESPONSE
DESCRIPTOR.message_types_by_name['RunRequest'] = _RUNREQUEST
DESCRIPTOR.message_types_by_name['RunRsyncRequest'] = _RUNRSYNCREQUEST
DESCRIPTOR.message_types_by_name['RunRsyncResponse'] = _RUNRSYNCRESPONSE
DESCRIPTOR.message_types_by_name['RunAttachRequest'] = _RUNATTACHREQUEST
DESCRIPTOR.message_types_by_name['RunAttachResponse'] = _RUNATTACHRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Run = _reflection.GeneratedProtocolMessageType('Run', (_message.Message,), {

  'Sample' : _reflection.GeneratedProtocolMessageType('Sample', (_message.Message,), {

    'File' : _reflection.GeneratedProtocolMessageType('File', (_message.Message,), {
      'DESCRIPTOR' : _RUN_SAMPLE_FILE,
      '__module__' : 'porerefiner.protocols.porerefiner.rpc.porerefiner_pb2'
      # @@protoc_insertion_point(class_scope:porerefiner.rpc.Run.Sample.File)
      })
    ,
    'DESCRIPTOR' : _RUN_SAMPLE,
    '__module__' : 'porerefiner.protocols.porerefiner.rpc.porerefiner_pb2'
    # @@protoc_insertion_point(class_scope:porerefiner.rpc.Run.Sample)
    })
  ,
  'DESCRIPTOR' : _RUN,
  '__module__' : 'porerefiner.protocols.porerefiner.rpc.porerefiner_pb2'
  # @@protoc_insertion_point(class_scope:porerefiner.rpc.Run)
  })
_sym_db.RegisterMessage(Run)
_sym_db.RegisterMessage(Run.Sample)
_sym_db.RegisterMessage(Run.Sample.File)

Error = _reflection.GeneratedProtocolMessageType('Error', (_message.Message,), {
  'DESCRIPTOR' : _ERROR,
  '__module__' : 'porerefiner.protocols.porerefiner.rpc.porerefiner_pb2'
  # @@protoc_insertion_point(class_scope:porerefiner.rpc.Error)
  })
_sym_db.RegisterMessage(Error)

RunResponse = _reflection.GeneratedProtocolMessageType('RunResponse', (_message.Message,), {
  'DESCRIPTOR' : _RUNRESPONSE,
  '__module__' : 'porerefiner.protocols.porerefiner.rpc.porerefiner_pb2'
  # @@protoc_insertion_point(class_scope:porerefiner.rpc.RunResponse)
  })
_sym_db.RegisterMessage(RunResponse)

RunListRequest = _reflection.GeneratedProtocolMessageType('RunListRequest', (_message.Message,), {
  'DESCRIPTOR' : _RUNLISTREQUEST,
  '__module__' : 'porerefiner.protocols.porerefiner.rpc.porerefiner_pb2'
  # @@protoc_insertion_point(class_scope:porerefiner.rpc.RunListRequest)
  })
_sym_db.RegisterMessage(RunListRequest)

RunList = _reflection.GeneratedProtocolMessageType('RunList', (_message.Message,), {
  'DESCRIPTOR' : _RUNLIST,
  '__module__' : 'porerefiner.protocols.porerefiner.rpc.porerefiner_pb2'
  # @@protoc_insertion_point(class_scope:porerefiner.rpc.RunList)
  })
_sym_db.RegisterMessage(RunList)

RunListResponse = _reflection.GeneratedProtocolMessageType('RunListResponse', (_message.Message,), {
  'DESCRIPTOR' : _RUNLISTRESPONSE,
  '__module__' : 'porerefiner.protocols.porerefiner.rpc.porerefiner_pb2'
  # @@protoc_insertion_point(class_scope:porerefiner.rpc.RunListResponse)
  })
_sym_db.RegisterMessage(RunListResponse)

RunRequest = _reflection.GeneratedProtocolMessageType('RunRequest', (_message.Message,), {
  'DESCRIPTOR' : _RUNREQUEST,
  '__module__' : 'porerefiner.protocols.porerefiner.rpc.porerefiner_pb2'
  # @@protoc_insertion_point(class_scope:porerefiner.rpc.RunRequest)
  })
_sym_db.RegisterMessage(RunRequest)

RunRsyncRequest = _reflection.GeneratedProtocolMessageType('RunRsyncRequest', (_message.Message,), {
  'DESCRIPTOR' : _RUNRSYNCREQUEST,
  '__module__' : 'porerefiner.protocols.porerefiner.rpc.porerefiner_pb2'
  # @@protoc_insertion_point(class_scope:porerefiner.rpc.RunRsyncRequest)
  })
_sym_db.RegisterMessage(RunRsyncRequest)

RunRsyncResponse = _reflection.GeneratedProtocolMessageType('RunRsyncResponse', (_message.Message,), {
  'DESCRIPTOR' : _RUNRSYNCRESPONSE,
  '__module__' : 'porerefiner.protocols.porerefiner.rpc.porerefiner_pb2'
  # @@protoc_insertion_point(class_scope:porerefiner.rpc.RunRsyncResponse)
  })
_sym_db.RegisterMessage(RunRsyncResponse)

RunAttachRequest = _reflection.GeneratedProtocolMessageType('RunAttachRequest', (_message.Message,), {
  'DESCRIPTOR' : _RUNATTACHREQUEST,
  '__module__' : 'porerefiner.protocols.porerefiner.rpc.porerefiner_pb2'
  # @@protoc_insertion_point(class_scope:porerefiner.rpc.RunAttachRequest)
  })
_sym_db.RegisterMessage(RunAttachRequest)

RunAttachResponse = _reflection.GeneratedProtocolMessageType('RunAttachResponse', (_message.Message,), {
  'DESCRIPTOR' : _RUNATTACHRESPONSE,
  '__module__' : 'porerefiner.protocols.porerefiner.rpc.porerefiner_pb2'
  # @@protoc_insertion_point(class_scope:porerefiner.rpc.RunAttachResponse)
  })
_sym_db.RegisterMessage(RunAttachResponse)



_POREREFINER = _descriptor.ServiceDescriptor(
  name='PoreRefiner',
  full_name='porerefiner.rpc.PoreRefiner',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1385,
  serialized_end=1723,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetRuns',
    full_name='porerefiner.rpc.PoreRefiner.GetRuns',
    index=0,
    containing_service=None,
    input_type=_RUNLISTREQUEST,
    output_type=_RUNLISTRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetRunInfo',
    full_name='porerefiner.rpc.PoreRefiner.GetRunInfo',
    index=1,
    containing_service=None,
    input_type=_RUNREQUEST,
    output_type=_RUNRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='AttachSheetToRun',
    full_name='porerefiner.rpc.PoreRefiner.AttachSheetToRun',
    index=2,
    containing_service=None,
    input_type=_RUNATTACHREQUEST,
    output_type=_RUNATTACHRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='RsyncRunTo',
    full_name='porerefiner.rpc.PoreRefiner.RsyncRunTo',
    index=3,
    containing_service=None,
    input_type=_RUNRSYNCREQUEST,
    output_type=_RUNRSYNCRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_POREREFINER)

DESCRIPTOR.services_by_name['PoreRefiner'] = _POREREFINER

# @@protoc_insertion_point(module_scope)
