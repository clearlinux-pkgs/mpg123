#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x231C4CBC60D5CAFE (thomas@orgis.org)
#
Name     : mpg123
Version  : 1.25.6
Release  : 7
URL      : https://www.mpg123.de/download/mpg123-1.25.6.tar.bz2
Source0  : https://www.mpg123.de/download/mpg123-1.25.6.tar.bz2
Source99 : https://www.mpg123.de/download/mpg123-1.25.6.tar.bz2.sig
Summary  : An optimised MPEG Audio decoder
Group    : Development/Tools
License  : LGPL-2.1
Requires: mpg123-bin
Requires: mpg123-lib
Requires: mpg123-doc
BuildRequires : alsa-lib-dev
BuildRequires : pkgconfig(libpulse-simple)
BuildRequires : pkgconfig(sdl)

%description
This is a console based decoder/player for mono/stereo mpeg audio files,
probably more familiar as MP3 or MP2 files. It's focus is speed.
It can play MPEG1.0/2.0/2.5 layer I, II, II (1, 2, 3;-) files
(VBR files are fine, too) and produce output on a number of different ways:
raw data to stdout and different sound systems depending on your platform.

%package bin
Summary: bin components for the mpg123 package.
Group: Binaries

%description bin
bin components for the mpg123 package.


%package dev
Summary: dev components for the mpg123 package.
Group: Development
Requires: mpg123-lib
Requires: mpg123-bin
Provides: mpg123-devel

%description dev
dev components for the mpg123 package.


%package doc
Summary: doc components for the mpg123 package.
Group: Documentation

%description doc
doc components for the mpg123 package.


%package lib
Summary: lib components for the mpg123 package.
Group: Libraries

%description lib
lib components for the mpg123 package.


%prep
%setup -q -n mpg123-1.25.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1502462122
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-semantic-interposition "
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1502462122
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/mpg123
/usr/bin/mpg123-id3dump
/usr/bin/mpg123-strip
/usr/bin/out123

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/libmpg123.so
/usr/lib64/libout123.so
/usr/lib64/pkgconfig/libmpg123.pc
/usr/lib64/pkgconfig/libout123.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libmpg123.so.0
/usr/lib64/libmpg123.so.0.44.5
/usr/lib64/libout123.so.0
/usr/lib64/libout123.so.0.2.1
/usr/lib64/mpg123/output_alsa.so
/usr/lib64/mpg123/output_dummy.so
/usr/lib64/mpg123/output_oss.so
/usr/lib64/mpg123/output_pulse.so
/usr/lib64/mpg123/output_sdl.so
