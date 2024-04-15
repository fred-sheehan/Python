## notes for standalone pomodoro build
make sure you have pyinstaller on your system

```bash
pip3 install pyinstaller
```

and then, from within the folder where main.py and the image and sound file are, run this command to build the standalone app

```bash
pyinstaller --onefile --add-data "timer.mp3:." --add-data "tomato.png:." main.py
```

this will create a dist folder with the standalone app in it. you can move this app to wherever you want and run it from there.
