import string 
# import one library common string operations

# function that finds and returns the mirror string based on the sum of 128
def mirror_strings(x):
    if(x!=' ' and x!='\n'):  
        point=128-ord(x)
        end_point=chr(point)
    elif (x==' '):
        end_point=' '
    elif (x=='\n'):
        end_point='\n'
    return end_point

str_nothing=""    
general=[] # list that stores the content of the file by character 
words_list=[] # list that stores the mirror strings of the file reversed
file=open("filename128.txt","r+")
data=file.read()

# the whitespace is being replaced by the whitespace and * and then when this special character  
# is found the text is being splitted in a list
words=(data.replace(' '," *")).split("*")

for i in words:
    for k in i:
        general.append(k)
for j in general:
    check=mirror_strings(j)
    words_list.append(check)
words_list.reverse() # method that reverses the content of the file in place
for l in words_list:
    str_nothing+=l
print(str_nothing)
file.close()