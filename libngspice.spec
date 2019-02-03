Name:           libngspice
Version:        28
Release:        101%{?dist}
Summary:        Shared libraries for ngspice

License:        BSD
URL:            http://ngspice.sourceforge.net

Source0:        https://github.com/aimylios/fedora-libngspice-packaging/raw/master/ngspice-%{version}.tar.gz
Source1:        https://github.com/aimylios/fedora-libngspice-packaging/raw/master/ng_adms_va.tar.gz

BuildRequires:  libGL-devel
BuildRequires:  libICE-devel
BuildRequires:  libpng-devel
BuildRequires:  libXaw-devel
BuildRequires:  libXext-devel
BuildRequires:  libXt-devel
BuildRequires:  readline-devel
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  bison
BuildRequires:  byacc
BuildRequires:  flex
BuildRequires:  libtool
BuildRequires:  mot-adms

Requires:       ngspice

%description
Ngspice is a general-purpose circuit simulator program.
This package contains the shared libraries for ngspice.

%package devel
Summary:        Headers for libngspice
License:        BSD
Requires:       libngspice

%description devel
Ngspice is a general-purpose circuit simulator program.
This package contains the header files for ngspice.

%prep
%setup -q -n ngspice-%{version} -a 1
export ACLOCAL_FLAGS=-Im4
./autogen.sh --adms

%build
%configure \
    --disable-silent-rules \
    --with-ngshared \
    --enable-adms \
    --enable-xspice \
    --enable-maintainer-mode \
    --enable-dependency-tracking \
    --enable-cider \
    --enable-openmp \
    --enable-predictor \
    --enable-shared \
    --with-readline=yes \
    --libdir=%{_libdir} \
    --enable-oldapps
%make_build

%install
%make_install

%files
%exclude %{_bindir}
%exclude %{_datadir}
%exclude %{_mandir}
%exclude %{_libdir}/ngspice
%{_libdir}/%{name}.so.*
%license COPYING

%files devel
%{_includedir}/ngspice/
%{_libdir}/%{name}.la
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/ngspice.pc

%changelog
* Sun Feb 03 2019 Aimylios <aimylios@xxx.xx> - 28-101
- Fix location and ownership of files and folders
- Synchronise options to the new upstream package of libngspice

* Mon Jul 16 2018 Aimylios <aimylios@xxx.xx> - 28-100
- Update to ngspice 28

* Fri Mar 16 2018 Aimylios <aimylios@xxx.xx> - 27-101
- Add License and Requires tags for devel package

* Sun Feb 25 2018 Aimylios <aimylios@xxx.xx> - 27-100
- Initial release based on ngspice-27-2.fc28
