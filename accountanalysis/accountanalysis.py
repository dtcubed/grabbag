#!/usr/bin/python
#############################################################################
#  The MIT License
#  
#  Copyright (c) 2011 dtcubed 
#  
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#  
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#  
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#  THE SOFTWARE.
#############################################################################
import argparse
import csv
import datetime
import os
import time

from sys import argv, exit

#############################################################################
# def calc_future_value()
#
# Where: present_value   - otherwise known as "Principal"
#        asir            - Annual simple interest rate (expressed as decimal)
#        start_datestamp - expressed in the form YYYYMMDD
#        end_datestamp   - expressed in the form YYYYMMDD
#
# The start_datestamp and end_datestamp will be used to calculate 
# "tiy" (Time in years).  Then, future_value = present_value(1 + (asir * tiy))
#
#############################################################################
def calc_future_value(present_value, asir, start_datestamp, end_datestamp, debugging=False):
    #####
    # Convert the datestamps into their respective struct time. If these 
    # actions don't cause an exception to be thrown, these datestamps 
    # represent valid days on the calendar. 
    #
    # Below, we are going to use the following abreviations for conciseness:
    # sst - start struct time
    # est - end struct time
    #####
    sst = time.strptime(start_datestamp, '%Y%m%d')
    est = time.strptime(end_datestamp, '%Y%m%d')

    start_datetime = datetime.date(sst.tm_year, sst.tm_mon, sst.tm_mday) 
    end_datetime = datetime.date(est.tm_year, est.tm_mon, est.tm_mday)
    time_delta = end_datetime - start_datetime

    if debugging:
        print "End Datestamp: [", end_datestamp, "] Start Datestamp:[", start_datestamp, "]"
        print "Difference In Days: [", time_delta.days, "]"

#############################################################################
def main():
    parser = argparse.ArgumentParser(description='Analyze An Account For Overall Rate Of Return.')
    parser.add_argument('--debug', dest='debug', default=0, type=int, choices=[0, 1])
    parser.add_argument('--deposits', dest='deposits_input_file', type=file, required=True)
    parser.add_argument('--end_date', dest='end_date', required=True)
    parser.add_argument('--interest_rate', dest='interest_rate', type=float, required=True)
    parser.add_argument('--withdrawals', dest='withdrawals_input_file', type=file, required=False)
    args = parser.parse_args()

    #transactionReader = csv.reader(open(transactions_file, 'rb'))
    transactionReader = csv.reader(args.deposits_input_file)

    #####
    # Each row is really a list of strings as parsed by the csv reader.
    #####
    for transaction in transactionReader:
        #calc_future_value(transaction[1], 0.04, transaction[0], '20110402', debugging=True)
        calc_future_value(transaction[1], 0.04, transaction[0], '198diff = datetime.date(year1, month1, day1) - datetime.date(year2, month2, day2)00402', debugging=True)

#############################################################################
if __name__ == '__main__':
    main()

#############################################################################
#############################################################################
#############################################################################
