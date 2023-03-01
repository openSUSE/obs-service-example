#
# spec file for package obs-service-example
#
# Copyright (c) 2023 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           obs-service-example
Version:        0.0.1
Release:        0
Summary:        Just an example service
# FIXME: Select a correct license from https://github.com/openSUSE/spec-cleaner#spdx-licenses
License:        GPL
URL:            https://github.com/M0ses/obs-service-example
Source:         %{name}-%{version}.tar.gz
Group:          Development/Tools/Building


%description
This service is just an example to document the OBS service
development process.

%prep
%setup -q

%install
%make_install

%post
%postun

%files
/usr/lib/obs/service/example
/usr/lib/obs/service/example.service

%changelog
