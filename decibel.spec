#
# Conditional build:
#
%define		qt_ver		4.4.3
%define		snap 		890391

Summary:	Decibel
Summary(pl.UTF-8):	Decibel
Name:		decibel
Version:	0.7.0
Release:	0.%{snap}.2
License:	LGPL v2+
Group:		X11/Applications
#Source0:	http://decibel.kde.org/fileadmin/downloads/decibel/releases/%{name}-%{version}.tar.gz
Source0:	%{name}-%{version}-%{snap}.tar.gz
# Source0-md5:	595c8f1ac65880f73dbbe8d81c02ec58
URL:		http://decibel.kde.org/
BuildRequires:	QtCore-devel >= %{qt_ver}
BuildRequires:	QtDBus-devel >= %{qt_ver}
BuildRequires:	QtGui-devel >= %{qt_ver}
BuildRequires:	automoc4 >= 0.9.84
BuildRequires:	cmake >= 2.6.2
BuildRequires:	qt4-build >= %{qt_ver}
BuildRequires:	qt4-qmake >= %{qt_ver}
BuildRequires:	rpmbuild(macros) >= 1.293
BuildRequires:	tapioca-qt-devel >= 0.17.7
BuildRequires:	telepathy-qt-devel >= 0.17.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Decibel is a realtime communications framework, integrating services
like CTI (Computer Telephone Integration), VoIP (Voice over IP), text
based chat and instant messaging.

#%description -l pl.UTF-8

%package devel
Summary:	Header files for decibel library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki decibel
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for decibel library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki decibel.

%prep
%setup -q -n %{name}-%{version}-%{snap}

%build
install -d build
cd build
%cmake .. \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64
%endif

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/decibel
%attr(755,root,root) %{_bindir}/decibel_logger
%attr(755,root,root) %{_bindir}/textchannelgui
%attr(755,root,root) %{_libdir}/libDecibel.so.0.7.1
%attr(755,root,root) %{_libdir}/libdecibel_pluginhelper.so.0.7.1
%{_libdir}/Decibel
%dir %{_datadir}/Decibel
%dir %{_datadir}/Decibel/components
%{_datadir}/Decibel/components/org.kde.Decibel.Log.component
%{_datadir}/Decibel/components/org.kde.SimpleClient.TextChannel.component
%{_datadir}/Decibel/components/org.kde.textchannelgui.TextChannel.component
%{_datadir}/dbus-1/services/org.kde.Decibel.Daemon.service
%{_datadir}/dbus-1/services/org.kde.Decibel.Log.service
%{_datadir}/dbus-1/services/org.kde.SimpleClient.service
%{_datadir}/dbus-1/services/org.kde.textchannelgui.service

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libDecibel.so
%attr(755,root,root) %{_libdir}/libdecibel_pluginhelper.so
%{_includedir}/Decibel
%{_pkgconfigdir}/Decibel.pc
