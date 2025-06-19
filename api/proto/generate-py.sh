#!/bin/bash
python -m grpc_tools.protoc -I. --python_out=../../py/api/proto --grpc_python_out=../../py/api/proto echoservice.proto 
python ../../py/api/proto/fix_imports.py