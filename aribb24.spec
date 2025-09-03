%global git 20160216

Name:           aribb24
Version:        1.0.3%{git}
Release:        1
Summary:        A library for ARIB STD-B24
License:        LGPL-3.0-only
URL:            https://github.com/nkoriyama/%{name}

Source0:        https://github.com/nkoriyama/aribb24/archive/refs/heads/aribb24-master.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig(libpng)

%description
A library for ARIB STD-B24, decoding JIS 8 bit characters and parsing MPEG-TS
stream.

%package devel
Summary:        Development files for the ARIB STD-B24 library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files and headers for the ARIB STD-B24 library.

%prep
%autosetup -p1 -n %{name}-master

%build
export LDFLAGS="$LDFLAGS -lm"
autoreconf -vif
%configure --disable-static
%make_build

%install
%make_install
rm -f %{buildroot}%{_libdir}/lib%{name}.la

# Pick docs in the files section
rm -fr %{buildroot}%{_docdir}/%{name}

%files
%license COPYING
%doc README.md
%{_libdir}/lib%{name}.so.0
%{_libdir}/lib%{name}.so.0.0.0

%files devel
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
