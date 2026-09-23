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
# System cjson and lz4. Crypto stays on upstream's bundled mbedtls:
# the GnuTLS switch leaves HAVE_MBEDTLS and HAVE_NETTLE unset and the
# SRP authenticator does not compile. c11 is required so glibc's
# _Generic strchr macro is not a pedantic error under -std=c99.
BuildOption:	-Dc_std=c11 -Dbuiltin_cjson=false -Dbuiltin_lz4=false -Dbuiltin_mbedtls=true -Dfallback_builtin=false -Dtest=false
BuildRequires:	pkgconfig(libcjson)
BuildRequires:	pkgconfig(liblz4)

%patchlist
librist-vcs-fallback.patch

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
