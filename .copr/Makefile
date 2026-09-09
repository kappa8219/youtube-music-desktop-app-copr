spec := youtube-music-desktop-app.spec
version := 2.0.12
release_url := https://github.com/ytmdesktop/ytmdesktop/releases/download/v$(version)
sources := youtube-music-desktop-app-$(version)-1.x86_64.rpm youtube-music-desktop-app-$(version)-1.arm64.rpm

.PHONY: srpm
srpm:
	for source in $(sources); do curl --fail --location --output $$source $(release_url)/$$source; done
	rpmbuild -bs --define "_sourcedir $(CURDIR)" --define "_srcrpmdir $(outdir)" $(spec)
