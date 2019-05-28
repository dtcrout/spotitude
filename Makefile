# META ]------------------------------------------------------------------------
help:
	@echo "test				Return status of source files."
	@echo "config				Make config file for Spotify API."
	@echo "deps				Make dependencies."
	@echo "clean				Remove artifacts and standardize repo."

# CORE ]------------------------------------------------------------------------
test:
	black --check .

config:
	touch spotitude.config && \
	echo "[DEFAULT]\nUSERNAME=\nSCOPE=\nREDIRECT_URI=\nCLIENT_ID=\nCLIENT_SECRET=" > spotitude.config

deps:
	pip3 install -r requirements.txt

clean:
	black . && \
	rm -f *.html *.csv .cache-*
