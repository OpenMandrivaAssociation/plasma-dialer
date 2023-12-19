#define snapshot 20200825
#define commit 0974c6f3fe71164d9d2f4acfb861db07ff2b484d

Name:		plasma-dialer
Version:	23.01.0
Release:	%{?snapshot:1.%{snapshot}.}1
Summary:	Dialer for Plasma Mobile
Source0:	https://download.kde.org/stable/plasma-mobile/%{version}/%{name}-%{version}.tar.xz
License:	GPLv3
Group:		Applications/Productivity
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Feedback)
BuildRequires:	cmake(Qt5Qml)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5Sql)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(Qt5WaylandClient)
BuildRequires:	cmake(Qt5QuickControls2)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5Contacts)
BuildRequires:	cmake(KF5People)
BuildRequires:	cmake(KF5ModemManagerQt)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5PulseAudioQt)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(PulseAudio)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(protobuf)
BuildRequires:	pkgconfig(mpris-qt5)
BuildRequires:	pkgconfig(libcallaudio-0.1)
BuildRequires:	pkgconfig(wayland-client)
BuildRequires:	pkgconfig(wayland-server)
BuildRequires:	pkgconfig(wayland-cursor)
BuildRequires:	pkgconfig(wayland-egl)
BuildRequires:	cmake(PlasmaWaylandProtocols)
BuildRequires:	qt5-qtwayland-private-devel
BuildRequires:	%mklibname phonenumber -d

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

# Not currently used by anything, so no need for
# a -devel package so far
rm -rf %{buildroot}%{_includedir} %{buildroot}%{_libdir}/*.a

%files -f %{name}.lang
%{_bindir}/plasmaphonedialer
%{_datadir}/applications/org.kde.phone.dialer.desktop
%{_datadir}/icons/hicolor/scalable/apps/dialer.svg
%{_datadir}/knotifications5/plasma_dialer.notifyrc
%{_datadir}/metainfo/org.kde.phone.dialer.appdata.xml
%{_sysconfdir}/xdg/autostart/org.kde.modem.daemon.desktop
%{_sysconfdir}/xdg/autostart/org.kde.telephony.daemon.desktop
%{_libdir}/libexec/kde-telephony-daemon
%{_libdir}/libexec/modem-daemon
%{_libdir}/qt5/qml/org/kde/telephony
%{_datadir}/dbus-1/interfaces/org.kde.telephony.*.xml
%{_datadir}/dbus-1/services/org.kde.modemdaemon.service
%{_datadir}/dbus-1/services/org.kde.telephony.service
