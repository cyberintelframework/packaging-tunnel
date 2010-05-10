Summary: perl Net::DHCP libraries
Name: perl-Net-DHCP
Version: 0.66
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-DHCP/
Source: http://www.cpan.org/modules/by-module/Net/Net-DHCP-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch
BuildRequires: perl
 
%description
Net::DHCP is a DHCP set of classes designed to handle basic DHCP handling. It can be used to develop either client, server or relays.
It is composed of 100% pure Perl.
 
The author invites feedback on Net::DHCP. If there's something you'd like to have added, please let me know.  If you find a bug, please send me the information described in the BUGS section below.
 
The original version of this module was written by Francis van Dun, and has been deeply reorganized.
 
%prep
%setup -n %{real_name}-%{version}
 
%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}
 
%install
%{__rm} -rf %{buildroot}
%{__make} pure_install
 
### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;
 
%clean
%{__rm} -rf %{buildroot}
 
%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Net::DHCP::Constants.3pm*
%doc %{_mandir}/man3/Net::DHCP::Packet.3pm*
%dir %{perl_vendorlib}/Net/
%{perl_vendorlib}/Net/DHCP/Constants.pm
%{perl_vendorlib}/Net/DHCP/Packet.pm
 
%changelog
* Mon Apr 27 2010 Ernest Neijenhuis <ernest utreg net> - 0.66-1
- Initial package.

