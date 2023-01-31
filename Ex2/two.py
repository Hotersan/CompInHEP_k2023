import re

#the file is opened and the summary is located
with open('brilcalc.log', "r") as fo:
    content_as_string = fo.read()
    match = re.search('Summary', content_as_string)
finn=content_as_string[match.span()[0]:]

#The column is located
match = re.search('totrecorded', finn)
cont=0
for i in finn[:match.span()[1]]:
    if i=='|':
        cont+=1

#The row of the data is located
match = re.search('\| [0-9]', finn)
ro=match.span()[0]
finn2=finn[ro:]
pp=0
ii=0
while pp<cont:
    if finn2[ii]=='|':
        pp+=1
    ii+=1
lum=''
for i in finn2[ii:]:
#    print(i)
    if i!=' ':
        if i=='|':
            break
        lum = lum + i
lum = float(lum)
print('luminosity in fb-1',round(lum/1000,1))

