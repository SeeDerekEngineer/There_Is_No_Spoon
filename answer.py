import sys
import math

# Don't let the machines win. You are humanity's last hope...

width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis
record = []
lines = []
answer = ""
answers = []
for i in range(height):
    line = input()  # width characters, each either 0 or .
    lines.append(line)
#print (lines, height, width)
for i in range(height):
    for j in range(len(line)):
        answer = ''
        #print(lines[j][i])
        if(lines[i][j] == '0'):
            answer =str(str(j) + ' ' + str(i) + ' ')
           # print (answer)
            for k in range(j, len(line)):
                try:
                    if lines[i][k+1] == '0':
                        answer += str(k+1) + ' ' + str(i) + ' '
                        break

                except:
                    answer += '-1 -1 '
            for k in range(i, height):
                try:
                    if lines[k+1][j] == '0':
                        answer += str(j) + ' ' + str(k+1) + ' '
                        break
                    
                except:
                    answer += '-1 -1 '
                    
            answers.append(answer)
for ans in answers:
    print(ans)
        
