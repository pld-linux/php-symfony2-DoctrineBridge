%define		package	DoctrineBridge
%define		php_min_version 5.3.9
%include	/usr/lib/rpm/macros.php
Summary:	Symfony2 Doctrine Bridge
Name:		php-symfony2-DoctrineBridge
Version:	2.7.7
Release:	1
License:	MIT
Group:		Development/Languages/PHP
Source0:	https://github.com/symfony/%{package}/archive/v%{version}/%{package}-%{version}.tar.gz
# Source0-md5:	79dd758c2a1456b4f7c75d8cc456e012
URL:		https://github.com/symfony/DoctrineBridge
BuildRequires:	phpab
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php(core) >= %{php_min_version}
Requires:	php(date)
Requires:	php(hash)
Requires:	php(json)
Requires:	php(mbstring)
Requires:	php(pcre)
Requires:	php(spl)
Requires:	php-dirs >= 1.6
#Requires:	php-doctrine-common >= 2.4
#Suggests:	php-doctrine-data-fixtures
#Suggests:	php-doctrine-dbal >= 2.4
#Suggests:	php-doctrine-orm >= 2.4.5
Suggests:	php-symfony2-Form
Suggests:	php-symfony2-Validator
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides integration for Doctrine with various Symfony2 components.

%prep
%setup -q -n doctrine-bridge-%{version}

%build
phpab -n -e '*/Tests/*' -o autoload.php .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_data_dir}/Symfony/Bridge/Doctrine
cp -a *.php */ $RPM_BUILD_ROOT%{php_data_dir}/Symfony/Bridge/Doctrine
rm -r $RPM_BUILD_ROOT%{php_data_dir}/Symfony/Bridge/Doctrine/Tests

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE README.md
%dir %{php_data_dir}/Symfony/Bridge/Doctrine
%{php_data_dir}/Symfony/Bridge/Doctrine/*.php
%{php_data_dir}/Symfony/Bridge/Doctrine/CacheWarmer
%{php_data_dir}/Symfony/Bridge/Doctrine/DataCollector
%{php_data_dir}/Symfony/Bridge/Doctrine/DataFixtures
%{php_data_dir}/Symfony/Bridge/Doctrine/DependencyInjection
%{php_data_dir}/Symfony/Bridge/Doctrine/ExpressionLanguage
%{php_data_dir}/Symfony/Bridge/Doctrine/Form
%{php_data_dir}/Symfony/Bridge/Doctrine/HttpFoundation
%{php_data_dir}/Symfony/Bridge/Doctrine/Logger
%{php_data_dir}/Symfony/Bridge/Doctrine/Security
%{php_data_dir}/Symfony/Bridge/Doctrine/Test
%{php_data_dir}/Symfony/Bridge/Doctrine/Validator
