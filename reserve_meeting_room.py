# encoding=utf8
import argparse
import requests
import sys

parser = argparse.ArgumentParser()
parser.add_argument('--username', type=str, default='r07922009', help='username')
parser.add_argument('--password', type=str, help='password', required=True)
parser.add_argument('--date', type=str, help='date format:2019-08-05', required=True)
parser.add_argument('--start', type=str, default='18:25', help='start time')
parser.add_argument('--end', type=str, default='22:00', help='end time')
parser.add_argument('--description', type=str, default=u'[meeting] CMLab - 吳家麟', help='description' )
parser.add_argument('--room', type=str, default=u'519研討室', help='room')
args = parser.parse_args()


if __name__ == '__main__':
    s = requests.Session()
    form_data = {
        'to': '/',
        'username': args.username,
        'password': args.password
    }
    try:
        s.post('https://esystem.csie.ntu.edu.tw/login', data=form_data)
    except requests.exceptions.HTTPError as e:
        print(e)
        sys.exit(1)
    except requests.exceptions.RequestException as e:
        print(e)
        sys.exit(1)
    form_data = {
        'room': args.room,
        'group': '57',
        'date': args.date,
        'start': args.start,
        'end': args.end,
        'description': args.description
    }
    try:
        s.post('https://esystem.csie.ntu.edu.tw/room', data=form_data)
    except requests.exceptions.HTTPError as e:
        print(e)
        sys.exit(1)
    except requests.exceptions.RequestException as e:
        print(e)
        sys.exit(1)
