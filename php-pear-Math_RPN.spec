%include	/usr/lib/rpm/macros.php
%define         _class          Math
%define         _subclass       RPN
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - RPN (Reverse Polish Notation) support
Summary(pl):	%{_pearname} - obs³uga odwrotnej notacji polskiej (RPN)
Name:		php-pear-%{_pearname}
Version:	1.0
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	d49f7ce5aa6c800e9f890241edf0166e
URL:		http://pear.php.net/package/%{_pearname}/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
%{_pearname} provides an easy way to change given expression to RPN
(Reverse Polish Notation) and evaluate it.

This class has in PEAR status: %{_status}.

%description -l pl
Za pomoc± %{_pearname} mo¿na w ³atwy sposób zmieniæ dane wyra¿enie na
odwrotn± notacjê polsk± (RPN) oraz je obliczyæ.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_pear_dir}/%{_class}/*.php
