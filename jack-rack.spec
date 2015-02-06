Name:		jack-rack
Summary:		LADSPA effects rack for JACK
Version:		1.4.7
Release:		12
URL:		http://jack-rack.sourceforge.net/
License:		GPLv2+
Group:		Sound
Source0:		http://prdownloads.sourceforge.net/jack-rack/%{name}-%{version}.tar.bz2
Patch0:		jack-rack-1.4.7-undeprec.patch
Patch1:		jack-rack-1.4.7-jacksession.patch
BuildRequires:	ladspa-devel
BuildRequires:	pkgconfig
BuildRequires:	jackit-devel
BuildRequires:	gtk2-devel
BuildRequires:	imagemagick
BuildRequires:	chrpath
BuildRequires:	desktop-file-utils
BuildRequires:	ecasound-devel
BuildRequires:	liblrdf-devel
BuildRequires:	raptor-devel
BuildRequires:	gettext-devel

%description
JACK Rack is an effects "rack" for the JACK low latency audio API. The rack
can be filled with LADSPA effects plugins. It's phat; it turns your
computer into an effects box.


%prep
%setup -q
%patch0 -p1
%patch1 -p1


%build
# Fix explicit lm and ldl linking requirement
%define _disable_ld_as_needed   1
%configure
perl -pi -e 's/LDFLAGS =/LDFLAGS = -ldl -lm -lpthread /g' Makefile src/Makefile
%make


%install
%makeinstall_std
chrpath -d %{buildroot}/%{_bindir}/%{name}

#menu
perl -pi -e 's,%{name}-icon.png,%{name}-icon,g' %{buildroot}%{_datadir}/applications/*
desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="GTK" \
  --add-category="AudioVideo;Audio;Sequencer" \
  --add-category="X-MandrivaLinux-Sound" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

#icons
mkdir -p %{buildroot}/%{_liconsdir}
convert -size 48x48 pixmaps/jack-rack-icon.png %{buildroot}/%{_liconsdir}/%{name}.png
mkdir -p %{buildroot}/%{_iconsdir}
convert -size 32x32 pixmaps/jack-rack-icon.png %{buildroot}/%{_iconsdir}/%{name}.png
mkdir -p %{buildroot}/%{_miconsdir}
convert -size 16x16 pixmaps/jack-rack-icon.png %{buildroot}/%{_miconsdir}/%{name}.png

%find_lang %name %{name}.lang


%files -f %{name}.lang
%doc README AUTHORS BUGS COPYING ChangeLog NEWS TODO
%{_bindir}/%{name}
%{_bindir}/ecarack
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/*.png
%{_datadir}/dtds
%{_liconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png



%changelog
* Fri Nov 02 2012 Giovanni Mariani <mc2374@mclink.it> 1.4.7-11
- Dropped BuildRoot and %%defattr
- Made use consistently of the curly brackets for macro names

* Sat Apr 28 2012 Frank Kober <emuse@mandriva.org> 1.4.7-10
+ Revision: 794206
+ rebuild (emptylog)

* Sat Apr 28 2012 Frank Kober <emuse@mandriva.org> 1.4.7-9
+ Revision: 794196
- rebuild to fix plugin lrdf support

* Fri Dec 23 2011 Frank Kober <emuse@mandriva.org> 1.4.7-8
+ Revision: 744841
- sync sources
- avoid to reconfigure build, added jacksession upstream patch
- giving up on find-lang.sh and install .mo explicitly
- try find-lang.sh with options
- fix desktop categories
- rebuild for new gtk stuff
  o lash support deactivated
  o explicit linking with lm and ldl fixed

* Mon Dec 06 2010 Frank Kober <emuse@mandriva.org> 1.4.7-7mdv2011.0
+ Revision: 612607
- remove obsolete ladcca-devel BR (now lash)

  + Oden Eriksson <oeriksson@mandriva.com>
    - the mass rebuild of 2010.1 packages

* Sat Dec 05 2009 Jérôme Brenier <incubusss@mandriva.org> 1.4.7-5mdv2010.1
+ Revision: 473824
- add BuildRequires : gettext-devel
- rediff Patch0
- enable lash support / BR : lash-devel
- autoreconf
- fix license tag

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild
    - fix no-buildroot-tag

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Wed Jan 02 2008 Emmanuel Andry <eandry@mandriva.org> 1.4.7-1mdv2008.1
+ Revision: 140795
- New version

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Sep 06 2007 Emmanuel Andry <eandry@mandriva.org> 1.4.6-1mdv2008.0
+ Revision: 81217
- remove icon extension in desktop file
- buildrequires ladcca-devel imagemagick
- New version
- drop old menu
- fix build with suse patch
- add ecasound support


* Sat Jan 27 2007 Emmanuel Andry <eandry@mandriva.org> 1.4.5-1mdv2007.0
+ Revision: 114355
- buildrequires desktop-file-utils
- New version 1.4.5
- Import jack-rack

* Mon Sep 04 2006 Emmanuel Andry <eandry@mandriva.org> 1.4.4-4mdv2007.0
- %%mkrel
- xdg menu

* Fri Apr 21 2006 Austin Acton <austin@mandriva.org> 1.4.4-3mdk
- URL (littletux)
- disable rpath (me)

* Sat Apr 01 2006 Austin Acton <austin@mandriva.org> 1.4.4-2mdk
- Rebuild

* Thu Aug 25 2005 Austin Acton <austin@mandriva.org> 1.4.4-1mdk
- 1.4.4
- source URL

* Sun Feb 06 2005 Austin Acton <austin@mandrake.org> 1.4.3-2mdk
- birthday
- fix summary
- configure 2.5

