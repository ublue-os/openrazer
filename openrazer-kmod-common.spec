%if 0%{?fedora}
%global debug_package %{nil}
%endif

Name:     openrazer-kmod-common
Version:  100.{{{ git_dir_version }}}
Release:  1%{?dist}
Summary:  OpenRazer driver common package
License:  GPLv2
URL:      https://github.com/ublue-os/openrazer

VCS:      {{{ git_dir_vcs }}}
Source:   {{{ git_dir_pack }}}

# A small lie
Provides: razer-kernel-modules-dkms = %{version}
Provides: razer-chroma-driver = %{version}
Provides: openrazer-kernel-modules-dkms = %{version}
Requires: openrazer-kmod >= %{version}

BuildRequires: systemd-rpm-macros

%description
OpenRazer driver common package

%prep
{{{ git_dir_setup_macro }}}

%files
%doc README.md
%license LICENSES/GPL-2.0-or-later.txt

%changelog
{{{ git_dir_changelog }}}
