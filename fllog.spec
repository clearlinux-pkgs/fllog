#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : fllog
Version  : 1.2.6
Release  : 2
URL      : https://sourceforge.net/projects/fldigi/files/fllog/fllog-1.2.6.tar.gz
Source0  : https://sourceforge.net/projects/fldigi/files/fllog/fllog-1.2.6.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: fllog-bin = %{version}-%{release}
Requires: fllog-data = %{version}-%{release}
Requires: fllog-license = %{version}-%{release}
BuildRequires : fltk-dev
BuildRequires : fontconfig-dev
BuildRequires : libXcursor-dev
BuildRequires : libXft-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : pkgconfig(x11)

%description
Fllog is a logbook application for Amateur Radio use.  It supports the
identical adif logbook in fldigi.  fllog can act as a server to multiple
clients over LAN/WAN tcpip connections.  Multiple fldigi / flwkey clients
may connect to the fllog server.

%package bin
Summary: bin components for the fllog package.
Group: Binaries
Requires: fllog-data = %{version}-%{release}
Requires: fllog-license = %{version}-%{release}

%description bin
bin components for the fllog package.


%package data
Summary: data components for the fllog package.
Group: Data

%description data
data components for the fllog package.


%package license
Summary: license components for the fllog package.
Group: Default

%description license
license components for the fllog package.


%prep
%setup -q -n fllog-1.2.6
cd %{_builddir}/fllog-1.2.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1604357225
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1604357225
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/fllog
cp %{_builddir}/fllog-1.2.6/COPYING %{buildroot}/usr/share/package-licenses/fllog/b47456e2c1f38c40346ff00db976a2badf36b5e3
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/fllog

%files data
%defattr(-,root,root,-)
/usr/share/applications/fllog.desktop
/usr/share/pixmaps/fllog.xpm

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/fllog/b47456e2c1f38c40346ff00db976a2badf36b5e3
