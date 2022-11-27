# Every Frame in Order Bot
This is tool i use to run my [Every Gotoubun no Hanayome Frame In Order](https://www.facebook.com/GotoubunFrameInOrder) Facebook Fanspage.

Tested in Debian with Python 3.10.8.
## Preparation
Since basicly i create this tool for my personal needs, i don't automate all process. There are several steps that must be executed before you can use this tool.

First, you need to extract all frames from video into **frames** folder. You can use **ffmpeg** for this.

Example, if you have Gotoubun-Episode4.mp4, you can run this command.
``` bash
mkdir frames
ffmpeg -i 'Gotoubun-Episode4.mp4' -vf fps=1 ./frames/%04d.png -hide_banner
```
Your extracted frames will named 0001.png, 0002.png, etc. Example:
```bash
nino@nakano:~$ ls -lha ./frames/ | head -n 8
total 49M
drwxr-xr-x 2 nino nino 4.0K Nov 27 17:51 .
drwxr-xr-x 5 nino nino 4.0K Nov 27 17:51 ..
-rw-r--r-- 1 nino nino 7.0M Nov 27 17:51 0001.png
-rw-r--r-- 1 nino nino 8.1M Nov 27 17:51 0002.png
-rw-r--r-- 1 nino nino 8.2M Nov 27 17:51 0003.png
-rw-r--r-- 1 nino nino 5.5M Nov 27 17:51 0004.png
-rw-r--r-- 1 nino nino 5.5M Nov 27 17:51 0005.png
```
If you need to delete opening images, ending images, or some images from **frames** directory, you need to reorder the file name again. Use this command:
``` bash
cd frames
ls -v | grep '.png' | cat -n | while read new old; do mv -n "$old" `printf "%04d.png" $new`; done
```
## Setup Application and Token
First, create your apps in [Facebook Developer](https://developers.facebook.com/apps). Next, get your token at [Graph API Explorer](https://developers.facebook.com/tools/explorer). And then, extend your token expiration at [Access Token Debugger](https://developers.facebook.com/tools/debug/accesstoken/)

## Setup Bot
Ok, all frames is ready to upload. Next, ajjust some value from ``frame-in-order.py``.

Change value of ``ACCESS_TOKEN`` with your token.

To avoid your application blocked (because of spam detection), i am adding time sleep on every requests (```time.sleep(3)```) at line 49. You can change to your desired value.

In my case, for 1 Episode of Gotoubun no Hanayome, around **4GB** disk will be used for extracted frames. So, this tool will remove every frame that already uploaded to freed your disk space.

## Run Bot
After all is completed, just run Frame in Order bot with this command:
``` bash
python3 frame-in-order.py --start 1
```
And if you want to continue running again, start from frame 41.
``` bash
python3 frame-in-order.py --start 41
```
Example of output:
![Gotoubun Frames in Order](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjW3MxC4AiqoqFqFDgCykftjmWrztlZMKEslCF5trpiLSMht1_-ySZGIeJsHm7EtWdJcpVQZz-zim_ZdBmM2yavKou1h3spfEbZGLF_sBGuhLlc_vu-JXbVoeaiFSN21uJhrW9Lyw8_63XlWJsv4AP-PNMe3qlT1ZvS9QxcaguYJXVrkSgYqPSu_8TK_g/s873/framebot.png)

Default loop value is 40. But you can set loop value using --loop flag. Example:
``` bash
python3 frame-in-order.py --start 41 -loop 4
```
Above command will upload frame from 0041.png until 0045.png.

## Contact
If you have any question about this Bot, you can contact me directly on [Twitter](https://twitter.com/yuyudhn).