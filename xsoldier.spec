Summary:	Shooting game on X Window System
Name:		xsoldier
Version:	0.96
Release:	14
License:	GPL
Group:		X11/Games
Group(pl):	X11/Gry
URL:		http://www.surfline.ne.jp/hachi/xsoldier.html
Source0:	http://www.surfline.ne.jp/hachi/xsoldier/%{name}-%{version}.tar.gz
Source1:	%{name}
Source2:	%{name}.xpm
Source3:	%{name}-icons.tar.bz2
Patch0:		%{name}-securityfix.patch.bz2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Great little shoot 'em up game in the style of galaga. Very neat
graphics, but there's no sound support yet.

%prep
%setup -q
%patch0 -p1

%build
xmkmf -a
%{__make} CDEBUGFLAGS="${RPM_OPT_FLAGS}" \
       PIXMAPDIR=%{_libdir}/games/xsoldier \
        SCOREDIR=/var/lib/games \
       SCOREFILE=xsoldier.scores \
          BINDIR=/usr/games all

%install
rm -rf $RPM_BUILD_ROOT

%{__make} PIXMAPDIR=${RPM_BUILD_ROOT}%{_libdir}/games/xsoldier \
      SCOREDIR=${RPM_BUILD_ROOT}/var/lib/games \
     SCOREFILE=xsoldier.scores \
        BINDIR=${RPM_BUILD_ROOT}/usr/games install

install -m 755 -d $RPM_BUILD_ROOT%{_libdir}/menu
install %SOURCE1 $RPM_BUILD_ROOT%{_libdir}/menu/
install -m 755 -d $RPM_BUILD_ROOT%{_datadir}/icons
install %SOURCE2 $RPM_BUILD_ROOT%{_datadir}/icons/

bunzip2 -c %{SOURCE3} | tar xvf - -C $RPM_BUILD_ROOT

%post
if [ ! -r /var/lib/games/xsoldier.scores ]; then
   echo -e "\
110000 1 8 hachi
100000 1 8 pochi
90000 1 7 nao
80000 1 7 ryu
70000 1 6 zuno
60000 1 6 draemon
50000 1 3 hoge
40000 1 5 yoko
30000 1 5 tsuyoshi
20000 1 4 tama" > /var/lib/games/xsoldier.scores
   chown games.games /var/lib/games/xsoldier.scores
   chmod 660 /var/lib/games/xsoldier.scores
fi

if [ -x /usr/bin/update-menus ]; then
  /usr/bin/update-menus
fi
  
%postun
if [ "$1" = 0 ]; then
  if [ -x /usr/bin/update-menus ]; then
    /usr/bin/update-menus
  fi
fi  

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CONDITION COPYING ChangeLog.jp README.1st README.joystick README.score
%doc scorefile.txt
%defattr(-,root,root)
%attr(2711, root, games) /usr/games/xsoldier
%{_libdir}/games/xsoldier
%ghost %attr(0660, games, games) /var/lib/games/xsoldier.scores
%{_libdir}/menu/*
%{_datadir}/icons/*
