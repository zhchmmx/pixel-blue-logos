Name:		pixel-blue-logos
Summary:	Pixel Blue-related icons and pictures
Version:	1.0.0
Release:	1%{?dist}
URL:		https://github.com/zhchmmx/pixel-blue-logos
Source0:	%{url}/release/v%{version}/%{name}-%{version}.tar.gz
License:	CC-BY-4.0
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
mkdir -p %{buildroot}%{_datadir}/pixmaps
for i in pixmaps/* ; do
  install -p -m 644 "$i" %{buildroot}%{_datadir}/pixmaps
done

# gnome-control-center hardcodes these Fedora filenames in its About panel.
# The file names are not trademarks, and Conflicts: fedora-logos guarantees
# that there is no path collision.
install -p -m 644 pixmaps/pixel-blue-logo-med.png \
  %{buildroot}%{_datadir}/pixmaps/fedora_logo_med.png
install -p -m 644 pixmaps/pixel-blue-whitelogo-med.png \
  %{buildroot}%{_datadir}/pixmaps/fedora_whitelogo_med.png

# httpd ships a welcome page that expects poweredby.png.  Use a Pixel Blue
# badge rather than the Fedora wordmark.
install -p -m 644 pixmaps/pixel-blue-logo-small.png \
  %{buildroot}%{_datadir}/pixmaps/poweredby.png

# Pixel Blue logo icons
for size in 16x16 22x22 24x24 32x32 36x36 48x48 96x96 256x256 ; do
  mkdir -p %{buildroot}%{_datadir}/icons/hicolor/$size/apps
  install -p -m 644 icons/hicolor/$size/apps/pixel-blue-logo-icon.png \
    %{buildroot}%{_datadir}/icons/hicolor/$size/apps
  ( cd %{buildroot}%{_datadir}/icons/hicolor/$size/apps
    for i in icon-panel-menu.svg gnome-main-menu.svg kmenu.svg start-here.svg ; do
      ln -s ../../../hicolor/scalable/apps/pixel-blue-logo-icon.svg $i
    done
  )
done
mkdir -p $RPM_BUILD_ROOT%{_kf6_datadir}/oxygen/scalable/apps/
install -p -m 644 icons/hicolor/scalable/apps/org.fedoraproject.AnacondaInstaller.svg $RPM_BUILD_ROOT%{_kf6_datadir}/oxygen/scalable/apps/

# Pixel Blue favicon
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}
pushd $RPM_BUILD_ROOT%{_sysconfdir}
  ln -s %{_datadir}/icons/hicolor/16x16/apps/pixel-blue-logo-icon.png favicon.png
popd

# Pixel Blue scalable icon
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
install -p -m 644 icons/hicolor/scalable/apps/pixel-blue-logo-icon.svg \
  %{buildroot}%{_datadir}/icons/hicolor/scalable/apps

# Pixel Blue scalable start-here icon
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/places
( cd %{buildroot}%{_datadir}/icons/hicolor/scalable/places
  ln -s ../apps/pixel-blue-logo-icon.svg start-here.svg
)

# SVG masters
mkdir -p %{buildroot}%{_datadir}/pixel-blue/logos
for i in pixel-blue/logos/*.svg ; do
  install -p -m 644 "$i" %{buildroot}%{_datadir}/pixel-blue/logos
done

# Plymouth spinner watermark.  The theme itself is provided by plymouth; we
# only replace the lockup that build.sh validates in the initrd.
mkdir -p %{buildroot}%{_datadir}/plymouth/themes/spinner
install -p -m 644 plymouth/themes/spinner/watermark.png \
  %{buildroot}%{_datadir}/plymouth/themes/spinner/watermark.png

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
%doc README
%config(noreplace) %{_sysconfdir}/favicon.png
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/icons/hicolor/*/places/*
%{_datadir}/pixel-blue/logos/*.svg
%{_datadir}/plymouth/themes/spinner/watermark.png
%{_datadir}/anaconda/boot/*
%{_datadir}/anaconda/pixmaps/*
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
