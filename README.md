
Ozone Widget Framework (OWF) Cartridge on OpenShift
===================

This git repository contains the source for the owf-cartridge RPM package.

Dependencies:
 - JBoss EWS-2.0
 - PostgreSQL-8.4

Provides:
 - Ozone Widget Framework 7
 - Ozone Widget Framework 8

Building the RPM package
------------------------
Prerequisites

* RHEL or Fedora with the "Development Tools" group installed

* The Tito rpm build tools
> yum install tito

* Git (if not already installed)
> yum install git
> git clone https://*yourusername*@bitbucket.org/pvm-engineering/openshift-cartridges.git
> cd  openshift-cartridges/owf-cartridge
> tito build --rpm --test

Tito will generate the rpm package in /tmp/tito/noarch/owf-cartridge{*}.rpm

Open Issues/Stories/Tasks
----------
See the component backlog @ https://pvm-engineering.atlassian.net/browse/OPENSHIFT/component/10000
