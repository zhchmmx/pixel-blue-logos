Name: generic-logos
Summary: Icons and pictures
Version: 9.99.0
Release: 1%{?dist}
Group: System Environment/Base
Source0: generic-logos-%{version}.tar.bz2
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

mkdir -p $RPM_BUILD_ROOT%{_datadir}/rhgb
for i in rhgb/* ; do
  install -m 644 $i $RPM_BUILD_ROOT%{_datadir}/rhgb
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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc COPYING
%{_datadir}/firstboot/*
%{_datadir}/rhgb/*
%{_datadir}/anaconda/pixmaps/*
%{_datadir}/pixmaps/*
/usr/lib/anaconda-runtime/*.jpg
# should be ifarch i386
/boot/grub/splash.xpm.gz
# end i386 bits

%changelog
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
