# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: minknow/rpc/manager.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import instance_pb2 as minknow_dot_rpc_dot_instance__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='minknow/rpc/manager.proto',
  package='ont.rpc.manager',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x19minknow/rpc/manager.proto\x12\x0font.rpc.manager\x1a\x1aminknow/rpc/instance.proto\"\x14\n\x12ListDevicesRequest\"\xb3\x03\n\x13ListDevicesResponse\x12\x10\n\x08inactive\x18\x01 \x03(\t\x12\x0f\n\x07pending\x18\x02 \x03(\t\x12\x41\n\x06\x61\x63tive\x18\x03 \x03(\x0b\x32\x31.ont.rpc.manager.ListDevicesResponse.ActiveDevice\x1ap\n\x08RpcPorts\x12\x0f\n\x07jsonrpc\x18\x01 \x01(\r\x12\x16\n\x0ejson_websocket\x18\x02 \x01(\r\x12\x0e\n\x06secure\x18\x03 \x01(\r\x12\x15\n\rinsecure_grpc\x18\x04 \x01(\r\x12\x14\n\x0cinsecure_web\x18\x05 \x01(\r\x1a$\n\x0c\x44\x65viceLayout\x12\t\n\x01x\x18\x01 \x01(\x05\x12\t\n\x01y\x18\x02 \x01(\x05\x1a\x9d\x01\n\x0c\x41\x63tiveDevice\x12\x0c\n\x04name\x18\x01 \x01(\t\x12<\n\x05ports\x18\x02 \x01(\x0b\x32-.ont.rpc.manager.ListDevicesResponse.RpcPorts\x12\x41\n\x06layout\x18\x03 \x01(\x0b\x32\x31.ont.rpc.manager.ListDevicesResponse.DeviceLayout\"\x17\n\x15GetVersionInfoRequest\"\xab\x02\n\x16GetVersionInfoResponse\x12H\n\x07minknow\x18\x01 \x01(\x0b\x32\x37.ont.rpc.instance.GetVersionInfoResponse.MinknowVersion\x12\x11\n\tprotocols\x18\x02 \x01(\t\x12\x1c\n\x14\x64istribution_version\x18\x03 \x01(\t\x12X\n\x13\x64istribution_status\x18\x04 \x01(\x0e\x32;.ont.rpc.instance.GetVersionInfoResponse.DistributionStatus\x12\x1b\n\x13guppy_build_version\x18\x05 \x01(\t\x12\x1f\n\x17guppy_connected_version\x18\x06 \x01(\t2\xd4\x01\n\x0eManagerService\x12[\n\x0clist_devices\x12#.ont.rpc.manager.ListDevicesRequest\x1a$.ont.rpc.manager.ListDevicesResponse\"\x00\x12\x65\n\x10get_version_info\x12&.ont.rpc.manager.GetVersionInfoRequest\x1a\'.ont.rpc.manager.GetVersionInfoResponse\"\x00\x62\x06proto3')
  ,
  dependencies=[minknow_dot_rpc_dot_instance__pb2.DESCRIPTOR,])




_LISTDEVICESREQUEST = _descriptor.Descriptor(
  name='ListDevicesRequest',
  full_name='ont.rpc.manager.ListDevicesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=74,
  serialized_end=94,
)


_LISTDEVICESRESPONSE_RPCPORTS = _descriptor.Descriptor(
  name='RpcPorts',
  full_name='ont.rpc.manager.ListDevicesResponse.RpcPorts',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='jsonrpc', full_name='ont.rpc.manager.ListDevicesResponse.RpcPorts.jsonrpc', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='json_websocket', full_name='ont.rpc.manager.ListDevicesResponse.RpcPorts.json_websocket', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='secure', full_name='ont.rpc.manager.ListDevicesResponse.RpcPorts.secure', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='insecure_grpc', full_name='ont.rpc.manager.ListDevicesResponse.RpcPorts.insecure_grpc', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='insecure_web', full_name='ont.rpc.manager.ListDevicesResponse.RpcPorts.insecure_web', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=222,
  serialized_end=334,
)

_LISTDEVICESRESPONSE_DEVICELAYOUT = _descriptor.Descriptor(
  name='DeviceLayout',
  full_name='ont.rpc.manager.ListDevicesResponse.DeviceLayout',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='ont.rpc.manager.ListDevicesResponse.DeviceLayout.x', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='ont.rpc.manager.ListDevicesResponse.DeviceLayout.y', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=336,
  serialized_end=372,
)

_LISTDEVICESRESPONSE_ACTIVEDEVICE = _descriptor.Descriptor(
  name='ActiveDevice',
  full_name='ont.rpc.manager.ListDevicesResponse.ActiveDevice',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='ont.rpc.manager.ListDevicesResponse.ActiveDevice.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ports', full_name='ont.rpc.manager.ListDevicesResponse.ActiveDevice.ports', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='layout', full_name='ont.rpc.manager.ListDevicesResponse.ActiveDevice.layout', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=375,
  serialized_end=532,
)

_LISTDEVICESRESPONSE = _descriptor.Descriptor(
  name='ListDevicesResponse',
  full_name='ont.rpc.manager.ListDevicesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='inactive', full_name='ont.rpc.manager.ListDevicesResponse.inactive', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pending', full_name='ont.rpc.manager.ListDevicesResponse.pending', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='active', full_name='ont.rpc.manager.ListDevicesResponse.active', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_LISTDEVICESRESPONSE_RPCPORTS, _LISTDEVICESRESPONSE_DEVICELAYOUT, _LISTDEVICESRESPONSE_ACTIVEDEVICE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=97,
  serialized_end=532,
)


_GETVERSIONINFOREQUEST = _descriptor.Descriptor(
  name='GetVersionInfoRequest',
  full_name='ont.rpc.manager.GetVersionInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=534,
  serialized_end=557,
)


_GETVERSIONINFORESPONSE = _descriptor.Descriptor(
  name='GetVersionInfoResponse',
  full_name='ont.rpc.manager.GetVersionInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='minknow', full_name='ont.rpc.manager.GetVersionInfoResponse.minknow', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='protocols', full_name='ont.rpc.manager.GetVersionInfoResponse.protocols', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='distribution_version', full_name='ont.rpc.manager.GetVersionInfoResponse.distribution_version', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='distribution_status', full_name='ont.rpc.manager.GetVersionInfoResponse.distribution_status', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='guppy_build_version', full_name='ont.rpc.manager.GetVersionInfoResponse.guppy_build_version', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='guppy_connected_version', full_name='ont.rpc.manager.GetVersionInfoResponse.guppy_connected_version', index=5,
      number=6, type=9, cpp_type=9, label=1,
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
  ],
  serialized_start=560,
  serialized_end=859,
)

_LISTDEVICESRESPONSE_RPCPORTS.containing_type = _LISTDEVICESRESPONSE
_LISTDEVICESRESPONSE_DEVICELAYOUT.containing_type = _LISTDEVICESRESPONSE
_LISTDEVICESRESPONSE_ACTIVEDEVICE.fields_by_name['ports'].message_type = _LISTDEVICESRESPONSE_RPCPORTS
_LISTDEVICESRESPONSE_ACTIVEDEVICE.fields_by_name['layout'].message_type = _LISTDEVICESRESPONSE_DEVICELAYOUT
_LISTDEVICESRESPONSE_ACTIVEDEVICE.containing_type = _LISTDEVICESRESPONSE
_LISTDEVICESRESPONSE.fields_by_name['active'].message_type = _LISTDEVICESRESPONSE_ACTIVEDEVICE
_GETVERSIONINFORESPONSE.fields_by_name['minknow'].message_type = minknow_dot_rpc_dot_instance__pb2._GETVERSIONINFORESPONSE_MINKNOWVERSION
_GETVERSIONINFORESPONSE.fields_by_name['distribution_status'].enum_type = minknow_dot_rpc_dot_instance__pb2._GETVERSIONINFORESPONSE_DISTRIBUTIONSTATUS
DESCRIPTOR.message_types_by_name['ListDevicesRequest'] = _LISTDEVICESREQUEST
DESCRIPTOR.message_types_by_name['ListDevicesResponse'] = _LISTDEVICESRESPONSE
DESCRIPTOR.message_types_by_name['GetVersionInfoRequest'] = _GETVERSIONINFOREQUEST
DESCRIPTOR.message_types_by_name['GetVersionInfoResponse'] = _GETVERSIONINFORESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListDevicesRequest = _reflection.GeneratedProtocolMessageType('ListDevicesRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTDEVICESREQUEST,
  '__module__' : 'minknow.rpc.manager_pb2'
  # @@protoc_insertion_point(class_scope:ont.rpc.manager.ListDevicesRequest)
  })
_sym_db.RegisterMessage(ListDevicesRequest)

ListDevicesResponse = _reflection.GeneratedProtocolMessageType('ListDevicesResponse', (_message.Message,), {

  'RpcPorts' : _reflection.GeneratedProtocolMessageType('RpcPorts', (_message.Message,), {
    'DESCRIPTOR' : _LISTDEVICESRESPONSE_RPCPORTS,
    '__module__' : 'minknow.rpc.manager_pb2'
    # @@protoc_insertion_point(class_scope:ont.rpc.manager.ListDevicesResponse.RpcPorts)
    })
  ,

  'DeviceLayout' : _reflection.GeneratedProtocolMessageType('DeviceLayout', (_message.Message,), {
    'DESCRIPTOR' : _LISTDEVICESRESPONSE_DEVICELAYOUT,
    '__module__' : 'minknow.rpc.manager_pb2'
    # @@protoc_insertion_point(class_scope:ont.rpc.manager.ListDevicesResponse.DeviceLayout)
    })
  ,

  'ActiveDevice' : _reflection.GeneratedProtocolMessageType('ActiveDevice', (_message.Message,), {
    'DESCRIPTOR' : _LISTDEVICESRESPONSE_ACTIVEDEVICE,
    '__module__' : 'minknow.rpc.manager_pb2'
    # @@protoc_insertion_point(class_scope:ont.rpc.manager.ListDevicesResponse.ActiveDevice)
    })
  ,
  'DESCRIPTOR' : _LISTDEVICESRESPONSE,
  '__module__' : 'minknow.rpc.manager_pb2'
  # @@protoc_insertion_point(class_scope:ont.rpc.manager.ListDevicesResponse)
  })
_sym_db.RegisterMessage(ListDevicesResponse)
_sym_db.RegisterMessage(ListDevicesResponse.RpcPorts)
_sym_db.RegisterMessage(ListDevicesResponse.DeviceLayout)
_sym_db.RegisterMessage(ListDevicesResponse.ActiveDevice)

GetVersionInfoRequest = _reflection.GeneratedProtocolMessageType('GetVersionInfoRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETVERSIONINFOREQUEST,
  '__module__' : 'minknow.rpc.manager_pb2'
  # @@protoc_insertion_point(class_scope:ont.rpc.manager.GetVersionInfoRequest)
  })
_sym_db.RegisterMessage(GetVersionInfoRequest)

GetVersionInfoResponse = _reflection.GeneratedProtocolMessageType('GetVersionInfoResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETVERSIONINFORESPONSE,
  '__module__' : 'minknow.rpc.manager_pb2'
  # @@protoc_insertion_point(class_scope:ont.rpc.manager.GetVersionInfoResponse)
  })
_sym_db.RegisterMessage(GetVersionInfoResponse)



_MANAGERSERVICE = _descriptor.ServiceDescriptor(
  name='ManagerService',
  full_name='ont.rpc.manager.ManagerService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=862,
  serialized_end=1074,
  methods=[
  _descriptor.MethodDescriptor(
    name='list_devices',
    full_name='ont.rpc.manager.ManagerService.list_devices',
    index=0,
    containing_service=None,
    input_type=_LISTDEVICESREQUEST,
    output_type=_LISTDEVICESRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='get_version_info',
    full_name='ont.rpc.manager.ManagerService.get_version_info',
    index=1,
    containing_service=None,
    input_type=_GETVERSIONINFOREQUEST,
    output_type=_GETVERSIONINFORESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_MANAGERSERVICE)

DESCRIPTOR.services_by_name['ManagerService'] = _MANAGERSERVICE

# @@protoc_insertion_point(module_scope)
