Summary:	Shooting game on X Window System
Summary(pl):	Strzelanina pod X Window System
Name:		xsoldier
Version:	0.96
Release:	21
License:	GPL
Group:		X11/Applications/Games
Source0:	http://www.surfline.ne.jp/hachi/xsoldier/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}.xpm
Patch0:		%{name}-securityfix.patch
Patch1:		%{name}-xf4.patch
Patch2:		%{name}-font.patch
URL:		http://www.surfline.ne.jp/hachi/xsoldier.html
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Great little shoot 'em up game in the style of galaga. Very neat
graphics, but there's no sound support yet.

%description -l pl
Niewielka gra typu "zestrzel wszystko co siê rusza" w stylu galagi.
Przyjemna grafika, ale na razie bez d¼wiêku.

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

%{__make} PIXMAPDIR=$RPM_BUILD_ROOT%{_datadir}/xsoldier \
	SCOREDIR=$RPM_BUILD_ROOT/var/games \
	SCOREFILE=xsoldier.scores \
	BINDIR=$RPM_BUILD_ROOT%{_bindir} install

install -d $RPM_BUILD_ROOT{%{_applnkdir}/Games,%{_pixmapsdir}}
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Games
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

gzip -9nf README* ChangeLog.jp

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README*.gz
%lang(jp) %doc ChangeLog.jp.gz
%attr(2755,root,games) %{_bindir}/xsoldier
%{_datadir}/xsoldier
%attr(664,root,games) %config(noreplace) %verify(not size mtime md5) /var/games/xsoldier.scores
%{_pixmapsdir}/xsoldier.xpm
%{_applnkdir}/Games/xsoldier.desktop
