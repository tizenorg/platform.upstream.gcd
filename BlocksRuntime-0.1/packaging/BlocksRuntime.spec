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

Name:       BlocksRuntime
Summary:    Blocks Runtime library
Version:    0.1
Release:    1
License:    LICENSE
Vendor:     AUTHOR
Group:      System Environment/Libraries
Source0:    %{name}-%version.tar.gz
BuildRoot:  %{_tmppath}/%{name}-%{version}-build
Provides:   libBlocksRuntime.so.0

%description
Blocks Runtime library.

%package devel  
Summary:    Blocks Runtime library. (Development)  
Group:      TO_BE/FILLED_IN  
Requires:   %{name} = %{version}-%{release}  
  
%description devel  
Blocks Runtime library. (DEV)  

%prep
%setup -q -n BlocksRuntime-0.1

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

/usr/lib/libBlocksRuntime.so.0
/usr/lib/libBlocksRuntime.so.0.0

%files devel  
/usr/include/Block.h
/usr/include/Block_private.h
/usr/lib/libBlocksRuntime.so
/usr/lib/libBlocksRuntime.so.0
/usr/lib/libBlocksRuntime.so.0.0

%changelog
