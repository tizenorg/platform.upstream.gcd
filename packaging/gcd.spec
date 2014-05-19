Name:       gcd
Summary:    GCD(Grand Central Dispatch) library
Version:    1.0
Release:    1
License:    Apache-2.0 and BSD-2-Clause
Group:      System/Libraries
Source0:    %{name}-%{version}.tar.gz
BuildRequires:  clang

%description
Grand Central Dispatch (GCD) is a technology developed by Apple Inc.

%package devel
Summary:    GCD(Grand Central Dispatch) library
Requires:   %{name} = %{version}-%{release}

%description devel
Grand Central Dispatch (GCD) is a technology developed by Apple Inc. (DEV)

%prep
%setup -q -n %{name}-%{version}

%build
for sub_pkg in kqueue-1.0.4 \
               pthread_workqueue-0.8.2 \
               BlocksRuntime-0.1; do
    pushd ${sub_pkg}
    %configure
    make
    popd
done

pushd dispatch-1.0
export KQUEUE_CFLAGS="-I../../kqueue-1.0.4/include"
export KQUEUE_LIBS="%{_libdir}"
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:%{_builddir}/%{name}-%{version}/BlocksRuntime-0.1"
export CFLAGS="$CFLAGS -L%{_builddir}/%{name}-%{version}/BlocksRuntime-0.1 -lBlocksRuntime -I%{_builddir}/%{name}-%{version}/BlocksRuntime-0.1 -Xlinker --build-id"

export COMPILER_PATH="%{_libdir}/gcc/$(gcc -v 2>&1 | grep Target | sed -e 's/.*\s//')/$(gcc -v 2>&1 | grep 'gcc version' | sed -e 's/gcc\sversion\s//;s/\.[[:digit:]]\s.*$//')"

%ifarch %{ix86}
export CC="clang -target i586-tizen-linux"
export CFLAGS="$CFLAGS -Xlinker -L$COMPILER_PATH"
%else
export CC="clang -target %{_target_cpu}-tizen-linux"
export CFLAGS="$CFLAGS -Xlinker -L$COMPILER_PATH"
%endif

%configure --with-blocks-runtime=%{_libdir}
make
popd

%install
for sub_pkg in kqueue-1.0.4 \
               pthread_workqueue-0.8.2 \
               BlocksRuntime-0.1 \
               dispatch-1.0; do
    pushd ${sub_pkg}
    %make_install
    popd
done

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%manifest gcd.manifest
%license LICENSE
%{_libdir}/libkqueue.so.*
%{_libdir}/libpthread_workqueue.so.*
%{_libdir}/libBlocksRuntime.so.*
%{_libdir}/libdispatch.so.*

%files devel
%{_includedir}/kqueue/sys/event.h
%{_libdir}/libkqueue.so
%{_libdir}/pkgconfig/libkqueue.pc
%{_includedir}/pthread_workqueue.h
%{_libdir}/libpthread_workqueue.so
%{_includedir}/Block.h
%{_includedir}/Block_private.h
%{_libdir}/libBlocksRuntime.so
%{_includedir}/dispatch/*.h
%{_libdir}/libdispatch.so
%{_mandir}/man2/*.gz
%{_mandir}/man3/*.gz
