%define upstream_name    Module-Inspector
Name:		perl-%{upstream_name}
Version:	1.05
Release:	7

Summary:	An integrated API for inspecting Perl distributions 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/Module-Inspector
Source0:	https://cpan.metacpan.org/authors/id/A/AD/ADAMK/Module-Inspector-%{version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildArch:	noarch

%description
An integrated API for inspecting Perl distributions 

%prep
%setup -q -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# Do not make test because they need gtk display
#make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 1.50.0-2mdv2011.0
+ Revision: 655053
- rebuild for updated spec-helper

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 1.50.0-1mdv2011.0
+ Revision: 403864
- rebuild using %1.05 Sat Aug 30 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.05-1mdv2009.0
+ Revision: 277610
- Add description
- import perl-Module-Inspector


