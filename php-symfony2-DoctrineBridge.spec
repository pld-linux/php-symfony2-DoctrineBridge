%define		pearname	DoctrineBridge
%define		php_min_version 5.3.3
%include	/usr/lib/rpm/macros.php
Summary:	Symfony2 Doctrine Bridge
Name:		php-symfony2-DoctrineBridge
Version:	2.4.8
Release:	1
License:	MIT
Group:		Development/Languages/PHP
Source0:	https://github.com/symfony/%{pearname}/archive/v%{version}/%{pearname}-%{version}.tar.gz
# Source0-md5:	30c1f6d4f26b6817d0dcb911742e52bd
URL:		https://github.com/symfony/DoctrineBridge
BuildRequires:	phpab
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php(core) >= %{php_min_version}
Requires:	php(date)
Requires:	php(hash)
Requires:	php(json)
Requires:	php(mbstring)
Requires:	php(pcre)
Requires:	php(spl)
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
%setup -q -n %{pearname}-%{version}

%build
phpab -n -e '*/Tests/*' -o autoloader.php .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/Symfony/Bridge/Doctrine
cp -a *.php */ $RPM_BUILD_ROOT%{php_pear_dir}/Symfony/Bridge/Doctrine
rm -r $RPM_BUILD_ROOT%{php_pear_dir}/Symfony/Bridge/Doctrine/Tests

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE README.md
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
