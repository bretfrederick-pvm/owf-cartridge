%global cartridgedir %{_libexecdir}/openshift/cartridges/owf

Summary:       Provides Ozone Widget Framework  support
Name:          owf-cartridge
Version: 0.8.2
Release:       1%{?dist}
Group:         Development/Frameworks
License:       ASL 2.0
URL:           http://www.owfgoss.org
Source0:       https://https://www.assembla.com/code/pvm-occp-engineering/git/nodes

Requires:      openshift-origin-cartridge-jbossews
Requires:      openshift-origin-cartridge-postgresql
%if 0%{?rhel}
Requires:      maven3
%endif
%if 0%{?fedora}
Requires:      maven
%endif
BuildRequires: jpackage-utils
BuildArch:     noarch

Obsoletes:  pvm-aif-cartridge-2.0.0
Obsoletes:  pvm-owf-cartridge-7.1.0


%description
Provides OWF7 support to OpenShift. (Cartridge Format V2)

%prep
%setup -q

%build
%__rm %{name}.spec

%install
%__mkdir -p %{buildroot}%{cartridgedir}
%__cp -r * %{buildroot}%{cartridgedir}

%post
# To modify an alternative you should:
# - remove the previous version if it's no longer valid
# - install the new version with an increased priority
# - set the new version as the default to be safe

%files
%dir %{cartridgedir}
%attr(0755,-,-) %{cartridgedir}/bin/
%attr(0755,-,-) %{cartridgedir}/hooks/
%{cartridgedir}
%doc %{cartridgedir}/README.md
%doc %{cartridgedir}/COPYRIGHT
%doc %{cartridgedir}/LICENSE

%changelog
* Fri Aug 02 2013 Unknown name 0.8.2-1
- 

* Fri Aug 02 2013 Bret Frederick 
- new package built with tito

