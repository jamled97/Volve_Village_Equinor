The directory /project/volvepub/Geophysical_Interpretations/Horizons 
contains horizon interpretations.

Horizons_TWT: Horizons in time
	Official_Horizons: Interpolated versions of key horizons
	Timelapse_Horizons: Horizons used for computing 4D attribute maps. There are different versions with different extensions.
	Other_Horizons: Some other relevant horizons
	Multiples: Indicating first and second multiple of strongest horizons, interfering with reservoir.  
Horizons_DEPTH: Horizons in depth
	Official_Horizons: Interpolated versions of key horizons (in depth)
	Other_Horizons: Some other relevant horizons

Naming standard for Horizon files:
  Stratigrafic_surface+Seismic_info+Interpreter+Output_Domain.dat

Horizon-OW-IO-formatfile.xml: Format file used to export horizons from OW, using the "Data Export" utility.

The horizon files contain IL, XL, UTMX, UTMY, and TWT or Z.

ST0202 and ST10010 survey have different but related IL/XL system:

XL(ST10010) = XL(ST0202)
IL(ST10010) = 2 x IL(ST0202) - 1

 
