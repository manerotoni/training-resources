**Validate an OME-Zarr in the browser:**

Enter the following into your browser: `https://ome.github.io/ome-ngff-validator/?source=`

Then paste the dataset url after the 'equal' sign, constructing the following link: 

[https://ome.github.io/ome-ngff-validator/?source=https://uk1s3.embassy.ebi.ac.uk/idr/zarr/v0.4/idr0062A/6001240.zarr](https://ome.github.io/ome-ngff-validator/?source=https://uk1s3.embassy.ebi.ac.uk/idr/zarr/v0.4/idr0062A/6001240.zarr) 


* Find out the metadata fields such as axes, units and scales.
* Check the array and chunk shapes and bytes per resolution level.
* Visualize a single chunk.

Note that with the remote url it is possible to copy the link from your browser and share it with your colleagues.

**Open the OME-Zarr validator from the command line:**

```bash
ome_zarr view /path/to/local/omezarr # eg: ~/image_data_course/data/zarr/6001240.zarr
```

The validator will open in a web browser.