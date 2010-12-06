Summary:	Top-like monitor for network traffic
Name:		nethogs
Version:	0.7.0
Release:	%mkrel 2
Group:		Monitoring
License:	GPL+
URL:		http://nethogs.sourceforge.net
Source0:	http://osdn.dl.sourceforge.net/sourceforge/nethogs/%{name}-%{version}.tar.gz
BuildRequires:	ncurses-devel
BuildRequires:	pcap-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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

%setup -q -n nethogs

%build

%make CFLAGS="%{optflags}"

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_sbindir}
install -m0755 nethogs %{buildroot}%{_sbindir}/

install -d %{buildroot}%{_mandir}/man8
install -m0644 nethogs.8 %{buildroot}%{_mandir}/man8/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changelog DESIGN README
%{_sbindir}/nethogs
%{_mandir}/man*/*
