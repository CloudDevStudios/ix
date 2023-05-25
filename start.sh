#!/bin/bash

# Run setup
make dev_setup

# Start server and worker in the background
make server &
make worker &

# Keep script running as long as the services are running
wait
