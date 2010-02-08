%define upstream_name    Vim-Tag
%define upstream_version 0.04

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Generate perl tags for vim
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Vim/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Find::Upwards)
BuildRequires: perl(Getopt::Attribute)
BuildRequires: perl(Getopt::Inherited)
BuildRequires: perl(Hash::Rename)
BuildRequires: perl(Test::Compile)
BuildRequires: perl(Test::More)
BuildRequires: perl(UNIVERSAL::require)

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
Manage tags for perl code in vim, with ideas on integrating tags with the
bash programmable completion project. See the synopsis.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*
%{_bindir}/ptags*
