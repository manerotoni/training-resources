- Open the above mentioned image
- **[ Plugins > MorpholibJ > Label Images > Remove Border Labels ]** to remove labels at the border
- **[ Plugins > MorpholibJ > Analyze > Analyze Regions ]** to see area and number of objects
  - Using `[X] Pixel Count`. One can uncheck the rest of measurements
- **[ Plugins > MorpholibJ > Label Images > Label Size Filtering ]** to remove smaller objects
  - `Operation "Greater_than"`
    - This will keep all objects greater than `Size Limit (pixels)`
  - `Size Limit (pixels) 100`
