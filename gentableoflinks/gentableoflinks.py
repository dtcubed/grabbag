#!/usr/bin/python
#############################################################################
####################### SOF #################################################
#############################################################################
import json

from sys import argv
from time import sleep, time

def main():
    debug_messages = False 
    debug_dtcubed = True

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

    number_of_rows = number_of_links / links_per_row
    
    if (number_of_links % links_per_row) != 0:
        number_of_rows += 1
        
    if debug_dtcubed:
        print "Total Number of Links:", number_of_links
        print "Links per row:", links_per_row
        print "Number of rows:", number_of_rows 
    
    #####
    # Print out the input value.
    #####
    if debug_messages:
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
    output_file.write("<head>\n")
    output_file.write("%s%s%s" % ("<title>\n", title, "\n</title>\n"))
    output_file.write("</head>\n")
    output_file.write("<body>\n")
    output_file.write("%s%s%s" % ("<h3>\n", h3_text, "\n</h3>\n"))
    output_file.write("<table border=\"1\">\n")
    row_counter = 0
    total_link_counter = 0 
    while row_counter < number_of_rows:
        output_file.write("<tr>\n")
        link_counter = 0
        while link_counter < links_per_row and total_link_counter < number_of_links:
            output_file.write("%s\"%s\">" % ("<td><a href=", link_list[total_link_counter]['href']))
            output_file.write("%s%s" % (link_list[total_link_counter]['label'], "</a></td>\n"))
            link_counter += 1
            total_link_counter += 1
        output_file.write("</tr>\n")
        row_counter += 1
    output_file.write("</table>\n")
    output_file.write("</body>\n")
    output_file.write("</html>\n")
    output_file.close()

if __name__ == '__main__':
    main()

#############################################################################
####################### EOF #################################################
#############################################################################
