
Summary:		Audio Plugin API
Name:		clap
Version:		1.2.6
Release:		1
License:		MIT
Group:	Sound
Url:	https://cleveraudio.org/
Source0:	https://github.com/free-audio/clap/archive/refs/tags/%{name}-%{version}.tar.gz
Patch0:		clap-1.2.6-fix-pkgconfig-file.patch
BuildRequires:		cmake >= 3.21
# Header only package
BuildArch:		noarch

%description
CLAP stands for CLever Audio Plugin. It is an interface that provides a stable
ABI to define a standard for Digital Audio Workstations and audio plugins
(synthesizers, audio effects, ...) to work together.

#-----------------------------------------------------------------------------

%package devel
Summary:		Development files for CLAP
Group:	Development/C

%description devel
CLAP stands for CLever Audio Plugin. It is an interface that provides a stable
ABI to define a standard for Digital Audio Workstations and audio plugins
(synthesizers, audio effects, ...) to work together.
This package contains the development files for %{name}.


%files devel
%license LICENSE
%doc README.md ChangeLog.md
%{_includedir}/%{name}/
%{_libdir}/cmake/%{name}/
%{_libdir}/pkgconfig/%{name}.pc

#-----------------------------------------------------------------------------

%prep
%autosetup -p1


%build
%cmake
%make_build


%install
%make_install -C build
