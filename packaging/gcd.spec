%define gcc_version %(LANG=C gcc --version | head -1 | sed 's/.* (.*) \\([0-9]\\.[0-9]\\).*$/\\1/')

Name:       gcd
Summary:    GCD(Grand Central Dispatch) library
Version:    1.0
Release:    1
License:    Apache-2.0 and BSD-2-Clause
Group:      System/Libraries
Source0:    %{name}-%{version}.tar.gz
BuildRequires:  clang


%description
GCD(Grand Central Dispatch) library.

%package devel
Summary:    GCD(Grand Central Dispatch) library
Requires:   %{name} = %{version}-%{release}

%description devel
GCD(Grand Central Dispatch) library. (DEV)


%prep
%setup -q -n gcd-1.0

%build

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
export CC="clang -target i586-tizen-linux"
export CFLAGS="$CFLAGS -Xlinker -L/usr/lib/gcc/i586-tizen-linux/%{gcc_version}"
export COMPILER_PATH=/usr/lib/gcc/i586-tizen-linux/%{gcc_version}
%else
export CC="clang -target %{_target_cpu}-tizen-linux-gnueabi"
export CFLAGS="$CFLAGS -Xlinker -L/usr/lib/gcc/%{_target_cpu}-tizen-linux-gnueabi/%{gcc_version}"
export COMPILER_PATH=/usr/lib/gcc/%{_target_cpu}-tizen-linux-gnueabi/%{gcc_version}
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
export COMPILER_PATH=/usr/lib/gcc/i586-tizen-linux/%{gcc_version}
%else
export COMPILER_PATH=/usr/lib/gcc/%{_target_cpu}-tizen-linux-gnueabi/%{gcc_version}
%endif
make DESTDIR=$RPM_BUILD_ROOT install
cd ..

find %{?buildroot:%{buildroot}} -regex ".*\\.la$" | xargs rm -f --

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%manifest gcd.manifest
%license LICENSE
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
%{_libdir}/libkqueue.a
%{_libdir}/pkgconfig/libkqueue.pc
%{_includedir}/pthread_workqueue.h
%{_libdir}/libpthread_workqueue.so
%{_includedir}/Block.h
%{_includedir}/Block_private.h
%{_libdir}/libBlocksRuntime.so
%{_includedir}/dispatch/*.h
%{_libdir}/libdispatch.a
%{_libdir}/libdispatch.so
/usr/share/man/man3/pthread_workqueue.3.gz
/usr/share/man/man2/kqueue.2.gz
/usr/share/man/man2/kevent.2.gz
/usr/share/man/man3/dispatch*
