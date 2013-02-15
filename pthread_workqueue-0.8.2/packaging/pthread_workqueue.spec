#
# Copyright (c) 2009 Mark Heily <mark@heily.com>
#
# Permission to use, copy, modify, and distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
# 
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#

Name:       pthread_workqueue
Summary:    thread pool library
Version:    0.8.2
Release:    1
License:    LICENSE
Vendor:     AUTHOR
Group:      System Environment/Libraries
Source0:    %{name}-%version.tar.gz
BuildRoot:  %{_tmppath}/%{name}-%{version}-build
Provides:   libpthread_workqueue.so.0 libpthread_workqueue.so

%description
thread pool library.

%package devel  
Summary:    thread pool library. (Development)  
Group:      TO_BE/FILLED_IN  
Requires:   %{name} = %{version}-%{release}  
  
%description devel  
thread pool library. (DEV)  

%prep
%setup -q -n pthread_workqueue-0.8.2

%build
./configure --prefix=/usr
make

%install
make DESTDIR=$RPM_BUILD_ROOT install

%clean
[ ${RPM_BUILD_ROOT} != "/" ] && rm -rf ${RPM_BUILD_ROOT}

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%defattr(-,root,root)

/usr/lib/libpthread_workqueue.so.0
/usr/lib/libpthread_workqueue.so.0.0

%files devel  
/usr/include/pthread_workqueue.h
/usr/lib/libpthread_workqueue.so
/usr/lib/libpthread_workqueue.so.0
/usr/lib/libpthread_workqueue.so.0.0
/usr/share/man/man3/pthread_workqueue.3.gz

%changelog
