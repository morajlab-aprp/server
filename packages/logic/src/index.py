from concurrent import futures
import logging
import grpc
import packages.logic.monitor_pb2 as monitor__pb2
import packages.logic.monitor_pb2_grpc as monitor_pb2__grpc


class Monitor(monitor_pb2__grpc.MonitorServicer):

    def SendData(self, request, context):
        return monitor__pb2.MonitorReply(message='Hello, %s!' % request.data)


def main():
    port = '50051'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    monitor_pb2__grpc.add_MonitorServicer_to_server(Monitor(), server)
    server.add_insecure_port('[::]:' + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    main()
