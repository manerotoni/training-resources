# %% 
# Open a CZI image file
# minimal conda env for this module
# conda create -n ImageFileFormats python=3.10
# activate ImageFileFormat
# pip install bioio bioio-tifffile bioio-lif bioio-czi bioio-ome-tiff bioio-ome-zarr notebook
# Note: for only dealing with .czi just do pip install bioio bioio-czi


# %%
# Load .czi file
# file needs first to be downloaded from https://github.com/NEUBIAS/training-resources/raw/master/image_data/xyz__multiple_images.czi
# save file in the same directory as this notebook
# - Observe that BioImage chooses the correct reader plugin
from bioio import BioImage
from pathlib import Path
bioimage = BioImage(Path().cwd()/'ExampleImages/xyz__multiple_images.czi')
print(bioimage)
print(type(bioimage))

# %%
# Inspect number of images in object
print(bioimage.scenes)

# %%
# Inspect both images in the object
for image in bioimage.scenes:
    print(f'Image name: {image}')
    # Select image:
    bioimage.set_scene(image)
    # Inspect dimension and shape of image
    print(f'Image dimension: {bioimage.dims}')
    print(f'Dimension order is: {bioimage.dims.order}')
    print(f'Image shape: {bioimage.shape}')
    # Extract image data (5D)
    image_data = bioimage.data
    print(f'Image type: {type(image_data)}')
    print(f'Image array shape: {image_data.shape}')
    # Extract specific image part
    image_data = bioimage.get_image_data('YX')
    print(f'Image type: {type(image_data)}')
    print(f'Image array shape: {image_data.shape}')
    # Read pixel size
    print(f'Pixel size: {bioimage.physical_pixel_sizes}')
    # Read metadata
    print(f'Metadata type: {type(bioimage.metadata)}')
    print(f'Metadata: {bioimage.metadata}')
    print('\n')

#%%
# Handle metadata
import xml.etree.ElementTree as ET
from xml.dom import minidom
# print a pretty version of the xml metadata
md = bioimage.metadata
xml_string = ET.tostring(md, encoding='unicode')
pretty_xml = minidom.parseString(xml_string).toprettyxml(indent="  ")
print(pretty_xml)

#%%
# Grab specific information
size_x = md.findtext(".//Image/SizeX")
pixel_type = md.findtext(".//Image/PixelType")
excitation_wavelength = md.findtext(".//Channel/ExcitationWavelength")
emission_wavelength = md.findtext(".//Channel/EmissionWavelength")
print(f'Image size in X: {size_x}')
print(f'Pixel type: {pixel_type}')
print(f'Excitation wavelength: {excitation_wavelength}')
print(f'Emission wavelength: {emission_wavelength}')