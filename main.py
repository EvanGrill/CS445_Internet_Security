import platform
import shutil
import os
import sqlite3
from glob import glob

def fetch_os():
    system = platform.system()
    if system == "Windows":
        return (system, platform.release())
    elif system == "Darwin":
        return ("Mac OS", platform.mac_ver()[0])
    elif system == "Linux":
        return ("Linux", platform.release())
    else:
        return ("N/A", "N/A")

def copy_firefox_cookie_db(OS):
    os.remove("./cookies.sqlite")
    if OS[0] == "Mac OS":
        folder = os.path.expanduser("~")+"/Library/Application Support/Firefox/Profiles/"
    else:
        folder = "N/A"
    cookie_location = glob(folder + "*/")[0] + "cookies.sqlite"   
    try:
        shutil.copyfile(cookie_location, "./cookies.sqlite")
        return True
    except:
        return False

def fetch_twitter_token(dbfile):
    conn = sqlite3.connect(dbfile)
    c = conn.cursor()
    for row in c.execute("SELECT value FROM moz_cookies WHERE baseDomain='twitter.com' AND name='auth_token'"):
        return row[0]
    pass

def main():
    OS = fetch_os()
    copy_firefox_cookie_db(OS)
    print(fetch_twitter_token("./cookies.sqlite"))


if __name__ == "__main__":
    main()