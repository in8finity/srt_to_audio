#!/bin/sh

_term() {
  echo "Caught SIGTERM signal! Stopping!"
  # unbind traps
  trap - TERM
  trap - INT
  exit
}

# register handler for selected signals
trap _term TERM
trap _term INT

RUN_COMMAND=$1
ARG1=$2

if [ -z "$RUN_COMMAND" ]; then
  RUN_COMMAND='loop'
fi

case "$RUN_COMMAND" in
"loop") ./bin/dev/loop.sh;;
"converter") /usr/local/bin/python3 ./src/main.py $ARG1;;
esac
