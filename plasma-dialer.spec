#define snapshot 20200825
#define commit 0974c6f3fe71164d9d2f4acfb861db07ff2b484d

%define devname %{mklibname -d -s ktelephonymetatypes}

Name:		plasma-dialer
Version:	6.5.0
Release:	%{?snapshot:1.%{snapshot}.}1
Summary:	Dialer for Plasma Mobile
Source0:	https://download.kde.org/stable/plasma/%{version}/%{name}-%{version}.tar.xz
License:	GPLv3
Group:		Applications/Productivity
BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6Sql)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6WaylandClient)
BuildRequires:	cmake(Qt6QuickControls2)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6Contacts)
BuildRequires:	cmake(KF6People)
BuildRequires:	cmake(KF6ModemManagerQt)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6PulseAudioQt)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6KirigamiAddons)
BuildRequires:	cmake(KTactileFeedback)
BuildRequires:	cmake(PulseAudio)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(protobuf)
BuildRequires:	pkgconfig(libcallaudio-0.1)
BuildRequires:	pkgconfig(wayland-client)
BuildRequires:	pkgconfig(wayland-server)
BuildRequires:	pkgconfig(wayland-cursor)
BuildRequires:	pkgconfig(wayland-egl)
BuildRequires:	cmake(PlasmaWaylandProtocols)
BuildRequires:	%mklibname phonenumber -d

%description
Dialer for Plasma Mobile

%package -n %{devname}
Summary:	Development files for plasma-dialer
Requires:	%{name} = %{EVRD}

%description -n %{devname}
Development files for plasma-dialer

%files -f %{name}.lang
%{_sysconfdir}/xdg/autostart/org.kde.modem.daemon.desktop
%{_sysconfdir}/xdg/autostart/org.kde.telephony.daemon.desktop
%{_bindir}/plasma-dialer
%{_libdir}/libexec/kde-telephony-daemon
%{_libdir}/libexec/modem-daemon
%{_qtdir}/qml/org/kde/telephony/libKTelephonyPluginDeclarative.so
%{_qtdir}/qml/org/kde/telephony/qmldir
%{_datadir}/applications/org.kde.plasma.dialer.desktop
%{_datadir}/dbus-1/interfaces/org.kde.telephony.*.xml
%{_datadir}/dbus-1/services/org.kde.modemdaemon.service
%{_datadir}/dbus-1/services/org.kde.telephony.service
%{_datadir}/icons/hicolor/scalable/apps/dialer.svg
%{_datadir}/knotifications6/plasma-dialer.notifyrc
%{_datadir}/metainfo/org.kde.plasma.dialer.appdata.xml

%files -n %{devname}
%{_libdir}/lib*.a
%{_includedir}/KF6/kTelephonyMetaTypes
