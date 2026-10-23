Name:       pixel-blue-logos
Version:    1.0.0
Release:    1%{?dist}
Summary:    Pixel Blue icons and pictures

URL:        https://github.com/zhchmmx/pixel-blue-logos
Source0:    %{name}-%{version}.tar.gz
License:    CC-BY-4.0
BuildArch:  noarch

Obsoletes:  redhat-logos
Obsoletes:  generic-logos < 17.0.0-5
Provides:   redhat-logos = %{version}-%{release}
Provides:   system-logos = %{version}-%{release}
Provides:   gnome-logos = %{version}-%{release}
# Fake provide as we don't have generic logos for icewm
# See: https://src.fedoraproject.org/rpms/fedora-logos/pull-request/13
Provides:   system-logos-icewm = %{version}-%{release}

Conflicts:  fedora-logos
Conflicts:  anaconda-images <= 10
Conflicts:  redhat-artwork <= 5.0.5

%description
Logo for Pixel Blue Distro.

%package httpd
Summary:	Pixel Blue icons and pictures used by httpd
Provides:	system-logos-httpd = %{version}-%{release}
BuildArch:	noarch
Provides:	system-logos(httpd-logo-ng)

%description httpd
This package contains Pixel Blue icons and pictures used by httpd.


%prep
%setup -q

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

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
install -p -m 644 icons/hicolor/scalable/apps/pixel-blue-logo-icon.svg \
  %{buildroot}%{_datadir}/icons/hicolor/scalable/apps

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

%files
%license COPYING
%doc README
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/icons/hicolor/*/places/*
%{_datadir}/pixmaps/*
%exclude %{_datadir}/pixmaps/poweredby.png
%dir %{_datadir}/pixel-blue
%dir %{_datadir}/pixel-blue/logos
%{_datadir}/pixel-blue/logos/*
%{_datadir}/plymouth/themes/spinner/watermark.png

%files httpd
%license COPYING
%{_datadir}/pixmaps/poweredby.png

%changelog
* Fri Oct 23 2026 zhchmmx <zhchmmx@gmail.com> - 1.0.0
- Original
