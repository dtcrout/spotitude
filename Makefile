# META ]------------------------------------------------------------------------
help:
	@echo "test				Return status of source files."
	@echo "config				Make config file for Spotify API."
	@echo "deps				Make dependencies."
	@echo "server				Create server to view visualization."
	@echo "clean				Remove artifacts and standardize repo."

# CORE ]------------------------------------------------------------------------
test:
	black --check .

config:
	touch spotitude.config && \
	printf "[DEFAULT]\nUSERNAME=\nSCOPE=user-top-read\nREDIRECT_URI=http://localhost:8080\nCLIENT_ID=\nCLIENT_SECRET=" > spotitude.config

deps:
	pip3 install -r requirements.txt

server:
	python3 -m http.server 8080

clean:
	black . && \
	rm -rf *.html *.csv .cache-* __pycache__
