Name:           libngspice
Version:        27
Release:        100%{?dist}
Summary:        Shared libraries for ngspice

License:        BSD
URL:            http://ngspice.sourceforge.net

Source0:        https://downloads.sourceforge.net/project/ngspice/ng-spice-rework/ngspice/ngspice-%{version}.tar.gz

BuildRequires:  libGL-devel
BuildRequires:  libICE-devel
BuildRequires:  libpng-devel
BuildRequires:  libXaw-devel
BuildRequires:  libXext-devel
BuildRequires:  libXt-devel
BuildRequires:  readline-devel
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  bison
BuildRequires:  byacc
BuildRequires:  flex
BuildRequires:  mot-adms

Requires:       ngspice

%description
Ngspice is a general-purpose circuit simulator program.
This package contains the shared libraries for ngspice.

%package devel
Summary:        Headers for libngspice

%description devel
Ngspice is a general-purpose circuit simulator program.
This package contains the header files for ngspice.

%prep
%setup -q -n ngspice-%{version}
export ACLOCAL_FLAGS=-Im4
./autogen.sh --adms

%build
%configure \
    --disable-silent-rules \
    --with-ngshared \
    --disable-xgraph \
    --enable-adms \
    --enable-xspice \
    --enable-maintainer-mode \
    --enable-dependency-tracking \
    --enable-capzerobypass \
    --enable-cider \
    --enable-expdevices \
    --enable-intnoise \
    --enable-openmp \
    --enable-predictor \
    --enable-numparam \
    --enable-dot-global \
    --enable-shared \
    --enable-ndev \
    --with-readline=yes \
    --libdir=%{_libdir}
%make_build

%install
%make_install

%files
%exclude %{_bindir}
%exclude %{_datadir}
%exclude %{_mandir}
%exclude %{_libdir}/ngspice
%{_libdir}/%{name}.la
%{_libdir}/%{name}.so*
%license COPYING

%files devel
%{_includedir}

%changelog
* Sun Feb 25 2018 Aimylios <aimylios@gmx.de> - 27-100
- Initial release based on ngspice-27-2.fc28
