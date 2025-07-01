#!/usr/bin/env python
"""
This script fixes the imports in the generated Python gRPC files.
Run this after generating the Python stubs.
Template file - echoservice will be replaced with actual proto file base name.
"""
import os
import re

def fix_imports(grpc_file_path):
    """Fix the imports in the generated gRPC Python file."""
    with open(grpc_file_path, 'r') as f:
        content = f.read()
    
    # Replace simple 'import echoservice_pb2' with 'from . import echoservice_pb2'
    fixed_content = re.sub(
        r'import echoservice_pb2 as echoservice__pb2',
        r'from . import echoservice_pb2 as echoservice__pb2',
        content
    )
    
    with open(grpc_file_path, 'w') as f:
        f.write(fixed_content)
    
    print(f"Fixed imports in {grpc_file_path}")

if __name__ == "__main__":
    # Path to the generated gRPC file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    grpc_file = os.path.join(current_dir, "echoservice_pb2_grpc.py")
    
    if os.path.exists(grpc_file):
        fix_imports(grpc_file)
    else:
        print(f"File not found: {grpc_file}")
        print("Generate the Python stubs first.") 