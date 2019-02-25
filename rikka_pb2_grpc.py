# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import rikka_pb2 as rikka__pb2


class RikkaStub(object):
  """This is the serivce for all Ai related request 
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Query = channel.unary_unary(
        '/Rikka/Query',
        request_serializer=rikka__pb2.QueryRequest.SerializeToString,
        response_deserializer=rikka__pb2.AnswerReply.FromString,
        )
    self.Summarize = channel.unary_unary(
        '/Rikka/Summarize',
        request_serializer=rikka__pb2.SummaryRequest.SerializeToString,
        response_deserializer=rikka__pb2.SummaryReply.FromString,
        )
    self.GenerateQuestion = channel.unary_unary(
        '/Rikka/GenerateQuestion',
        request_serializer=rikka__pb2.QuestionRequest.SerializeToString,
        response_deserializer=rikka__pb2.QuestionReply.FromString,
        )


class RikkaServicer(object):
  """This is the serivce for all Ai related request 
  """

  def Query(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Summarize(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GenerateQuestion(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_RikkaServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Query': grpc.unary_unary_rpc_method_handler(
          servicer.Query,
          request_deserializer=rikka__pb2.QueryRequest.FromString,
          response_serializer=rikka__pb2.AnswerReply.SerializeToString,
      ),
      'Summarize': grpc.unary_unary_rpc_method_handler(
          servicer.Summarize,
          request_deserializer=rikka__pb2.SummaryRequest.FromString,
          response_serializer=rikka__pb2.SummaryReply.SerializeToString,
      ),
      'GenerateQuestion': grpc.unary_unary_rpc_method_handler(
          servicer.GenerateQuestion,
          request_deserializer=rikka__pb2.QuestionRequest.FromString,
          response_serializer=rikka__pb2.QuestionReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Rikka', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
