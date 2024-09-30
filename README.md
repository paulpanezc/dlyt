# Youtube Video Downloader

### System requirements
- python 3.12.3
- poetry 1.8.3
- pytubefix 7.1.3

### Use

> poetry install --no-root

> pip install pyinstaller

> python main.py

### Generate Installer with PyInstaller

> pyinstaller --noconfirm --onefile --windowed --add-data "./dlyt;dlyt/" --paths "VIRTUALENV_PATH/Lib/site-packages/"  "./main.py"
