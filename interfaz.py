name: Build Mac App
on: [push]

jobs:
  build:
    runs-on: macos-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Install dependencies
        run: |
          pip install customtkinter pillow pyinstaller

      - name: Build with PyInstaller
        run: |
          # Generamos la App sin logos ni dependencias de imagen externas
          pyinstaller --noconsole --onefile --windowed --name "Rodriguez_Asociados_Mac" interfaz.py

      - name: Upload Artifact
        uses: actions/upload-artifact@v3
        with:
          name: Mac-App
          path: dist/Rodriguez_Asociados_Mac.app