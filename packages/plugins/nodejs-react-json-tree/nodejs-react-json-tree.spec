%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name react-json-tree

Name: %{?scl_prefix}nodejs-react-json-tree
Version: 0.11.0
Release: 4%{?dist}
Summary: React JSON Viewer Component, Extracted from redux-devtools
License: MIT
Group: Development/Libraries
URL: https://github.com/chibicode/react-json-tree
Source0: https://registry.npmjs.org/babel-runtime/-/babel-runtime-6.26.0.tgz
Source1: https://registry.npmjs.org/base16/-/base16-1.0.0.tgz
Source2: https://registry.npmjs.org/core-js/-/core-js-2.6.9.tgz
Source3: https://registry.npmjs.org/js-tokens/-/js-tokens-4.0.0.tgz
Source4: https://registry.npmjs.org/lodash.curry/-/lodash.curry-4.1.1.tgz
Source5: https://registry.npmjs.org/lodash.flow/-/lodash.flow-3.5.0.tgz
Source6: https://registry.npmjs.org/loose-envify/-/loose-envify-1.4.0.tgz
Source7: https://registry.npmjs.org/object-assign/-/object-assign-4.1.1.tgz
Source8: https://registry.npmjs.org/prop-types/-/prop-types-15.7.2.tgz
Source9: https://registry.npmjs.org/pure-color/-/pure-color-1.3.0.tgz
Source10: https://registry.npmjs.org/react-base16-styling/-/react-base16-styling-0.5.3.tgz
Source11: https://registry.npmjs.org/react-is/-/react-is-16.10.2.tgz
Source12: https://registry.npmjs.org/react-json-tree/-/react-json-tree-0.11.0.tgz
Source13: https://registry.npmjs.org/regenerator-runtime/-/regenerator-runtime-0.11.1.tgz
Source14: nodejs-react-json-tree-%{version}-registry.npmjs.org.tgz
%if 0%{?scl:1}
BuildRequires: %{?scl_prefix_nodejs}npm
%else
BuildRequires: nodejs-packaging
BuildRequires: npm
%endif
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

Provides: %{?scl_prefix}npm(%{npm_name}) = %{version}
Provides: bundled(npm(babel-runtime)) = 6.26.0
Provides: bundled(npm(base16)) = 1.0.0
Provides: bundled(npm(core-js)) = 2.6.9
Provides: bundled(npm(js-tokens)) = 4.0.0
Provides: bundled(npm(lodash.curry)) = 4.1.1
Provides: bundled(npm(lodash.flow)) = 3.5.0
Provides: bundled(npm(loose-envify)) = 1.4.0
Provides: bundled(npm(object-assign)) = 4.1.1
Provides: bundled(npm(prop-types)) = 15.7.2
Provides: bundled(npm(pure-color)) = 1.3.0
Provides: bundled(npm(react-base16-styling)) = 0.5.3
Provides: bundled(npm(react-is)) = 16.10.2
Provides: bundled(npm(react-json-tree)) = 0.11.0
Provides: bundled(npm(regenerator-runtime)) = 0.11.1
AutoReq: no
AutoProv: no

%if 0%{?scl:1}
%define npm_cache_dir npm_cache
%else
%define npm_cache_dir /tmp/npm_cache_%{name}-%{version}-%{release}
%endif

%description
%{summary}

%prep
mkdir -p %{npm_cache_dir}
%{?scl:scl enable %{?scl_nodejs} - << \end_of_scl}
for tgz in %{sources}; do
  echo $tgz | grep -q registry.npmjs.org || npm cache add --cache %{npm_cache_dir} $tgz
done
%{?scl:end_of_scl}

%setup -T -q -a 14 -D -n %{npm_cache_dir}

%build
%{?scl:scl enable %{?scl_nodejs} - << \end_of_scl}
npm install --cache-min Infinity --cache %{?scl:../}%{npm_cache_dir} --no-shrinkwrap --no-optional --global-style true %{npm_name}@%{version}
%{?scl:end_of_scl}

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/lib %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%clean
rm -rf %{buildroot} %{npm_cache_dir}

%files
%{nodejs_sitelib}/%{npm_name}
%license node_modules/%{npm_name}/LICENSE.md
%doc node_modules/%{npm_name}/CHANGELOG.md
%doc node_modules/%{npm_name}/CODE_OF_CONDUCT.md
%doc node_modules/%{npm_name}/README.md

%changelog
* Mon Apr 20 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.11.0-4
- Add npm to buildrequires for el8

* Tue Oct 22 2019 Eric D. Helms <ericdhelms@gmail.com> - 0.11.0-3
- Build for SCL

* Sun Oct 06 2019 Eric D. Helms <ericdhelms@gmail.com> - 0.11.0-2
- Update to allow building for SCL

* Wed Apr 18 2018 Daniel Lobato Garcia <me@daniellobato.me> 0.11.0-1
- Add nodejs-react-json-tree generated by npm2rpm using the bundle strategy
