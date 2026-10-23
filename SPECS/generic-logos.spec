Name:		pixel-blue-logos
Summary:	Pixel Blue-related icons and pictures
Version:	1.0.0
Release:	1%{?dist}
URL:		https://github.com/zhchmmx/pixel-blue-logos
Source0:	%{url}/release/v%{version}/%{name}-%{version}.tar.gz
License:	CC BY
Provides:	redhat-logos = %{version}-%{release}
Provides:	gnome-logos = %{version}-%{release}
Provides:	system-logos = %{version}-%{release}
Provides:	system-logos-icewm = %{version}-%{release}
Obsoletes:	redhat-logos
Obsoletes:	generic-logos < 17.0.0-5
Conflicts:	fedora-logos
BuildArch:	noarch

BuildRequires:	make
BuildRequires:	hardlink
# For _kf6_datadir macro
BuildRequires:	kf6-rpm-macros

%description
The pixel-blue-logos package contains image files for the Pixel Blue
distribution.

%package httpd
Summary:	Pixel Blue icons and pictures used by httpd
Provides:	system-logos-httpd = %{version}-%{release}
BuildArch:	noarch
Provides:	system-logos(httpd-logo-ng)

%description httpd
The pixel-blue-logos-httpd package contains image files used by httpd.

%prep
%autosetup -p1

%build

%install
# Bootloader related files
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps/bootloader
install -p -m 644 bootloader/fedora.icns $RPM_BUILD_ROOT%{_datadir}/pixmaps/bootloader
install -p -m 644 bootloader/fedora_classic.icns $RPM_BUILD_ROOT%{_datadir}/pixmaps/bootloader
install -p -m 644 bootloader/fedora.vol bootloader/fedora-media.vol $RPM_BUILD_ROOT%{_datadir}/pixmaps/bootloader
install -p -m 644 bootloader/bootlogo_128.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/bootloader/bootlogo_128.png
install -p -m 644 bootloader/bootlogo_256.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/bootloader/bootlogo_256.png

# General purpose Pixel Blue logos
for i in pixmaps/* ; do
  install -p -m 644 $i $RPM_BUILD_ROOT%{_datadir}/pixmaps
done

# Pixel Blue logo icons
for size in 16x16 22x22 24x24 32x32 36x36 48x48 96x96 256x256 ; do
  mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/$size/apps
  for i in icons/hicolor/$size/apps/* ; do
    install -p -m 644 $i $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/$size/apps
  done
  mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/$size/places
  install -p -m 644 -D icons/hicolor/$size/apps/pixel-blue-logo-icon.png \
    $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/$size/places/start-here.png
done

# Symbolic icons
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/symbolic/apps
for i in icons/hicolor/symbolic/apps/* ; do
  install -p -m 644 $i $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/symbolic/apps
done

# Scalable icons
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps
for i in icons/hicolor/scalable/apps/* ; do
  install -p -m 644 $i $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps
done

# KDE/Oxygen icons
for i in 16 22 24 32 36 48 96 256 ; do
  mkdir -p $RPM_BUILD_ROOT%{_kf6_datadir}/oxygen/${i}x${i}/apps
  install -p -m 644 -D icons/hicolor/${i}x${i}/apps/pixel-blue-logo-icon.png $RPM_BUILD_ROOT%{_kf6_datadir}/oxygen/${i}x${i}/apps/start-here-kde-pixel-blue.png
done
mkdir -p $RPM_BUILD_ROOT%{_kf6_datadir}/oxygen/scalable/apps/
install -p -m 644 icons/hicolor/scalable/apps/org.fedoraproject.AnacondaInstaller.svg $RPM_BUILD_ROOT%{_kf6_datadir}/oxygen/scalable/apps/

# Pixel Blue favicon
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}
pushd $RPM_BUILD_ROOT%{_sysconfdir}
  ln -s %{_datadir}/icons/hicolor/16x16/apps/pixel-blue-logo-icon.png favicon.png
popd

# Pixel Blue scalable start-here icon
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/places/
pushd $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/places/
  ln -s ../apps/pixel-blue-logo-icon.svg start-here.svg
popd

# Anaconda art
mkdir -p $RPM_BUILD_ROOT%{_datadir}/anaconda/boot
install -p -m 644 anaconda/splash.lss $RPM_BUILD_ROOT%{_datadir}/anaconda/boot/
install -p -m 644 anaconda/syslinux-splash.png $RPM_BUILD_ROOT%{_datadir}/anaconda/boot/
install -p -m 644 anaconda/syslinux-vesa-splash.png $RPM_BUILD_ROOT%{_datadir}/anaconda/boot/splash.png
mkdir -p $RPM_BUILD_ROOT%{_datadir}/anaconda/pixmaps
install -p -m 644 anaconda/anaconda_header.png $RPM_BUILD_ROOT%{_datadir}/anaconda/pixmaps/
install -p -m 644 anaconda/anaconda_header_classic.png $RPM_BUILD_ROOT%{_datadir}/anaconda/pixmaps/
install -p -m 644 anaconda/sidebar-logo.png $RPM_BUILD_ROOT%{_datadir}/anaconda/pixmaps/
install -p -m 644 anaconda/sidebar-logo_classic.png $RPM_BUILD_ROOT%{_datadir}/anaconda/pixmaps/
install -p -m 644 anaconda/sidebar-bg.png $RPM_BUILD_ROOT%{_datadir}/anaconda/pixmaps/
install -p -m 644 anaconda/topbar-bg.png $RPM_BUILD_ROOT%{_datadir}/anaconda/pixmaps/
install -p -m 644 anaconda/fedora.css $RPM_BUILD_ROOT%{_datadir}/anaconda/pixmaps/

# Variant Anaconda art
pushd anaconda
for i in atomic cloud server silverblue workstation ; do
  cp -a $i $RPM_BUILD_ROOT%{_datadir}/anaconda/pixmaps/
done
popd

# save some dup'd icons
# Except in /boot. Because some people think it is fun to use VFAT for /boot.
# hardlink is /usr/sbin/hardlink on Fedora <= 30 and /usr/bin/hardlink on F31+
hardlink -vv %{buildroot}/usr

%files
%license COPYING
%config(noreplace) %{_sysconfdir}/favicon.png
%{_datadir}/pixmaps/*
# This lives in the http subpackage
%exclude %{_datadir}/pixmaps/poweredby.png
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/icons/hicolor/*/places/*
%{_datadir}/icons/hicolor/symbolic/apps/*
%{_kf6_datadir}/oxygen/
%{_datadir}/anaconda/pixmaps/*
%{_datadir}/anaconda/boot/splash.lss
%{_datadir}/anaconda/boot/syslinux-splash.png
%{_datadir}/anaconda/boot/splash.png
# we multi-own these directories, so as not to require the packages that
# provide them, thereby dragging in excess dependencies.
%dir %{_datadir}/icons/hicolor/
%dir %{_datadir}/icons/hicolor/16x16/
%dir %{_datadir}/icons/hicolor/16x16/apps/
%dir %{_datadir}/icons/hicolor/16x16/places/
%dir %{_datadir}/icons/hicolor/22x22/
%dir %{_datadir}/icons/hicolor/22x22/apps/
%dir %{_datadir}/icons/hicolor/22x22/places/
%dir %{_datadir}/icons/hicolor/24x24/
%dir %{_datadir}/icons/hicolor/24x24/apps/
%dir %{_datadir}/icons/hicolor/24x24/places/
%dir %{_datadir}/icons/hicolor/32x32/
%dir %{_datadir}/icons/hicolor/32x32/apps/
%dir %{_datadir}/icons/hicolor/32x32/places/
%dir %{_datadir}/icons/hicolor/36x36/
%dir %{_datadir}/icons/hicolor/36x36/apps/
%dir %{_datadir}/icons/hicolor/36x36/places/
%dir %{_datadir}/icons/hicolor/48x48/
%dir %{_datadir}/icons/hicolor/48x48/apps/
%dir %{_datadir}/icons/hicolor/48x48/places/
%dir %{_datadir}/icons/hicolor/96x96/
%dir %{_datadir}/icons/hicolor/96x96/apps/
%dir %{_datadir}/icons/hicolor/96x96/places/
%dir %{_datadir}/icons/hicolor/256x256/
%dir %{_datadir}/icons/hicolor/256x256/apps/
%dir %{_datadir}/icons/hicolor/256x256/places/
%dir %{_datadir}/icons/hicolor/scalable/
%dir %{_datadir}/icons/hicolor/scalable/apps/
%dir %{_datadir}/icons/hicolor/scalable/places/
%dir %{_datadir}/icons/hicolor/symbolic/
%dir %{_datadir}/icons/hicolor/symbolic/apps/
%dir %{_datadir}/anaconda
%dir %{_datadir}/anaconda/boot/
%dir %{_datadir}/anaconda/pixmaps/

%files httpd
%license COPYING
%{_datadir}/pixmaps/poweredby.png

%changelog
* Fri Oct 23 2026 zhchmmx <zhchmmx@gmail.com> - 1.0.0-1
- Rewrite spec based on Fedora's fedora-logos spec.
