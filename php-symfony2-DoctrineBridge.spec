%define		status		stable
%define		pearname	DoctrineBridge
%define		php_min_version 5.3.3
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - Symfony2 Doctrine Bridge
Name:		php-symfony2-DoctrineBridge
Version:	2.1.6
Release:	1
License:	MIT
Group:		Development/Languages/PHP
Source0:	http://pear.symfony.com/get/%{pearname}-%{version}.tgz
# Source0-md5:	e3ee8dc64a8fed866f96bc8d79ef4858
URL:		http://pear.symfony.com/package/DoctrineBridge/
BuildRequires:	php-channel(pear.symfony.com)
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php(core) >= %{php_min_version}
Requires:	php-channel(pear.symfony.com)
Requires:	php-pear >= 4:1.3.10
Suggests:	php-symfony2-Form
Suggests:	php-symfony2-Validator
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Symfony2 Doctrine Bridge

In PEAR status of this package is: %{status}.

%prep
%pear_package_setup

# no packaging of tests
rm -r .%{php_pear_dir}/Symfony/Bridge/Doctrine/Tests
rm .%{php_pear_dir}/Symfony/Bridge/Doctrine/phpunit.xml.dist

# fixups
mv .%{php_pear_dir}/Symfony/Bridge/Doctrine/CHANGELOG.md .
rm .%{php_pear_dir}/Symfony/Bridge/Doctrine/.gitattributes
mv docs/%{pearname}/Symfony/Bridge/Doctrine/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE README.md install.log
%{php_pear_dir}/.registry/.channel.*/*.reg
%dir %{php_pear_dir}/Symfony/Bridge/Doctrine
%{php_pear_dir}/Symfony/Bridge/Doctrine/*.php
%{php_pear_dir}/Symfony/Bridge/Doctrine/CacheWarmer
%{php_pear_dir}/Symfony/Bridge/Doctrine/DataCollector
%{php_pear_dir}/Symfony/Bridge/Doctrine/DataFixtures
%{php_pear_dir}/Symfony/Bridge/Doctrine/DependencyInjection
%{php_pear_dir}/Symfony/Bridge/Doctrine/Form
%{php_pear_dir}/Symfony/Bridge/Doctrine/HttpFoundation
%{php_pear_dir}/Symfony/Bridge/Doctrine/Logger
%{php_pear_dir}/Symfony/Bridge/Doctrine/Security
%{php_pear_dir}/Symfony/Bridge/Doctrine/Validator
