%define		_state		stable
%define		orgname		libkmahjongg
%define		qtver		4.8.0

Summary:	libkmahjongg
Name:		kde4-%{orgname}
Version:	4.13.0
Release:	1
License:	LGPL
Group:		X11/Libraries
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	c0fa0f9ca5c0a7fa26b91d9e47f5e417
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cmake >= 2.8.0
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	libsndfile-devel
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.600
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libkmahjongg.

%package devel
Summary:	Development files for libkmahjongg
Summary(pl.UTF-8):	Pliki przydatne twórcom gier dla libkmahjongg
Summary(pt_BR.UTF-8):	Arquivos de inclusão do libkmahjongg
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	kde4-kdelibs-devel >= %{version}

%description devel
Development files for libkmahjongg.

%description devel -l pl.UTF-8
libkmahjongg - pliki dla programistów.

%description devel -l pt_BR.UTF-8
Este pacote detém os arquivos de inclusão necessários para compilar
aplicativos que usam bibliotecas do libkmajongg.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

install -d $RPM_BUILD_ROOT/var/games
# remove locolor icons
rm -rf $RPM_BUILD_ROOT%{_iconsdir}/locolor

%clean
rm -rf $RPM_BUILD_ROOT

%post			-p /sbin/ldconfig
%postun			-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libkmahjongglib.so.?
%attr(755,root,root) %{_libdir}/libkmahjongglib.so.*.*.*
%{_datadir}/apps/kmahjongglib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkmahjongglib.so
%{_includedir}/kmahjonggbackground.h
%{_includedir}/kmahjonggconfigdialog.h
%{_includedir}/kmahjonggtileset.h
%{_includedir}/libkmahjongg_export.h
