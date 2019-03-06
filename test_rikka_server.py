import grpc
from concurrent import futures
import time
import os
import signal
import sys

import rikka_pb2
import rikka_pb2_grpc

class RikkaServicer(rikka_pb2_grpc.RikkaServicer):
    def Query(self, request, context):
        response = rikka_pb2.AnswerReply()
        response.answer = "Test Answer return Correct"
        response.score = 0.999
        return response

    def Summarize(self, request, context):
        response = rikka_pb2.SummaryReply()
        response.summary = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
        return response

    def GenerateQuestion(self, request, context):
        response = rikka_pb2.QuestionReply()
        response.question = "Why did my father leave us?"
        return response


def main():
    rikka_server = grpc.server(futures.ThreadPoolExecutor(max_workers=64))
    rikka_pb2_grpc.add_RikkaServicer_to_server(
                RikkaServicer(), rikka_server)

    print('Starting server. Listening on port 50051')
    rikka_server.add_insecure_port('[::]:50051')
    rikka_server.start()

    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        rikka_server.stop(0)


def set_exit_handler(func):
    signal.signal(signal.SIGTERM, func)


def on_exit(sig, func=None):
    print("exit handler triggered")
    sys.exit(1)


if __name__ == "__main__":
    set_exit_handler(on_exit)
    main()
