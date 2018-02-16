%global pypi_name tenacity

%if 0%{?fedora} >= 24
%global with_python3 1
%endif

Name:           python-tenacity
Version:        4.8.0
Release:        1%{?dist}
Summary:        Tenacity is a general purpose retrying library
License:        ASL 2.0
URL:            https://github.com/jd/tenacity
Source0:        https://pypi.io/packages/source/t/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%package -n python2-%{pypi_name}
Summary:         Tenacity is a general purpose retrying library
%{?python_provide:%python_provide python2-tenacity}

BuildRequires:    python-setuptools
BuildRequires:    python2-devel
BuildRequires:    python-pbr
BuildRequires:    python-futures >= 3.0
BuildRequires:    python-monotonic >= 0.6
BuildRequires:    python-six >= 1.9.0
BuildRequires:    python-tools

Requires:         python-futures >= 3.0
Requires:         python-monotonic >= 0.6
Requires:         python-six >= 1.9.0


%description -n python2-%{pypi_name}
 Tenacity is a general purpose retrying library

%if 0%{?with_python3}
%package -n python3-%{pypi_name}

Summary:          Tenacity is a general purpose retrying library
%{?python_provide:%python_provide python3-tenacity}

BuildRequires:    python3-setuptools
BuildRequires:    python3-devel
BuildRequires:    python3-pbr
BuildRequires:    python3-monotonic >= 0.6
BuildRequires:    python3-six >= 1.9.0
BuildRequires:    python3-tools

Requires:         python3-monotonic >= 0.6
Requires:         python3-six >= 1.9.0


%description -n python3-%{pypi_name}
Tenacity is a general-purpose retrying library, written in Python, to simplify
the task of adding retry behavior to just about anything. It originates from a
fork of Retrying. 

%endif

%description
Tenacity is a general-purpose retrying library, written in Python, to simplify
the task of adding retry behavior to just about anything. It originates from a
fork of Retrying.

%prep
%setup -q -n %{pypi_name}-%{version}

%build
%py2_build

%if 0%{?with_python3}
LANG=en_US.UTF-8 %py3_build
%endif

%install
%if 0%{?with_python3}
LANG=en_US.UTF-8 %py3_install
%endif
%py2_install
# Remove python3-only code (asyncio)
for file in async.py tests/test_async.py; do
  rm %{buildroot}/%{python2_sitelib}/%{pypi_name}/$file
done

%check
%if 0%{?with_python3}
# XXX: fails under python3
#%{__python3} setup.py test
%{__python3} -m unittest
%endif
%{__python2} setup.py test

%files -n python2-%{pypi_name}
%doc README.rst
%license LICENSE
%{python2_sitelib}/*

%if 0%{?with_python3}
%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/*
%endif


%changelog
* Fri Feb 16 2018 Pradeep Kilambi <pkilambi@redhat.com> - 4.8.0-1
- rebase to 4.8.0

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug  5 2017 Haïkel Guémar <hguemar@fedoraproject.org> - 4.4.0-1
- Upstream 4.4.0
- Run unit tests

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 3.2.1-2
- Rebuild for Python 3.6

* Thu Oct 06 2016 Pradeep Kilambi <pkilambi@redhat.com> - 3.2.1-1
- rebase to 3.2.1

* Wed Sep 07 2016 Pradeep Kilambi <pkilambi@redhat.com> - 3.0.0-1
- initial package release
