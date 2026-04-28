def plot(grid, size, scale = 5):
    from PIL import Image
    import numpy as np
    '''
    Honestly, don't worry about this. I wrote this code ages ago for another project and have been using it ever since. 
    I can't even remember how it works anymore tbh. 
    '''
    img_array = np.where(grid == 1, 0, 255).astype(np.uint8)

    img = Image.fromarray(img_array, mode='L')

    width, height = img.size
    img = img.resize((width * scale, height * scale),
                     Image.Resampling.NEAREST)

    img.show()