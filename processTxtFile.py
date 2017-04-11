import re
import json
import argparse
import sys

def runParser():
    parser = argparse.ArgumentParser(description='Enter a text file that has been processed by tesseract. Accepts line by line of reuters news headlines')
    parser.add_argument('--txtfile', dest='file', help="You must enter a txt file to be processed. eg: txtfile = tesseract image1.png file.txt -l eng -psm 6" )
    # parser.add_argument('--h', help="You must enter a txt file to be processed. eg: txtfile = tesseract image1.png file.txt -l eng -psm 6" )
    a1 = vars(parser.parse_args())
    if not any(a1.values()):
        print(parser.description)
        print(parser.print_help())
        sys.exit()
    else:
        args = parser.parse_args()
        return args

def parseFile(txtfile):
    with open(txtfile, encoding='utf-8') as f:
        content = f.readlines()
    processedContent = filter(lambda x: x != '\n', content)
    for x in list(processedContent):
        results = re.split(r'(\d\d:\d\d:\d\d\sPM|\d\d:\d\d:\d\d\sAM)', x)
        res1 = list(results[0].strip().split(" ")) + results[1:-1]
        res1.append(results[-1].strip())
        if len(res1) == 3:
            obj = {u"Source": res1[0], u"Time":res1[1], u"Headline":res1[2]} 
            print(obj)
            # print(json.dumps(obj, indent=4))
        elif len(res1) == 4:
            obj = {u"Source": res1[0],u"RIC":res1[1], u"Time":res1[2], u"Headline":res1[3]} 
            print(obj)
            # print(json.dumps(obj, indent=4))
        else:
            continue


if __name__ == "__main__":
    file =  runParser().file
    parseFile(file)
