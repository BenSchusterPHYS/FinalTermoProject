def plot(grid, T, save, scale = 5):
    from PIL import Image
    import numpy as np
    from pathlib import Path
    '''
    Honestly, don't worry about this. I wrote this code ages ago for another project and have been using it ever since. 
    I can't even remember how it works anymore tbh. 
    '''
    img_array = np.where(grid == 1, 0, 255).astype(np.uint8)

    img = Image.fromarray(img_array, mode='L')

    width, height = img.size
    img = img.resize((width * scale, height * scale),
                     Image.Resampling.NEAREST)

    if save:
        project_dir = Path(__file__).parent.parent

        save_dir = project_dir / "Images"
        save_dir.mkdir(exist_ok=True)

        save_path = save_dir / f"ising_at_T_{T}.png"

        img.save(save_path)
    
    img.show()