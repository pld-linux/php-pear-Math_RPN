%include	/usr/lib/rpm/macros.php
%define		_class		Math
%define		_subclass	RPN
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - RPN (Reverse Polish Notation) support
Summary(pl.UTF-8):	%{_pearname} - obsługa odwrotnej notacji polskiej (RPN)
Name:		php-pear-%{_pearname}
Version:	1.1.1
Release:	3
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	5e121f83444d826ba006f0d6bff70295
URL:		http://pear.php.net/package/Math_RPN/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
%{_pearname} provides an easy way to change given expression to RPN
(Reverse Polish Notation) and evaluate it.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Za pomocą %{_pearname} można w łatwy sposób zmienić dane wyrażenie na
odwrotną notację polską (RPN) oraz je obliczyć.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
