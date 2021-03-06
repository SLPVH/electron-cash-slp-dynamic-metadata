# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: addressmetadata.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='addressmetadata.proto',
  package='models',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x15\x61\x64\x64ressmetadata.proto\x12\x06models\"%\n\x06Header\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"J\n\x05\x45ntry\x12\x0c\n\x04kind\x18\x01 \x01(\t\x12\x1f\n\x07headers\x18\x02 \x03(\x0b\x32\x0e.models.Header\x12\x12\n\nentry_data\x18\x03 \x01(\x0c\"I\n\x07Payload\x12\x11\n\ttimestamp\x18\x01 \x01(\x03\x12\x0b\n\x03ttl\x18\x02 \x01(\x03\x12\x1e\n\x07\x65ntries\x18\x03 \x03(\x0b\x32\r.models.Entry\"\xbb\x01\n\x0f\x41\x64\x64ressMetadata\x12\x0f\n\x07pub_key\x18\x01 \x01(\x0c\x12\x11\n\tsignature\x18\x02 \x01(\x0c\x12\x37\n\x06scheme\x18\x03 \x01(\x0e\x32\'.models.AddressMetadata.SignatureScheme\x12 \n\x07payload\x18\x04 \x01(\x0b\x32\x0f.models.Payload\")\n\x0fSignatureScheme\x12\x0b\n\x07SCHNORR\x10\x00\x12\t\n\x05\x45\x43\x44SA\x10\x01\x62\x06proto3')
)



_ADDRESSMETADATA_SIGNATURESCHEME = _descriptor.EnumDescriptor(
  name='SignatureScheme',
  full_name='models.AddressMetadata.SignatureScheme',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SCHNORR', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ECDSA', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=370,
  serialized_end=411,
)
_sym_db.RegisterEnumDescriptor(_ADDRESSMETADATA_SIGNATURESCHEME)


_HEADER = _descriptor.Descriptor(
  name='Header',
  full_name='models.Header',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='models.Header.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='models.Header.value', index=1,
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
  ],
  serialized_start=33,
  serialized_end=70,
)


_ENTRY = _descriptor.Descriptor(
  name='Entry',
  full_name='models.Entry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='kind', full_name='models.Entry.kind', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='headers', full_name='models.Entry.headers', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='entry_data', full_name='models.Entry.entry_data', index=2,
      number=3, type=12, cpp_type=9, label=1,
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
  ],
  serialized_start=72,
  serialized_end=146,
)


_PAYLOAD = _descriptor.Descriptor(
  name='Payload',
  full_name='models.Payload',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='models.Payload.timestamp', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ttl', full_name='models.Payload.ttl', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='entries', full_name='models.Payload.entries', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=148,
  serialized_end=221,
)


_ADDRESSMETADATA = _descriptor.Descriptor(
  name='AddressMetadata',
  full_name='models.AddressMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pub_key', full_name='models.AddressMetadata.pub_key', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='signature', full_name='models.AddressMetadata.signature', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scheme', full_name='models.AddressMetadata.scheme', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payload', full_name='models.AddressMetadata.payload', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ADDRESSMETADATA_SIGNATURESCHEME,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=224,
  serialized_end=411,
)

_ENTRY.fields_by_name['headers'].message_type = _HEADER
_PAYLOAD.fields_by_name['entries'].message_type = _ENTRY
_ADDRESSMETADATA.fields_by_name['scheme'].enum_type = _ADDRESSMETADATA_SIGNATURESCHEME
_ADDRESSMETADATA.fields_by_name['payload'].message_type = _PAYLOAD
_ADDRESSMETADATA_SIGNATURESCHEME.containing_type = _ADDRESSMETADATA
DESCRIPTOR.message_types_by_name['Header'] = _HEADER
DESCRIPTOR.message_types_by_name['Entry'] = _ENTRY
DESCRIPTOR.message_types_by_name['Payload'] = _PAYLOAD
DESCRIPTOR.message_types_by_name['AddressMetadata'] = _ADDRESSMETADATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Header = _reflection.GeneratedProtocolMessageType('Header', (_message.Message,), dict(
  DESCRIPTOR = _HEADER,
  __module__ = 'addressmetadata_pb2'
  # @@protoc_insertion_point(class_scope:models.Header)
  ))
_sym_db.RegisterMessage(Header)

Entry = _reflection.GeneratedProtocolMessageType('Entry', (_message.Message,), dict(
  DESCRIPTOR = _ENTRY,
  __module__ = 'addressmetadata_pb2'
  # @@protoc_insertion_point(class_scope:models.Entry)
  ))
_sym_db.RegisterMessage(Entry)

Payload = _reflection.GeneratedProtocolMessageType('Payload', (_message.Message,), dict(
  DESCRIPTOR = _PAYLOAD,
  __module__ = 'addressmetadata_pb2'
  # @@protoc_insertion_point(class_scope:models.Payload)
  ))
_sym_db.RegisterMessage(Payload)

AddressMetadata = _reflection.GeneratedProtocolMessageType('AddressMetadata', (_message.Message,), dict(
  DESCRIPTOR = _ADDRESSMETADATA,
  __module__ = 'addressmetadata_pb2'
  # @@protoc_insertion_point(class_scope:models.AddressMetadata)
  ))
_sym_db.RegisterMessage(AddressMetadata)


# @@protoc_insertion_point(module_scope)
