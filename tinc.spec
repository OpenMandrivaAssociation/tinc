Name:           tinc
Version:	1.0.36
Release:	2
Summary:        A virtual private network daemon
Group:          System/Configuration/Networking
License:        GPLv2+
URL:            http://www.tinc-vpn.org/
Source0:        http://www.tinc-vpn.org/packages/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig(openssl)
BuildRequires:  lzo-devel
BuildRequires:  pkgconfig(zlib)

Requires(post):  info
Requires(preun): info


%description
tinc is a Virtual Private Network (VPN) daemon that uses tunnelling
and encryption to create a secure private network between hosts on
the Internet. Because the tunnel appears to the IP level network
code as a normal network device, there is no need to adapt any
existing software. This tunnelling allows VPN sites to share
information with each other over the Internet without exposing any
information to others.


%prep
%autosetup -p1 


%build
%configure
%make_build

%install
%make_install
#rm -f %{buildroot}%{_infodir}/dir

%files
%doc AUTHORS COPYING COPYING.README NEWS README THANKS doc/sample* doc/*.tex
%{_mandir}/man*/%{name}*.*
%{_infodir}/tinc.info.*
%{_sbindir}/%{name}d
