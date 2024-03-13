check-conda:
    @echo "Checking if Conda is installed..."
    @if ! conda --version >/dev/null 2>&1; then \
        echo "Error: Conda is not installed."; \
        exit 1; \
    else \
        echo "Conda is installed."; \
    fi

install-aria: check-conda
    conda install aria2 -y

download-glad:
	cd code/glad_ard \
	&& wget --no-check-certificate https://gaftp.epa.gov/EPADataCommons/ORD/Ecoregions/us/us_eco_l3.zip -O us_eco_l3.zip\
	&& python generate_rockies_flist.py

download-ard-with-flist:
    aria2c --http-passwd=ardpas --http-user=glad -i flist.txt -j2 --dir=data