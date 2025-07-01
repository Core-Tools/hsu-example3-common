import argparse
import time

parser = argparse.ArgumentParser(description="Echo gRPC Client")
parser.add_argument("--port", type=int, default=50055, help="Port to connect to")
args = parser.parse_args()

from hsu_core.control.client_conn import ClientConn
from hsu_core.control.gateway import Gateway as CoreGateway
from hsu_echo.control.gateway import Gateway as EchoGateway

retry_period = 1
while True:
    try:
        client_conn = ClientConn(args.port)
        core_gateway = CoreGateway(client_conn.GRPC())
        echo_gateway = EchoGateway(client_conn.GRPC())

        core_gateway.Ping()

        message = echo_gateway.Echo("Hello, World!")
        print(message)

        break
    except Exception as e:
        if "ConnectEx: Connection refused (No connection could be made because the target machine actively refused it." in str(e):
            print("Connection error, retrying in %s second..." % retry_period)
            time.sleep(retry_period)
            retry_period *= 2
            continue
        else:
            print(e)
            raise e
