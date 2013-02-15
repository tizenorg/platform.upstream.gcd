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

Name:       dispatch
Summary:    user space implementation of the Grand Central Dispatch API
Version:    1.0
Release:    1
License:    LICENSE
Vendor:     AUTHOR
Group:      System Environment/Libraries
Source0:    %{name}-%version.tar.gz
BuildRoot:  %{_tmppath}/%{name}-%{version}-buildRequires: capi-account-manager 

BuildRequires:  kqueue-devel
BuildRequires:  pthread_workqueue-devel
BuildRequires:  BlocksRuntime-devel
Requires: kqueue pthread_workqueue BlocksRuntime
Provides:   libdispatch.so.0

%description
user space implementation of the Grand Central Dispatch API.

%package devel  
Summary:    user space implementation of the Grand Central Dispatch API. (Development)  
Group:      TO_BE/FILLED_IN  
Requires:   %{name} = %{version}-%{release}  
  
%description devel  
user space implementation of the Grand Central Dispatch API. (DEV)  

%prep
%setup -q -n dispatch-1.0

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

/usr/lib/libdispatch.so.0
/usr/lib/libdispatch.so.0.0.0

%files devel
/usr/include/dispatch/base.h
/usr/include/dispatch/dispatch.h
/usr/include/dispatch/group.h
/usr/include/dispatch/object.h
/usr/include/dispatch/once.h
/usr/include/dispatch/queue.h
/usr/include/dispatch/semaphore.h
/usr/include/dispatch/source.h
/usr/include/dispatch/time.h
/usr/lib/libdispatch.a
/usr/lib/libdispatch.la
/usr/share/man/man3/dispatch.3.gz
/usr/share/man/man3/dispatch_after.3.gz
/usr/share/man/man3/dispatch_after_f.3.gz
/usr/share/man/man3/dispatch_api.3.gz
/usr/share/man/man3/dispatch_apply.3.gz
/usr/share/man/man3/dispatch_apply_f.3.gz
/usr/share/man/man3/dispatch_async.3.gz
/usr/share/man/man3/dispatch_async_f.3.gz
/usr/share/man/man3/dispatch_benchmark.3.gz
/usr/share/man/man3/dispatch_benchmark_f.3.gz
/usr/share/man/man3/dispatch_get_context.3.gz
/usr/share/man/man3/dispatch_get_current_queue.3.gz
/usr/share/man/man3/dispatch_get_global_queue.3.gz
/usr/share/man/man3/dispatch_get_main_queue.3.gz
/usr/share/man/man3/dispatch_group_async.3.gz
/usr/share/man/man3/dispatch_group_async_f.3.gz
/usr/share/man/man3/dispatch_group_create.3.gz
/usr/share/man/man3/dispatch_group_enter.3.gz
/usr/share/man/man3/dispatch_group_leave.3.gz
/usr/share/man/man3/dispatch_group_notify.3.gz
/usr/share/man/man3/dispatch_group_notify_f.3.gz
/usr/share/man/man3/dispatch_group_wait.3.gz
/usr/share/man/man3/dispatch_main.3.gz
/usr/share/man/man3/dispatch_object.3.gz
/usr/share/man/man3/dispatch_once.3.gz
/usr/share/man/man3/dispatch_once_f.3.gz
/usr/share/man/man3/dispatch_queue_create.3.gz
/usr/share/man/man3/dispatch_queue_get_label.3.gz
/usr/share/man/man3/dispatch_release.3.gz
/usr/share/man/man3/dispatch_resume.3.gz
/usr/share/man/man3/dispatch_retain.3.gz
/usr/share/man/man3/dispatch_semaphore_create.3.gz
/usr/share/man/man3/dispatch_semaphore_signal.3.gz
/usr/share/man/man3/dispatch_semaphore_wait.3.gz
/usr/share/man/man3/dispatch_set_context.3.gz
/usr/share/man/man3/dispatch_set_finalizer_f.3.gz
/usr/share/man/man3/dispatch_set_target_queue.3.gz
/usr/share/man/man3/dispatch_source_cancel.3.gz
/usr/share/man/man3/dispatch_source_create.3.gz
/usr/share/man/man3/dispatch_source_get_data.3.gz
/usr/share/man/man3/dispatch_source_get_handle.3.gz
/usr/share/man/man3/dispatch_source_get_mask.3.gz
/usr/share/man/man3/dispatch_source_merge_data.3.gz
/usr/share/man/man3/dispatch_source_set_cancel_handler.3.gz
/usr/share/man/man3/dispatch_source_set_cancel_handler_f.3.gz
/usr/share/man/man3/dispatch_source_set_event_handler.3.gz
/usr/share/man/man3/dispatch_source_set_event_handler_f.3.gz
/usr/share/man/man3/dispatch_source_set_timer.3.gz
/usr/share/man/man3/dispatch_source_testcancel.3.gz
/usr/share/man/man3/dispatch_suspend.3.gz
/usr/share/man/man3/dispatch_sync.3.gz
/usr/share/man/man3/dispatch_sync_f.3.gz
/usr/share/man/man3/dispatch_time.3.gz
/usr/share/man/man3/dispatch_walltime.3.gz  
/usr/lib/libdispatch.so
/usr/lib/libdispatch.so.0
/usr/lib/libdispatch.so.0.0.0

%changelog
