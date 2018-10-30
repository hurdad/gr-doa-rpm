Name:           gr-doa
Version:        %{VERSION}
Release:        %{RELEASE}%{?dist}
Summary:        Direction-of-Arrival (DoA) Demo for GNU Radio (OOT)
Group:          System Environment/Libraries
License:        Apache 2.0
URL:            https://github.com/EttusResearch/gr-doa
Source:         %{name}-%{version}.tar.gz      
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  gnuradio-devel
BuildRequires:  armadillo-devel
BuildRequires:  cppunit-devel
BuildRequires:  gcc-c++ 
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  doxygen-latex
BuildRequires:  swig

%description
Direction-of-Arrival (DoA) Demo for GNU Radio (OOT) with the USRP™ X-Series and TwinRX™

%prep
%setup

%build
cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
cp README.md $RPM_BUILD_ROOT%{_docdir}/gr-doa/

%clean
rm -rf $RPM_BUILD_ROOT

%post
ldconfig

%postun
ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/libgnuradio-doa.so
%{_libdir}/python2.7/site-packages/doa
%{_libdir}/cmake/doa/doaConfig.cmake
%{_datadir}/gnuradio/grc/blocks/*.xml
%{_includedir}/doa/*
%{_docdir}/gr-doa/*

%changelog
