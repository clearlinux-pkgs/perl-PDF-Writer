#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-PDF-Writer
Version  : 0.06
Release  : 1
URL      : https://cpan.metacpan.org/authors/id/R/RK/RKINYON/PDF-Writer-0.06.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/R/RK/RKINYON/PDF-Writer-0.06.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libp/libpdf-writer-perl/libpdf-writer-perl_0.06-1.debian.tar.xz
Summary  : PDF writer abstraction layer
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-PDF-Writer-man

%description
PDF::Writer version 0.01
===========================
See the individual module documentation for more information

%package man
Summary: man components for the perl-PDF-Writer package.
Group: Default

%description man
man components for the perl-PDF-Writer package.


%prep
tar -xf %{SOURCE1}
cd ..
%setup -q -n PDF-Writer-0.06
mkdir -p %{_topdir}/BUILD/PDF-Writer-0.06/deblicense/
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
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.26.1/PDF/Writer.pm
/usr/lib/perl5/site_perl/5.26.1/PDF/Writer/mock.pm
/usr/lib/perl5/site_perl/5.26.1/PDF/Writer/pdfapi2.pm
/usr/lib/perl5/site_perl/5.26.1/PDF/Writer/pdflib.pm

%files man
%defattr(-,root,root,-)
/usr/share/man/man3/PDF::Writer.3
/usr/share/man/man3/PDF::Writer::pdfapi2.3
/usr/share/man/man3/PDF::Writer::pdflib.3
