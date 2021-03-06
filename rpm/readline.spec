#specfile originally created for Fedora, modified for Moblin Linux
Summary: A library for editing typed command lines
Name: readline
Version: 8.1
Release: 1
License: GPLv3+
URL: https://tiswww.case.edu/php/chet/readline/rltop.html
Source: %{name}-%{version}.tar.xz
Patch1: readline-5.2-shlib.patch

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
Requires: %{name} = %{version}-%{release}
Requires: ncurses-devel

%description devel
The Readline library provides a set of functions that allow users to
edit typed command lines. If you want to develop programs that will
use the readline library, you need to have the readline-devel package
installed. You also need to have the readline package installed.

%package doc
Summary:   Documentation for %{name}
Requires:  %{name} = %{version}-%{release}
Obsoletes: %{name}-docs

%description doc
Examples, man and info pages for %{name}.

%prep
%autosetup -p1 -n %{name}-%{version}/upstream

pushd examples
rm -f rlfe/configure
iconv -f iso8859-1 -t utf8 -o rl-fgets.c{_,}
touch -r rl-fgets.c{,_}
mv -f rl-fgets.c{_,}
popd

%build
export CPPFLAGS="-I%{_includedir}/ncurses"
%configure --enable-static=no
%make_build

%install
%make_install

rm -f %{buildroot}/%{_infodir}/dir

mkdir -p %{buildroot}/%{_docdir}/%{name}-%{version}
install -m0644 -t %{buildroot}/%{_docdir}/%{name}-%{version} \
        CHANGELOG CHANGES NEWS examples/*.c examples/*.h examples/rlfe/*.c \
        examples/rlfe/*.h examples/rlfe/README examples/rlfe/ChangeLog

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%license COPYING
%{_libdir}/libreadline*.so.*
%{_libdir}/libhistory*.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/readline/*.h
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/%{name}.pc

%files doc
%defattr(-,root,root,-)
%{_infodir}/*.*
%{_mandir}/man3/%{name}.*
%{_mandir}/man3/history.*
%{_docdir}/%{name}-%{version}
%{_docdir}/%{name}
