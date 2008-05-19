%include	/usr/lib/rpm/macros.php
%define		_class		HTML
%define		_subclass	QuickForm_CAPTCHA
%define		_status		beta
%define		_pearname	HTML_QuickForm_CAPTCHA
Summary:	%{_pearname} - Drop-in CAPTCHA element for QuickForm forms
Summary(pl.UTF-8):	%{_pearname} - element CAPTCHA dla formularzy QuickForm
Name:		php-pear-%{_pearname}
Version:	0.3.0
Release:	2
License:	New BSD License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	7eb64ad3361323fa4806a7d937219804
URL:		http://pear.php.net/package/HTML_QuickForm_CAPTCHA/
BuildRequires:	php-pear-PEAR >= 1.7.1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Requires:	php-pear-HTML_QuickForm >= 3.2.7
Requires:	php-pear-PEAR-core >= 1.7.1
Requires:	php-pear-Text_CAPTCHA >= 0.3.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides QuickForm interface to the Text_CAPTCHA package.
It requires the use of a session to serialize a Text_CAPTCHA instance.
Currently drivers for Image, Equation, Figlet and Word are included.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Pakiet ten dostarcza interfejs QuickForm do pakietu Text_CAPTCHA.
Wymagane jest użycie sesji do serializacji instancji obiektu
Text_CAPTCHA. Aktualnie obsługiwane są sterowniki Image, Equation,
Figlet.

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
%doc install.log docs/HTML_QuickForm_CAPTCHA/docs/examples
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/HTML/QuickForm/CAPTCHA
%{php_pear_dir}/HTML/QuickForm/CAPTCHA.php
%{php_pear_dir}/HTML/QuickForm/Rule/CAPTCHA.php
