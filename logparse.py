#! -*- coding: utf-8 -*-
#
# Tiny Skype debug log parser.
# Created by aki in about half an hour, at the request of bn0x.
#
# ---------------------------------------------------------------------------------
# "THE BEER-WARE LICENSE" (Revision 43.5):
# @__akiaki wrote this file. As long as you retain this notice you can do whatever
# you want with this stuff. If we meet some day, and you think this stuff is worth
# it, you can buy me a beer (or caffeinated beverage) in return. --aki
# ---------------------------------------------------------------------------------

"""
Usage:

    >>> import logparse
    >>> for i in logparse.search("skype.log", "username"):
    ...     print "Public: %s, Local: %s" % (i['public'], i['local'])
    ...

    "Public: 8.56.212.72:41323, Local: 192.168.1.1:41323"

"""

import re
import codecs


def _parseline(line, username=None):
    try:
        if not (re.search('PresenceManager:', line) and re.search('noticing', line)):
            return None

        if username != None and not re.search(username, line):
            return None

        l = re.findall("(\d+\.\d+\.\d+\.\d+)\:(\d+)?", line)
        
        top = 1
        if len(l) is 2:
            top = 0
            
        public = l[top][0] + ":" + l[top][1][:5 if len(l[top][1]) > 5 else len(l[top][1])]
        local = l[top + 1][0] + ":" + l[top + 1][1][:5 if len(l[top + 1][1]) > 5 else len(l[top + 1][1])]
        
        return {'public': public.encode('utf-8'), 'local': local.encode('utf-8')}

    except:
        return None

def search(file, username=None):
    """
    Search the Skype log file `file` for IPs.
    Matches against the Skype name `username` if given.

    Returns a list of dictionaries, with the keys 'public' and
    'local' which are in the format ``aaa.bbb.ccc.ddd:xxxxx``.
    """

    buf = []    
    
    f = codecs.open(file, 'r', encoding='ascii', errors='ignore').read()
    for line in f.split("\n"):
        l = _parseline(line.strip(), username)
        if l != None:
            buf.append(l)

    t = []
    for b in buf:
        if not b in t:
            t.append(b)

    return t
