%define rl_major 8
%define rversion 8.2
%define rpatchlvl 10

#specfile originally created for Fedora, modified for Moblin Linux
Summary: A library for editing typed command lines
Name: readline
# Git Tag should match these 
Version: %{rversion}.%{rpatchlvl}
Release: 1
License: GPL-3.0-or-later
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


%package -n libreadline%{rl_major}
Summary:        The Readline Library
Group:          System/Libraries
Suggests:       readline-doc = %{version}
Provides:       libreadline%{rl_major} = %{rversion}
Provides:       readline = %{rversion}
Obsoletes:      readline <= 8.1

%description -n libreadline%{rl_major}
The readline library is used by the Bourne Again Shell (bash, the
standard command interpreter) for easy editing of command lines.  This
includes history and search functionality.

%package devel
Summary: Files needed to develop programs which use the readline library
Requires: libreadline%{rl_major} >= %{rversion}
Requires: ncurses-devel
Recommends: readline-doc = %{version}

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

%build
%configure --enable-static=no \
           --enable-shared			\
           --enable-multibyte		\
           --disable-bracketed-paste-default \
           %{nil}

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

%files -n libreadline%{rl_major}
%license COPYING
%{_libdir}/libreadline*.so.*
%{_libdir}/libhistory*.so.*

%files devel
%{_includedir}/readline/*.h
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/pkgconfig/history.pc

%files doc
%{_infodir}/*.*
%{_mandir}/man3/%{name}.*
%{_mandir}/man3/history.*
%{_docdir}/%{name}-%{version}
%{_docdir}/%{name}
