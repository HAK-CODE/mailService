import argparse
import sys
import configparser
import os
import time
from mailSender import Mail
from fileManager import FileManager
from subprocess import check_output
import time
from datetime import datetime as dt



parser = argparse.ArgumentParser(prog='MAILER',
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter,
                                 description='Send mail watching the directory.')

parser.add_argument('--path', '-p', type=str, help="Specify full path to a directory.")
parser.add_argument('--time', '-t', type=int, default=10, help="Specify time frequency to watch directory.")
parser.add_argument('--maillist', '-l', type=str, help="Specify sender email list.")
parser.add_argument('--timeDiff', '-tf', type=int, default=15, help="Specify time difference threshold to trigger.")
parser.add_argument('--file', '-f', type=str, help="Specify file name.")
parser.add_argument('--screen', '-sr', type=str, help="Specify screen name.")
args = parser.parse_args()

programStart = False
emailtoDIH = False
emailtoClients = False

if args.path is None or \
        args.maillist is None or \
        args.timeDiff is None or \
        args.file is None or \
        args.screen is None:
    print('One of the parameter missing.')
    sys.exit(0)

if os.path.isdir(args.path) is not True:
    print('Directory Not exist.')
    sys.exit(0)

f = FileManager()
f.setFile(args.file)


def sendMailtoDIH():
    global emailtoDIH
    if not emailtoDIH:
        print('sending to dih')
        config = configparser.ConfigParser()
        config.read('./Config/mailList.ini')
        if config.has_section('dih.support'):
            senderList = [x[1] for x in config.items('dih.support')]
            config.clear()
            config.read('./Config/messages.ini')
            messageList = [x[1] for x in config.items('dih.support')]
            service = Mail()
            service.send_mail(messageList[0],
                              messageList[1],
                              senderList)
            f.addLine(dt.now().strftime('%a %b %d %H:%M:%S %Y'), 1)
            emailtoDIH = True
    latestTime = dt.now()
    screenTime = f.getEmailTime(screen=True)
    if (latestTime - screenTime).days > 1:
        print('screen email set again')
        f.addLine(dt.now().strftime('%a %b %d %H:%M:%S %Y'), 1)
        emailtoDIH = False


def sendMailtoClients():
    global emailtoClients
    if not emailtoClients:
        print('sending to clients')
        config = configparser.ConfigParser()
        config.read('./Config/mailList.ini')
        if config.has_section(args.maillist):
            senderList = [x[1] for x in config.items(args.maillist)]
            ccList = [x[1] for x in config.items('dih.support')]
            config.clear()
            config.read('./Config/messages.ini')
            if config.has_section(args.maillist):
                messageList = [x[1] for x in config.items(args.maillist)]
                service = Mail()
                service.send_mail(messageList[0],
                                  messageList[1],
                                  senderList,
                                  ccList)
                f.addLine(dt.now().strftime('%a %b %d %H:%M:%S %Y'), 2)
                emailtoClients = True
    latestTime = dt.now()
    dirTime = f.getEmailTime(screen=False)
    print((latestTime - dirTime).days)
    if (latestTime - dirTime).days > 1:
        print('dir email set again')
        f.addLine(dt.now().strftime('%a %b %d %H:%M:%S %Y'), 1)
        emailtoClients = False


while True:
    screenNames = check_output(["screen -ls; true"], shell=True)
    if not "." + args.screen + "\t(" in screenNames.decode('utf-8'):
        sendMailtoDIH()
    if not programStart:
        f.addLine(str(time.ctime(os.path.getctime(args.path))), 0)
        programStart = True
    else:
        f.addLine(str(time.ctime(os.path.getctime(args.path))), 0)
        dirTime = f.getDirTime()
        currTime = dt.now()
        if int(round((currTime - dirTime).total_seconds()) / 60) > args.timeDiff:
            sendMailtoClients()

    time.sleep(args.time)
