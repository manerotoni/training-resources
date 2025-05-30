# %% 
# Load different image files and access various levels of metadata
# minimal conda env for this module
# conda create -n ImageFileFormats python=3.10
# activate ImageFileFormat
# pip install bioio bioio-tifffile bioio-lif bioio-czi bioio-ome-tiff bioio-ome-zarr notebook

# IMPORTANT: bioio by default expects z,y,x to be in microns and T to be in frames per second

# %%
# Load .tif file with minimal metadata
# - Observe that BioImage chooses the correct reader plugin
# - Observe that the return object is not the image matrix
from bioio import BioImage
image_url = 'https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit__nuclei_PLK1_control.tif'
bioimage = BioImage(image_url)
print(bioimage)
print(type(bioimage))

# %%
# Print some onject attributes
# - Observe that the object is 5 dimensional with most dimensions being empty
# - Observe that the dimension order is always time, channel, z, y, x, (TCZYX)
print(bioimage.dims)
print(bioimage.shape)
print(f'Dimension order is: {bioimage.dims.order}')
print(type(bioimage.dims.order))
print(f'Size of X dimension is: {bioimage.dims.X}')

# %%
# Extract image data
# - Observe that the returned numpy.array is still 5 dimensional
image_data = bioimage.data
print(type(image_data))
print(image_data)
print(image_data.shape)

# %%
# Extract specific part of image data
# - Observe that numpy.array is reduced to populated dimensions only
yx_image_data = bioimage.get_image_data('YX')
print(type(yx_image_data))
print(yx_image_data)
print(yx_image_data.shape)

# %%
# Access pixel size
import numpy as np
print(bioimage.physical_pixel_sizes)
print(f'An pixel has a length of {np.round(bioimage.physical_pixel_sizes.X,2)} microns in X dimension.')

# %%
# Access general metadata
print(type(bioimage.metadata))
print(bioimage.metadata)

# %%
# Load .tif file with extensive metadata
image_url = "https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_16bit__collagen.md.tif"
bioimage = BioImage(image_url)
print(bioimage)
print(type(bioimage))

# - Observe that the image is larger than the previous
print(bioimage.dims)

# %%
# Access image and reduce to only populated dimensions
yx_image_data = bioimage.data.squeeze()
print(type(yx_image_data))
print(yx_image_data)
print(yx_image_data.shape)

# %%
# Access pixel size
print(bioimage.physical_pixel_sizes)
print(f'An pixel has a length of {np.round(bioimage.physical_pixel_sizes.Y,2)} microns in Y dimension.')

# Access general metadata
# - Observe that metadata are more extensive than in the previous image
print(type(bioimage.metadata))
print(bioimage.metadata)

# %%
# Load .lif file
# - Observe that BioImage chooses the correct reader plugin
# - Observe that the return object has 4 different channels
# - Observe that the general metadata are an abstract element
image_url = "https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_xyc__two_images.lif"
bioimage = BioImage(image_url)
print(bioimage)
print(type(bioimage))
print(bioimage.dims)
print(bioimage.metadata)
print(type(bioimage.metadata))

# %%
# Access channel information
print(bioimage.channel_names)

# %%
# Access image data for all channels
img_4channel = bioimage.data.squeeze()

# Alternative
img_4channel = bioimage.get_image_data('CYX')

# - Observe that numpy.array shape is 3 dimensional representing channel,y,x
print(img_4channel.shape)

# Access only one channel
img_1channel = bioimage.get_image_data('YX',C=0)

# Alternative
img_1channel = img_4channel[0]

# - Observe that numpy.array shape is 2 dimensional representing y,x
print(img_1channel.shape)

# %%
# Access different images in one image file (scenes)
# - Observe that one image file can contain several scenes
# - Observe that they can be different in various aspects
print(bioimage.scenes)
print(f'Current scene: {bioimage.current_scene}')

# - Observe that the image in the current scene as 4 channel and Y/X dimensions have the size of 1024
print(bioimage.dims)
print(bioimage.physical_pixel_sizes)

# Switch to second scene
# - Observe that the image in the other scene as only one channel and Y/X dimensions are half as large as the first scene
# - Observe that the pixel sizes are doubled
bioimage.set_scene(1)
print(bioimage.dims)
print(bioimage.physical_pixel_sizes)

# %%
# Load .czi file
# file needs first to be downloaded from https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyz__multiple_images.czi
# save file in the same directory as this notebook
# - Observe that BioImage chooses the correct reader plugin
# - Observe that the return object has a z dimension
# TODO FIX THIS!!
bioimage = BioImage('/Users/fschneider/skimage-napari-tutorial/ExampleImages/xyz__multiple_images.czi')
print(bioimage)
print(type(bioimage))

# %%
# little excersise in between
# Access image dimensions
print(bioimage.dims)

# Access general metadata
# - Observe that metadata are abstract
print(bioimage.metadata)
print(type(bioimage.metadata))

# Access pixel size
print(bioimage.physical_pixel_sizes)

# Access image data for all channels
img_3d = bioimage.data.squeeze()

# Alternative
img_3d = bioimage.get_image_data('ZYX')

# - Observe that numpy.array shape is 3 dimensional representing z,y,x
print(img_3d.shape)

# Access only one channel
img_2d = bioimage.get_image_data('YX',Z=0)

# Alternative
img_2d = img_3d[0]

# - Observe that numpy.array shape is 2 dimensional representing y,x
print(img_2d.shape)

# %%
# little excercise:
# paticipants should try to open one of their files with python
