Name:       gcd
Summary:    GCD(Grand Central Dispatch) library
Version:    1.0
Release:    1
License:    Apache License, Version 2.0 and BSD
Vendor:     AUTHOR
Group:      System Environment/Libraries
Source0:    %{name}-%{version}.tar.gz
BuildRoot:  %{_tmppath}/%{name}-%{version}-build
Provides:   libdispatch.so.0 libkqueue.so.0 libBlocksRuntime.so.0 libpthread_workqueue.so.0
BuildRequires:  clang


%description
GCD(Grand Central Dispatch) library.

%package devel  
Summary:    GCD(Grand Central Dispatch) library.  
Group:      TO_BE/FILLED_IN  
Requires:   %{name} = %{version}-%{release}  
  
%description devel  
GCD(Grand Central Dispatch) library. (DEV)  

%prep
%setup -q -n gcd-1.0

%build

export GCCVER=$(LANG=C gcc --version | head -1 | sed 's/\([a-z+]*\) \((.*)\) \([1-9\.]*\)\(.*\)/\3/')

cd kqueue-1.0.4
./configure --prefix=/usr
make
cd ..
cd pthread_workqueue-0.8.2
./configure --prefix=/usr
make
cd ..
cd BlocksRuntime-0.1
./configure --prefix=/usr
make
cd ..
cd dispatch-1.0
export KQUEUE_CFLAGS="-I../../kqueue-1.0.4/include"
export KQUEUE_LIBS="/usr/lib"
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:%{_builddir}/%{name}-%{version}/BlocksRuntime-0.1"
export CFLAGS="$CFLAGS -L%{_builddir}/%{name}-%{version}/BlocksRuntime-0.1 -lBlocksRuntime -I%{_builddir}/%{name}-%{version}/BlocksRuntime-0.1 -Xlinker --build-id"

%ifarch %{ix86}
export CC="clang -target i386-tizen-linux-gnueabi"
export CFLAGS="$CFLAGS -Xlinker -L/usr/lib/gcc/i586-tizen-linux/$GCCVER"
export COMPILER_PATH=/usr/lib/gcc/i586-tizen-linux/$GCCVER
%else
export CC="clang -target arm-tizen-linux-gnueabi"
export CFLAGS="$CFLAGS -Xlinker -L/usr/lib/gcc/armv7l-tizen-linux-gnueabi/$GCCVER"
export COMPILER_PATH=/usr/lib/gcc/armv7l-tizen-linux-gnueabi/$GCCVER
%endif

./configure --with-blocks-runtime=/usr/lib --prefix=/usr
make
cd ..

%install
cd kqueue-1.0.4
make DESTDIR=$RPM_BUILD_ROOT install
gzip $RPM_BUILD_ROOT/usr/share/man/man2/kqueue.2
gzip $RPM_BUILD_ROOT/usr/share/man/man2/kevent.2
cd ..
cd pthread_workqueue-0.8.2
make DESTDIR=$RPM_BUILD_ROOT install
cd ..
cd BlocksRuntime-0.1
make DESTDIR=$RPM_BUILD_ROOT install
cd ..
cd dispatch-1.0
%ifarch %{ix86}
export COMPILER_PATH=/usr/lib/gcc/i586-tizen-linux/$GCCVER
%else
export COMPILER_PATH=/usr/lib/gcc/armv7l-tizen-linux-gnueabi/$GCCVER
%endif
make DESTDIR=$RPM_BUILD_ROOT install
cd ..
mkdir -p %{buildroot}/usr/share/license
cp %{_builddir}/%{name}-%{version}/LICENSE  %{buildroot}/usr/share/license/%{name}


%clean
[ ${RPM_BUILD_ROOT} != "/" ] && rm -rf ${RPM_BUILD_ROOT}

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%manifest gcd.manifest
/usr/share/license/%{name}
%defattr(-,root,root)
%{_libdir}/libkqueue.so.0
%{_libdir}/libkqueue.so.0.0
%{_libdir}/libpthread_workqueue.so.0
%{_libdir}/libpthread_workqueue.so.0.0
%{_libdir}/libBlocksRuntime.so.0
%{_libdir}/libBlocksRuntime.so.0.0
%{_libdir}/libdispatch.so.0
%{_libdir}/libdispatch.so.0.0.0

%files devel
%{_includedir}/kqueue/sys/event.h
%{_libdir}/libkqueue.so
%{_libdir}/libkqueue.so.0
%{_libdir}/libkqueue.so.0.0
%{_libdir}/libkqueue.la
%{_libdir}/libkqueue.a
%{_libdir}/pkgconfig/libkqueue.pc
/usr/share/man/man2/kqueue.2.gz
/usr/share/man/man2/kevent.2.gz
%{_includedir}/pthread_workqueue.h
%{_libdir}/libpthread_workqueue.so
%{_libdir}/libpthread_workqueue.so.0
%{_libdir}/libpthread_workqueue.so.0.0
/usr/share/man/man3/pthread_workqueue.3.gz
%{_includedir}/Block.h
%{_includedir}/Block_private.h
%{_libdir}/libBlocksRuntime.so
%{_libdir}/libBlocksRuntime.so.0
%{_libdir}/libBlocksRuntime.so.0.0
%{_includedir}/dispatch/*.h
%{_libdir}/libdispatch.a
%{_libdir}/libdispatch.la
/usr/share/man/man3/dispatch*
%{_libdir}/libdispatch.so

%changelog
