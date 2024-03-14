download-glad:
	cd code/glad_ard \
	&& wget --no-check-certificate https://gaftp.epa.gov/EPADataCommons/ORD/Ecoregions/us/us_eco_l3.zip -O us_eco_l3.zip \
	&& python generate_rockies_flist.py
