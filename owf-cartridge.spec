%global cartridgedir %{_libexecdir}/openshift/cartridges/v2/owf

Summary:       Provides OWF support
Name:          owf-cartridge
Version: 0.8.10
Release:       1%{?dist}
Group:         Development/Languages
License:       ASL 2.0
URL:           http://www.openshift.com
Source0:       http://mirror.openshift.com/pub/openshift-origin/source/%{name}/%{name}-%{version}.tar.gz
Requires:      rubygem(openshift-origin-node)
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

%description
Provides OWF support to OpenShift. (Cartridge Format V2)

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

%if 0%{?rhel}
alternatives --install /etc/alternatives/maven-3.0 maven-3.0 /usr/share/java/apache-maven-3.0.3 100
alternatives --set maven-3.0 /usr/share/java/apache-maven-3.0.3
%endif

%if 0%{?fedora}
alternatives --remove maven-3.0 /usr/share/java/apache-maven-3.0.3
alternatives --install /etc/alternatives/maven-3.0 maven-3.0 /usr/share/maven 102
alternatives --set maven-3.0 /usr/share/maven
%endif

/usr/sbin/oo-admin-cartridge -a install -s %{cartridgedir}
/usr/sbin/oo-admin-broker-cache -c --console

%postun
rm -rf /var/lib/openshift/.cartridge_repository/pvm-owf
/usr/sbin/oo-admin-broker-cache -c --console

%files
%dir %{cartridgedir}
%attr(0755,-,-) %{cartridgedir}/bin/
%attr(0755,-,-) %{cartridgedir}/hooks/
%{cartridgedir}
%doc %{cartridgedir}/README.md
%doc %{cartridgedir}/COPYRIGHT
%doc %{cartridgedir}/LICENSE

%changelog
* Sun Nov 24 2013 Bret Frederick <bret.frederick@patvmackinc.com> 0.8.10-1
- 

* Sun Nov 24 2013 Bret Frederick <bret.frederick@patvmackinc.com> 0.8.9-1
- OS-41 #comment added Valve to context.xml (bret.frederick@patvmackinc.com)

* Sat Nov 23 2013 Bret Frederick <bret.frederick@patvmackinc.com> 0.8.8-1
- new package built with tito after moving into own repo

* Mon Sep 23 2013 Bret Frederick <bret.frederick@patvmackinc.com> 0.8.7-1
- resolving OPENSHIFT-13
- OPENSHIFT-13 added template (bret.frederick@patvmackinc.com)
- OPENSHIFT-13 added seed-db (bret.frederick@patvmackinc.com)
- OPENSHIFT-13 #time 2h replaced template app with pvm branded one.  added owf
  seed-db.sql (bret.frederick@patvmackinc.com)
- OPENSHIFT-5 #time 3h #comment added STK generated .czml to demo folder in the
  cesium.war.  added coademo.html (coa analysis widget) to the sandcastle
  gallery with buttons to load .czml files.  updated owf seed.db with coa
  analysis widget (bret.frederick@patvmackinc.com)
- updated readme (bret.frederick@patvmackinc.com)
- updated readme (bret.frederick@patvmackinc.com)
- OPENSHIFT-11 #time 1h  #resolve completed and tested on local system
  (bret.frederick@patvmackinc.com)
- change owf 8 description (bret.frederick@patvmackinc.com)
- OPENSHIFT-11 moved owf.war to correct version
  (bret.frederick@patvmackinc.com)
- OPENSHIFT-11 #time 4h remove owf.war from template and added some logic to
  keep the cart provided owf app in place when deploying updates to the
  template app (bret.frederick@patvmackinc.com)

* Sat Aug 31 2013 Bret Frederick <bret.frederick@patvmackinc.com> 0.8.6-1
- new package built with tito
