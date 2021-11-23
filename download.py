#!/usr/bin/env python3

import re
from time import sleep
import os.path
import time
import requests
import wget
import shutil

mainDirectory = "DIRECTORY"

def VPNRequest():
        todayDate = time.strftime("%d-%m-%y")
        directory = mainDirectory + todayDate
        url = "https://raw.githubusercontent.com/jychp/vpns/main/servers.lst"
        if not os.path.exists(directory):
                os.makedirs(directory)
        filename = wget.download(url)
        filename
        source = mainDirectory + "servers.lst"
        destination = mainDirectory + todayDate
        dest = shutil.move(source, destination)

        print(" Sleeping 1 day, see you tomorrow :)")
        time.sleep(86400)

while True:
        VPNRequest()

if __name__ == '__main__':
        main()
