#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-PDF-Writer
Version  : 0.06
Release  : 27
URL      : https://cpan.metacpan.org/authors/id/R/RK/RKINYON/PDF-Writer-0.06.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/R/RK/RKINYON/PDF-Writer-0.06.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libp/libpdf-writer-perl/libpdf-writer-perl_0.06-1.debian.tar.xz
Summary  : PDF writer abstraction layer
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-PDF-Writer-license = %{version}-%{release}
Requires: perl-PDF-Writer-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
PDF::Writer version 0.01
===========================
See the individual module documentation for more information

%package dev
Summary: dev components for the perl-PDF-Writer package.
Group: Development
Provides: perl-PDF-Writer-devel = %{version}-%{release}
Requires: perl-PDF-Writer = %{version}-%{release}

%description dev
dev components for the perl-PDF-Writer package.


%package license
Summary: license components for the perl-PDF-Writer package.
Group: Default

%description license
license components for the perl-PDF-Writer package.


%package perl
Summary: perl components for the perl-PDF-Writer package.
Group: Default
Requires: perl-PDF-Writer = %{version}-%{release}

%description perl
perl components for the perl-PDF-Writer package.


%prep
%setup -q -n PDF-Writer-0.06
cd %{_builddir}
tar xf %{_sourcedir}/libpdf-writer-perl_0.06-1.debian.tar.xz
cd %{_builddir}/PDF-Writer-0.06
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/PDF-Writer-0.06/deblicense/

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
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-PDF-Writer
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-PDF-Writer/536ebc89587aa040e55f78494e91737ad4f5a68b
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
/usr/share/man/man3/PDF::Writer.3
/usr/share/man/man3/PDF::Writer::pdfapi2.3
/usr/share/man/man3/PDF::Writer::pdflib.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-PDF-Writer/536ebc89587aa040e55f78494e91737ad4f5a68b

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
