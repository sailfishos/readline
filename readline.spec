#specfile originally created for Fedora, modified for Moblin Linux
Summary: A library for editing typed command lines
Name: readline
Version: 5.2
Release: 13
License: GPLv2+
Group: System/Libraries
URL: http://cnswww.cns.cwru.edu/php/chet/readline/rltop.html
Source: ftp://ftp.gnu.org/gnu/readline/readline-%{version}.tar.gz
Patch1: readline-5.2-shlib.patch
Patch2: readline-5.2-001.patch
Patch3: readline-5.2-002.patch
Patch4: readline-5.2-003.patch
Patch5: readline-5.2-004.patch
Patch6: readline-5.2-005.patch
Patch7: readline-5.2-006.patch
Patch8: readline-5.2-007.patch
Patch9: readline-5.2-008.patch
Patch10: readline-5.2-009.patch
Patch11: readline-5.2-010.patch
Patch12: readline-5.2-011.patch
Patch13: readline-5.2-redisplay-sigint.patch
Patch14: readline-aarch64.patch

BuildRequires: ncurses-devel

%description
The Readline library provides a set of functions that allow users to
edit command lines. Both Emacs and vi editing modes are available. The
Readline library includes additional functions for maintaining a list
of previously-entered command lines for recalling or editing those
lines, and for performing csh-like history expansion on previous
commands.

%package devel
Summary: Files needed to develop programs which use the readline library
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: ncurses-devel

%description devel
The Readline library provides a set of functions that allow users to
edit typed command lines. If you want to develop programs that will
use the readline library, you need to have the readline-devel package
installed. You also need to have the readline package installed.

%package static
Summary: Static libraries for the readline library
Group: Development/Libraries
Requires: %{name}-devel = %{version}-%{release}

%description static
The readline-static package contains the static version of the readline
library.

%prep
%setup -q
%patch1 -p1 -b .shlib
%patch2 -p0 -b .001
%patch3 -p0 -b .002
%patch4 -p0 -b .003
%patch5 -p0 -b .004
%patch6 -p0 -b .005
%patch7 -p0 -b .006
%patch8 -p0 -b .007
%patch9 -p0 -b .008
%patch10 -p0 -b .009
%patch11 -p0 -b .010
%patch12 -p0 -b .011
%patch13 -p1 -b .redisplay-sigint
%patch14 -p1

pushd examples
rm -f rlfe/configure
iconv -f iso8859-1 -t utf8 -o rl-fgets.c{_,}
touch -r rl-fgets.c{,_}
mv -f rl-fgets.c{_,}
popd

%build
export CPPFLAGS="-I%{_includedir}/ncurses"
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install

rm -f $RPM_BUILD_ROOT%{_infodir}/dir

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%docs_package

%files
%defattr(-,root,root,-)
%doc COPYING 
%{_libdir}/libreadline*.so.*
%{_libdir}/libhistory*.so.*

%files devel
%defattr(-,root,root,-)
%doc examples/*.c examples/*.h examples/rlfe
%{_includedir}/readline/*.h
%{_libdir}/lib*.so

%files static
%defattr(-,root,root,-)
%{_libdir}/lib*.a

