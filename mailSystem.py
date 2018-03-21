import argparse
import sys
import configparser
import os
import time
from mailSender import Mail
from fileManager import FileManager

parser = argparse.ArgumentParser(prog='MAILER',
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter,
                                 description='Send mail watching the directory.')

parser.add_argument('--path', '-p', type=str, help="Specify full path to a directory.")
parser.add_argument('--time', '-t', type=int, default=10, help="Specify time frequency to watch directory.")
parser.add_argument('--maillist', '-l', type=str, help="Specify sender email list.")
parser.add_argument('--timeDiff', '-tf', type=int, default=15, help="Specify time difference threshold to trigger.")
parser.add_argument('--file', '-f', type=str, help="Specify file name.")
args = parser.parse_args()

if args.path is None or args.maillist is None or args.timeDiff is None or args.file is None:
    print('One of the parameter missing.')
    sys.exit(0)

if os.path.isdir(args.path) is not True:
    print('Directory Not exist.')
    sys.exit(0)

f = FileManager()
f.setFile(args.file)
f.addLine('hello', False)

#while True:
#    time.sleep(args.time)

'''
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
#service = Mail()
#service.send_mail('FILES', 'hello baby', ['hammad4898@gmail.com'], ['hammad.ali@inboxbiz.com'])
'''