# Generated by rust2rpm
%bcond_without check

%global crate bindgen

Name:           rust-%{crate}
Version:        0.47.0
Release:        1%{?dist}
Summary:        Automatically generates Rust FFI bindings to C and C++ libraries

# Upstream license specification: BSD-3-Clause
License:        BSD
URL:            https://crates.io/crates/bindgen
Source0:        https://crates.io/api/v1/crates/%{crate}/%{version}/download#/%{crate}-%{version}.crate

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging
BuildRequires:  (crate(bitflags/default) >= 1.0.3 with crate(bitflags/default) < 2.0.0)
BuildRequires:  (crate(cexpr/default) >= 0.3.3 with crate(cexpr/default) < 0.4.0)
BuildRequires:  (crate(cfg-if/default) >= 0.1.0 with crate(cfg-if/default) < 0.2.0)
BuildRequires:  (crate(clang-sys/clang_6_0) >= 0.27.0 with crate(clang-sys/clang_6_0) < 0.28.0)
BuildRequires:  (crate(clang-sys/default) >= 0.27.0 with crate(clang-sys/default) < 0.28.0)
BuildRequires:  (crate(clang-sys/runtime) >= 0.27.0 with crate(clang-sys/runtime) < 0.28.0)
BuildRequires:  (crate(clap/default) >= 2.0.0 with crate(clap/default) < 3.0.0)
BuildRequires:  (crate(env_logger/default) >= 0.6.0 with crate(env_logger/default) < 0.7.0)
BuildRequires:  (crate(hashbrown/default) >= 0.1.0 with crate(hashbrown/default) < 0.2.0)
BuildRequires:  (crate(lazy_static/default) >= 1.0.0 with crate(lazy_static/default) < 2.0.0)
BuildRequires:  (crate(log/default) >= 0.4.0 with crate(log/default) < 0.5.0)
BuildRequires:  (crate(peeking_take_while/default) >= 0.1.2 with crate(peeking_take_while/default) < 0.2.0)
BuildRequires:  (crate(proc-macro2) >= 0.4.0 with crate(proc-macro2) < 0.5.0)
BuildRequires:  (crate(quote) >= 0.6.0 with crate(quote) < 0.7.0)
BuildRequires:  (crate(regex/default) >= 1.0.0 with crate(regex/default) < 2.0.0)
BuildRequires:  (crate(which/default) >= 2.0.0 with crate(which/default) < 3.0.0)
%if %{with check}
BuildRequires:  (crate(clap/default) >= 2.0.0 with crate(clap/default) < 3.0.0)
BuildRequires:  (crate(diff/default) >= 0.1.0 with crate(diff/default) < 0.2.0)
BuildRequires:  (crate(shlex/default) >= 0.1.0 with crate(shlex/default) < 0.2.0)
%endif

%global _description \
Automatically generates Rust FFI bindings to C and C++ libraries.

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}

%description -n %{crate}
%{summary}.

%files       -n %{crate}
%license LICENSE
%doc README.md
%{_bindir}/bindgen

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE
%doc README.md
%{cargo_registry}/%{crate}-%{version}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+env_logger-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+env_logger-devel %{_description}

This package contains library source intended for building other packages
which use "env_logger" feature of "%{crate}" crate.

%files       -n %{name}+env_logger-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+log-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+log-devel %{_description}

This package contains library source intended for building other packages
which use "log" feature of "%{crate}" crate.

%files       -n %{name}+log-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+logging-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+logging-devel %{_description}

This package contains library source intended for building other packages
which use "logging" feature of "%{crate}" crate.

%files       -n %{name}+logging-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Tue Jan 22 2019 Josh Stone <jistone@redhat.com> - 0.47.0-1
- Update to 0.47.0

* Mon Jan 14 2019 Josh Stone <jistone@redhat.com> - 0.46.0-1
- Update to 0.46.0

* Sat Nov 10 2018 Josh Stone <jistone@redhat.com> - 0.43.1-1
- Update to 0.43.1

* Sun Nov 04 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.43.0-2
- Adapt to new packaging

* Mon Oct 22 2018 Josh Stone <jistone@redhat.com> - 0.43.0-1
- Update to 0.43.0

* Thu Oct 11 2018 Josh Stone <jistone@redhat.com> - 0.42.2-1
- Update to 0.42.2

* Mon Oct 08 2018 Josh Stone <jistone@redhat.com> - 0.42.1-1
- Update to 0.42.1

* Thu Oct 04 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.42.0-1
- Initial package
