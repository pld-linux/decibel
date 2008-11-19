#
# Conditional build:
#
%define		qt_ver		4.4.3

Summary:	Decibel
Summary(pl.UTF-8):	Decibel
Name:		decibel
Version:	0.5.0
Release:	0.1
License:	GPL v2
Group:		X11/Applications
Source0:	http://decibel.kde.org/fileadmin/downloads/decibel/releases/%{name}-%{version}.tar.gz
# Source0-md5:	7de299ace568c87a746388ad765228e5
Patch0:		%{name}-types.patch
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
Summary:        Header files for decibel library
Summary(pl.UTF-8):      Pliki nag�~B처wkowe biblioteki decibel
Group:          Development/Libraries
Requires:      %{name} = %{version}-%{release}

%description devel
Header files for decibel library.

%description devel -l pl.UTF-8
Pliki nag�~B처wkowe biblioteki decibel.

%prep
%setup -q
%patch0 -p0

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
%attr(755,root,root)

%files devel
%defattr(644,root,root,755)
