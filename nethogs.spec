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


%changelog
* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 0.7.0-2mdv2011.0
+ Revision: 613034
- the mass rebuild of 2010.1 packages

* Sat Jan 30 2010 JÃ©rÃ´me Brenier <incubusss@mandriva.org> 0.7.0-1mdv2010.1
+ Revision: 498609
- new version 0.7.0
- drop gcc43 patch
- fix License tag

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 0.6.1-0.cvs20050321.9mdv2010.0
+ Revision: 440317
- rebuild

* Wed Oct 29 2008 Oden Eriksson <oeriksson@mandriva.com> 0.6.1-0.cvs20050321.8mdv2009.1
+ Revision: 298623
- fix build
- rebuilt against libpcap-1.0.0

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Aug 25 2007 GaÃ«tan Lehmann <glehmann@mandriva.org> 0.6.1-0.cvs20050321.7mdv2008.0
+ Revision: 71332
- rebuild


* Wed Aug 09 2006 glehmann
+ 08/09/06 20:00:20 (55100)
rebuild

* Sun Jul 30 2006 glehmann
+ 07/30/06 10:26:06 (42698)
Import nethogs

* Tue May 09 2006 Gaetan Lehmann <gaetan.lehmann@jouy.inra.fr> 0.6.1-0.cvs20050321.5mdk
- fix readline BuildRequires

* Tue Apr 18 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.6.1-0.cvs20050321.4mdk
- Fix BuildRequires

* Thu Jul 28 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.6.1-0.cvs20050321.3mdk
- Fix BuildRequires

* Wed Jul 13 2005 Oden Eriksson <oeriksson@mandriva.com> 0.6.1-0.cvs20050321.2mdk
- rebuilt against new libpcap-0.9.1 (aka. a "play safe" rebuild)

* Mon Mar 21 2005 Gaetan Lehmann <gaetan.lehmann@jouy.inra.fr> 0.6.1-0.cvs20050321.1mdk
- mandrake contrib

* Fri Sep 17 2004 Pascal Bleser <guru@unixtech.be>
- version 0.6.0

* Sat Jun 12 2004 Pascal Bleser <guru@unixtech.be>
- new package

