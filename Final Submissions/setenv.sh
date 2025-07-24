#!/usr/bin/env bash
set -x
INSTANCE_NAME=cse_1 PORT=8000 python3 response.py &
INSTANCE_NAME=cse_2 PORT=8001 python3 response.py &
INSTANCE_NAME=cse_3 PORT=8002 python3 response.py &

INSTANCE_NAME=eee_1 PORT=8003 python3 response.py &
INSTANCE_NAME=eee_2 PORT=8004 python3 response.py &
INSTANCE_NAME=eee_3 PORT=8005 python3 response.py &

INSTANCE_NAME=ice_1 PORT=8006 python3 response.py &
INSTANCE_NAME=ice_2 PORT=8007 python3 response.py &
INSTANCE_NAME=ice_3 PORT=8008 python3 response.py &
