#!/bin/bash

set -e

pyinstaller --noconfirm --onefile --windowed --icon="src/assets/logos/window_logo.ico" "app.py"