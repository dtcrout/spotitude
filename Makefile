# META ]------------------------------------------------------------------------
help:
	@echo "test				Return status of source files."
	@echo "config				Make config file for Spotify API."
	@echo "deps				Make dependencies."
	@echo "server				Create server to view visualization."
	@echo "clean				Remove artifacts and standardize repo."

# CORE ]------------------------------------------------------------------------
venv: venv/bin/activate
venv/bin/activate: requirements.txt
	test -d venv || python3 -m venv venv
	venv/bin/pip3 install -r requirements.txt
	touch venv/bin/activate

test: venv
	. venv/bin/activate ;\
	black --check . --exclude venv

config:
	touch spotitude.config && \
	printf "[DEFAULT]\nUSERNAME=\nSCOPE=user-top-read playlist-modify-private\nREDIRECT_URI=http://localhost:8080\nCLIENT_ID=\nCLIENT_SECRET=" > spotitude.config

deps: venv

server:
	python3 -m http.server 8080

clean: venv
	. venv/bin/activate ;\
	black . --exclude venv && \
	rm -rf *.html *.csv .cache-* __pycache__ venv/
	