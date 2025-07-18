Summary:	Shooting game on X Window System
Summary(es.UTF-8):	Spaceship vertical-scrolling shooting game for X
Summary(pl.UTF-8):	Strzelanina pod X Window System
Summary(pt_BR.UTF-8):	Jogo de nave-espacial-que-atira-e-voa-pra-cima-na-tela, para X
Name:		xsoldier
Version:	1.8
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://www.interq.or.jp/libra/oohara/xsoldier/%{name}-%{version}.tar.gz
# Source0-md5:	f76c2e5465a1a2aca2286415b13b01a4
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-make.patch
Patch1:		%{name}-format.patch
URL:		http://www.interq.or.jp/libra/oohara/xsoldier/
BuildRequires:	SDL-devel
BuildRequires:	SDL_image-devel
BuildRequires:	autoconf >= 2.64
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Great little shoot 'em up game in the style of galaga. Very neat
graphics, but there's no sound support yet.

%description -l es.UTF-8
Spaceship vertical-scrolling shooting game for X, with nice graphics,
3 types of shot, big boss at the end of each level and highscores. No
sound yet.

%description -l pl.UTF-8
Niewielka gra typu "zestrzel wszystko co się rusza" w stylu galagi.
Przyjemna grafika, ale na razie bez dźwięku.

%description -l pt_BR.UTF-8
Jogo de nave-espacial-que-atira-e-voa-pra-cima-na-tela, para X, com
gráficos legais, 3 tipos de tiro, chefão no final do cada fase e
recordes. Ainda não tem som.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-sdl
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
cp -p %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%triggerun -- xsoldier < 1.0
mv -f /var/games/xsoldier.scores /var/games/xsoldier/xsoldier.scores 2>/dev/null
exit 0

%files
%defattr(644,root,root,755)
%doc ChangeLog LICENSE README
%attr(2755,root,games) %{_bindir}/xsoldier
%{_datadir}/xsoldier
%dir /var/games/xsoldier
%attr(664,root,games) %config(noreplace) %verify(not md5 mtime size) /var/games/xsoldier/xsoldier.scores
%{_mandir}/man6/xsoldier.6*
%{_pixmapsdir}/xsoldier.png
%{_desktopdir}/xsoldier.desktop
