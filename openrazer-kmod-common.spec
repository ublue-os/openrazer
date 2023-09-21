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
Source1:  https://raw.githubusercontent.com/ublue-os/openrazer/master/install_files/udev/99-razer.rules
Source2:  https://raw.githubusercontent.com/ublue-os/openrazer/master/install_files/udev/razer_mount

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

%install
install -m 644 -v -D %{SOURCE1} %{buildroot}%{_udevrulesdir}/99-razer.rules
install -m 755 -v -D %{SOURCE2} %{buildroot}%{_udevrulesdir}/../razer_mount

%files
%doc README.md
%license LICENSES/GPL-2.0-or-later.txt
%{_udevrulesdir}/99-razer.rules
%{_udevrulesdir}/../razer_mount

%changelog
{{{ git_dir_changelog }}}
