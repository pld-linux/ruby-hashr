#
# Conditional build:
%bcond_without	tests		# build without tests

%define	pkgname	hashr
Summary:	Simple Hash extension to make working with nested hashes
Name:		ruby-%{pkgname}
Version:	2.0.1
Release:	2
License:	MIT
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	3678d2cdfc0e1154d39e2e3c4216e7ef
URL:		http://github.com/svenfuchs/hashr
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
BuildRequires:	sed >= 4.0
%if %{with tests}
BuildRequires:	rubygem(rspec)
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Simple Hash extension to make working with nested hashes (e.g. for
configuration) easier and less error-prone.

%prep
%setup -q -n %{pkgname}-%{version}

%build
%__gem_helper spec

%if %{with tests}
rspec -Ilib -rspec_helper spec/
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_specdir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -p %{pkgname}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc MIT-LICENSE README.md
%{ruby_vendorlibdir}/%{pkgname}.rb
%{ruby_vendorlibdir}/%{pkgname}
%{ruby_specdir}/%{pkgname}-%{version}.gemspec
