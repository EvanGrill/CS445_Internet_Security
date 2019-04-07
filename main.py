import platform
import shutil
import os
import sqlite3
from glob import glob

def fetch_os():
    '''Returns (OS, Version) of the currently running OS.'''
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
    '''Copies the cookies sqlite database from Firefox from a given
    OS.  Currently only Mac OS is supported.  Future work will merge
    copy functions together and take OS and Browser as arguemnts.'''
    try:
        os.remove("./ff_cookies.sqlite")
    except:
        pass
    if OS[0] == "Mac OS":
        folder = os.path.expanduser("~")+"/Library/Application Support/Firefox/Profiles/"
    else:
        folder = "N/A"
    cookie_location = glob(folder + "*/")[0] + "cookies.sqlite"   
    try:
        shutil.copyfile(cookie_location, "./ff_cookies.sqlite")
        return True
    except:
        return False

def copy_chrome_cookie_db(OS):
    '''Copies the cookies sqlite database from Chrome from a given
    OS.  Currently only Mac OS is supported.  Future work will merge
    copy functions together and take OS and Browser as arguemnts.'''
    try:
        os.remove("./ch_cookies.sqlite")
    except:
        pass
    if OS[0] == "Mac OS":
        folder = os.path.expanduser("~")+"/Library/Application Support/Google/Chrome/Default/"
    else:
        folder = "N/A"
    cookie_location = folder + "Cookies"
    print(cookie_location)
    try:
        shutil.copyfile(cookie_location, "./ch_cookies.sqlite")
        return True
    except:
        return False


def fetch_twitter_token(dbfile, browser):
    '''Retreive auth_token cookie for specific browsers.
    Presently works for Firefox.  Chrome support is in progress,
    but only retreives the encrypted cookie. Decryption is not
    yet available.'''
    conn = sqlite3.connect(dbfile)
    c = conn.cursor()
    if browser == "FF":
        query = "SELECT value FROM moz_cookies WHERE baseDomain='twitter.com' AND name='auth_token'"
    if browser == "CH":
        query = "SELECT encrypted_value FROM cookies WHERE host_key='.twitter.com' AND name='auth_token'"
    for row in c.execute(query):
        return row[0]
    pass

def main():
    OS = fetch_os()
    copy_firefox_cookie_db(OS)
    copy_chrome_cookie_db(OS)
    print(fetch_twitter_token("./ff_cookies.sqlite", "FF"))
    print(fetch_twitter_token("./ch_cookies.sqlite", "CH"))


if __name__ == "__main__":
    main()