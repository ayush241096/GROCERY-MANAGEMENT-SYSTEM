import cx_Freeze
import tkinter
import sqlite3
import PIL
import sys
import os

os.environ['TCL_LIBRARY'] = "C:\\LOCAL_TO_PYTHON\\Python35-32\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\LOCAL_TO_PYTHON\\Python35-32\\tcl\\tk8.6"
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

executables = [cx_Freeze.Executable("index.py", base=base, icon="favicon.ico")]

cx_Freeze.setup(
    name = "Grocery",
    options = {"build_exe": {"packages":["tkinter"], "include_files":["collage.jpg","favicon.ico","front.jpg","billingdetails.py","expirycheck.py","stockdetails.py"]}},
    version = "0.01",
    description = "Sea of BTC trading application",
    executables = executables
    )