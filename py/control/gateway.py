from ..domain.contract import Contract
from ..api.proto import echoservice_pb2, echoservice_pb2_grpc

class Gateway(Contract):
    def __init__(self, channel):
        self.echo_stub = echoservice_pb2_grpc.EchoServiceStub(channel)

    def Echo(self, message: str) -> str:
        response = self.echo_stub.Echo(echoservice_pb2.EchoRequest(message=message))
        return response.message
