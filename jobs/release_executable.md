### Run this script _(from the root directory)_ to create a release executable for the application.

```bash
pyinstaller --noconfirm --onefile --windowed --icon=src/assets/logos/window_logo.ico nemesis.py --version-file=meta/version_info.txt
```

- `--noconfirm`: Overwrites existing files without prompting (e.g. if the executable already exists).
- `--onefile`: Bundles the application into a single executable file.
- `--windowed`: Suppresses the additional console window on Windows.
- `--icon`: Specifies the icon path for the executable.
- `--version-file`: Specifies the path to the executable's metadata file.