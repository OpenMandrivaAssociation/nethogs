Summary:	Top-like monitor for network traffic
Name:		nethogs
Version:	0.8.7
Release:	2
Group:		Monitoring
License:	GPL+
URL:		https://github.com/raboof/nethogs
# git clone https://github.com/raboof/nethogs.git
# git archive --format=tar --prefix nethogs-0.8.2-$(date +%Y%m%d)/ HEAD | xz -vf > nethogs-0.8.2-$(date +%Y%m%d).tar.xz
Source0:	https://github.com/raboof/nethogs/archive/v%{version}.tar.gz
BuildRequires:	ncurses-devel
BuildRequires:	pcap-devel

%description
NetHogs is a small "net top" tool.

Instead of breaking the traffic down per protocol or per subnet, like
most such tools do, it groups bandwidth by process and does not rely
on a special kernel module to be loaded.

So if there's suddenly a lot of network traffic, you can fire up
NetHogs and immediately see which PID is causing this, and if it's
some kind of spinning process, kill it.

Features:
- shows TCP download- and upload-speed per process
- supports both IPv4 and IPv6
- supports both Ethernet and PPP

%prep

%setup -q
%build

%make CFLAGS="%{optflags}" CXXFLAGS="%{optflags}" CC=%{__cc} CXX=%{__cxx}

%install
install -d %{buildroot}%{_sbindir}
install -m0755 src/nethogs %{buildroot}%{_sbindir}/

install -d %{buildroot}%{_mandir}/man8
install -m0644 doc/nethogs.8 %{buildroot}%{_mandir}/man8/

%files
%doc DESIGN
%{_sbindir}/nethogs
%{_mandir}/man*/*
