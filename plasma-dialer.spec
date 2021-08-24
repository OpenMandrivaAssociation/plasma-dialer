#define snapshot 20200825
#define commit 0974c6f3fe71164d9d2f4acfb861db07ff2b484d

Name:		plasma-dialer
Version:	21.07
Release:	%{?snapshot:0.%{snapshot}.}1
Summary:	Dialer for Plasma Mobile
Source0:	https://download.kde.org/stable/plasma-mobile/%{version}/%{name}-%{version}.tar.xz
License:	GPLv3
Group:		Applications/Productivity
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Qml)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5Sql)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5People)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(PulseAudio)
BuildRequires:	cmake(TelepathyQt5)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(protobuf)
BuildRequires:	%mklibname phonenumber -d
Requires:	ofono
Requires:	telepathy-ofono
Requires:	telepathy-mission-control
Requires:	telepathy-filesystem
Requires:	telepathy-accounts-signon

%description
Dialer for Plasma Mobile

%prep
%autosetup -p1
%cmake_kde5 -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
%find_lang %{name} --all-name

%files -f %{name}.lang
%{_bindir}/plasma-telepathy-approver
%{_bindir}/plasmaphonedialer
%{_datadir}/applications/org.kde.phone.dialer.desktop
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.Client.Plasma.Approver.service
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.Client.Plasma.Dialer.service
%{_datadir}/icons/hicolor/scalable/apps/dialer.svg
%{_datadir}/knotifications5/plasma_dialer.notifyrc
%{_datadir}/metainfo/org.kde.phone.dialer.appdata.xml
%{_datadir}/telepathy/clients/Plasma.Dialer.client
%{_sysconfdir}/xdg/autostart/telephony-services.desktop
%{_sysconfdir}/xdg/autostart/org.kde.phone.dialer.desktop
