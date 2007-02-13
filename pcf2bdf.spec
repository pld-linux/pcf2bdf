# TODO: optflags
Summary:	PCF to BDF font conwerter
Summary(pl.UTF-8):	Konwerter fontów PCF do formatu BDF
Name:		pcf2bdf
Version:	1.04
Release:	1
License:	Freeware
Group:		Development/Tools
Source0:	http://www.tsg.ne.jp/GANA/S/pcf2bdf/%{name}-%{version}.tgz
# Source0-md5:	8ce3b6a57491c67ef0cbf2f5413451f3
Patch0:		%{name}-cvs.patch
Patch1:		%{name}-DESTDIR.patch
Patch2:		%{name}-gzip.patch
# in Japanese :)
URL:		http://www.tsg.ne.jp/GANA/S/pcf2bdf/
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pcf2bdf is a font de-compiler.  It converts X font from Portable
Compiled Format (PCF) to Bitmap Distribution Format (BDF).  It can
also accept a compressed/gzipped PCF file as input, but gzip must be
found in your PATH.

%description -l pl.UTF-8
pcf2bdf jest dekompilatorem fontów służącym do konwersji z formatu
PCF (Portable Compiled Format) do BDF (Bitmap Distribution Format).
Można mu podawać jako dane wejściowe również plik PCF skompresowany
gzipem, ale wymaga to dostępności programu gzip w PATH.

%prep
%setup -q -c
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
cp -f Makefile.gcc Makefile
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
