# DroneFish, a game to spread #TeamSeas

This game is quite simple, catch the trash with your drone. But be careful! You musn't touch the fish or they'll die.

## Platform availability

* Windows ✅
* OS X ❎
* Linux ✅

# How to install

## Building from source

The requirements for building from source are:

* Python 3
* pygame
* PyInstaller

Download the source code

```bash
git clone https://github.com/CodyMarkix/DroneFish.git
```

Install the dependencies

```bash
pip install pygame PyInstaller 
```

And begin the compilation process.

```bash
cd DroneFish
cd bin
cd <instert your platform here>
pyinstaller --onefile ..\..\main.py
```