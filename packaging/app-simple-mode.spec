
Name: app-simple-mode
Epoch: 1
Version: 1.1.1
Release: 1%{dist}
Summary: Simple Mode - Core
License: LGPLv3
Group: ClearOS/Libraries
Source: app-simple-mode-%{version}.tar.gz
Buildarch: noarch

%description
The Simple Mode app provides a standalone driver for the Central Management system.

%package core
Summary: Simple Mode - Core
Provides: system-mode-driver
Requires: app-base-core
Requires: app-mode-core >= 1:1.1.0

%description core
The Simple Mode app provides a standalone driver for the Central Management system.

This package provides the core API and libraries.

%prep
%setup -q
%build

%install
mkdir -p -m 755 %{buildroot}/usr/clearos/apps/simple_mode
cp -r * %{buildroot}/usr/clearos/apps/simple_mode/


%post core
logger -p local6.notice -t installer 'app-simple-mode-core - installing'

if [ $1 -eq 1 ]; then
    [ -x /usr/clearos/apps/simple_mode/deploy/install ] && /usr/clearos/apps/simple_mode/deploy/install
fi

[ -x /usr/clearos/apps/simple_mode/deploy/upgrade ] && /usr/clearos/apps/simple_mode/deploy/upgrade

exit 0

%preun core
if [ $1 -eq 0 ]; then
    logger -p local6.notice -t installer 'app-simple-mode-core - uninstalling'
    [ -x /usr/clearos/apps/simple_mode/deploy/uninstall ] && /usr/clearos/apps/simple_mode/deploy/uninstall
fi

exit 0

%files core
%defattr(-,root,root)
%exclude /usr/clearos/apps/simple_mode/packaging
%exclude /usr/clearos/apps/simple_mode/tests
%dir /usr/clearos/apps/simple_mode
/usr/clearos/apps/simple_mode/deploy
/usr/clearos/apps/simple_mode/language
/usr/clearos/apps/simple_mode/libraries
