%define		filedate 2004-09-25
Summary:	Worms of Prey
Summary(en.UTF-8):   Wörms of Prey
Summary(pl.UTF-8):   Drapieżrobaki
Name:		wop
Version:	0.4.3
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://wormsofprey.org/download/%{name}-%{version}-src.tar.bz2
# Source0-md5:	ae07e9e1092de6c447a9af2cf8e90959
Source1:	http://wormsofprey.org/download/%{name}data-2005-12-21.tar.bz2
# Source1-md5:	0bf42f28e03dcac5c8066b46d7733907
Source2:	%{name}-client.desktop
Source3:	%{name}-server.desktop
URL:		http://wormsofprey.org/
BuildRequires:	SDL-devel >= 1.2
BuildRequires:	SDL_image-devel >= 1.2
BuildRequires:	SDL_mixer-devel >= 1.2
BuildRequires:	SDL_net-devel >= 1.2.5
BuildRequires:	SDL_ttf-devel >= 2.0
BuildRequires:	zlib-devel >= 1.2
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_wopdata	/usr/share/wop

%description
Worms of Prey is the new and free real-time Worms game for Linux and
Windows.

%description -l en.UTF-8
Wörms of Prey is the new and free real-time Worms game for Linux and
Windows.

%description -l pl.UTF-8
Wörms of Prey są nową i darmową grą czasu rzeczywistego, podobną do
Worms dla Linuksa i Windows.

%prep
%setup -q -a1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir},%{_pixmapsdir},%{_wopdata}}

install bin/%{name} $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE2} %{SOURCE3} $RPM_BUILD_ROOT%{_desktopdir}
cp -r wopdata-2005-12-21/* $RPM_BUILD_ROOT%{_wopdata}
ln -s %{_wopdata}/images/misc/icons/wop16.png $RPM_BUILD_ROOT%{_pixmapsdir}/wop16.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/%{name}
%{_desktopdir}/%{name}-client.desktop
%{_desktopdir}/%{name}-server.desktop
%{_pixmapsdir}/wop16.png
%{_wopdata}
