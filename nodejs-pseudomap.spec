%{?scl:%scl_package nodejs-rimraf}
%{!?scl:%global pkg_name %{name}}

%global npm_name pseudomap
%{?nodejs_find_provides_and_requires}

%global enable_tests 0

Name:		%{?scl_prefix}nodejs-pseudomap
Version:	1.0.2
Release:	1%{?dist}
Summary:	A thing that is a lot like ES6 `Map`, but without iterators, for use in environments where `for..of` syntax and `Map` are not available.
Url:		https://github.com/isaacs/pseudomap#readme
Source0:	https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
License:	ISC

BuildArch:	noarch
ExclusiveArch:	%{ix86} x86_64 %{arm} noarch

BuildRequires:	%{?scl_prefix}nodejs-devel

%if 0%{?enable_tests}
BuildRequires:	npm(tap)
%endif

%description
A thing that is a lot like ES6 `Map`, but without iterators, for use in environments where `for..of` syntax and `Map` are not available.

%prep
%setup -q -n package

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}

cp -pr package.json map.js pseudomap.js \
	%{buildroot}%{nodejs_sitelib}/%{npm_name}

%{nodejs_symlink_deps}

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
tap test/*.js
%endif

%files
%{nodejs_sitelib}/pseudomap

%doc README.md
%doc LICENSE

%changelog
* Thu Apr 07 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.2-1
- Initial build

