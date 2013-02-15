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

Name:       kqueue
Summary:    cross-platform library for kernel event notification
Version:    1.0.4
Release:    1
License:    LICENSE
Vendor:     AUTHOR
Group:      System Environment/Libraries
Source0:    %{name}-%version.tar.gz
BuildRoot:  %{_tmppath}/%{name}-%{version}-build
Provides:   libkqueue.so.0

%description
cross-platform library for kernel event notification.

%package devel  
Summary:    cross-platform library for kernel event notification. (Development)  
Group:      TO_BE/FILLED_IN  
Requires:   %{name} = %{version}-%{release}  
  
%description devel  
cross-platform library for kernel event notification. (DEV)  

%prep
%setup -q -n kqueue-1.0.4

%build
./configure --prefix=/usr
make

%install
make DESTDIR=$RPM_BUILD_ROOT install
gzip $RPM_BUILD_ROOT/usr/share/man/man2/kqueue.2
gzip $RPM_BUILD_ROOT/usr/share/man/man2/kevent.2

%clean
[ ${RPM_BUILD_ROOT} != "/" ] && rm -rf ${RPM_BUILD_ROOT}

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%defattr(-,root,root)

%{_libdir}/libkqueue.so.0
%{_libdir}/libkqueue.so.0.0

%files devel  
/usr/include/kqueue/sys/event.h
%{_libdir}/libkqueue.so
%{_libdir}/libkqueue.so.0
%{_libdir}/libkqueue.so.0.0
%{_libdir}/libkqueue.la
%{_libdir}/libkqueue.a
%{_libdir}/pkgconfig/libkqueue.pc
/usr/share/man/man2/kqueue.2.gz
/usr/share/man/man2/kevent.2.gz

%changelog
