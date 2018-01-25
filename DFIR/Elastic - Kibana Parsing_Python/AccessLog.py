import fileinput
import re
import os
try: import simplejson as json
except ImportError: import json


def actionString (id_number):
    action_and_meta_data = {}
    content = {}
    content['_index'] = 'my_web_log'
    content['_type'] =  'my_log_line'
    content['_id'] = id_number
    action_and_meta_data['create']  = content
    return action_and_meta_data
    
#read input file and return entries' Dict Object    
def readfile(file):
    output_file = open("logs.jsonl", "w")
    index = 1
    #check necessary file size checking
    statinfo = os.stat(file)

    #just a guestimate. I believe a single entry contains atleast 150 chars
    if statinfo.st_size < 150:
        print "Not a valid access_log file. It does not have enough data"
    else:
        for line in fileinput.input(file):
            if line != "\n": #don't read newlines
            	output_file.write(json.JSONEncoder().encode(actionString(index)) + "\n")
            	output_file.write(json.JSONEncoder().encode(line2dict(line)) + "\n")
            index = index + 1

        fileinput.close()

#gets a line of string from Log and convert it into Dict Object
def line2dict(line):
    #Snippet, thanks to http://www.seehuhn.de/blog/52
    parts = [
    r'(?P<host>\S+)',                   # host %h
    r'(?P<identity>\S+)',               # indent %l (unused)
    r'(?P<user>\S+)',                   # user %u
    r'\[(?P<time>.+)\]',                # time %t
    r'"(?P<request>.+)"',               # request "%r"
    r'(?P<status>[0-9]+)',              # status %>s
    r'(?P<size>\S+)',                   # size %b (careful, can be '-')
    r'"(?P<referer>.*)"',               # referer "%{Referer}i"
    r'"(?P<user_agent>.*)"',            # user agent "%{User-agent}i"
]

    motif = {"create" : { "_index" : "log_web", "_type" : "type1", "_id" : "3" }}
    pattern = re.compile(r'\s+'.join(parts)+r'\s*\Z')
    m = pattern.match(line)
    res = m.groupdict()
    return res

def toJson(file):
    #get dict object for each entry
    readfile(file)
    
