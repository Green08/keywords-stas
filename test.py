
import os
import sys
import re


files = os.listdir('.')
for filename in files:
	portion = os.path.splitext(filename)
	if portion[1] == ".cpp" or portion[1] == ".c":
		
		newname = "test" + ".txt"
		os.rename(filename,newname)

PY_PATTERN = re.compile(

	r"""

     \s*\#(?:[^\r\n])*

     | \s*__(?:[^\r\n]*)

     | "{3}(?:\\.|[^\\])*"{3}

     | '{3}(?:\\.|[^\\])*'{3}

     """,

	re.VERBOSE | re.MULTILINE | re.DOTALL

)

txt = open("test.txt").readlines()

b = re.sub(PY_PATTERN, '', ''.join(txt))

single = re.compile(r"\n\n")

b = re.sub(single, '\n', b)

#print(b)

def keywords_num (code):
    count = {}
    Key_sum = 0
    key_list = ['auto','break','case','char','const','continue','default','do','if','while','static','double','else','enum','extern','float','for','goto','int','long','register','return','short','signed','sizeof','struct','switch','typedef','union','unsigned','void','volatile']
    for key in key_list:
        n = len(re.findall("[^0-9a-zA-Z\_]" + key + "[^0-9a-zA-Z\_]", code))
        if n != 0:
            count[key] = n
            Key_sum += n
    print('The total num is: ',Key_sum)
    #return Key_sum

def switch_num(code):
    case_num = []
    switch_num = 0
    switch_list = re.finditer(r"\sswitch\([^)]*\)\s*{",code)
    for i in switch_list:
        switch_num += 1
        index = i.end()
        case_list = re.findall(r"\scase\s",code[index:])
        case_num.append(len(case_list))
    for j in range(switch_num-1):
        case_num[j] = case_num[j]-case_num[j+1]
    print ('The swith num is: ',switch_num)
    print('The case num is',case_num)
    #return switch_num, case_num
    

def if_elseif_else_num(text):
    pattern_out = r'[\w](else if|if|else)[\w]'
    pattern_key = r'(else if|if|else)'
 
    text = re.sub(pattern_out, ' ', text, flags=re.MULTILINE)
    key_data = re.findall(pattern_key, text)
 

    pattern_front_space = r'\n( *)(?=if|else if|else)'
    space_data = re.findall(pattern_front_space, text)
    space_data = [len(i) for i in space_data]

    stack = []
    if_else_num = 0
    if_elseif_else_num = 0
    for index, values in enumerate(key_data):
        while len(stack) > 0:
            if space_data[index] < space_data[stack[len(stack) - 1]]:
                stack.pop()
            else:
                break
        if values == 'if':
            stack.append(index)
        elif values == 'else if':
            if len(stack) == 0:
                continue
            if key_data[stack[len(stack) - 1]] == 'if':
                stack.append(index)
        else:
            if len(stack) == 0:
                continue
            if key_data[stack[len(stack) - 1]] == 'if':
                if_else_num += 1
                stack.pop()
            else:
                while len(stack) > 0:
                    if key_data[stack[len(stack) - 1]] == 'else if':
                        stack.pop()
                    else:
                        break
                stack.pop()
                if_elseif_else_num += 1
    print('The if_elseif_else num is',if_elseif_else_num)
    #return if_else_num, if_elseif_else_num
 
#switch_num(b)
#if_elseif_else_num(b)
#print('The total num is: ',keywords_num (b))
#print ('The swith num is: ',switch_num)
#print('The case num is')
#print('The if_elseif_else num is',if_elseif_else_num)
keywords_num (b)
switch_num(b)
if_elseif_else_num(b)