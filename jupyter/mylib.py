

def plotimage(img, title=None, figsize=None, invert=True):
    #Source: https://stackoverflow.com/a/42314798
    import numpy as np
    from matplotlib import pyplot as plt
    
    if invert:
        img = np.max(img) - img.copy()
    h = img.shape[0]
    w = img.shape[1]
    dpi = 80
    if figsize is None:
        figsize = w / float(dpi), h / float(dpi)
    fig = plt.figure(figsize=figsize)
    ax = fig.add_axes([0, 0, 1, 1])    
    ax.axis('off')
    ax.imshow(img, cmap='gray')
    if title:
        plt.title(title)
    plt.show()


def gray_to_bw(gray, thresh):
    '''
    Returns a new image
    '''
    import numpy as np

    bw = gray.copy()
    bw[bw<thresh]=0
    bw[bw>=thresh]=255
    return bw    

def draw_borders(img, color=0):
    
    import numpy as np
    
    if len(img.shape)==2:
        res = color * np.ones((img.shape[0]+2,img.shape[1]+2),dtype=img.dtype)
    else:
        res = color * np.ones((img.shape[0]+2,img.shape[1]+2,3),dtype=img.dtype)
        
    res[1:-1,1:-1] = img
    return res

def vert_seg(bw, black=1):
    import numpy as np

    lines = []

    height = bw.shape[0]

    i = 0
    start = 0
    while True:
        if black not in bw[i,:] or i==height-1:
            if i==height-1:
                end = i
            else:
                end = i-1
                
            if i!=start:
                lines.append({'start': start,'end': end+1})            
            start=i+1

        if i==height-1:
            break
        i+=1    
        
    return lines

def draw_vert_lines(vert, lines, blue=(255,255,0), red=(0,255,255)):
    import cv2
    import numpy as np
    
    width = vert.shape[1]
    for line in lines:
        start = line['start']
        end = line['end']
        cv2.line(vert, (0,start), (width,start), blue)
        cv2.line(vert, (0,end), (width,end), red)

def hor_seg(img, black=1):
    
    import numpy as np
    
    width = img.shape[1]
    
    j = 0
    start = 0
    chars = []
    while True:
        if black not in img[:,j] or j==width-1: 
            if j==width-1:
                end = j
            else:
                end = j-1
            if j!=start:
                chars.append({'start':start,'end':end+1})
                
            start=j+1

        if j==width-1:
            break
        j+=1
        
    return chars

def draw_hor_lines(hor, chars, start, end, blue=(255,255,0), red=(0,255,255)):
    
    import cv2
    import numpy as np
    
    for char in chars:
        char_start = char['start']
        char_end = char['end']
        cv2.line(hor, (char_start,start), (char_start,end), blue)  
        cv2.line(hor, (char_end,start), (char_end,end), red) 

def inner_prod(a,b):
    '''
    a and b are n-D numpy arrays, with exact same shape
    '''

    import numpy as np
    #return int(np.sum(np.abs(np.array(a)-np.array(b))))    
    return int(np.sum(np.array(a)*np.array(b)))

def normalize(v):
    import numpy as np

    norm = np.linalg.norm(v)
    if norm == 0: 
        return v
    return v / norm

def distance(a, b):
    import numpy as np

#    return np.dot(normalize(a), normalize(b))
#    return inner_prod(a,b)
    return int(np.sum(np.abs(np.array(a)-np.array(b))))    

