# %% 
# Morphological internal gradient of a binary image

# %%
from OpenIJTIFF import open_ij_tiff
from napari.viewer import Viewer
from skimage.morphology import erosion

# Create a napari_viewer and visualize image and labels.
viewer = Viewer()

# %%
# Explore internal gradient.
fpath = "https://github.com/NEUBIAS/training-resources/raw/master/image_data/xy_8bit_binary__h2b.tif"
image, _, _, _ = open_ij_tiff(fpath)

# Internal gradient is the difference between the image and the eroded version of it.
eroded = erosion(image)
internal_gradient = image - eroded

# %%
# Create a napari_viewer and visualize images.
viewer.add_image(image)
viewer.add_labels(eroded)
viewer.add_labels(internal_gradient)

# %% [markdown]
# The internal gradient represents the inner edge of the object.\
# Discuss when and how this can be useful.

# %% [markdown]
# **Learning opportunity**
# * Compute the external gradient (dilation - image)
# * Try different sized structuring elements for the dilation
# * What controls the thickness of the edge?
# * Compute the central gradient (dilation - erosion)

# %% 
# Close the viewer (CI test requires this)
viewer.close()