#! /usr/bin/env python3
import requests
import urllib3
import signal
import sys
import os
import logging
import argparse
import time

signal.signal(signal.SIGINT, lambda x, y: sys.exit(1))
urllib3.disable_warnings()

parser = argparse.ArgumentParser()
parser.add_argument('--start', metavar='123', type=int, help='First frame you want to upload')
parser.add_argument('--loop', metavar='40', nargs='?', default=40, type=int, help='Loop value')
args = parser.parse_args()
frame_start = args.start
loopvalue = args.loop

class color:
   purple = '\033[95m'
   cyan = '\033[96m'
   darkcyan = '\033[36m'
   blue = '\033[94m'
   green = '\033[92m'
   yellow = '\033[93m'
   red = '\033[91m'
   bold = '\033[1m'
   underline = '\033[4m'
   reset = '\033[0m'
   magenta = "\033[35m"

if len(sys.argv)==1:
        parser.print_help(sys.stderr)
        sys.exit(1)
elif frame_start == None:
        parser.print_help(sys.stderr)
        print()
        print(f"{color.red}{color.bold}Error! First frame value is mandatory{color.reset}{color.reset}")
        sys.exit(1)

logging.basicConfig(level=logging.DEBUG)
ACCESS_TOKEN = '' # User your access token
url = "https://graph.facebook.com/v5.0/me/photos"
x = frame_start
y = loopvalue
for i in range(x, x+y):
        time.sleep(3)
        num = (f"{i:0>4}")
        image_source = (f"./frames/{num}.png")
        caption = (f"Gotoubun no Hanayome Season 2 Episode 6: The Last Exam [Frame {num}/1440]")
        payload = {
                'access_token' : ACCESS_TOKEN,
                'caption': caption, 
                'published' : 'true',
        }
        files = {'source': (image_source, open(image_source, 'rb'))}
        r = requests.post(url, files=files, data=payload)
        if r.status_code == 200:
            logging.debug(f"{color.bold}{color.green}Frame {num} Uploaded{color.reset}. {r.json()}")
            os.remove(f"{image_source}")
        else:
            logging.debug(f"{color.bold}{color.red}Failed to Upload Frame {num}{color.reset}. {r.json()}")
            break
print(f"{color.bold}Task Done{color.reset}")