# Banzai PyInstaller Example

#You have just created an awesome new application. Maybe it’s a game or maybe it’s an image viewer. Whatever your application is, you want to share it with your friend or a family member. However, you know they won’t know how to install Python or any of the dependencies. What do you do? You need something that will transform your code into an executable!
#Python has many different tools you can use to convert your Python code into a Windows executable. Here are a few different tools you can use:
#PyInstaller
#py2exe
#cx_freeze
#Nuitka
#Briefcase
 
#These various tools can all be used to create executables for Windows. They work slightly differently, but the end result is that you will have an executable and perhaps some other files that you need to distribute too.
#PyInstaller and Briefcase can be used to create Windows and MacOS executables. Nuitka is a little different in that it turns your Python code into C code before converting it into an executable. What this means is that the result ends up much smaller than PyInstaller’s executable.
#By converting your Python script into an executable file, you can protect your code from being modified or stolen, make it easier for others to use your program, and schedule tasks to run automatically

 
 

[Back to Sheena Utils README](../README.md)

## Overview

 

Steps to create an executable from Python script

 

1) pip install pyinstaller

2) echo print('Hello Word') > helloworld.py

3) pyinstaller --onefile helloworld.py
#pyinstaller pysearch.py

4) the output helloworld.exe will be located at<br>


#https://pyinstaller.org/en/stable/index.html


(venv) C:\pyinstaller>dist\helloworld.exe

Hello Word

 

Reference:<br>

https://www.pyinstaller.org/en/stable/operating-mode.html

 

https://python.land/deployment/pyinstaller<br>

 

**PyInstaller** supports making executables for Windows, Linux, and macOS, but it cannot cross compile. Therefore, you cannot make an executable targeting one Operating System from another Operating System. So, to distribute executables for multiple types of OS, you'll need a build machine for each supported OS.
