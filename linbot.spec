Summary:     Amazing Site Management Tool for webmasters
Summary(pl): Zadziwiaj±ce Narzêdzie Do Zarz±dzania Serwisami WWW
Name:	     linbot
Version:     0.9
Release:     1d
Copyright:   GPL
Vendor:	     Marduk <marduk@starship.skyport.net>
Group:	     Applications/Networking
Group(pl):   Aplikacje/Sieciowe
Source:	     %{name}-%{version}.tar.gz
Patch:	     linbot.diff
URL:	     http://starship.skyport.net/crew/marduk/linbot
BuildArch:   noarch
Requires:    python >= 1.5.1
BuildRoot:	/tmp/%{name}-%{version}-buildroot

%description
Linbot is a FREE clone of Linkbot and plans to incorporate many of 
Linkbot's features as well as enhancements of its own.

Linbot allows webmasters to:
* View The Structure Of A Site
* Track Down Broken Links
* Find Potentially Outdated Web Pages
* List Links Pointing To External Sites
* View Portfolio Of Inline Images
* Do All This Periodically And Without User Intervention

%description -l pl
Linbot to DARMOWY klon Linkbot'a, który zawiera wiele "features" podobnie
jak i zawiera w³asne,

Linbot pozwala webmasterom na:
* Przegl±danie Struktury Serwisu
* Wyszukiwanie Nieprawid³owych Odno¶ników
* Wyszukiwanie Starych Stron
* Przegl±danie Listy Odno¶ników Wskazuj±cych Na Inne Serwisy
* Przegl±danie Obrazków Z Danego Serwisu
* Robienie Tego Wszystkiego Bez Ingerencji U¿ytkownika

%prep
%setup -q
%patch -p1

%build
./linbot.py ||

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/{lib/linbot/buttons,bin,man/man1}

cp *.* $RPM_BUILD_ROOT%{_libdir}/linbot
cp contrib/cwlinbot.gif $RPM_BUILD_ROOT%{_libdir}/linbot/buttons/linbot.gif
cp contrib/buttons/*.* $RPM_BUILD_ROOT%{_libdir}/linbot/buttons
cp contrib/linbot.1 $RPM_BUILD_ROOT%{_mandir}/man1
cd $RPM_BUILD_ROOT%{_bindir}; ln -s ../lib/linbot/linbot.py linbot

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README 

%attr(755,root,root) %{_bindir}/linbot
%attr(755,root,root) %{_libdir}/linbot/linbot.py
%attr(644,root,root) %{_libdir}/linbot/*.pyc
%attr(644,root,root) %{_libdir}/linbot/config.py
%attr(644,root,root) %{_libdir}/linbot/linbot.css
%attr(644,root,root) %{_libdir}/linbot/myUrlLib.py
%attr(644,root,root) %{_libdir}/linbot/robotparser.py
%attr(644,root,root) %{_libdir}/linbot/buttons/*
%{_mandir}/man1/*
