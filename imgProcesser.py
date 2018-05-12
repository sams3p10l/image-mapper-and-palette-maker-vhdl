from PIL import Image

inputImg = input("Image for processing: (or path to it)\n")

image = Image.open(inputImg)
image = image.convert('RGB')
pixel = image.load()

pixelTuples = []
pixelList = []
output = ""

outputFilename = inputImg[:-4] + '_out.txt'

f = open(outputFilename, 'w')

for x_pos in range(image.size[0]):
    for y_pos in range(image.size[1]):
        pixelTuples.append(pixel[x_pos, y_pos])

for i in range(len(pixelTuples)):
    pixelList.append(list(pixelTuples[i]))      #RGBA

cnt = 0

for i in range(len(pixelList)):
    pixelList[i].reverse()                      #ABGR
    for j in range(len(pixelList[i])):
        if(cnt == 0):
            output += str(i) + " => " + 'x"'

        pixelList[i][j] = format(pixelList[i][j], '02x')
        output += str(pixelList[i][j]).upper()
        
        cnt += 1

        if cnt == 4 and i != len(pixelList) - 1:
            output += '",\n'
            cnt = 0

output += '"'
f.write(output)
f.close()

print("Generated output " + outputFilename + " successfully")
   