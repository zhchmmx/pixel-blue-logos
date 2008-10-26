Name: generic-logos
Summary: Icons and pictures
Version: 10.0.0
Release: 2%{?dist}
Group: System Environment/Base
Source0: generic-logos-%{version}.tar.bz2
Source1: SolarComet-kde.png
License: GPLv2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch
Obsoletes: redhat-logos
Provides: redhat-logos = %{version}-%{release}
Provides: system-logos = %{version}-%{release}
Conflicts: fedora-logos
Conflicts: kdebase <= 3.1.5
Conflicts: anaconda-images <= 10
Conflicts: redhat-artwork <= 5.0.5
# For _kde4_appsdir macro:
BuildRequires: kde-filesystem

%description
The generic-logos package contains various image files which can be
used by the bootloader, anaconda, and other related tools. It can
be used as a replacement for the fedora-logos package, if you are
unable for any reason to abide by the trademark restrictions on the
fedora-logos package.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT

# should be ifarch i386
mkdir -p $RPM_BUILD_ROOT/boot/grub
install -m 644 bootloader/grub-splash.xpm.gz $RPM_BUILD_ROOT/boot/grub/splash.xpm.gz
# end i386 bits

mkdir -p $RPM_BUILD_ROOT%{_datadir}/firstboot/pixmaps
for i in firstboot/* ; do
  install -m 644 $i $RPM_BUILD_ROOT%{_datadir}/firstboot/pixmaps
done

mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps/splash
for i in gnome-splash/* ; do
  install -m 644 $i $RPM_BUILD_ROOT%{_datadir}/pixmaps/splash
done

mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
for i in pixmaps/* ; do
  install -m 644 $i $RPM_BUILD_ROOT%{_datadir}/pixmaps
done

(cd anaconda; make DESTDIR=$RPM_BUILD_ROOT install)

# KDE logo for KDE splash screen
cat >COPYING-kde-logo <<EOF
From http://wiki.kde.org/tiki-index.php?page=KDE+Logo:
Trademark License
Copying of the KDE Logo is subject to the LGPL copyright license.
Trading and branding with the KDE Logo is subject to our trademark licence:
1. The KDE logo can be used freely as long as it is not used to refer to
   products other than KDE itself.
2. There is no formal procedure for using the KDE logo as long as you stay
   within the above guideline for usage.
3. Whilst not required you should acknowledge the KDE e.V.s rights by mentioning
   "KDE, K Desktop Environment and the KDE Logo are trademarks of KDE e.V."
EOF
mkdir -p $RPM_BUILD_ROOT%{_kde4_appsdir}/ksplash/Themes/SolarComet/1280x1024
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_kde4_appsdir}/ksplash/Themes/SolarComet/1280x1024/logo.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc COPYING COPYING-kde-logo
%{_datadir}/firstboot/*
%{_datadir}/anaconda/pixmaps/*
%{_datadir}/pixmaps/*
%{_kde4_appsdir}/ksplash/Themes/SolarComet/1280x1024/logo.png
/usr/lib/anaconda-runtime/*.jpg
# should be ifarch i386
/boot/grub/splash.xpm.gz
# end i386 bits

%changelog
* Sun Oct 26 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> - 10.0.0-2
- Add (current version of) KDE logo for SolarComet KSplash theme

* Thu Oct 23 2008 Bill Nottingham <notting@redhat.com> - 10.0.0-1
- update for current fedora-logos, with Solar theme

* Fri Jul 11 2008 Bill Nottingham <notting@redhat.com> - 9.99.0-1
- add a system logo for plymouth's spinfinity plugin

* Tue Apr 15 2008 Bill Nottingham <notting@redhat.com> - 9.0.0-1
- updates for current fedora-logos (much thanks to <duffy@redhat.com>)
- remove KDE Infinity splash
 
* Mon Oct 29 2007 Bill Nottingham <notting@redhat.com> - 8.0.2-1
- Add Infinity splash screen for KDE

* Thu Sep 13 2007 Bill Nottingham <notting@redhat.com> - 7.92.1-1
- add powered-by logo (#250676)
- updated rhgb logo (<duffy@redhat.com>)

* Tue Sep 11 2007 Bill Nottinghan <notting@redhat.com> - 7.92.0-1
- initial packaging. Forked from fedora-logos, adapted from the Fedora
  Art project's Infinity theme
