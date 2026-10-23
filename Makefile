NAME    := pixel-blue-logos
VERSION := 1.0.0
TARBALL := $(NAME)-$(VERSION).tar.gz

.PHONY: sources srpm rpm clean

# Build the upstream source tarball from the SOURCES/ payload and refresh the
# dist-git sources file with its SHA512.
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
