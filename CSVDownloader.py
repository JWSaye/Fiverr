import datetime
import ftplib
import glob
import os
import shutil
import time

import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

WorkDir = r"C:\Users\jwsay\Downloads\Fiverr\jonathan242"  # Set the path to download files to and manipulate them from
ChromeDriver = r"C:\Users\jwsay\Downloads\Fiverr\jonathan242\chromedriver.exe"  # Set the path of the Chrome driver
Webpage = "https://sample-videos.com/download-sample-csv.php"  # Set the webpage to interact with
Adblock = r"C:\Users\jwsay\Downloads\Fiverr\jonathan242\3.10.1_0"  # Set the path to adblock for chrome
FTP_Host = "134.122.7.95"
FTP_User = "jwelchs"
FTP_Password = "test123"

chromeOptions = Options()

chromeOptions.add_argument("load-extension=" + Adblock)
chromeOptions.add_experimental_option("prefs", {"download.default_directory": WorkDir})

driver = webdriver.Chrome(executable_path=ChromeDriver, options=chromeOptions)
driver.create_options()

driver.get(Webpage)

download = driver.find_element_by_class_name("download_csv")

download.click()

time.sleep(.5)

driver.quit()

print("File downloaded from website")

extension = "csv"
os.chdir(WorkDir)
result = glob.glob('*.{}'.format(extension))

file = result[0]

df = pd.read_csv(file, encoding='unicode_escape')

row_count = len(df) + 1

now = datetime.datetime.now()

new_file = file[:-4] + "--" + now.strftime("%d-%m-%Y-%H-%M-%S") + "--" + str(row_count) + ".csv"
os.rename(file, new_file)

print("File renamed to " + new_file)

ftp = ftplib.FTP(FTP_Host, FTP_User, FTP_Password)
ftp.encoding = "utf-8"

with open(new_file, "rb") as file:
    ftp.storbinary(f"STOR {new_file}", file)

shutil.move(new_file, "Uploaded\\" + new_file)

print("File uploaded to FTP server")
print("File moved to Uploaded folder")
print("Process Complete")
