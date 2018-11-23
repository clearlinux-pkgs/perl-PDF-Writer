#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-PDF-Writer
Version  : 0.06
Release  : 4
URL      : https://cpan.metacpan.org/authors/id/R/RK/RKINYON/PDF-Writer-0.06.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/R/RK/RKINYON/PDF-Writer-0.06.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libp/libpdf-writer-perl/libpdf-writer-perl_0.06-1.debian.tar.xz
Summary  : PDF writer abstraction layer
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-PDF-Writer-license = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
PDF::Writer version 0.01
===========================
See the individual module documentation for more information

%package dev
Summary: dev components for the perl-PDF-Writer package.
Group: Development
Provides: perl-PDF-Writer-devel = %{version}-%{release}

%description dev
dev components for the perl-PDF-Writer package.


%package license
Summary: license components for the perl-PDF-Writer package.
Group: Default

%description license
license components for the perl-PDF-Writer package.


%prep
%setup -q -n PDF-Writer-0.06
cd ..
%setup -q -T -D -n PDF-Writer-0.06 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/PDF-Writer-0.06/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-PDF-Writer
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-PDF-Writer/deblicense_copyright
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
/usr/lib/perl5/vendor_perl/5.28.0/PDF/Writer.pm
/usr/lib/perl5/vendor_perl/5.28.0/PDF/Writer/mock.pm
/usr/lib/perl5/vendor_perl/5.28.0/PDF/Writer/pdfapi2.pm
/usr/lib/perl5/vendor_perl/5.28.0/PDF/Writer/pdflib.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/PDF::Writer.3
/usr/share/man/man3/PDF::Writer::pdfapi2.3
/usr/share/man/man3/PDF::Writer::pdflib.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-PDF-Writer/deblicense_copyright
