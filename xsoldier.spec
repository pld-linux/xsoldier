%define ver 0.96
%define rel 13mdk

Summary: Shooting game on X Window System
Name: xsoldier
Version: %{ver}
Release: %{rel}
Copyright: GPL
Group: Games/Arcade
Source: http://www.surfline.ne.jp/hachi/xsoldier/xsoldier-0.96.tar.bz2
Source1: %{name}
Source2: %{name}.xpm
Source3: %{name}-icons.tar.bz2
URL: http://www.surfline.ne.jp/hachi/xsoldier.html
BuildRoot: %{_tmppath}/%{name}
Patch0: xsoldier-securityfix.patch.bz2

%description
Great little shoot 'em up game in the style of galaga. Very neat
graphics, but there's no sound support yet.

%prep
%setup
%patch0 -p1

%build
xmkmf -a
make CDEBUGFLAGS="${RPM_OPT_FLAGS}" \
       PIXMAPDIR=/usr/lib/games/xsoldier \
        SCOREDIR=/var/lib/games \
       SCOREFILE=xsoldier.scores \
          BINDIR=/usr/games all

%install
rm -fr $RPM_BUILD_ROOT

make PIXMAPDIR=${RPM_BUILD_ROOT}/usr/lib/games/xsoldier \
      SCOREDIR=${RPM_BUILD_ROOT}/var/lib/games \
     SCOREFILE=xsoldier.scores \
        BINDIR=${RPM_BUILD_ROOT}/usr/games install

install -m 755 -d $RPM_BUILD_ROOT/usr/lib/menu
install -m 644 %SOURCE1 $RPM_BUILD_ROOT/usr/lib/menu/
install -m 755 -d $RPM_BUILD_ROOT/usr/share/icons
install -m 644 %SOURCE2 $RPM_BUILD_ROOT/usr/share/icons/

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
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc CONDITION COPYING ChangeLog.jp README.1st README.joystick README.score
%doc scorefile.txt
%defattr(-,root,root)
%attr(2711, games, games) /usr/games/xsoldier
/usr/lib/games/xsoldier
%ghost %attr(0660, games, games) /var/lib/games/xsoldier.scores
/usr/lib/menu/*
/usr/share/icons/*

%changelog
* Wed May 17 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 0.96-13mdk
- Add security fix from debian.

* Tue Apr 18 2000 dam's <damien@mandrakesoft.com> 0.96-12mdk
- Convert gif icon to xpm.

* Mon Apr 17 2000 dam's <damien@mandrakesoft.com> 0.96-11mdk
- Added menu entry.

* Thu Mar 30 2000 dam's <damien@mandrakesoft.com> 0.96-10mdk
- New icons.

* Tue Jan 18 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 0.96-9mdk
- Fix pablo sucks (tm) with a defattr.

* Wed Jan 12 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 0.96-8mdk
- Fix pablo sucks.

* Tue Nov 02 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- added a default high scores file
- corrected the URLs

* Fri Sep 10 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- moved the kde menu file to the right place

* Wed Jul 21 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- Adapted to Mandrake my favourite X11 game :)
- Added an icon & menu entries fro Gnome & KDE

* Wed Jan 21 1998 Atsushi Yamagata <yamagata@jwu.ac.jp>
- 4th release
- mv /usr/local/games/lib/xsoldier/.scorefile /var/lib/games/xsoldier/.scorefile
- %doc scorefile.txt

* Sat Dec 06 1997 Atsushi Yamagata <yamagata@jwu.ac.jp>
- 3rd release
- %attr(4711, games, -) /usr/local/games/xsoldier
- %attr(0600, games, -) /usr/local/games/lib/xsoldier/.scorefile

* Fri Dec 05 1997 Atsushi Yamagata <yamagata@jwu.ac.jp>
- 2nd release
- added script for X11R6.3 at the prep stage
- added Distribution and Vendor tags

* Fri Sep 12 1997 Atsushi Yamagata <yamagata@jwu.ac.jp>
- 1st release
