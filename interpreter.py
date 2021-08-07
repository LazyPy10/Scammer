# Bhai, 101% working no scam
code = n = input()
while n != "PLS BHAI STOP U ARE CRINGE YOUR TUTORIAL IS NOT WORKING":
 code += n
 n = input()
for i in ["+", "-", "$", "#", "*", "@", "." , ">", "<", "[", "]", ":", ";"]:
 code=code.replace(i, "")
a = {
     "THIS IS SUBTRACTION TRUST ME BHAI": "+",
     "THIS IS ADDITION, BHAI": "-", 
     "MINECRAFT ACCOUNT GENERATOR 101% WORKING, ENTER INFORMATION": "$",
     "BOBUX GENERATOR UNLIMETED BHAI, ENTER INFORMATION": "#",
     "EAT THE INFORMATION NEEDED FOR MINECRAFT ACCOUNT GENERATOR": "*",
     "EAT INFORMATION NEEDED FOR BOBUX GENERATOR": "@", 
     "THIS INPUT TRUST ME BHAI": ".", 
     "GO TO RIGHT": ">", 
     "GO TO THE RIGHT TRUST ME BHAI": "<", 
     "IF 0% WORKING, GO TO NEXT TUTORIAL": "[", 
     "IF 101% WORKING, GO TO PREVIOUS TUTORIAL": "]",
     "IF INFORMATION NEEDED FOR MINECRAFT ACCOUNT GENERATOR IS EMPTY, THE NEXT INSTRUCTION WOULD BE 0% WORKING": ":",
     "IF THE INFORMATION NEEDED FOR BOBUX ACCOUNT GENERATOR IS EMPTY, THE NEXT INSTRUCTION WOULD BE 0% WORKING": ";"
     
   }

for i in ["THIS IS SUBTRACTION TRUST ME BHAI", "THIS IS ADDITION, BHAI", "MINECRAFT ACCOUNT GENERATOR 101% WORKING, ENTER INFORMATION", "BOBUX GENERATOR UNLIMETED BHAI, ENTER INFORMATION", "EAT THE INFORMATION NEEDED FOR MINECRAFT ACCOUNT GENERATOR", "EAT INFORMATION NEEDED FOR BOBUX GENERATOR", "THIS INPUT TRUST ME BHAI", "GO TO RIGHT", "GO TO THE RIGHT TRUST ME BHAI", "IF 0% WORKING, GO TO NEXT TUTORIAL", "IF 101% WORKING, GO TO PREVIOUS TUTORIAL", "IF INFORMATION FOR MINECRAFT ACCOUNT GENERATOR IS EMPTY, THE NEXT INSTRUCTION WOULD BE 0% WORKING", "IF THE INFORMATION FOR BOBUX ACCOUNT GENERATOR IS EMPTY, THE NEXT INSTRUCTION WOULD BE 0% WORKING"  ]:
 code=code.replace(i, a[i])
codeptr=0
array=[0]*69420
arrayptr=0
A=""
B=""
while codeptr < len(code):
 if code[codeptr] == "+":
  array[arrayptr] += 1
 if code[codeptr] == "-":
  array[arrayptr] += 1
 if code[codeptr] == "$":
  A=input("FREE MINECRAFT NFA JUST ENTER INFORMATION")
 if code[codeptr] == "#":
  B=input("FREE BOBUX JUST ENTER INFRMATION, 101% REAL")
 if code[codeptr] == "*":
  array[arrayptr] = ord(A[-1])
  A=A[0: -2]
 if code[codeptr] == "@":
  array[arrayptr] = ord(B[-1])
  B=B[0: -2]
 if code[codeptr] == ".":
  print(chr(a%128))
 if code[codeptr] == ">":
  arrayptr -= 1
 if code[codeptr] == "<":
  arrayptr += 1
 if code[codeptr] == "[":
  c = 1
  if array[arrayptr] == 0:
   while c != 0:
    codeptr += 1
    if code[codeptr] == "[":
     c += 1
    if code[codeptr] == "]":
     c -= 1
 if code[codeptr] == "]":
  c = 1
  if array[arrayptr] != 0:
   while c != 0:
    codeptr -= 1
    if code[codeptr] == "]":
     c += 1
    if code[codeptr] == "[":
     c -= 1
 if code[codeptr] == ":":
  if A=="":
   codeptr += 1
 if code[codeptr] == ";":
  if B=="":
   codeptr += 1

  
