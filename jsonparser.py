import json

with open('whole.json','r') as f:
    data = json.load(f)
import re
for i in range(0,len(data)):
    outputfile = open("album" + str(i) + ".txt", "w")
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
    f.close()

