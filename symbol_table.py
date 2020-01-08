# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 09:54:42 2019

@author: shakil
"""

blocks={"«": "Start of a Condition/Loop", "»": "End of a Condition/Loop",
"(": "Left Parantese", ")": "Right Parantese", "[": "Start of an Operation",
"]": "End of an Operation", ":": "Start of Single Line Comment",
"\"": "Start/End of Multiline Comment", "'": "Start/End of a String"}

comment={"Samovar": "Single Line Comment", "Ballet": "Multiline Comment Start"}

delimiter={"~": "Assignment", ",": "Seperator"}

#parsing problems
arithmetic={"Kievskaya": "Plus", "Matryoshka": "Division",
"ScarletSails": "Multiplication", "Novodevichy": "Minus",
"Peterhof": "Power", "MoscowRiver": "Quotient", "NevaRiver": "Remainder"}

logic={"StIsaacCatherdal":"Equals", "SpilledBlood": "Not Equal",
"Yakutsk": "Less than", "SparrowHills": "Greater than",
"Elbrus": "Greater than or Equal to", "CaspianSea": "Less than or Equal to",
"GorkyPark": "AND", "Gum": "OR"}

function={"PalaceBridge": "Input", "FinlandGulf": "Output", "Kievskaya": "Plus",
"Matryoshka": "Division", "ScarletSails": "Multiplication", "Novodevichy": "Minus",
"Peterhof": "Power", "MoscowRiver": "Quotient", "NevaRiver": "Remainder",
"StIsaacCatherdal":"Equals", "SpilledBlood": "Not Equal", "Yakutsk": "Less than",
"SparrowHills": "Greater than", "Elbrus": "Greater than or Equal to",
"CaspianSea": "Less than or Equal to", "GorkyPark": "AND", "Gum": "OR"}

keyword={"RedSquare": "Start of a Loop", "AlexanderGarden": "End of a Loop",
"VictoryPark": "Condition", "Hermitage": "Array"}

data_type={"PeacockClock": "Integer", "PazyrykCarpet": "Float", "AmberRoom": "String"}

reserved={"«": "Start of a Condition/Loop", "»": "End of a Condition/Loop",
"(": "Left Parantese", ")": "Right Parantese", "[": "Start of an Operation",
"]": "End of an Operation", ":": "Start of Single Line Comment",
"\"": "End of Multiline Comment", "'": "Start/End of a String","Samovar": "Single Line Comment",
"Ballet": "Multiline Comment Start", "~": "Assignment", ",": "Seperator",
"PalaceBridge": "Input", "FinlandGulf": "Output","Kievskaya": "Plus",
"Matryoshka": "Division", "ScarletSails": "Multiplication", "Novodevichy": "Minus",
"Peterhof": "Power", "MoscowRiver": "Quotient", "NevaRiver": "Remainder",
"StIsaacCatherdal":"Equals", "SpilledBlood": "Not Equal", "Yakutsk": "Less than",
"SparrowHills": "Greater than", "Elbrus": "Greater than or Equal to",
"CaspianSea": "Less than or Equal to", "GorkyPark": "AND", "Gum": "OR",
"RedSquare": "Start of a Loop", "AlexanderGarden": "End of a Loop",
"VictoryPark": "Condition", "Hermitage": "Array", "PeacockClock": "Integer",
"PazyrykCarpet": "Float", "AmberRoom": "String"}