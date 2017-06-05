Pywin32
=======

Pywin32 support for Kodi


# Using Pywin32
Import `pywin32setup` before including any pywin32 modules.  You can include it once in the top most level file, and all subsequent includes from that file should be guaranteed access.  It does not have to be included in all files that call pywin32 modules, just once in the top level file that is the entry point.  Example (show url path of all open explorer windows):

```python
import pywin32setup
from win32com.client.gencache import EnsureDispatch


def run():
    for w in EnsureDispatch("Shell.Application").Windows():
        print(w.LocationName + "=" + w.LocationURL)

run()
```
