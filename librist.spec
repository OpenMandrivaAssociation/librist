%define libname %mklibname librist
%define devname %mklibname librist -d

Name:		librist
Version:	0.2.20
Release:	1
Summary:	Library for the Reliable Internet Stream Transport protocol
License:	BSD-2-Clause
Group:		System/Libraries
URL:		https://code.videolan.org/rist/librist
Source0:	https://code.videolan.org/rist/librist/-/archive/v%{version}/librist-v%{version}.tar.gz
BuildSystem:	meson
%patchlist
librist-vcs-fallback.patch
# System cjson, lz4 and GnuTLS. Do not compile the bundled copies.
BuildOption:	-Dbuiltin_cjson=false -Dbuiltin_lz4=false -Dbuiltin_mbedtls=false -Duse_mbedtls=false -Duse_gnutls=true -Dfallback_builtin=false -Dtest=false
BuildRequires:	pkgconfig(libcjson)
BuildRequires:	pkgconfig(liblz4)
BuildRequires:	pkgconfig(gnutls)
BuildRequires:	pkgconfig(nettle)
BuildRequires:	pkgconfig(hogweed)
BuildRequires:	pkgconfig(gmp)

%description
libRIST implements the Video Services Forum TR-06 RIST protocol.
VLC's RIST access modules use this library.

%package -n %{libname}
Summary:	Reliable Internet Stream Transport library
Group:		System/Libraries

%description -n %{libname}
Shared library for the RIST protocol.

%package -n %{devname}
Summary:	Development files for librist
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	librist-devel = %{EVRD}

%description -n %{devname}
Headers and pkg-config file for building against librist.

%files
%license COPYING
%doc README.md NEWS
%{_bindir}/ristsender
%{_bindir}/ristreceiver
%{_bindir}/rist2rist
%{_bindir}/udp2udp
%{_bindir}/risttunnel
%{_bindir}/ristsrppasswd

%files -n %{libname}
%{_libdir}/liblibrist.so.*

%files -n %{devname}
%{_includedir}/librist/
%{_libdir}/pkgconfig/librist.pc
%{_libdir}/liblibrist.so
