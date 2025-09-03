%define libname %mklibname aribb24
%define devname %mklibname -d aribb24
%global git 20160216

Name:           aribb24
Version:        1.0.3.%{git}
Release:        2
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

%package -n %{libname}
Summary:        Shared library for %{name}

%description -n %{libname}
This package contains the shared library files.

%package -n %{devname}
Summary:        Development files for %{name}
Requires:	%{libname} = %{EVRD}
Provides:  aribb24-devel = %{EVRD}

%description -n %{devname}
This package contains development files for %{name}.

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

%files -n %{libname}
%license COPYING
%doc README.md
%{_libdir}/lib%{name}.so.0
%{_libdir}/lib%{name}.so.0.0.0

%files -n %{devname}
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
