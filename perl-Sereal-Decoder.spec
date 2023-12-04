#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
#
Name     : perl-Sereal-Decoder
Version  : 5.004
Release  : 36
URL      : https://cpan.metacpan.org/authors/id/Y/YV/YVES/Sereal-Decoder-5.004.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/Y/YV/YVES/Sereal-Decoder-5.004.tar.gz
Summary  : 'Fast, compact, powerful binary deserialization'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Sereal-Decoder-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Sub::Uplevel)
BuildRequires : perl(Test::Deep)
BuildRequires : perl(Test::Differences)
BuildRequires : perl(Test::LongString)
BuildRequires : perl(Test::Warn)
BuildRequires : pkgconfig(libzstd)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
No detailed description available

%package dev
Summary: dev components for the perl-Sereal-Decoder package.
Group: Development
Provides: perl-Sereal-Decoder-devel = %{version}-%{release}
Requires: perl-Sereal-Decoder = %{version}-%{release}

%description dev
dev components for the perl-Sereal-Decoder package.


%package perl
Summary: perl components for the perl-Sereal-Decoder package.
Group: Default
Requires: perl-Sereal-Decoder = %{version}-%{release}

%description perl
perl components for the perl-Sereal-Decoder package.


%prep
%setup -q -n Sereal-Decoder-5.004
cd %{_builddir}/Sereal-Decoder-5.004

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test || :

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Sereal::Decoder.3
/usr/share/man/man3/Sereal::Performance.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
