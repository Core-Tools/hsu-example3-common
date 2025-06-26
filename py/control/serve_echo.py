from hsu_core.py.control.server import Server
from hsu_core.py.control.def_handler import register_grpc_default_server_handler as register_core_grpc_default_server_handler
from .handler import register_grpc_server_handler as register_echo_grpc_server_handler

def serve_echo(handler):
    import argparse

    parser = argparse.ArgumentParser(description="Echo gRPC Server")
    parser.add_argument("--port", type=int, default=50055, help="Port to listen on")
    args = parser.parse_args()
    
    server = Server(args.port)
    register_core_grpc_default_server_handler(server.GRPC())
    register_echo_grpc_server_handler(server.GRPC(), handler)
    server.run(None)
