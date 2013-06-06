%define upstream_name    Vim-Tag
%define upstream_version 1.110690
Name:		perl-%{upstream_name}
Version:	%perl_convert_version 1.110690
Release:	1

Summary:	Generate perl tags for vim
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Vim/Vim-Tag-1.110690.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Class::Accessor)
BuildRequires:	perl(Class::Accessor::Constructor)
BuildRequires:	perl(Class::Accessor::Installer)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(File::Find::Upwards)
BuildRequires:	perl(Getopt::Attribute)
BuildRequires:	perl(Getopt::Inherited)
BuildRequires:	perl(Hash::Rename)
BuildRequires:	perl(Test::Compile)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(UNIVERSAL::require)
BuildRequires:	perl(URI::Escape)

BuildArch:	noarch

%description
Manage tags for perl code in vim, with ideas on integrating tags with the
bash programmable completion project. See the synopsis.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{_mandir}/man1/*
%{perl_vendorlib}/*
%{_bindir}/ptag*

%changelog
* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 1.100.880-2mdv2011.0
+ Revision: 654345
- rebuild for updated spec-helper

* Tue Mar 30 2010 Jérôme Quelin <jquelin@mandriva.org> 1.100.880-1mdv2011.0
+ Revision: 529785
- update to 1.100880

* Mon Feb 08 2010 Jérôme Quelin <jquelin@mandriva.org> 0.40.0-1mdv2010.1
+ Revision: 502200
- packaging all files in %%bindir
- adding missing requires:
- update to 0.04
- update to 0.03

* Tue Dec 08 2009 Jérôme Quelin <jquelin@mandriva.org> 0.30.0-1mdv2010.1
+ Revision: 474765
- update to 0.03

* Thu Sep 17 2009 Jérôme Quelin <jquelin@mandriva.org> 0.20.0-1mdv2010.0
+ Revision: 444066
- import perl-Vim-Tag


* Thu Sep 17 2009 cpan2dist 0.02-1mdv
- initial mdv release, generated with cpan2dist

