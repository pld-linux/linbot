Summary:	Amazing Site Management Tool for webmasters
Summary(pl.UTF-8):	Zadziwiające Narzędzie Do Zarządzania Serwisami WWW
Name:		linbot
Version:	1.0b7
Release:	1
License:	GPL
Vendor:		Marduk <marduk@starship.skyport.net>
Group:		Applications/Networking
Source0:	ftp://sunsite.unc.edu/pub/Linux/apps/www/misc/%{name}-%{version}.tgz
# Source0-md5:	09f8c7b5a3ba58a1e056921a91be56ee
Patch0:		%{name}-config.patch
URL:		http://starship.python.net/crew/marduk/linbot/
BuildArch:	noarch
Requires:	python >= 1.5.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Linbot is a FREE clone of Linkbot and plans to incorporate many of
Linkbot's features as well as enhancements of its own.

Linbot allows webmasters to:
- View The Structure Of A Site
- Track Down Broken Links
- Find Potentially Outdated Web Pages
- List Links Pointing To External Sites
- View Portfolio Of Inline Images
- Do All This Periodically And Without User Intervention

%description -l pl.UTF-8
Linbot to DARMOWY klon Linkbota, który zawiera wiele "features"
podobnie jak i zawiera własne.

Linbot pozwala webmasterom na:
- Przeglądanie Struktury Serwisu
- Wyszukiwanie Nieprawidłowych Odnośników
- Wyszukiwanie Starych Stron
- Przeglądanie Listy Odnośników Wskazujących Na Inne Serwisy
- Przeglądanie Obrazków Z Danego Serwisu
- Robienie Tego Wszystkiego Bez Ingerencji Użytkownika

%prep
%setup -q
%patch -P0 -p1

%build
./linbot.py || :

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir}/linbot,%{_bindir}}

install *.py* $RPM_BUILD_ROOT%{_libdir}/linbot
install plugins/*.py* $RPM_BUILD_ROOT%{_libdir}/linbot
install schemes/*.py* $RPM_BUILD_ROOT%{_libdir}/linbot
install contrib/plugins/*.py* $RPM_BUILD_ROOT%{_libdir}/linbot
install linbot.css $RPM_BUILD_ROOT%{_libdir}/linbot
(cd $RPM_BUILD_ROOT%{_bindir}; ln -sf ../lib/linbot/linbot.py linbot)

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README BUGS TODO
%attr(755,root,root) %{_bindir}/linbot
%attr(755,root,root) %{_libdir}/linbot/linbot.py
%{_libdir}/linbot/linbot.pyc
%{_libdir}/linbot/_*
%{_libdir}/linbot/[a-k]*
%{_libdir}/linbot/[m-z]*
%{_libdir}/linbot/linbot.css
