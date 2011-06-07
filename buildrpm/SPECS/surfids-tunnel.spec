Summary: The tunnel server for the SURFids framework.
Name: surfids-tunnel
Version: 3.02
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
Source: surfids-tunnel-3.02.tar.gz
URL: http://ids.surfnet.nl/
BuildRoot: /home/build/rpmbuild/surfids-tunnel/BUILDROOT/
Requires: vconfig, xinetd, httpd, perl, php, php-pgsql, perl-DBI, perl-DBD-Pg, gnupg, rrdtool, perl-rrdtool, openvpn <= 2.0.9, openssl, dhclient, iproute, iputils, sendmail, mod_ssl

%define surfinstall /opt/surfnetids
%define surfconfig /etc/surfnetids

%description
The tunnel component of the SURFids framework.

%prep
%setup -q
%install
rm -rf %{_buildroot}
# Create surfnetids directories
install -m 755 -d %{_buildroot}%{surfinstall}
install -m 755 -d %{_buildroot}%{surfconfig}
install	-m 755 -d %{_buildroot}/etc/cron.d/
install	-m 755 -d %{_buildroot}/var/log/
install	-m 755 -d %{_buildroot}/etc/httpd/conf.d/
mv -f * %{_buildroot}%{surfinstall}/
mv -f %{_buildroot}%{surfinstall}/surfnetids-tn.conf %{_buildroot}%{surfconfig}/
mv -f %{_buildroot}%{surfinstall}/surfnetids-tn-apache.conf %{_buildroot}%{surfconfig}/
mv -f %{_buildroot}%{surfinstall}/dhclient.conf %{_buildroot}%{surfconfig}/
mv -f %{_buildroot}%{surfinstall}/openvpn-server.conf %{_buildroot}%{surfconfig}/openvpn.conf

# install important files
install -m 644 %{_buildroot}%{surfinstall}/tunnel-cron.d %{_buildroot}/etc/cron.d/surfids-tunnel

%clean

%post
ln -s %{surfconfig}/surfnetids-tn-apache.conf /etc/httpd/conf.d/surfids-tunnel.conf

%files
%defattr(-,root,root,-)
# Directory
%dir %{surfinstall}
%dir %{surfconfig}
%attr(755,apache,adm) %{surfinstall}/clientkeys/
%attr(755,apache,adm) %{surfinstall}/serverkeys/
# All it's subcontents
%{surfinstall}/*
%config %{surfconfig}/surfnetids-tn.conf
%config %{surfconfig}/surfnetids-tn-apache.conf
%config %{surfconfig}/dhclient.conf
%config %{surfconfig}/openvpn.conf
# Misc config files
/etc/cron.d/surfids-tunnel
# surfids logfile
%attr(744,apache,adm) /var/log/surfids.log

%changelog
* Wed Aug 26 2009 SURFids Development Team <ids at, surfnet.nl> 3.02-1
- Fixed bug #176.
* Fri Aug 21 2009 SURFids Development Team <ids at, surfnet.nl> 3.01-1
- Fixed RSS bug. (#168)
* Wed Aug 19 2009 SURFids Development Team <ids at, surfnet.nl> 3.0-1
- Flash graphs.
- Centralized logging of all scripts via the webinterface (admin only).
- Sensor grouping.
- Mail reports with UTC time format.
- The ability to always let a mail report even if there's nothing to report. Useful for automated systems receiving the emails.
- Home page now configurable.
- Sensor status page now configurable.
