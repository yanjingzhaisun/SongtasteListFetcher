import json

with open('whole.json','r') as f:
    data = json.load(f)
import re
import os
for i in range(0,len(data)):
    filename = "album" + str(i) + ".txt"
    outputfile = open(filename, "w")
    string = data[i]['desc']
    string = string[8:]
    string = string.replace("<script>","")
    string = string.replace("</script>","")
    string = string.replace(";",";\n")
    string = string.replace("WS","")
    string = re.sub('\(\"[0-9]+\",\"[0-9]+\",',"(",string)
    string = string.replace('\"', "")
    string = string.replace('\\',"")
    print (string, file = outputfile)
    outputfile.close()
    os.system('mv ' + filename + ' ./albums')

