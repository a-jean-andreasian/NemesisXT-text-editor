#!/bin/bash

set -e

APP_NAME="Nemesis XT"
ENTRY_FILE="app.py"
ICON_FILE="src/assets/logos/window_logo.ico"


# Build --add-data args
ADD_DATA_ARGS=()
for pair in "${DATA_FILES[@]}"; do
  ADD_DATA_ARGS+=(--add-data "$pair")
done

DATA_FILES=(
  "src/assets/logos/window_logo.ico;src/assets/logos"
)
echo "[1] Installing PyInstaller..."
pip install --upgrade pyinstaller

echo "[2] Building standalone executable..."
pyinstaller --noconfirm --onefile --windowed --icon="src/assets/logos/window_logo.ico" "$ENTRY_FILE"
# pyinstaller --noconfirm --onefile --windowed --icon=src/assets/logos/window_logo.ico app.py

EXE_PATH="dist/$(basename "$ENTRY_FILE" .py).exe"
echo "[3] Executable created at: $EXE_PATH"

echo "[4] Generating Inno Setup script..."
INSTALLER_SCRIPT="${APP_NAME}_installer.iss"

cat > "$INSTALLER_SCRIPT" <<EOF
[Setup]
AppName=$APP_NAME
AppVersion=1.0
DefaultDirName={pf}\\$APP_NAME
OutputDir=dist
OutputBaseFilename=${APP_NAME}_Installer
Compression=lzma
SolidCompression=yes

[Files]
Source: "$EXE_PATH"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\\$APP_NAME"; Filename: "{app}\\$(basename "$EXE_PATH")"
Name: "{group}\\Uninstall $APP_NAME"; Filename: "{uninstallexe}"
EOF

echo "[5] Inno Setup script generated: $INSTALLER_SCRIPT"
echo "    Open it in Inno Setup Compiler to create the installer."
