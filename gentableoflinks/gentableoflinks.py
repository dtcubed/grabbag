#!/usr/bin/python
#############################################################################
####################### SOF #################################################
#############################################################################
import json

from sys import argv
from time import sleep, time

def print_html_tag_start(file_desc, text):
    file_desc.write(text)

def main():
    debug_messages = False 
    #####
    # Open the JSON config file passed in as the 1st argument and read the contents
    # into a Python dictionary object named "config".
    #####
    config_file = file(argv[1], 'r')
    config = json.load(config_file)
    config_file.close()
    if debug_messages:
        print config['h3_text']
        print config['links_per_row']
        print config['title']
        print config['link'][0]['href']
        print config['link'][0]['label']
    
    h3_text = config['h3_text']
    links_per_row = config['links_per_row']
    #####
    # Given the structure of the link information, the default Python sort seems to 
    # work out fine for our purposes here. It sorts the list (ascending) according 
    # to the collating sequence of the information stored in the "label".
    #####
    link_list = sorted(config['link'])
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

    #####
    # Take care of the output file here (for now).
    #####
    output_file = file('index.html', 'w')
    output_file.write("<html>\n")
    output_file.write("</html>\n")
    output_file.close()

if __name__ == '__main__':
    main()

#############################################################################
####################### EOF #################################################
#############################################################################
