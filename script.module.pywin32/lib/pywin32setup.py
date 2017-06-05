import sys
import os
import imp
import xbmc
home = xbmc.translatePath("special://home")
package_path = os.path.join(home, "addons", "script.module.pywin32")
assert xbmc.getCondVisibility("system.platform.windows")
ARCH = "x32"
LIB_PATHS = [
    (os.path.join(package_path, "lib", ARCH, "win32"), "win32"),
    (os.path.join(package_path, "lib", ARCH, "win32", "lib"), "win32/lib"),
    (os.path.join(package_path, "lib", ARCH), "win32com"),
    (os.path.join(package_path, "lib", ARCH, "win32comext"), "win32comext"),
    (os.path.join(package_path, "lib", ARCH, "pywin32_system32"), "pywin32_system32")
]

for lib in LIB_PATHS:
    if lib[0] not in sys.path:
        sys.path.append(lib[0])

try:
        # KODI 17.3 doesn't like loading the dll files from "script.module.pywin32" lib dir;
        # However, loading them from the main Python directory works just fine.
        # 
        # not really a big deal unless you install python to a directory other than c:\python27
        #
        # this doesn't work:
        # imp.load_dynamic("pythoncom", os.path.join(package_path, "lib", ARCH, "pywin32_system32", "pythoncom27.dll"))
        #
        # this doesn't work:
        # imp.load_dynamic("pywintypes", "C:\\Users\\Username\\AppData\\Roaming\\Kodi\\addons\\
        # script.module.pywin32\\lib\\x32\\pywin32_system32\\pywintypes27.dll")
        # imp.load_dynamic("pythoncom", "C:\\Users\\Username\\AppData\\Roaming\\Kodi\\addons\\
        # script.module.pywin32\\lib\\x32\\pywin32_system32\\pythoncom27.dll")
        #
        # but, this does :
        imp.load_dynamic("pywintypes", "C:\\Python27\\Lib\\site-packages\\pywin32_system32\\pywintypes27.dll")
        imp.load_dynamic("pythoncom", "C:\\Python27\\Lib\\site-packages\\pywin32_system32\\pythoncom27.dll")
except ImportError as e:
    if "DLL load failed" in str(e):
        path = "C:\\Python27\\"
        path2 = os.path.join(package_path, "lib", ARCH, "pywin32_system32")
        path3 = "C:\\Python27\\Lib\\site-packages\\pywin32_system32"
        os.environ["PATH"] = os.environ["PATH"] + ";" + path + ";" + path2 + ";" + path3
        try:
            import pythoncom
        except ImportError as e:
            dll = os.listdir(path)
            dll = [os.path.join(path, x) for x in dll if "dll" in x.lower()]
            raise ImportError("{}".format(str(e)))
    else:
        raise e
