import os
import operator

inputList = []

data = ""
dataList = []
dataHist = {}

palette = [00000000]*255

inputList = os.listdir()

for i in range(len(inputList)):
    if inputList[i] == 'output.txt':
        with open(inputList[i], 'r') as myfile:
            if i != len(inputList) - 1:
                data += myfile.read().replace('"', "").replace(',', "")
                data += '\n'
            else:
                data += myfile.read().replace('"', "").replace(',', "")

dataList = data.split('\n')
dataList.remove("")

for i in range(len(dataList)):
    if len(dataList[i]) == 14:
        dataList[i] = dataList[i][6:]
    elif len(dataList[i]) == 15:
        dataList[i] = dataList[i][7:] 
    elif len(dataList[i]) == 16:
        dataList[i] = dataList[i][8:]
    else:
        dataList[i] = dataList[i][9:]

for i in range(len(dataList)):
    if dataList[i] not in dataHist:
        dataHist[dataList[i]] = 1
    else:
        dataHist[dataList[i]] += 1

sortedDataHist = sorted(dataHist.items(), key = operator.itemgetter(1), reverse = True)

if len(sortedDataHist) <= 255:
    for i in range(len(sortedDataHist)):
        palette[i] = sortedDataHist[i][0]
else:
    for i in range(255):
        palette[i] = sortedDataHist[i][0]

f = open("palette.txt", 'a+')

for i in range(len(palette)):
    paletteString = str(i) + ' => x"' + str(palette[i]) + '",\n'
    f.write(paletteString)

f.close()
print("Palette generated successfully")