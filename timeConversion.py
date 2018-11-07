hr12 = "01:05:45AM" #12hr time in format 00:00:00AM
hr24 = ""

h = int(hr12[0:2])
m = int(hr12[3:5])
s = int(hr12[6:8])
tm = hr12[8:10]

if(h==12 and tm=='PM'):
    hr24 = str(format(h,"02"))+':'+str(format(m,"02"))+':'+str(format(s,"02"))
elif(h==12 and tm=='AM'):
    hr24 = str(format(00,"02"))+':'+str(format(m,"02"))+':'+str(format(s,"02"))
elif(tm=='AM'):
    hr24 = str(format(h,"02"))+':'+str(format(m,"02"))+':'+str(format(s,"02"))
elif(tm=='PM'):
    hr24 = str(format(h+12,"02"))+':'+str(format(m,"02"))+':'+str(format(s,"02"))
else:
    hr24="error"
  
print(hr24)
