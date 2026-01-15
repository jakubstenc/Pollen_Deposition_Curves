#!/bin/bash

# Ensure we use the local virtual environment's Python
# This avoids "ModuleNotFoundError" for packages installed in .venv
export QUARTO_PYTHON=$(pwd)/.venv/bin/python

print_usage() {
    echo "Usage: ./render.sh [file]"
    echo "  If [file] is provided, only that file is rendered."
    echo "  Otherwise, the whole project is rendered."
}

if [ "$1" == "-h" ] || [ "$1" == "--help" ]; then
    print_usage
    exit 0
fi

if [ -n "$1" ]; then
    echo "Rendering $1 using local venv..."
    quarto render "$1"
else
    echo "Rendering project using local venv..."
    quarto render
fi
