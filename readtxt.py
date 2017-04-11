import re

with open('out.txt') as f:
    content = f.readlines()

processedContent = filter(lambda x: x != '\n', content)
for x in list(processedContent):
    results = re.split(r'(\d\d:\d\d:\d\d\sPM|\d\d:\d\d:\d\d\sAM)', x)
    print(results[0])
    results[0].strip()
    results1 = results[0].strip()
    res1 = results[0].split(" ") + results[1:]
    print(results)
    #print(res1)
    #if res1[1] == '':
        #res1[1] = "#NA"
    #print(res1)


    
