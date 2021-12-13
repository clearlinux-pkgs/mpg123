#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x231C4CBC60D5CAFE (thomas@orgis.org)
#
Name     : mpg123
Version  : 1.29.3
Release  : 44
URL      : https://www.mpg123.de/download/mpg123-1.29.3.tar.bz2
Source0  : https://www.mpg123.de/download/mpg123-1.29.3.tar.bz2
Source1  : https://www.mpg123.de/download/mpg123-1.29.3.tar.bz2.sig
Summary  : An optimised MPEG Audio decoder
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: mpg123-bin = %{version}-%{release}
Requires: mpg123-filemap = %{version}-%{release}
Requires: mpg123-lib = %{version}-%{release}
Requires: mpg123-license = %{version}-%{release}
Requires: mpg123-man = %{version}-%{release}
BuildRequires : alsa-lib-dev
BuildRequires : buildreq-cmake
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : pkg-config
BuildRequires : pkgconfig(32libpulse-simple)
BuildRequires : pkgconfig(32sdl2)
BuildRequires : pkgconfig(libpulse-simple)
BuildRequires : pkgconfig(sdl)
BuildRequires : pkgconfig(sdl2)

%description
This is a console based decoder/player for mono/stereo mpeg audio files,
probably more familiar as MP3 or MP2 files. It's focus is speed.
It can play MPEG1.0/2.0/2.5 layer I, II, II (1, 2, 3;-) files
(VBR files are fine, too) and produce output on a number of different ways:
raw data to stdout and different sound systems depending on your platform.

%package bin
Summary: bin components for the mpg123 package.
Group: Binaries
Requires: mpg123-license = %{version}-%{release}
Requires: mpg123-filemap = %{version}-%{release}

%description bin
bin components for the mpg123 package.


%package dev
Summary: dev components for the mpg123 package.
Group: Development
Requires: mpg123-lib = %{version}-%{release}
Requires: mpg123-bin = %{version}-%{release}
Provides: mpg123-devel = %{version}-%{release}
Requires: mpg123 = %{version}-%{release}

%description dev
dev components for the mpg123 package.


%package dev32
Summary: dev32 components for the mpg123 package.
Group: Default
Requires: mpg123-lib32 = %{version}-%{release}
Requires: mpg123-bin = %{version}-%{release}
Requires: mpg123-dev = %{version}-%{release}

%description dev32
dev32 components for the mpg123 package.


%package filemap
Summary: filemap components for the mpg123 package.
Group: Default

%description filemap
filemap components for the mpg123 package.


%package lib
Summary: lib components for the mpg123 package.
Group: Libraries
Requires: mpg123-license = %{version}-%{release}
Requires: mpg123-filemap = %{version}-%{release}

%description lib
lib components for the mpg123 package.


%package lib32
Summary: lib32 components for the mpg123 package.
Group: Default
Requires: mpg123-license = %{version}-%{release}

%description lib32
lib32 components for the mpg123 package.


%package license
Summary: license components for the mpg123 package.
Group: Default

%description license
license components for the mpg123 package.


%package man
Summary: man components for the mpg123 package.
Group: Default

%description man
man components for the mpg123 package.


%prep
%setup -q -n mpg123-1.29.3
cd %{_builddir}/mpg123-1.29.3
pushd ..
cp -a mpg123-1.29.3 build32
popd
pushd ..
cp -a mpg123-1.29.3 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1639417226
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mno-vzeroupper -mprefer-vector-width=256 "
export FCFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mno-vzeroupper -mprefer-vector-width=256 "
export FFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mno-vzeroupper -mprefer-vector-width=256 "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mno-vzeroupper -mprefer-vector-width=256 "
%configure --disable-static
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig:/usr/share/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
%configure --disable-static    --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
unset PKG_CONFIG_PATH
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3"
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3"
%configure --disable-static
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../build32;
make %{?_smp_mflags} check || :
cd ../buildavx2;
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1639417226
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/mpg123
cp %{_builddir}/mpg123-1.29.3/COPYING %{buildroot}/usr/share/package-licenses/mpg123/5b0649acc39fef80cccbf195783245940f951fc5
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
if [ -d %{buildroot}/usr/share/pkgconfig ]
then
pushd %{buildroot}/usr/share/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
pushd ../buildavx2/
%make_install_v3
popd
%make_install
## Remove excluded files
rm -f %{buildroot}*/usr/lib64/mpg123/haswell/output_alsa.so
rm -f %{buildroot}*/usr/lib64/mpg123/haswell/output_dummy.so
rm -f %{buildroot}*/usr/lib64/mpg123/haswell/output_openal.so
rm -f %{buildroot}*/usr/lib64/mpg123/haswell/output_oss.so
rm -f %{buildroot}*/usr/lib64/mpg123/haswell/output_pulse.so
rm -f %{buildroot}*/usr/lib64/mpg123/haswell/output_sdl.so
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot}/usr/share/clear/optimized-elf/ %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/mpg123
/usr/bin/mpg123-id3dump
/usr/bin/mpg123-strip
/usr/bin/out123
/usr/share/clear/optimized-elf/bin*

%files dev
%defattr(-,root,root,-)
/usr/include/fmt123.h
/usr/include/mpg123.h
/usr/include/out123.h
/usr/include/syn123.h
/usr/lib64/libmpg123.so
/usr/lib64/libout123.so
/usr/lib64/libsyn123.so
/usr/lib64/pkgconfig/libmpg123.pc
/usr/lib64/pkgconfig/libout123.pc
/usr/lib64/pkgconfig/libsyn123.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libmpg123.so
/usr/lib32/libout123.so
/usr/lib32/libsyn123.so
/usr/lib32/pkgconfig/32libmpg123.pc
/usr/lib32/pkgconfig/32libout123.pc
/usr/lib32/pkgconfig/32libsyn123.pc
/usr/lib32/pkgconfig/libmpg123.pc
/usr/lib32/pkgconfig/libout123.pc
/usr/lib32/pkgconfig/libsyn123.pc

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-mpg123

%files lib
%defattr(-,root,root,-)
/usr/lib64/libmpg123.so.0
/usr/lib64/libmpg123.so.0.46.7
/usr/lib64/libout123.so.0
/usr/lib64/libout123.so.0.4.3
/usr/lib64/libsyn123.so.0
/usr/lib64/libsyn123.so.0.1.4
/usr/lib64/mpg123/output_alsa.so
/usr/lib64/mpg123/output_dummy.so
/usr/lib64/mpg123/output_oss.so
/usr/lib64/mpg123/output_pulse.so
/usr/lib64/mpg123/output_sdl.so
/usr/share/clear/optimized-elf/lib*

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libmpg123.so.0
/usr/lib32/libmpg123.so.0.46.7
/usr/lib32/libout123.so.0
/usr/lib32/libout123.so.0.4.3
/usr/lib32/libsyn123.so.0
/usr/lib32/libsyn123.so.0.1.4
/usr/lib32/mpg123/output_dummy.so
/usr/lib32/mpg123/output_oss.so
/usr/lib32/mpg123/output_pulse.so
/usr/lib32/mpg123/output_sdl.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mpg123/5b0649acc39fef80cccbf195783245940f951fc5

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/mpg123.1
/usr/share/man/man1/out123.1
