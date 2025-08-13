#!/usr/bin/env python3

import sys
import re
fileToParse = sys.argv[1]
with open(fileToParse, 'r') as fp:
    lines = fp.readlines()
# note - readlines returns an array of newline-terminated strings. remove them:
for i in range(0,len(lines)):
    if lines[i].endswith('\n'):
        lines[i] = lines[i][0:-1]
        
if not lines[0].startswith('SIMPLE_MACRO_DEFS'):
    # do nothing
    outlines = lines
else:
    lineptr=1
    macro_defs = {}
    # parse macro defs:
    while 1:
        if lines[lineptr].startswith('END_SIMPLE_MACRO_DEFS'):
            lineptr += 1
            break
        #lineptr+=1
        if lines[lineptr].startswith('#'): 
            lineptr += 1
            continue # comment
        if len(lines[lineptr]) == 0: 
            lineptr += 1
            continue # blank line
        # macro definition:
        assert lines[lineptr].count('=')
        idx = lines[lineptr].index('=')
        macro_name = lines[lineptr][0:idx]
        assert lines[lineptr][idx+1] == '"'
        colptr = idx+2 # the start of the macro text
        macro_text = ''
        while 1:
            if lines[lineptr][colptr] == '"' and lines[lineptr][colptr + 1] == ';':
                lineptr += 1
                break
            elif lines[lineptr][colptr] == '\\' and lines[lineptr][colptr + 1] == '"':
                macro_text += '"'
                colptr += 2
            else:
                macro_text += lines[lineptr][colptr]
                colptr += 1
                if colptr >= len(lines[lineptr]):
                    # multi-line macro definition
                    macro_text += '\n'
                    colptr = 0
                    lineptr += 1
        macro_defs[macro_name] = macro_text
    # parse the rest of the file:
    outlines = []
    while lineptr < len(lines):
        if not lines[lineptr].count('$('):
            outlines.append(lines[lineptr])
            lineptr += 1; continue
        # test line for each macro:
        outline = lines[lineptr]
        for macro_name in macro_defs:
            tag = '$(' + macro_name + ')'
            if outline.count(tag):
                outline = outline.replace(tag, macro_defs[macro_name])
        outlines.append(outline)
        lineptr += 1

print('\n'.join(outlines))
