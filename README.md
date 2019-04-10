# Auto-Archive

This python script is built to archive folders and files from one place to another and appending the arcive date to the folder and file names. The date is acquired from the system and appended in a specific but a popular format: "\_dd_mm_YYYY".

## Running the script

To run the script, just run the **archive.exe** file in the **dist** folder. Provide the source path, the destination path and the operation you need to perform. This script currently supports **copy** and **move** operation.

## Build the script from source

If you need to do some changes in the script and want the exceutable to incorporate those changes, you need to rebuild the script. There are a few things you need to install in order to build the script.

- Python, version 3.5+. This can be downloaded and installed from here: <https://www.python.org/downloads/windows/>  
  This is the windows version. For any other platform, go here: <https://www.python.org/downloads/>  
  If you have a x64 bit system, kindly download the 64-bit version of Python distribution. If you need assistance with the installation, go here: <https://docs.python.org/3/using/windows.html>  
  You need to make sure that you add python to PATH. Refer to the link for instructions on how to do the same.

- Pyinstaller. This is used to package or build the executable from the script. After you install python, open the terminal/command line and type in the command `pip install pyinstaller`  
  This will install the latest stable version of pyinstaller package.

For building the script, navigate to the folder same folder where your script currently is and open terminal/command line here. Enter this command: `pyinstaller --onefile --name <any name you want> <name of your script>.py`  
This will create two new folders and a file with `.spec` extension. The first folder `build` will contain the compiled and temporary files. `dist` folder will contain the executable which you can run independently later. The file with `.spec` extension is the configuration file.

For more insformation on building with pyinstaller and different options that can be used with it, you can visit this url: <https://pyinstaller.readthedocs.io/en/stable/operating-mode.html>

After the above steps are complete, you can run the script independently.
