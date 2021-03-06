# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rikka.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='rikka.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0brikka.proto\"1\n\x0cQueryRequest\x12\x0f\n\x07passage\x18\x01 \x01(\t\x12\x10\n\x08question\x18\x02 \x01(\t\",\n\x0b\x41nswerReply\x12\x0e\n\x06\x61nswer\x18\x01 \x01(\t\x12\r\n\x05score\x18\x02 \x01(\x02\"!\n\x0eSummaryRequest\x12\x0f\n\x07passage\x18\x01 \x01(\t\"\x1f\n\x0cSummaryReply\x12\x0f\n\x07summary\x18\x01 \x01(\t\"0\n\x0fQuestionRequest\x12\x0f\n\x07passage\x18\x01 \x01(\t\x12\x0c\n\x04term\x18\x02 \x01(\t\"!\n\rQuestionReply\x12\x10\n\x08question\x18\x01 \x01(\t2\x96\x01\n\x05Rikka\x12&\n\x05Query\x12\r.QueryRequest\x1a\x0c.AnswerReply\"\x00\x12-\n\tSummarize\x12\x0f.SummaryRequest\x1a\r.SummaryReply\"\x00\x12\x36\n\x10GenerateQuestion\x12\x10.QuestionRequest\x1a\x0e.QuestionReply\"\x00\x62\x06proto3')
)




_QUERYREQUEST = _descriptor.Descriptor(
  name='QueryRequest',
  full_name='QueryRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='passage', full_name='QueryRequest.passage', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='question', full_name='QueryRequest.question', index=1,
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
  serialized_start=15,
  serialized_end=64,
)


_ANSWERREPLY = _descriptor.Descriptor(
  name='AnswerReply',
  full_name='AnswerReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='answer', full_name='AnswerReply.answer', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='score', full_name='AnswerReply.score', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=66,
  serialized_end=110,
)


_SUMMARYREQUEST = _descriptor.Descriptor(
  name='SummaryRequest',
  full_name='SummaryRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='passage', full_name='SummaryRequest.passage', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=112,
  serialized_end=145,
)


_SUMMARYREPLY = _descriptor.Descriptor(
  name='SummaryReply',
  full_name='SummaryReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='summary', full_name='SummaryReply.summary', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=147,
  serialized_end=178,
)


_QUESTIONREQUEST = _descriptor.Descriptor(
  name='QuestionRequest',
  full_name='QuestionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='passage', full_name='QuestionRequest.passage', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='term', full_name='QuestionRequest.term', index=1,
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
  serialized_start=180,
  serialized_end=228,
)


_QUESTIONREPLY = _descriptor.Descriptor(
  name='QuestionReply',
  full_name='QuestionReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='question', full_name='QuestionReply.question', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=230,
  serialized_end=263,
)

DESCRIPTOR.message_types_by_name['QueryRequest'] = _QUERYREQUEST
DESCRIPTOR.message_types_by_name['AnswerReply'] = _ANSWERREPLY
DESCRIPTOR.message_types_by_name['SummaryRequest'] = _SUMMARYREQUEST
DESCRIPTOR.message_types_by_name['SummaryReply'] = _SUMMARYREPLY
DESCRIPTOR.message_types_by_name['QuestionRequest'] = _QUESTIONREQUEST
DESCRIPTOR.message_types_by_name['QuestionReply'] = _QUESTIONREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

QueryRequest = _reflection.GeneratedProtocolMessageType('QueryRequest', (_message.Message,), dict(
  DESCRIPTOR = _QUERYREQUEST,
  __module__ = 'rikka_pb2'
  # @@protoc_insertion_point(class_scope:QueryRequest)
  ))
_sym_db.RegisterMessage(QueryRequest)

AnswerReply = _reflection.GeneratedProtocolMessageType('AnswerReply', (_message.Message,), dict(
  DESCRIPTOR = _ANSWERREPLY,
  __module__ = 'rikka_pb2'
  # @@protoc_insertion_point(class_scope:AnswerReply)
  ))
_sym_db.RegisterMessage(AnswerReply)

SummaryRequest = _reflection.GeneratedProtocolMessageType('SummaryRequest', (_message.Message,), dict(
  DESCRIPTOR = _SUMMARYREQUEST,
  __module__ = 'rikka_pb2'
  # @@protoc_insertion_point(class_scope:SummaryRequest)
  ))
_sym_db.RegisterMessage(SummaryRequest)

SummaryReply = _reflection.GeneratedProtocolMessageType('SummaryReply', (_message.Message,), dict(
  DESCRIPTOR = _SUMMARYREPLY,
  __module__ = 'rikka_pb2'
  # @@protoc_insertion_point(class_scope:SummaryReply)
  ))
_sym_db.RegisterMessage(SummaryReply)

QuestionRequest = _reflection.GeneratedProtocolMessageType('QuestionRequest', (_message.Message,), dict(
  DESCRIPTOR = _QUESTIONREQUEST,
  __module__ = 'rikka_pb2'
  # @@protoc_insertion_point(class_scope:QuestionRequest)
  ))
_sym_db.RegisterMessage(QuestionRequest)

QuestionReply = _reflection.GeneratedProtocolMessageType('QuestionReply', (_message.Message,), dict(
  DESCRIPTOR = _QUESTIONREPLY,
  __module__ = 'rikka_pb2'
  # @@protoc_insertion_point(class_scope:QuestionReply)
  ))
_sym_db.RegisterMessage(QuestionReply)



_RIKKA = _descriptor.ServiceDescriptor(
  name='Rikka',
  full_name='Rikka',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=266,
  serialized_end=416,
  methods=[
  _descriptor.MethodDescriptor(
    name='Query',
    full_name='Rikka.Query',
    index=0,
    containing_service=None,
    input_type=_QUERYREQUEST,
    output_type=_ANSWERREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Summarize',
    full_name='Rikka.Summarize',
    index=1,
    containing_service=None,
    input_type=_SUMMARYREQUEST,
    output_type=_SUMMARYREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GenerateQuestion',
    full_name='Rikka.GenerateQuestion',
    index=2,
    containing_service=None,
    input_type=_QUESTIONREQUEST,
    output_type=_QUESTIONREPLY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_RIKKA)

DESCRIPTOR.services_by_name['Rikka'] = _RIKKA

# @@protoc_insertion_point(module_scope)
