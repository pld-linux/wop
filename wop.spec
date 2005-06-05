%define		filedate 2004-09-25
Summary:	Worms of Prey
Summary(en):	Wörms of Prey
Summary(pl):	Drapie¿robaki
Name:		wop
Version:	0.3.1
Release:	0.2
License:	GPL
Group:		X11/Applications/Games
Source0:	http://wormsofprey.org/download/%{name}-%{version}-src.tar.bz2
# Source0-md5:	ffc33965efc9287ffd7c6b34b790c12f
Source1:	http://wormsofprey.org/download/%{name}data-2005-05-13.tar.bz2
# Source1-md5:	a74d77b0db2817bd09637643f464c4fa
Source2:	%{name}-client.desktop
Source3:	%{name}-server.desktop
URL:		http://wormsofprey.org/
BuildRequires:	SDL-devel >= 1.2
BuildRequires:	SDL_image-devel >= 1.2
BuildRequires:	SDL_mixer-devel >= 1.2
BuildRequires:	SDL_net-devel >= 1.2.5
BuildRequires:	SDL_ttf-devel >= 2.0
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_wopdata	/usr/share/wop

%description
Worms of Prey is the new and free real-time Worms game for Linux and
Windows.

%description -l en
Wörms of Prey is the new and free real-time Worms game for Linux and
Windows.

%description -l pl
Wörms of Prey s± now± i darmow± gr± czasu rzeczywistego, podobn± do
Worms dla Linuksa i Windows.

%prep
%setup -q -n %{name} -a1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir},%{_pixmapsdir},%{_wopdata}}

install bin/%{name} $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE2} %{SOURCE3} $RPM_BUILD_ROOT%{_desktopdir}
cp -r wopdata-2005-05-13/* $RPM_BUILD_ROOT%{_wopdata}
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
