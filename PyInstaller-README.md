# Banzai PyInstaller Example

 

[Back to Sheena Utils README](../README.md)

## Overview

 

Steps to create an executable from Python script

 

1) pip install pyinstaller

2) echo print('Hello Word') > helloworld.py

3) pyinstaller --onefile helloworld.py

4) the output helloworld.exe will be located at<br>

(venv) C:\pyinstaller>dist\helloworld.exe

Hello Word

 

Reference:<br>

https://www.pyinstaller.org/en/stable/operating-mode.html

 

https://python.land/deployment/pyinstaller<br>

 

**PyInstaller** supports making executables for Windows, Linux, and macOS, but it cannot cross compile. Therefore, you cannot make an executable targeting one Operating System from another Operating System. So, to distribute executables for multiple types of OS, you'll need a build machine for each supported OS.