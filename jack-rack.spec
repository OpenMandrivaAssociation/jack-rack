%define name    jack-rack
%define version 1.4.7
%define release 8

Name:           %{name}
Summary:        LADSPA effects rack for JACK
Version:        %{version}
Release:        %{release}

Source:         http://prdownloads.sourceforge.net/jack-rack/%{name}-%{version}.tar.bz2
Patch0:         jack-rack-1.4.7-undeprec.patch
URL:            http://jack-rack.sourceforge.net/
License:        GPLv2+
Group:          Sound
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:  ladspa-devel pkgconfig jackit-devel
BuildRequires:  gtk2-devel libgnomeui2-devel imagemagick
BuildRequires:  chrpath desktop-file-utils
BuildRequires:  ecasound-devel
# BuildRequires:  lash-devel
BuildRequires:  gettext-devel

%description
JACK Rack is an effects "rack" for the JACK low latency audio API. The rack
can be filled with LADSPA effects plugins. It's phat; it turns your computer
into an effects box.

%prep
%setup -q
%patch0 -p1

%build
# Fix explicit lm and ldl linking requirement
perl -pi -e 's/jack_rack_LDFLAGS =/jack_rack_LDFLAGS = -ldl -lm/g' src/Makefile.am

autoreconf -f -i
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
chrpath -d %buildroot/%_bindir/%name

#menu

perl -pi -e 's,%{name}-icon.png,%{name}-icon,g' %{buildroot}%{_datadir}/applications/*

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



