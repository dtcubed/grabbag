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
import os
import time

from sys import argv, exit

#############################################################################
def main():
    parser = argparse.ArgumentParser(description='Analyze An Account For Overall Rate Of Return.')
    parser.add_argument('--debug', dest='debug', default=0, type=int, choices=[0, 1])
    parser.add_argument('--deposits', dest='deposits_input_file', type=file, required=True)
    parser.add_argument('--end_date', dest='end_date', required=True)
    parser.add_argument('--interest_rate', dest='interest_rate', type=float, required=True)
    parser.add_argument('--withdrawals', dest='withdrawals_input_file', type=file, required=False)
    args = parser.parse_args()

    if args.debug:
        print "Debugging is TRUE"
    else:
        print "Debugging is FALSE"

    #transactionReader = csv.reader(open(transactions_file, 'rb'))
    transactionReader = csv.reader(args.deposits_input_file)

    #####
    # Each row is really a list of strings as parsed by the csv reader.
    #####
    for transaction in transactionReader:
        print "Date: [", transaction[0], "] Amount: [", transaction[1], "]"
        print "Returned: [", time.strptime(transaction[0], '%Y%m%d'), "]"

#############################################################################
if __name__ == '__main__':
    main()

#############################################################################
#############################################################################
#############################################################################
