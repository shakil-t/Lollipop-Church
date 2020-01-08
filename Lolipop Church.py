# -*- coding: utf-8 -*-
"""
Created on Mon May 20 18:29:04 2019

@author: shakil
"""

from symbol_table import *
from ll1_parsing_table import *
from lalr1_parsing_table import *

def is_float(token):
  try:
    number=float(token)
  except ValueError:
    return False
  return True

def is_int(token):
  try:
    number=int(token)
  except ValueError:
    return False
  return True

def seperating_numbers(number, file):
    for char in number:
        if char.isdigit():
         file.write("7\n")
        else:
            temp=char+"\n"
            file.write(temp)

def lexical_analyzer(program_file_name, tokens_file_name):
    #opening the program file
    program_file=open(program_file_name, "r")
    read_to_scan=program_file.read()
    program=read_to_scan.split("\n")
    line=0
    next_line=False
    multiline_comment=False
    #opening the tokens file
    tokens_file=open(tokens_file_name, "w")
    while(line<len(program)):
        tokens=program[line].split()
        #print(tokens)
        if multiline_comment and tokens[len(tokens)-1]=="\"":
            tokens_file.write("\"\n")
            multiline_comment=False
        elif multiline_comment:
            next_line=True
            line+=1
        else:
            for token in tokens:
                if token in blocks:
                    if token=="\"":
                        temp=token+"\n"
                        tokens_file.write(temp)
                        multiline_comment=True
                        next_line=True
                        line+=1
                        break
                    elif token==":":
                        temp=token+"\n"
                        tokens_file.write(temp)
                        next_line=True
                        line+=1
                        break
                    temp=token+"\n"
                    tokens_file.write(temp)
                if token in comment:
                    temp=token+"\n"
                    tokens_file.write(temp)
                if token in delimiter:
                    temp=token+"\n"
                    tokens_file.write(temp)
                if token in function:
                    if token in arithmetic:
                        tokens_file.write("Kievskaya\n")
                    elif token in logic:
                        tokens_file.write("Gum\n")
                    else:
                        temp=token+"\n"
                        tokens_file.write(temp)     
                if token in keyword:
                    temp=token+"\n"
                    tokens_file.write(temp)
                if token in data_type:
                    temp=token+"\n"
                    tokens_file.write(temp)
                if token not in reserved:
                    if is_int(token):
                        seperating_numbers(token, tokens_file)
                    elif is_float(token):
                        seperating_numbers(token, tokens_file)
                    elif len(token)>1 and ord(token[0])==39 and ord(token[len(token)-1])==39:
                        tokens_file.write("'\n")
                        tokens_file.write("'\n")
                    elif len(token)>=1 and ord(token[0])>96 and ord(token[0])<123:
                        tokens_file.write("k\n")
                    else:
                        #You can print errors here
                        #print("Error")
                        pass
        if not next_line:
            line+=1
        next_line=False
    
    if multiline_comment:
        #The comment block must end if not you can notice that here
        pass
    tokens_file.write("*\n")
    tokens_file.close()
    program_file.close()

def ll1_parser(tokens_file, start_symbol):
    acceptable=True
    temp=open(tokens_file, "r")
    read_tokens=temp.read()
    tokens=read_tokens.split("\n")
    stack=[]
    stack.append("*")
    stack.append(start_symbol)
    index=0
    while len(stack)>0:
        top=stack[len(stack)-1]
        current_token=tokens[index]
        if top==current_token:
            stack.pop()
            index+=1
        else:	
            if top not in ll1_parsing_table:
                acceptable=False
                #You can find the problem here
                #print(top, current_token)
                break
            command=ll1_parsing_table[top][current_token]
            if command!="empty":
                commands=command.split()
                commands.reverse()
                stack.pop()
                #termiable=terminal + variable
                for termiable in commands:
                    if termiable!="epsilon":
                        stack.append(termiable)
            else:
                stack.pop()
    if acceptable:
        print("Accepted")
    else:
        print("Not Accepted")
    
    temp.close()

def shift(stack, current_token, next_state):
    stack.append(current_token)
    stack.append(next_state)
                
def reduce(stack, production_num):
    #print("production num", production_num)
    left=grammer[production_num][0]
    #print(left)
    right=grammer[production_num][1]
    #print(right)
    right=right.split()
    right.reverse()
    if right!="epsilon":
        #termiable=terminal + variable
        for termiable in right:
            #print("termiable", termiable)
            for i in range(len(stack)-2, -1, -1):
                if stack[i]==termiable:
                    del stack[i+1]
                    del stack[i]
                    break
    stack.append(left)

def goto(stack):
    stack.append(int(lalr1_parsing_table[stack[len(stack)-2]][stack[len(stack)-1]]))

def lalr1_parser(tokens_file, start_Symbol):
    acceptable=True
    temp=open(tokens_file, "r")
    read_tokens=temp.read()
    tokens=read_tokens.split("\n")
    stack=[]
    stack.append(start_Symbol)
    index=0
    while acceptable:
        top=stack[len(stack)-1]
        #print("top", top)
        current_token=tokens[index]
        #print("current token", current_token)
        command=lalr1_parsing_table[int(top)][current_token]
        #print("command", command)
        if command!="empty":
            if command[0]=="s":
                next_state=int(command[1:])
                #print("next state", next_state)
                shift(stack, current_token, next_state)
                index+=1
            elif command[0]=="r":
                production_num=int(command[1:])
                reduce(stack, production_num)
                #print(lr1_parsing_table[stack[len(stack)-2]][stack[len(stack)-1]])
                if lalr1_parsing_table[stack[len(stack)-2]][stack[len(stack)-1]]!="empty":
                    goto(stack)
                else:
                    acceptable=False
            elif command=="Accept":
                break
        else:
            acceptable=False
    if acceptable:
        print("Accepted")
    else:
        print("Not Accepted")
    
    temp.close()

program_file_name="LC1.txt"
tokens_file_name="Tokens.txt"
lexical_analyzer(program_file_name, tokens_file_name)
#ll1_parser(tokens_file_name, "Statement")
lr1_parser(tokens_file_name, 0)