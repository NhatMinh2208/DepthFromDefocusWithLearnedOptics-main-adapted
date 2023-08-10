import numpy as np
import OpenEXR, Imath, array

def ReadExr_SingleChannel(filePath):
    pt = Imath.PixelType(Imath.PixelType.FLOAT)
    img_exr = OpenEXR.InputFile(filePath)


    r_str = img_exr.channel('R', pt)
    
    #print('r_str', r_str)

    red = np.array(array.array('f', r_str))
    

    dw = img_exr.header()['dataWindow']
    size = (dw.max.x - dw.min.x + 1, dw.max.y - dw.min.y + 1)
    #print(size)

    img = red.reshape(size[1], size[0],1)
    return img