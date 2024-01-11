%global tarball xf86-video-v4l
%global moduledir %(pkg-config xorg-server --variable=moduledir )
%global driverdir	%{moduledir}/drivers

%undefine _hardened_build

Summary:   Xorg X11 v4l video driver
Name:      xorg-x11-drv-v4l
Version:   0.3.0
Release:   2%{?dist}
URL:       http://www.x.org
License:   MIT
Group:     User Interface/X Hardware Support

Source0:   https://www.x.org/pub/individual/driver/%{tarball}-%{version}.tar.bz2

Patch01:   0001-Remove-unused-variable-osname.patch
Patch02:   0002-Ensure-the-device-name-is-null-terminated.patch
Patch03:   0003-Fix-handling-of-realloc-failure.patch
Patch04:   0004-Fix-ioctl-return-value-handling.patch

ExcludeArch: s390 s390x

BuildRequires: xorg-x11-server-devel >= 1.10.99.902
BuildRequires: autoconf automake libtool

Requires: Xorg %([ -e /usr/bin/xserver-sdk-abi-requires ] && xserver-sdk-abi-requires ansic || :)
Requires: Xorg %([ -e /usr/bin/xserver-sdk-abi-requires ] && xserver-sdk-abi-requires videodrv || :)

%description 
X.Org X11 v4l video driver.

%prep
%autosetup -p1 -n %{tarball}-%{version}

%build
autoreconf -vif
%configure --disable-static
make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

# FIXME: Remove all libtool archives (*.la) from modules directory.  This
# should be fixed in upstream Makefile.am or whatever.
find $RPM_BUILD_ROOT -regex ".*\.la$" | xargs rm -f --

%files
%{driverdir}/v4l_drv.so
%{_mandir}/man4/v4l.4*

%changelog
* Mon Oct 08 2018 Peter Hutterer <peter.hutterer@redhat.com> 0.3.0-2
- Fix coverity complaints (#1636829)
- Use autosetup

* Tue Aug 14 2018 Adam Jackson <ajax@redhat.com> - 0.3.0-1
- v4l 0.3.0

* Fri Jul 20 2018 Peter Hutterer <peter.hutterer@redhat.com> 0.2.0-54
- Remove call to LoaderGetOS (#1602317)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-53
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 02 2018 Adam Jackson <ajax@redhat.com> - 0.2.0-52
- Rebuild for xserver 1.20

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-51
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Sep 29 2016 Hans de Goede <hdegoede@redhat.com> - 0.2.0-47
- Rebuild against xserver-1.19

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 28 2016 Peter Hutterer <peter.hutterer@redhat.com>
- Remove unnecessary defattr
    
* Wed Jan 20 2016 Peter Hutterer <peter.hutterer@redhat.com>
- s/define/global/

* Wed Jul 29 2015 Dave Airlie <airlied@redhat.com> - 0.2.0-45
- 1.15 ABI rebuild

* Tue Jun 23 2015 Adam Jackson <ajax@redhat.com> - 0.2.0-44
- Undefine _hardened_build

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Feb 11 2015 Hans de Goede <hdegoede@redhat.com> - 0.2.0-42
- xserver 1.17 ABI rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun 16 2014 Hans de Goede <hdegoede@redhat.com> - 0.2.0-40
- xserver 1.15.99.903 ABI rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr 29 2014 Adam Jackson <ajax@redhat.com> 0.2.0-38
- v4l2 patch is MIT-compatible, fix License to match

* Mon Apr 28 2014 Hans de Goede <hdegoede@redhat.com> - 0.2.0-37
- xserver 1.15.99-20140428 git snapshot ABI rebuild

* Mon Jan 13 2014 Adam Jackson <ajax@redhat.com> - 0.2.0-36
- 1.15 ABI rebuild

* Tue Dec 17 2013 Adam Jackson <ajax@redhat.com> - 0.2.0-35
- 1.15RC4 ABI rebuild

* Wed Nov 20 2013 Adam Jackson <ajax@redhat.com> - 0.2.0-34
- 1.15RC2 ABI rebuild

* Wed Nov 06 2013 Adam Jackson <ajax@redhat.com> - 0.2.0-33
- 1.15RC1 ABI rebuild

* Fri Oct 25 2013 Adam Jackson <ajax@redhat.com> - 0.2.0-32
- ABI rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Mar 19 2013 Adam Jackson <ajax@redhat.com> 0.2.0-30
- Less RHEL customization

* Thu Mar 07 2013 Dave Airlie <airlied@redhat.com> 0.2.0-29
- autoreconf for aarch64

* Thu Mar 07 2013 Peter Hutterer <peter.hutterer@redhat.com> - 0.2.0-28
- require xorg-x11-server-devel, not -sdk

* Thu Mar 07 2013 Peter Hutterer <peter.hutterer@redhat.com> - 0.2.0-27
- ABI rebuild

* Fri Feb 15 2013 Peter Hutterer <peter.hutterer@redhat.com> - 0.2.0-26
- ABI rebuild

* Fri Feb 15 2013 Peter Hutterer <peter.hutterer@redhat.com> - 0.2.0-25
- ABI rebuild

* Thu Jan 10 2013 Adam Jackson <ajax@redhat.com> - 0.2.0-24
- ABI rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jul 18 2012 Dave Airlie <airlied@redhat.com> - 0.2.0-22
- ABI rebuild

* Thu Apr 05 2012 Adam Jackson <ajax@redhat.com> - 0.2.0-21
- RHEL arch exclude updates

* Sat Feb 11 2012 Peter Hutterer <peter.hutterer@redhat.com> - 0.2.0-20
- ABI rebuild

* Fri Feb 10 2012 Peter Hutterer <peter.hutterer@redhat.com> - 0.2.0-19
- ABI rebuild

* Tue Jan 24 2012 Peter Hutterer <peter.hutterer@redhat.com> - 0.2.0-18
- ABI rebuild

* Wed Jan 04 2012 Peter Hutterer <peter.hutterer@redhat.com> - 0.2.0-17
- Rebuild for server 1.12

* Mon Nov 14 2011 Adam Jackson <ajax@redhat.com> - 0.2.0-16
- ABI rebuild

* Wed Nov 09 2011 ajax <ajax@redhat.com> - 0.2.0-15
- ABI rebuild

* Thu Aug 18 2011 Adam Jackson <ajax@redhat.com> - 0.2.0-14
- Rebuild for xserver 1.11 ABI

* Wed May 11 2011 Peter Hutterer <peter.hutterer@redhat.com> - 0.2.0-13
- Rebuild for server 1.11

* Mon Feb 28 2011 Peter Hutterer <peter.hutterer@redhat.com> - 0.2.0-12
- Rebuild for server 1.10

* Thu Feb 10 2011 Mauro Carvalho Chehab <mchehabr@redhat.com> - 0.2.0-10
- Removed the v4l1 compat layer and converted the driver to direclty use
  the v4l2 API. With this, new standards and new Port Attributes are now
  shown, reflecting what the driver is exporting.

* Wed Feb 09 2011 Adam Jackson <ajax@redhat.com> 0.2.0-10
- Fix License tag to GPLv2+ due to v4l2 patch.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Feb 03 2011 Mauro Carvalho Chehab <mchehabr@redhat.com> - 0.2.0-8
- Make it work with V4L2 drivers

* Thu Dec 02 2010 Peter Hutterer <peter.hutterer@redhat.com> - 0.2.0-7
- Rebuild for server 1.10

* Wed Oct 27 2010 Adam Jackson <ajax@redhat.com> 0.2.0-6
- Add ABI requires magic (#542742)

* Mon Jul 05 2010 Peter Hutterer <peter.hutterer@redhat.com> - 0.2.0-5.1
- rebuild for X Server 1.9

* Thu Jan 21 2010 Peter Hutterer <peter.hutterer@redhat.com> - 0.2.0-4.1
- Rebuild for server 1.8

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-3.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 15 2009 Adam Jackson <ajax@redhat.com> - 0.2.0-2.1
- ABI bump

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Mar 20 2008 Dave Airlie <airlied@redhat.com> 0.2.0-1
- Latest upstream release

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.1.1-9
- Autorebuild for GCC 4.3

* Tue Aug 28 2007 Adam Jackson <ajax@redhat.com> 0.1.1-8
- Fix ioctl argument on LP64 machines. (#250070)

* Thu Aug 23 2007 Adam Jackson <ajax@redhat.com> - 0.1.1-7
- Rebuild for ppc toolchain bug

* Mon Jun 18 2007 Adam Jackson <ajax@redhat.com> 0.1.1-6
- Update Requires and BuildRequires.  Disown the module directories.

* Fri Feb 16 2007 Adam Jackson <ajax@redhat.com> 0.1.1-5
- ExclusiveArch -> ExcludeArch

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0.1.1-4
- rebuild

* Tue May 23 2006 Adam Jackson <ajackson@redhat.com> 0.1.1-3
- Rebuild for 7.1 ABI fix.

* Fri May 19 2006 Mike A. Harris <mharris@redhat.com> 0.1.1-2
- Added "BuildRequires: xorg-x11-proto-devel" for (#192386)

* Sun Apr  9 2006 Adam Jackson <ajackson@redhat.com> 0.1.1-1
- Update to 0.1.1 from 7.1RC1.

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> 0.0.1.5-1.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Wed Jan 18 2006 Mike A. Harris <mharris@redhat.com> 0.0.1.5-1
- Updated xorg-x11-drv-v4l to version 0.0.1.5 from X11R7.0

* Tue Dec 20 2005 Mike A. Harris <mharris@redhat.com> 0.0.1.4-1
- Updated xorg-x11-drv-v4l to version 0.0.1.4 from X11R7 RC4
- Removed 'x' suffix from manpage dirs to match RC4 upstream.

* Fri Nov 4 2005 Mike A. Harris <mharris@redhat.com> 0.0.1.1-1
- Updated xorg-x11-drv-v4l to version 0.0.1.1 from X11R7 RC1.  For some
  unknown reason, the version went backwards from 4.0.0 to 0.0.1.1.
- Fix *.la file removal.

* Mon Oct 3 2005 Mike A. Harris <mharris@redhat.com> 4.0.0-1
- Initial spec file for v4l video driver forked from cirrus driver package.
