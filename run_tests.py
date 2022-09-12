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

from sre_constants import FAILURE, SUCCESS
from subprocess import call
from os.path import exists

import unstable_app

import unittest
import mock

import sys
import io
import datetime
import random

class TestLog(unittest.TestCase):

    def test_log_empty(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        unstable_app.print_log('')
        sys.stdout = sys.__stdout__
        self.assertEqual('\n', capturedOutput.getvalue())

    def test_log_msg(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        unstable_app.print_log('test')
        sys.stdout = sys.__stdout__
        self.assertEqual('test\n', capturedOutput.getvalue())


class TestSmallProcess(unittest.TestCase):

    def test_small_process(self):
        unstable_app.print_log = mock.MagicMock()
        self.assertEqual(0, unstable_app.small_process())

    def test_small_process_2(self): 
        unstable_app.print_log = mock.MagicMock()
        self.assertRaises(Exception, unstable_app.small_process_2)

    def test_medium_process(self):
        unstable_app.print_log = mock.MagicMock()
        unstable_app.print_error = mock.MagicMock()
        self.assertEqual(1, unstable_app.medium_process())

    def test_dump_process(self):
        unstable_app.print_log = mock.MagicMock()
        unstable_app.print_error = mock.MagicMock()
        self.assertEqual(1, unstable_app.dump_process())

    def test_unsure_process_even(self):
        unstable_app.print_log = mock.MagicMock()
        datetime_mock = mock.MagicMock(wrap=datetime.datetime)
        datetime_mock.now.return_value = datetime.datetime(2020, 3, 11, 0, 0, 0)

        random.randrange = mock.MagicMock(return_value=1)
        self.assertEqual(1, unstable_app.unsure_process())

    def test_unsure_process_odd(self):
        unstable_app.print_log = mock.MagicMock()
        datetime_mock = mock.MagicMock(wrap=datetime.datetime)
        datetime_mock.now.return_value = datetime.datetime(2020, 3, 11, 0, 0, 1)

        random.randrange = mock.MagicMock(return_value=1)
        self.assertEqual(1, unstable_app.unsure_process())

    def test_unsure_process_2(self):
        unstable_app.print_log = mock.MagicMock()
        unstable_app.print_error = mock.MagicMock()
        self.assertEqual(0, unstable_app.unsure_process_2())
        

if __name__ == '__main__':
    
    print('This script will test unstable_app.py and the native C++ application.')

    print("\n[NATIVE] app tests : ")

    tests_failure = False

    if (not exists("./NERD-test")):
        print("There is a build issue, please contact the administrator.")
        exit(FAILURE)

    if (call("./NERD-test") == 0):
        print("Native application tests failure.")
        tests_failure = True

    print("\n[PYTHON] app tests : ")
    unittest.main()

    if (tests_failure):
        exit(FAILURE)
    else:
        exit(SUCCESS)
    