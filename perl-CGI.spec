Name:           perl-CGI
Summary:        Handle Common Gateway Interface requests and responses
Version:        3.63
Release:        3%{?dist}
License:        (GPL+ or Artistic) and Artistic 2.0
Group:          Development/Libraries
Source0:        http://search.cpan.org/CPAN/authors/id/M/MA/MARKSTOS/CGI.pm-%{version}.tar.gz
URL:            http://search.cpan.org/dist/CGI
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-requires:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(FCGI) >= 0.67
BuildRequires:  perl(File::Spec) >= 0.82
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Apache modules are optional
# Tests:
BuildRequires:  perl(Config)
BuildRequires:  perl(Encode)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  perl(utf8)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(FCGI) >= 0.67
Requires:       perl(File::Spec) >= 0.82
Obsoletes:      %{name}-tests <= 3.49

%{?perl_default_filter}
# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((FCGI|File::Spec)\\)$
# Remove false provides
%global __provides_exclude %{?__provides_exclude:__provides_exclude|}^perl\\((Fh|MultipartBuffer)\\)$

%description
CGI.pm is a stable, complete and mature solution for processing and preparing
HTTP requests and responses. Major features including processing form
submissions, file uploads, reading and writing cookies, query string
generation and manipulation, and processing and preparing HTTP headers. Some
HTML generation utilities are included as well.

CGI.pm performs very well in in a vanilla CGI.pm environment and also comes 
with built-in support for mod_perl and mod_perl2 as well as FastCGI.

%prep
%setup -q -n CGI.pm-%{version}
iconv -f iso8859-1 -t utf-8 < Changes > Changes.1
mv Changes.1 Changes
sed -i 's?usr/bin perl?usr/bin/perl?' t/init.t

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc cgi_docs.html Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
* Mon Jun 24 2013 Jitka Plesnikova <jplesnik@redhat.com> - 3.63-3
- Specify all dependencies
- Update License - CGI.pm is distributed under GPL and Artistic 2.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.63-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Nov 15 2012 Petr Pisar <ppisar@redhat.com> - 3.63-1
- 3.63 bump

* Wed Nov 14 2012 Petr Pisar <ppisar@redhat.com> - 3.62-1
- 3.62 bump

* Tue Nov 06 2012 Petr Šabata <contyk@redhat.com> - 3.61-1
- 3.61 bump, no code changes

* Fri Aug 17 2012 Petr Pisar <ppisar@redhat.com> - 3.60-1
- 3.60 bump

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.51-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 06 2012 Petr Pisar <ppisar@redhat.com> - 3.51-7
- Perl 5.16 rebuild

* Fri Jun 01 2012 Petr Pisar <ppisar@redhat.com> - 3.51-6
- Clean spec file
- Specify all dependencies

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.51-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jul 22 2011 Petr Pisar <ppisar@redhat.com> - 3.51-4
- RPM 4.9 dependency filtering added

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 3.51-3
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.51-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 20 2011 Marcela Mašláňová <mmaslano@redhat.com> 3.51-1
- update to fix CVE-2010-2761

* Mon Nov 29 2010 Marcela Mašláňová <mmaslano@redhat.com> 3.50-2
- remove -test sub-package, which would be needed also in perl-core

* Mon Nov 29 2010 Marcela Mašláňová <mmaslano@redhat.com> 3.50-1
- initial dual-life package

