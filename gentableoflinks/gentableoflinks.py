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
import json
import os

from sys import argv, exit

def main():
    #####
    # Open the JSON config file passed in as the 1st argument and read the contents
    # into a Python dictionary object named "config".
    #####
    config_file = file(argv[1], 'r')
    config = json.load(config_file)
    config_file.close()

    #####
    # Ensure that the output file passed in as the 2nd argument does not already exist. 
    # If it does exist, exit because we will not overwrite files in this script.
    #####
    output_file_name = argv[2]
    if os.path.exists(output_file_name):
        print "\nOutput file: [", output_file_name, "] exists and we will not overwrite. Exiting.\n" 
        exit()

    #####
    # Given the structure of the link information, the default Python sort seems to 
    # work out fine for our purposes here. It sorts the list (ascending) according 
    # to the collating sequence of the information stored in "a_label". 
    #
    # Also, pull the other stuff we need from the config dictionary object too.
    #####
    link_list = sorted(config['link'])
    h3_text = config['h3_text']
    links_per_row = config['links_per_row']
    title = config['title']
    
    #####
    # Determine the number of links by the length of the list.
    #####
    number_of_links = len(link_list)

    #####
    # Determine the number of rows our table will have. Account for partial rows too. 
    #####
    number_of_rows = number_of_links / links_per_row
    
    if (number_of_links % links_per_row) != 0:
        number_of_rows += 1
        
    #####
    # Now, take care of the output file. We already checked that we are not overwriting
    # anything earlier in the script.
    #####
    output_file = file(output_file_name, 'w')
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
            output_file.write("%s%s" % (link_list[total_link_counter]['a_label'], "</a></td>\n"))
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
#############################################################################
#############################################################################
