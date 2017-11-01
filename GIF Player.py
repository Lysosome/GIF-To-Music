from PIL import Image
from PIL import ImageShow

im = Image.open("dancing mr krabs.gif")
im.show();
frameNum = 0;

for elem in ImageShow._viewers:
    print (elem);

# To iterate through the entire gif
try:
    while 1:
        im.seek(im.tell()+1)
        print("frame is "+str(frameNum))
        #im.show();
        frameNum+=1;
        # do something to im
except EOFError:
    pass # end of sequence