# pywin32_hack

A Hack to get *script.module.pywin32*
working with KODI 17.3

Python2710 binary and source files origin 
- http://p-nand-q.com/python/building-python-27-with-visual_studio.html
- Build it yourself or use the pre-compiled binary.


Instructions for using the binary:

1. extract 2015.08.07-Python2710-x32-vs2015.7z 

2. copy the Python27 folder from the extracted directory to your C: drive.
You should now have a C:\Python27 directory.

3. navigate to C:\Python27 in windows explorer. 
find the python.reg file and add it to the registry. *(read it first, of course)*


KODI -> addons -> from zip -> 
(install the modified script.module.pywin32.zip)

##What's been modified?

script.module.pywin32/lib/x32/pywin32setup.py

## Why was it modified?

KODI 17.3 was built with a version of Python27
that was built with Visual Studio 2015.

The standard version of Python27 is NOT built with Visual Studio 2015.

I tried overwriting with compatible dll files , 
but KODI kept raising errors about not being about to find them...
 even when they were in the same directory. 


For more details, see :
- *script.module.pywin32/lib/x32/pywin32setup.py*