Summary:	Shooting game on X Window System
Summary(es):	Spaceship vertical-scrolling shooting game for X
Summary(pl):	Strzelanina pod X Window System
Summary(pt_BR):	Jogo de nave-espacial-que-atira-e-voa-pra-cima-na-tela, para X
Name:		xsoldier
Version:	0.96
Release:	23
License:	GPL
Group:		X11/Applications/Games
Source0:	http://www.surfline.ne.jp/hachi/xsoldier/%{name}-%{version}.tar.gz
# Source0-md5:	63f7ef2cd4de43524486b48c0f097553
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-securityfix.patch
Patch1:		%{name}-xf4.patch
Patch2:		%{name}-font.patch
URL:		http://www.surfline.ne.jp/hachi/xsoldier.html
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
Great little shoot 'em up game in the style of galaga. Very neat
graphics, but there's no sound support yet.

%description -l es
Spaceship vertical-scrolling shooting game for X, with nice graphics,
3 types of shot, big boss at the end of each level and highscores. No
sound yet.

%description -l pl
Niewielka gra typu "zestrzel wszystko co siê rusza" w stylu galagi.
Przyjemna grafika, ale na razie bez d¼wiêku.

%description -l pt_BR
Jogo de nave-espacial-que-atira-e-voa-pra-cima-na-tela, para X, com
gráficos legais, 3 tipos de tiro, chefão no final do cada fase e
recordes. Ainda não tem som.

%prep
%setup -q
%patch0 -p1
%patch1 -p0
%patch2 -p1

%build
xmkmf -a
%{__make} CDEBUGFLAGS="%{rpmcflags}" \
	PIXMAPDIR=%{_datadir}/xsoldier \
	SCOREDIR=/var/games \
	SCOREFILE=xsoldier.scores \
	BINDIR=%{_bindir} all

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Games/Arcade,%{_pixmapsdir}}

%{__make} PIXMAPDIR=$RPM_BUILD_ROOT%{_datadir}/xsoldier \
	SCOREDIR=$RPM_BUILD_ROOT/var/games \
	SCOREFILE=xsoldier.scores \
	BINDIR=$RPM_BUILD_ROOT%{_bindir} install

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Games/Arcade
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README*
%lang(ja) %doc ChangeLog.jp
%attr(2755,root,games) %{_bindir}/xsoldier
%{_datadir}/xsoldier
%attr(664,root,games) %config(noreplace) %verify(not size mtime md5) /var/games/xsoldier.scores
%{_pixmapsdir}/*
%{_applnkdir}/Games/Arcade/xsoldier.desktop
