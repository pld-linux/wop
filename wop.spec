%define		filedate 2004-09-25
Summary:	Wörms of Prey
Summary(pl):	Robaki modlitwy
Name:		wop
Version:	0.3.1
Release:	0.1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://wormsofprey.org/download/%{name}-%{version}-src.tar.bz2
# Source0-md5:	ffc33965efc9287ffd7c6b34b790c12f
Source1:	%{name}.desktop
URL:		http://wormsofprey.org/
BuildRequires:	SDL-devel >= 1.2
BuildRequires:	SDL_image-devel >= 1.2
BuildRequires:	SDL_mixer-devel >= 1.2
BuildRequires:	SDL_net-devel >= 1.2.5
BuildRequires:	SDL_ttf-devel >= 2.0
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Wörms of Prey is the new and free real-time Worms game for Linux and Windows.

%description -l pl
Wörms of Prey s± now± i darmow± gr± czasu rzeczywistego, podobn± do Worms dla
Linuksa i windows.

%prep
%setup -q -n %{name}

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir},%{_pixmapsdir}}

install bin/%{name} $RPM_BUILD_ROOT%{_bindir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/%{name}
