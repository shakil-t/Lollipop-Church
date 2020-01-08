# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 10:18:57 2019

@author: shakil
"""

terminals=["*", "k", "7", "-", ".", "»", "«", ")", "(", "VictoryPark", "AlexanderGarden",
"RedSquare", "~", "Hermitage", "PazyrykCarpet", "PeacockClock", "'", "AmberRoom", "]",
",", "[", "Gum", "Kievskaya", "PalaceBridge", "FinlandGulf", ":", "Samovar", "\"",
"Ballet"]

Statement=dict(zip(terminals, ["empty"]*len(terminals)))
Statement["*"]="epsilon"
Statement["k"]="Variable Statement"
Statement["»"]="epsilon"
Statement["VictoryPark"]="Condition Statement"
Statement["RedSquare"]="Loop Statement"
Statement["Hermitage"]="Variable Statement"
Statement["PazyrykCarpet"]="Variable Statement"
Statement["PeacockClock"]="Variable Statement"
Statement["AmberRoom"]="Variable Statement"
Statement["Gum"]="Operation Statement"
Statement["Kievskaya"]="Operation Statement"
Statement["FinlandGulf"]="Output Statement"
Statement["Samovar"]="Comment Statement"
Statement["Ballet"]="Comment Statement"

Comment=dict(zip(terminals, ["empty"]*len(terminals)))
Comment["Samovar"]="Samovar :"
Comment["Ballet"]="Ballet \" \""

Output=dict(zip(terminals, ["empty"]*len(terminals)))
Output["FinlandGulf"]=["FinlandGulf ( W3 )"]

Input=dict(zip(terminals, ["empty"]*len(terminals)))
Input["PalaceBridge"]="PalaceBridge ( )"

W3=dict(zip(terminals, ["empty"]*len(terminals)))
W3["k"]="Identifier"
W3["Gum"]="Operation"
W3["Kievskaya"]="Operation"

Operation=dict(zip(terminals, ["empty"]*len(terminals)))
Operation["Gum"]="Logic"
Operation["Kievskaya"]="Arithmetic"

Arithmetic=dict(zip(terminals, ["empty"]*len(terminals)))
Arithmetic["Kievskaya"]="Kievskaya [ W1 , W1 ]"

W1=dict(zip(terminals, ["empty"]*len(terminals)))
W1["k"]="Identifier"
W1["7"]="RealNumber"
W1["-"]="RealNumber"
W1["Kievskaya"]="Arithmetic"

Logic=dict(zip(terminals, ["empty"]*len(terminals)))
Logic["Gum"]="Gum [ W2 , W2 ]"

W2=dict(zip(terminals, ["empty"]*len(terminals)))
W2["k"]="Identifier"
W2["7"]="RealNumber"
W2["-"]="RealNumber"
W2["Gum"]="Operation"
W2["Kievskaya"]="Operation"

Variable=dict(zip(terminals, ["empty"]*len(terminals)))
Variable["k"]="Identifier ~ W4"
Variable["Hermitage"]="Array"
Variable["PazyrykCarpet"]="NonString Identifier ~ W5"
Variable["PeacockClock"]="NonString Identifier ~ W5"
Variable["AmberRoom"]="AmberRoom Identifier ~ W6"

W4=dict(zip(terminals, ["empty"]*len(terminals)))
W4["k"]="W1"
W4["7"]="W1"
W4["-"]="W1"
W4["'"]="' '"
W4["Kievskaya"]="W1"

W5=dict(zip(terminals, ["empty"]*len(terminals)))
W5["k"]="W1"
W5["7"]="W1"
W5["-"]="W1"
W5["Kievskaya"]="W1"
W5["PalaceBridge"]="Input"

W6=dict(zip(terminals, ["empty"]*len(terminals)))
W6["'"]="' '"
W6["PalaceBridge"]="Input"

W7=dict(zip(terminals, ["empty"]*len(terminals)))
W7["k"]="W2"
W7["7"]="W2"
W7["-"]="W2"
W7["Gum"]="W2"
W7["Kievskaya"]="W2"
W7["PalaceBridge"]="Input"

NonString=dict(zip(terminals, ["empty"]*len(terminals)))
NonString["PazyrykCarpet"]="PazyrykCarpet"
NonString["PeacockClock"]="PeacockClock"

Array=dict(zip(terminals, ["empty"]*len(terminals)))
Array["Hermitage"]="Hermitage Identifier ( IntNumber ) ~ W7"

Loop=dict(zip(terminals, ["empty"]*len(terminals)))
Loop["RedSquare"]="RedSquare « Statement » AlexanderGarden ( Operation )"

Condition=dict(zip(terminals, ["empty"]*len(terminals)))
Condition["VictoryPark"]="VictoryPark ( Operation ) « Statement »"

Identifier=dict(zip(terminals, ["empty"]*len(terminals)))
Identifier["k"]="Alphabet"

IntNumber=dict(zip(terminals, ["empty"]*len(terminals)))
IntNumber["7"]="Sign Part"
IntNumber["-"]="Sign Part"

RealNumber=dict(zip(terminals, ["empty"]*len(terminals)))
RealNumber["7"]="Sign FSign"
RealNumber["-"]="Sign FSign"

FSign=dict(zip(terminals, ["empty"]*len(terminals)))
FSign["7"]="Part FPart"

FPart=dict(zip(terminals, ["empty"]*len(terminals)))
FPart["*"]="epsilon"
FPart["k"]="epsilon"
FPart["."]=". Part"
FPart["»"]="epsilon"
FPart["VictoryPark"]="epsilon"
FPart["RedSquare"]="epsilon"
FPart["Hermitage"]="epsilon"
FPart["PazyrykCarpet"]="epsilon"
FPart["PeacockClock"]="epsilon"
FPart["AmberRoom"]="epsilon"
FPart["]"]="epsilon"
FPart[","]="epsilon"
FPart["Gum"]="epsilon"
FPart["Kievskaya"]="epsilon"
FPart["FinlandGulf"]="epsilon"
FPart["Samovar"]="epsilon"
FPart["Ballet"]="epsilon"

Part=dict(zip(terminals, ["empty"]*len(terminals)))
Part["7"]="Digit FDigit"

FDigit=dict(zip(terminals, ["empty"]*len(terminals)))
FDigit["*"]="epsilon"
FDigit["k"]="epsilon"
FDigit["7"]="Part"
FDigit["."]="epsilon"
FDigit["»"]="epsilon"
FDigit[")"]="epsilon"
FDigit["VictoryPark"]="epsilon"
FDigit["RedSquare"]="epsilon"
FDigit["Hermitage"]="epsilon"
FDigit["PazyrykCarpet"]="epsilon"
FDigit["PeacockClock"]="epsilon"
FDigit["AmberRoom"]="epsilon"
FDigit["]"]="epsilon"
FDigit[","]="epsilon"
FDigit["Gum"]="epsilon"
FDigit["Kievskaya"]="epsilon"
FDigit["FinlandGulf"]="epsilon"
FDigit["Samovar"]="epsilon"
FDigit["Ballet"]="epsilon"

Sign=dict(zip(terminals, ["empty"]*len(terminals)))
Sign["7"]="epsilon"
Sign["-"]="-"

Digit=dict(zip(terminals, ["empty"]*len(terminals)))
Digit["7"]="7"

Alphabet=dict(zip(terminals, ["empty"]*len(terminals)))
Alphabet["k"]="k"

ll1_parsing_table={"Statement": Statement, "Comment": Comment, "Output": Output,
"Input": Input, "W3": W3, "Operation": Operation, "Arithmetic": Arithmetic,
"W1": W1, "Logic": Logic, "W2": W2, "Variable": Variable, "W4": W4,
"W5": W5, "W6": W6, "W7": W7, "NonString": NonString, "Array": Array,
"Loop": Loop, "Condition" : Condition, "Identifier": Identifier,
"IntNumber": IntNumber, "RealNumber": RealNumber, "FSign": FSign,
"FPart": FPart, "Part": Part, "FDigit": FDigit, "Sign": Sign,
"Digit": Digit, "Alphabet": Alphabet}