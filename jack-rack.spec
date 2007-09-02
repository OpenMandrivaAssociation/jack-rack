%define name 	jack-rack
%define version 1.4.6
%define release %mkrel 1

Name: 		%{name}
Summary: 	LADSPA effects rack for JACK
Version: 	%{version}
Release: 	%{release}

Source:		http://prdownloads.sourceforge.net/jack-rack/%{name}-%{version}.tar.bz2
Patch:          jack-rack-undeprec.dif
URL:		http://jack-rack.sourceforge.net/
License:	GPL
Group:		Sound
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	ladspa-devel pkgconfig jackit-devel
BuildRequires:	gtk2-devel libgnomeui2-devel ImageMagick
BuildRequires:	chrpath desktop-file-utils
BuildRequires:	ecasound-devel

%description
JACK Rack is an effects "rack" for the JACK low latency audio API. The rack
can be filled with LADSPA effects plugins. It's phat; it turns your computer
into an effects box.

%prep
%setup -q
%patch

%build
%configure2_5x
%make
										
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
chrpath -d %buildroot/%_bindir/%name

#menu

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="GTK" \
  --add-category="AudioVideo;Sequencer" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

#icons
mkdir -p $RPM_BUILD_ROOT/%_liconsdir
convert -size 48x48 pixmaps/jack-rack-icon.png $RPM_BUILD_ROOT/%_liconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_iconsdir
convert -size 32x32 pixmaps/jack-rack-icon.png $RPM_BUILD_ROOT/%_iconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_miconsdir
convert -size 16x16 pixmaps/jack-rack-icon.png $RPM_BUILD_ROOT/%_miconsdir/%name.png

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_menus
		
%postun
%clean_menus

%files -f %{name}.lang
%defattr(-,root,root)
%doc README AUTHORS BUGS COPYING ChangeLog NEWS TODO
%{_bindir}/%name
%{_bindir}/ecarack
%{_datadir}/%name
%{_datadir}/applications/%name.desktop
%{_datadir}/pixmaps/*.png
%{_datadir}/dtds
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png



