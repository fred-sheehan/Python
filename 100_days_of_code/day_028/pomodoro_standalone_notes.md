## notes for standalone pomodoro build

The main.py file has been written to enable it to be built into a standalone app using pyinstaller. The programme uses the tkinter GUI programme, and the image and sound file in the folder with the main.py file, are included in the build process. I'm assuming you already have python 3 installed on your system.

first, make sure you also have pyinstaller on your system

```bash
pip3 install pyinstaller
```

and then, from within the folder where main.py and the image and sound file are, run this command to build the standalone app

```bash
pyinstaller --onefile --add-data "timer.mp3:." --add-data "tomato.png:." main.py
```

this will create a dist folder with the standalone app in it. you can move this app to wherever you want and run it from there.
