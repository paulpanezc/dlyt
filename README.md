# Youtube Video Downloader

### System requirements
- python 3.12
- pytube 15.0.0
- poetry 1.7.1

### Use

> poetry install --no-root

> python main.py

### Generate Installer with PyInstaller

> pyinstaller --noconfirm --onefile --windowed --add-data "./dlyt;dlyt/" --paths "VIRTUALENV_PATH/Lib/site-packages/"  "./main.py"
