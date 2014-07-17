%define		pearname	DoctrineBridge
%define		php_min_version 5.3.3
%include	/usr/lib/rpm/macros.php
Summary:	Symfony2 Doctrine Bridge
Name:		php-symfony2-DoctrineBridge
Version:	2.4.4
Release:	1
License:	MIT
Group:		Development/Languages/PHP
Source0:	http://pear.symfony.com/get/%{pearname}-%{version}.tgz
# Source0-md5:	d4b67f100526a2cc8909c7bbd58cfcea
URL:		https://github.com/symfony/DoctrineBridge
BuildRequires:	php-channel(pear.symfony.com)
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php(core) >= %{php_min_version}
Requires:	php(date)
Requires:	php(hash)
Requires:	php(json)
Requires:	php(mbstring)
Requires:	php(pcre)
Requires:	php(spl)
Requires:	php-channel(pear.symfony.com)
Requires:	php-pear >= 4:1.3.10
#Suggests:	php-doctrine-data-fixtures
#Suggests:	php-doctrine-dbal
#Suggests:	php-doctrine-orm
Suggests:	php-symfony2-Form
Suggests:	php-symfony2-Validator
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides integration for Doctrine with various Symfony2 components.

%prep
%pear_package_setup

# no packaging of tests
mv .%{php_pear_dir}/Symfony/Bridge/Doctrine/Tests .
mv .%{php_pear_dir}/Symfony/Bridge/Doctrine/phpunit.xml.dist .

# fixups
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
%{php_pear_dir}/Symfony/Bridge/Doctrine/ExpressionLanguage
%{php_pear_dir}/Symfony/Bridge/Doctrine/Form
%{php_pear_dir}/Symfony/Bridge/Doctrine/HttpFoundation
%{php_pear_dir}/Symfony/Bridge/Doctrine/Logger
%{php_pear_dir}/Symfony/Bridge/Doctrine/Security
%{php_pear_dir}/Symfony/Bridge/Doctrine/Test
%{php_pear_dir}/Symfony/Bridge/Doctrine/Validator
