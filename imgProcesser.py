from PIL import Image
import os

iterator = 0

fileList = []
fileList = os.listdir()

for i in range(len(fileList)):
    ext = fileList[i][-4:]
    if  ext == '.bmp' or ext == '.jpg' or ext == '.png':
        image = Image.open(fileList[i])
        image = image.convert('RGB')
        pixel = image.load()

        pixelTuples = []
        pixelList = []
        output = ""

        f = open('output.txt', 'a+')

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
                    output += str(iterator) + " => " + 'x"'
                    iterator += 1

                pixelList[i][j] = format(pixelList[i][j], '02x')
                output += str(pixelList[i][j]).upper()
                
                cnt += 1

                if cnt == 4 and i != len(pixelList) - 1:
                    output += '",\n'
                    cnt = 0

        output += '"\n'
        f.write(output)
        
f.close()
print("Output generated successfully")
   