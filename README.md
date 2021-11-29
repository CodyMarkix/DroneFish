# This project is abandoned. For now (As I'm not able to finish this game in time for the jam)

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

## Installing binary

### Installing from git tree

Binaries for Linux and Windows are available in the bin folder in the source code. Download the source code

```bash
git clone https://github.com/CodyMarkix/DroneFish.git
```

Navigate inside the bin folder and find the binary for your appropriate platform

```bash
cd DroneFish
cd bin
cd <insert your platform here>
```

and move the binary and the resources folder to your desired location. Or you can leave it in the bin folder, these binaries are portable! (Though make sure you don't seperate the Resources folder from the binary)

### Installing from releases

Click on the releases tab on the repo's homepage.

[logo]: https://i.imgur.com/hn8pYSD.png

Then find your desired release (latest is usually best) and download the zip named after your platform. Then extract the zip file and place the folder to any desired place! (You probably shouldn't move it into a folder that has administator/root privileges)