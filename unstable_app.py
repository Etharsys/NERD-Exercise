#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# /*-----------------------------------------------------------------------*
# Project: Support Recruitment Test

# Copyright (C) 2022 Nintendo, All rights reserved.

# These coded instructions, statements, and computer programs contain proprietary
# information of Nintendo and/or its licensed developers and are protected by
# national and international copyright laws. They may not be disclosed to third
# parties or copied or duplicated in any form, in whole or in part, without the
# prior written consent of Nintendo.

# The content herein is highly confidential and should be handled accordingly.
# *-----------------------------------------------------------------------*/

import sys
import argparse
import time
import datetime
import random

def print_log(msg):
    sys.stdout.write(str(msg) + '\n')
    sys.stdout.flush()

def print_error(msg):
    sys.stderr.write(str(msg) + '\n')

def small_process():
    print_log('Start running a small process...')
    for index in range(0, 5):
        print_log('Processing ['+str(index)+'] and some very important information ' + str(datetime.datetime.now()))
        time.sleep(random.randrange(1, 3))  
    return 0

def small_process_2():
    print_log('Start running another small process...')
    for index in range(0, 5):
        print_log('Processing ['+str(index)+'] and some very important information ' + str(datetime.datetime.now()))
        time.sleep(random.randrange(1, 3))
        if index == 2:
            raise Exception('Ouch !')
    return 0

def medium_process():
    print_log('Start running a kind of complicated process...')
    for index in range(0, 5):
        print_log('Processing ['+str(index)+'] and some very important information ' + str(datetime.datetime.now()))
        if index == 4:
            print_error('Invalid instruction! Help me!')
            return 1        
        time.sleep(random.randrange(1, 3))    
    return 0
    
def big_process():
    print_log('Start running a very big process...')    
    for index in range(0, 6):
        print_log('Processing ['+str(index)+'] and some very important information ' + str(datetime.datetime.now()))
        if index == 5:
            while True:
                time.sleep(random.randrange(3, 10))
                msg=['Trying very hard!', 'Some spam message!', 'Another try...', 'It will work', 'Crossing fingers.']
                print_log(msg[random.randrange(0, 5)])
        time.sleep(random.randrange(1, 3))
    return 0

def dump_process():
    print_log('Start running a dump process...')
    dump=[]
    for index in range(100):
        dump.append('        ' + ''.join(chr(random.randint(97, 121)) for i in range(72)))
    for index in range(0, 6):
        print_log('Processing ['+str(index)+'] and dumping some verbose info ' + str(datetime.datetime.now()))
        time.sleep(random.randrange(1, 3))
        for x in range(200):
            if index == 5 and x > 186:
                print_error('Invalid data!')
                return 1
            print_log('    Dumping [{:0>3}/200]'.format(x+1))
            msg = ''
            for y in range(150):
                msg += dump[random.randrange(0, 99)] + '\n'
            print_log(msg)
    return 0

def unsure_process():
    print_log('Start running an unsure process...')
    for index in range(0, 2):
        print_log('Processing ['+str(index)+'] and some very important information ' + str(datetime.datetime.now()))
        time.sleep(random.randrange(1, 3))
    if datetime.datetime.now().second % 2:
        return random.randrange(2, 127)
    else:
        return random.randrange(-127,-2)

def unsure_process_2():
    print_log('Start running another unsure process...')
    for index in range(0, 5):
        print_log('Processing ['+str(index)+'] and some very important information ' + str(datetime.datetime.now()))
        time.sleep(random.randrange(1, 3))
        if index == 2:
            print_error('Error: Invalid instruction!')
    return 0
    
if __name__ == '__main__':

    func = [
        small_process,
        small_process_2,
        medium_process,
        big_process,
        dump_process,
        unsure_process,
        unsure_process_2
    ]

    cmd_usage = 'Usage : unstable_app.py [options]\n\nPlease type unstable_app.py --help for help.'
    cmd_parser = argparse.ArgumentParser(cmd_usage)
    cmd_parser.add_argument('-p', '--process', action='store', dest='process_number', help='Process to run in [1-'+str(len(func))+']', default=1)
    cmd_options = cmd_parser.parse_args()
    
    return_code = 0
    
    func_index = int(cmd_options.process_number) - 1
    if func_index in range(len(func)):
        return_code = func[func_index]()
    else:
        sys.exit('Error: invalid process!')

    sys.exit(return_code)
