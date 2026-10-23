Name:       pixel-blue-logos
Version:    1.0.0
Release:    1%{?dist}
Summary:    Icons and pictures

URL:        https://github.com/zhchmmx/pixel-blue-logos
Source0:    %{url}/release/v%{version}/%{name}-%{version}.tar.gz
License:    CC BY
BuildArch:  noarch

Obsoletes:  redhat-logos
Obsoletes:  generic-logos < 17.0.0-5
Provides:   redhat-logos = %{version}-%{release}
Provides:   system-logos = %{version}-%{release}
# Fake provide as we don't have generic logos for icewm
# See: https://src.fedoraproject.org/rpms/fedora-logos/pull-request/13
Provides:   system-logos-icewm = %{version}-%{release}

Conflicts:  fedora-logos
Conflicts:  anaconda-images <= 10
Conflicts:  redhat-artwork <= 5.0.5
BuildRequires: make
BuildRequires: fdupes
# For _kf6_datadir macro
BuildRequires: kf6-rpm-macros
# For generating the EFI icon
BuildRequires: libicns-utils
Requires(post): coreutils

%description
Logo for Pixel Blue Distro.


%prep
%setup -qC

%build
make

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_datadir}/firstboot/themes/generic
for i in firstboot/* ; do
  install -p -m 644 $i %{buildroot}%{_datadir}/firstboot/themes/generic
done

mkdir -p %{buildroot}%{_datadir}/pixmaps/bootloader
install -p -m 644 bootloader/fedora.icns %{buildroot}%{_datadir}/pixmaps/bootloader
install -p -m 644 bootloader/fedora.vol %{buildroot}%{_datadir}/pixmaps/bootloader
install -p -m 644 bootloader/fedora-media.vol  %{buildroot}%{_datadir}/pixmaps/bootloader

mkdir -p %{buildroot}%{_datadir}/pixmaps/splash
for i in gnome-splash/* ; do
  install -p -m 644 $i %{buildroot}%{_datadir}/pixmaps/splash
done

mkdir -p %{buildroot}%{_datadir}/pixmaps
for i in pixmaps/* ; do
  install -p -m 644 $i %{buildroot}%{_datadir}/pixmaps
done

for size in scalable ; do
  mkdir -p %{buildroot}%{_datadir}/icons/hicolor/$size/apps
  ln -s ../../../hicolor/$size/apps/pixel-blue-logo-icon.svg icon-panel-menu.svg
  ln -s ../../../hicolor/$size/apps/pixel-blue-logo-icon.svg gnome-main-menu.svg
  ln -s ../../../hicolor/$size/apps/pixel-blue-logo-icon.svg kmenu.svg
  ln -s ../../../hicolor/$size/apps/pixel-blue-logo-icon.svg start-here.svg
  install -p -m 644 pixmaps/pixel-blue-logo-sprite.svg %{buildroot}%{_datadir}/icons/hicolor/$size/apps/pixel-blue-logo-icon.svg
done

mkdir -p %{buildroot}%{_kf6_datadir}/oxygen/48x48/apps/
install -p -m 644 icons/Fedora/48x48/apps/* %{buildroot}%{_kf6_datadir}/oxygen/48x48/apps/

mkdir -p %{buildroot}%{_datadir}/plymouth/themes/charge/
for i in plymouth/charge/* ; do
    install -p -m 644 $i %{buildroot}%{_datadir}/plymouth/themes/charge/
done

# File or directory names do not count as trademark infringement
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
install -p -m 644 icons/Fedora/48x48/apps/* %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/
install -p -m 644 icons/Fedora/scalable/apps/* %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
install -p -m 644 pixmaps/fedora-logo-sprite.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
install -p -m 644 pixmaps/fedora-logo-sprite.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/start-here.svg

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/places/
pushd %{buildroot}%{_datadir}/icons/hicolor/scalable/places/
ln -s ../apps/start-here.svg .
popd

(cd anaconda; make DESTDIR=%{buildroot} install)

# save some dup'd icons
%fdupes %{buildroot}/

%files
%license COPYING
%doc README
%{_datadir}/firstboot/themes/*
%{_datadir}/anaconda/boot/*
%{_datadir}/anaconda/pixmaps/*
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/icons/hicolor/*/places/*
%{_datadir}/pixmaps/*
%exclude %{_datadir}/pixmaps/poweredby.png
%{_datadir}/plymouth/themes/charge/*
%{_kf6_datadir}/oxygen/

%files httpd
%license COPYING
%{_datadir}/pixmaps/poweredby.png

%changelog
* Fri Oct 23 2026 zhchmmx <zhchmmx@gmail.com> - 1.0.0
- Original
