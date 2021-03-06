%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name google-api-client
%global rubyabi 1.9.1

Summary: Google API Ruby Client makes it trivial to access supported APIs
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.6.4
Release: 1%{?dist}
Group: Development/Languages
License: ASL 2.0
URL: http://code.google.com/p/google-api-ruby-client/
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem

%if 0%{?fedora} > 18
Requires: %{?scl_prefix}ruby(release)
%else
Requires: %{?scl_prefix}ruby(abi) = %{rubyabi}
%endif
Requires: %{?scl_prefix}ruby(rubygems)
Requires: %{?scl_prefix}ruby
Requires: %{?scl_prefix}rubygem(addressable) >= 2.3.2
Requires: %{?scl_prefix}rubygem(autoparse) >= 0.3.3
Requires: %{?scl_prefix}rubygem(extlib) >= 0.9.15
Requires: %{?scl_prefix}rubygem(faraday) >= 0.8.4
Requires: %{?scl_prefix}rubygem(faraday) < 0.9.0
Requires: %{?scl_prefix}rubygem(jwt) >= 0.1.5
Requires: %{?scl_prefix}rubygem(launchy) >= 2.1.1
Requires: %{?scl_prefix}rubygem(multi_json) >= 1.0.0
Requires: %{?scl_prefix}rubygem(signet) >= 0.4.5
Requires: %{?scl_prefix}rubygem(signet) < 0.5.0
Requires: %{?scl_prefix}rubygem(uuidtools) >= 2.1.0

%if 0%{?fedora} > 18
BuildRequires: %{?scl_prefix}ruby(release)
%else
BuildRequires: %{?scl_prefix}ruby(abi) = %{rubyabi}
%endif
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}ruby
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
The Google API Ruby Client makes it trivial to discover and access supported
APIs.

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir .%{gem_dir} \
            --bindir .%{_bindir} \
            --force %{SOURCE0}
%{?scl:"}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%files
%dir %{gem_instdir}
%{_bindir}/google-api
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%doc %{gem_instdir}/LICENSE

%exclude %{gem_instdir}/Gemfile
%exclude %{gem_instdir}/Rakefile
%exclude %{gem_instdir}/spec
%exclude %{gem_instdir}/tasks

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/CONTRIB.md
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/README.md

%changelog
* Sun Nov 10 2013 Dominic Cleal <dcleal@redhat.com> 0.6.4-1
- new package built with tito

