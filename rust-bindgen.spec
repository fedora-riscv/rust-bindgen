# Generated by rust2rpm
%bcond_without check

%global crate bindgen

Name:           rust-%{crate}
Version:        0.42.0
Release:        1%{?dist}
Summary:        Automatically generates Rust FFI bindings to C and C++ libraries

# Upstream license specification: BSD-3-Clause
License:        BSD
URL:            https://crates.io/crates/bindgen
Source0:        https://crates.io/api/v1/crates/%{crate}/%{version}/download#/%{crate}-%{version}.crate
# Initial patched metadata
# * Update quote and proc-macro2
Patch0:         bindgen-fix-metadata.diff
# https://github.com/rust-lang-nursery/rust-bindgen/pull/1409
Patch0001:      0001-Update-quote-and-proc-macro.patch

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging
# [dependencies]
BuildRequires:  (crate(bitflags) >= 1.0.3 with crate(bitflags) < 2.0.0)
BuildRequires:  (crate(cexpr) >= 0.3.0 with crate(cexpr) < 0.4.0)
BuildRequires:  (crate(cfg-if) >= 0.1.0 with crate(cfg-if) < 0.2.0)
BuildRequires:  ((crate(clang-sys) >= 0.24.0 with crate(clang-sys) < 0.25.0) with crate(clang-sys/runtime) with crate(clang-sys/clang_6_0))
BuildRequires:  (crate(clap) >= 2.0.0 with crate(clap) < 3.0.0)
BuildRequires:  (crate(env_logger) >= 0.5.0 with crate(env_logger) < 0.6.0)
BuildRequires:  (crate(lazy_static) >= 1.0.0 with crate(lazy_static) < 2.0.0)
BuildRequires:  (crate(log) >= 0.4.0 with crate(log) < 0.5.0)
BuildRequires:  (crate(peeking_take_while) >= 0.1.2 with crate(peeking_take_while) < 0.2.0)
BuildRequires:  (crate(proc-macro2) >= 0.4.0 with crate(proc-macro2) < 0.5.0)
BuildRequires:  (crate(quote) >= 0.6.0 with crate(quote) < 0.7.0)
BuildRequires:  (crate(regex) >= 1.0.0 with crate(regex) < 2.0.0)
BuildRequires:  (crate(which) >= 1.0.2 with crate(which) < 2.0.0)
%if %{with check}
# [dev-dependencies]
BuildRequires:  (crate(clap) >= 2.0.0 with crate(clap) < 3.0.0)
BuildRequires:  (crate(diff) >= 0.1.0 with crate(diff) < 0.2.0)
BuildRequires:  (crate(shlex) >= 0.1.0 with crate(shlex) < 0.2.0)
%endif

%description
%{summary}.

%package     -n %{crate}
Summary:        %{summary}

%description -n %{crate}
%{summary}.

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel
Automatically generates Rust FFI bindings to C and C++ libraries.

This package contains library source intended for building other packages
which use %{crate} from crates.io.

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
# https://github.com/rust-lang-nursery/rust-bindgen/issues/1412#issuecomment-427632052
%ifarch s390x
  %cargo_test || :
%else
  %cargo_test
%endif
%endif

%files       -n %{crate}
%license LICENSE
%doc README.md
%{_bindir}/bindgen

%files          devel
%license LICENSE
%doc README.md
%{cargo_registry}/%{crate}-%{version}/

%changelog
* Thu Oct 04 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.42.0-1
- Initial package
