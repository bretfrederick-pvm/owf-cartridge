%global cartridgedir %{_libexecdir}/openshift/cartridges/v2/owf/

Summary:       Provides OWF support for OpenShift
Name:          owf-cartridge
Version: 0.8.13
Release:       1%{?dist}
Group:         Development/Languages
License:       ASL 2.0
URL:           http://www.shadow-soft.com
Source0:       https://bitbucket.org/pvm-engineering/owf-cartridge/src
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
Provides the Ozone Widget Framework on  OpenShift. (Cartridge Format V2)

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

/usr/sbin/oo-admin-cartridge --action install -R -s %{cartridgedir}../
if [ -f /usr/sbin/oo-admin-broker-cache ]
then
    echo "clearing broker cache"
    /usr/sbin/oo-admin-broker-cache --clear --console
fi

%postun
/usr/sbin/oo-admin-cartridge --action erase --name owf --version 7.0 --cartridge_version 0.0.1
if [ -f /usr/sbin/oo-admin-broker-cache ]
then
    echo "clearing broker cache"
    /usr/sbin/oo-admin-broker-cache --clear --console
fi

%files
%dir %{cartridgedir}
%attr(0755,-,-) %{cartridgedir}/bin/
%attr(0755,-,-) %{cartridgedir}/hooks/
%{cartridgedir}
%doc %{cartridgedir}/README.md
%doc %{cartridgedir}/COPYRIGHT
%doc %{cartridgedir}/LICENSE

%changelog
* Sun Dec 08 2013 Bret Frederick <bret.frederick@patvmackinc.com> 0.8.13-1
- OS-40 #time 3h #comment finished dev.  moving to test
  (bret.frederick@patvmackinc.com)
- OS-40 #comment turn scaling off and create a new story for scaling
  (bret.frederick@patvmackinc.com)

* Sun Dec 08 2013 Bret Frederick <bret.frederick@patvmackinc.com> 0.8.12-1
- OS-40 #time 2h #comment redirect root context to owf
  (bret.frederick@patvmackinc.com)
- OS-40 #time 2h #comment refactored install to use OSE commands.  started
  removal of template application. (bret.frederick@patvmackinc.com)
- OS-40 #start-progress #time 1h #comment refactoring the current prototype
  cart for production and delivery to Shadow-Soft.  set it to scalable.
  removed the maven build.  removed the v8.0 owf.
  (bret.frederick@patvmackinc.com)

* Sun Nov 24 2013 Bret Frederick <bret.frederick@patvmackinc.com> 0.8.11-1
- OS-41 #time 4h #comment worked on getting CAS auth running.  requires the
  node cert & key to be stored in a keystore the app has access to.  need to
  work with RedHat on that one.  basic SSL task is mostly done, moving to test
  (bret.frederick@patvmackinc.com)

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
