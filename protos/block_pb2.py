# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: block.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='block.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x0b\x62lock.proto\"X\n\x0b\x42lockHeader\x12\x0f\n\x07\x65ntropy\x18\x01 \x01(\x07\x12\x11\n\ttimestamp\x18\x02 \x01(\x01\x12\x12\n\ndifficulty\x18\x03 \x01(\x07\x12\x11\n\tbody_hash\x18\x04 \x01(\x0c\"\x1a\n\tBlockBody\x12\r\n\x05\x62lobs\x18\x01 \x03(\x0c\"N\n\x05\x42lock\x12\r\n\x05nonce\x18\x01 \x01(\x07\x12\x1c\n\x06header\x18\x02 \x01(\x0b\x32\x0c.BlockHeader\x12\x18\n\x04\x62ody\x18\x03 \x01(\x0b\x32\n.BlockBodyb\x06proto3')
)




_BLOCKHEADER = _descriptor.Descriptor(
  name='BlockHeader',
  full_name='BlockHeader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entropy', full_name='BlockHeader.entropy', index=0,
      number=1, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='BlockHeader.timestamp', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='difficulty', full_name='BlockHeader.difficulty', index=2,
      number=3, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='body_hash', full_name='BlockHeader.body_hash', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=15,
  serialized_end=103,
)


_BLOCKBODY = _descriptor.Descriptor(
  name='BlockBody',
  full_name='BlockBody',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='blobs', full_name='BlockBody.blobs', index=0,
      number=1, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=105,
  serialized_end=131,
)


_BLOCK = _descriptor.Descriptor(
  name='Block',
  full_name='Block',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nonce', full_name='Block.nonce', index=0,
      number=1, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='header', full_name='Block.header', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='body', full_name='Block.body', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=133,
  serialized_end=211,
)

_BLOCK.fields_by_name['header'].message_type = _BLOCKHEADER
_BLOCK.fields_by_name['body'].message_type = _BLOCKBODY
DESCRIPTOR.message_types_by_name['BlockHeader'] = _BLOCKHEADER
DESCRIPTOR.message_types_by_name['BlockBody'] = _BLOCKBODY
DESCRIPTOR.message_types_by_name['Block'] = _BLOCK
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BlockHeader = _reflection.GeneratedProtocolMessageType('BlockHeader', (_message.Message,), dict(
  DESCRIPTOR = _BLOCKHEADER,
  __module__ = 'block_pb2'
  # @@protoc_insertion_point(class_scope:BlockHeader)
  ))
_sym_db.RegisterMessage(BlockHeader)

BlockBody = _reflection.GeneratedProtocolMessageType('BlockBody', (_message.Message,), dict(
  DESCRIPTOR = _BLOCKBODY,
  __module__ = 'block_pb2'
  # @@protoc_insertion_point(class_scope:BlockBody)
  ))
_sym_db.RegisterMessage(BlockBody)

Block = _reflection.GeneratedProtocolMessageType('Block', (_message.Message,), dict(
  DESCRIPTOR = _BLOCK,
  __module__ = 'block_pb2'
  # @@protoc_insertion_point(class_scope:Block)
  ))
_sym_db.RegisterMessage(Block)


# @@protoc_insertion_point(module_scope)