%global debug_package %{nil}
%global __strip /bin/true
%global __requires_exclude_from /usr/lib/youtube-music-desktop-app/.*

Name:           youtube-music-desktop-app
Version:        2.0.12
Release:        1%{?dist}
Summary:        YouTube Music Desktop App
License:        GPL-3.0-only
URL:            https://ytmdesktop.app/
Source0:        https://github.com/ytmdesktop/ytmdesktop/releases/download/v%{version}/youtube-music-desktop-app-%{version}-1.x86_64.rpm
Source1:        https://github.com/ytmdesktop/ytmdesktop/releases/download/v%{version}/youtube-music-desktop-app-%{version}-1.arm64.rpm
ExclusiveArch:  x86_64 aarch64

BuildRequires:  cpio
BuildRequires:  desktop-file-utils
BuildRequires:  rpm

Requires:       alsa-lib
Requires:       at-spi2-core
Requires:       gtk3
Requires:       libdrm
Requires:       libnotify
Requires:       libXScrnSaver
Requires:       libXtst
Requires:       mesa-libgbm
Requires:       nss
Requires:       xdg-utils

%description
YouTube Music Desktop App is an unofficial desktop application for YouTube
Music with desktop integration and additional features.

%prep
%ifarch x86_64
%global upstream_rpm %{SOURCE0}
%global upstream_sha256 6b9e19d6566ed42cabc7709855f4f9a9be1ea95b74d5dc70cd95098aeaf244cf
%else
%global upstream_rpm %{SOURCE1}
%global upstream_sha256 3a7c164ff88181e2f7fc9c5bf4ffd598238637b788779624496c6e12374d4e3e
%endif
echo "%{upstream_sha256}  %{upstream_rpm}" | sha256sum --check

%install
rpm2cpio %{upstream_rpm} | cpio --extract --make-directories --quiet --directory %{buildroot}
rm -rf %{buildroot}%{_prefix}/lib/.build-id

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/youtube-music-desktop-app.desktop

%files
%license /usr/lib/youtube-music-desktop-app/LICENSE
%license /usr/lib/youtube-music-desktop-app/LICENSES.chromium.html
%doc %{_defaultdocdir}/youtube-music-desktop-app
%{_bindir}/youtube-music-desktop-app
/usr/lib/youtube-music-desktop-app
%{_datadir}/applications/youtube-music-desktop-app.desktop
%{_datadir}/pixmaps/youtube-music-desktop-app.png

%changelog
* Wed Sep 09 2026 OK <o.kraievyi@gmail.com> - 2.0.12-1
- Package the upstream YouTube Music Desktop App RPMs for COPR
