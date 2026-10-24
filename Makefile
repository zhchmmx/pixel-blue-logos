NAME    := pixel-blue-logos
VERSION := 1.0.2
TARBALL := $(NAME)-$(VERSION).tar.gz

.PHONY: sources srpm rpm clean

# Build the upstream source tarball from the SOURCES/ payload and write its
# SHA512 to the dist-git style `sources` file.  That file is generated only
# for local/dist-git use and is git-ignored (it collides with SOURCES/ on
# case-insensitive filesystems).
sources:
	rm -rf $(NAME)-$(VERSION) $(TARBALL)
	mkdir -p $(NAME)-$(VERSION)
	cp -a SOURCES/. $(NAME)-$(VERSION)/
	tar --sort=name --mtime='UTC 2020-01-01' --owner=0 --group=0 --numeric-owner \
		-czf $(TARBALL) $(NAME)-$(VERSION)
	rm -rf $(NAME)-$(VERSION)
	@printf 'SHA512 (%s) = %s\n' '$(TARBALL)' "$$(sha512sum $(TARBALL) | cut -d' ' -f1)" > sources
	@echo "created $(TARBALL) and updated sources"

# rpmdev-setuptree is expected to have been run once.
srpm: sources
	rpmbuild -bs --define '_sourcedir $(CURDIR)' SPECS/generic-logos.spec

rpm: sources
	rpmbuild -ba --define '_sourcedir $(CURDIR)' SPECS/generic-logos.spec

clean:
	rm -rf $(NAME)-$(VERSION) $(TARBALL)
