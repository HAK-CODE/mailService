import argparse
import sys
import configparser
import os
import time
from mailSender import Mail

parser = argparse.ArgumentParser(prog='MAILER',
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter,
                                 description='Send mail watching the directory.')

parser.add_argument('--path', '-p', type=str, help="Specify full path to a directory.")
parser.add_argument('--time', '-t', type=int, default=10, help="Specify time frequency to watch directory.")
parser.add_argument('--maillist', '-l', type=str, help="Specify sender email list.")
args = parser.parse_args()

if args.path is None or args.maillist is None:
    print('Path and Mailist not mentioned.')
    sys.exit(0)

if os.path.isdir(args.path) is not True:
    print('Directory Not exist.')
    sys.exit(0)

#while True:
#    time.sleep(args.time)

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