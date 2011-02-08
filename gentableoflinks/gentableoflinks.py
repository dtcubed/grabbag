#!/usr/bin/python
#############################################################################
####################### SOF #################################################
#############################################################################
import json

from decimal import *
from sys import argv
from time import sleep, time

debug_messages = True 

#####
# Open the JSON config file passed in as the 1st argument. Read the contents into
# a Python dictionary object named "config".
#####
with open(argv[1]) as config_file:
    config = json.load(config_file)
    if debug_messages:
        print config['h3_text']
        print config['links_per_row']
        print config['title']
        print config['link'][0]['href']
        print config['link'][0]['label']

h3_text = config['h3_text']
links_per_row = config['links_per_row']
link_list = config['link']
title = config['title']

#####
# Determine the number of links by the length of the list.
#####
number_of_links = len(link_list)

#####
# Print out the input value.
#####
print "---------------------------------------------------------------"
print "------------------ Input via JSON File ------------------------"
print "---------------------------------------------------------------"
print "H3 Text:", h3_text
print "Links per row:", links_per_row
print "Title:", title
print "Total Number of Links:", number_of_links

link_index = 0
while link_index < number_of_links:
    print "Link: [", link_index, "] Label: [", link_list[link_index]['label'], "] Href: [", link_list[link_index]['href'], "]"
    link_index += 1

print "---------------------------------------------------------------"
print "---------------------------------------------------------------"
print "---------------------------------------------------------------"
#############################################################################
####################### EOF #################################################
#############################################################################
