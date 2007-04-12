
Summary:		Top-like monitor for network traffic
Name:			nethogs
Version:		0.6.1
Release:		%mkrel 0.cvs20050321.6
Source:			http://osdn.dl.sourceforge.net/sourceforge/nethogs/%{name}-%{version}.tar.bz2
URL:			http://nethogs.sourceforge.net
Group:			Monitoring
License:		GPL
BuildRoot:		%{_tmppath}/build-%{_name}-%{_version}
BuildRequires:          ncurses-devel
BuildRequires:          libpcap-devel

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
%setup -q -n "nethogs"

%build
%make

%install
%{__rm} -rf "${RPM_BUILD_ROOT}"

%{__mkdir_p} "${RPM_BUILD_ROOT}%{_sbindir}"
%{__install} -m 0755 -s nethogs "${RPM_BUILD_ROOT}%{_sbindir}/"

%{__mkdir_p} "${RPM_BUILD_ROOT}%{_mandir}/man8"
%{__install} -m 0644 nethogs.8 "${RPM_BUILD_ROOT}%{_mandir}/man8/"

%clean
%{__rm} -rf "${RPM_BUILD_ROOT}"

%files
%defattr(-,root,root)
%doc Changelog DESIGN README
%{_sbindir}/nethogs
%{_mandir}/man*/*


