# TODO: review configure options:
# - ENABLE_WEBXR (experimental; BR: OpenXR >= 1.0.9, openxr.pc)?
# - ENABLE_ENCRYPTED_MEDIA, ENABLE_THUNDER (experimental; https://github.com/rdkcentral/Thunder)?
# - FTL_JIT on !x86_64?
# - WEB_RTC (experimental; BR: gstreamer-plugins-bad-devel (webrtc component) >= 1.20, openssl-devel)
# - WEB_RTC+MEDIA_STREAM (BR: openwebrtc)
# - SPEECH_SYNTHESIS? (experimental; BR: flite-devel >= 2.2)
# - ENABLE_WPE_PLATFORM? (BR: libinput-devel >= 1.19.0 wayland-devel >= 1.20 wayland-protocols >= 1.24 xorg-lib-libxkbcommon-devel >= 0.4.0)
#
# Conditional build:
%bcond_without	libsoup2	# libWPEWebKit-1.0 (libsoup2 based) variant
%bcond_without	libsoup3	# libWPEWebKit-1.1/2.0 (libsoup3 based) variants (HTTP/2 support)
%bcond_without	api_1_1		# libWPEWebKit-1.1 (libsoup3 based) variant
%bcond_without	api_2_0		# libWPEWebKit-2.0 (libsoup3 based) variant
%bcond_with	lowmem		# try to reduce build memory usage by adjusting gcc gc
#
%if %{without libsoup3}
%undefine	with_api_1_1
%undefine	with_api_2_0
%endif
# it's not possible to build this with debuginfo on 32bit archs due to
# memory constraints during linking
%ifarch %{ix86} x32
%define		_enable_debug_packages		0
%endif
Summary:	Port of WebKit embeddable web component to WPE
Summary(pl.UTF-8):	Port osadzalnego komponentu WWW WebKit do WPE
Name:		wpe-webkit
# NOTE: 2.44.x is stable, 2.45.x devel
Version:	2.44.1
Release:	1
License:	BSD-like
Group:		X11/Libraries
Source0:	https://wpewebkit.org/releases/wpewebkit-%{version}.tar.xz
# Source0-md5:	51290d5cf1e032145f2a30971393b006
Patch0:		%{name}-x32.patch
Patch2:		%{name}-driver-version-suffix.patch
Patch3:		parallel-gir.patch
URL:		https://wpewebkit.org/
BuildRequires:	/usr/bin/ld.gold
BuildRequires:	EGL-devel
BuildRequires:	Mesa-libgbm-devel
BuildRequires:	OpenGLESv2-devel
BuildRequires:	at-spi2-atk-devel >= 2.5.3
BuildRequires:	atk-devel >= 1:2.16.0
BuildRequires:	bubblewrap >= 0.3.1
BuildRequires:	cairo-devel >= 1.16.0
BuildRequires:	cmake >= 3.20
BuildRequires:	docbook-dtd412-xml
BuildRequires:	fontconfig-devel >= 2.13.0
BuildRequires:	freetype-devel >= 1:2.9.0
BuildRequires:	gi-docgen
BuildRequires:	glib2-devel >= 1:2.70.0
BuildRequires:	glibc-misc
BuildRequires:	gobject-introspection-devel
BuildRequires:	gperf >= 3.0.1
BuildRequires:	gstreamer-devel >= 1.14.0
BuildRequires:	gstreamer-gl-devel >= 1.14.0
# codecparsers,mpegts
BuildRequires:	gstreamer-plugins-bad-devel >= 1.14.0
# app,audio,fft,pbutils,tag,video
BuildRequires:	gstreamer-plugins-base-devel >= 1.14.0
BuildRequires:	gstreamer-transcoder-devel >= 1.20
BuildRequires:	harfbuzz-devel >= 1.4.2
BuildRequires:	harfbuzz-icu-devel >= 1.4.2
BuildRequires:	lcms2-devel >= 2
BuildRequires:	libavif-devel >= 0.9.0
BuildRequires:	libdrm-devel
BuildRequires:	libepoxy-devel >= 1.5.4
BuildRequires:	libgcrypt-devel >= 1.7.0
BuildRequires:	libicu-devel >= 61.2
BuildRequires:	libjpeg-devel
BuildRequires:	libjxl-devel >= 0.7.0
BuildRequires:	libpng-devel
BuildRequires:	libseccomp-devel
%{?with_libsoup2:BuildRequires:	libsoup-devel >= 2.54}
%{?with_libsoup3:BuildRequires:	libsoup3-devel >= 3.0}
BuildRequires:	libstdc++-devel >= 6:10.2
BuildRequires:	libtasn1-devel
BuildRequires:	libwebp-devel
BuildRequires:	libwpe-devel >= 1.14.0
BuildRequires:	libxml2-devel >= 1:2.8.0
BuildRequires:	libxslt-devel >= 1.1.7
BuildRequires:	openjpeg2-devel >= 2.2.0
BuildRequires:	perl-base >= 1:5.10.0
BuildRequires:	pkgconfig
BuildRequires:	python >= 1:2.7.0
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.699
BuildRequires:	ruby >= 1:2.5
BuildRequires:	ruby-modules >= 1:2.5
BuildRequires:	sqlite3-devel >= 3
BuildRequires:	systemd-devel
BuildRequires:	tar >= 1:1.22
BuildRequires:	udev-devel
BuildRequires:	unifdef
BuildRequires:	wpebackend-fdo-devel >= 1.9.0
BuildRequires:	woff2-devel >= 1.0.2
BuildRequires:	xdg-dbus-proxy
BuildRequires:	xz
BuildRequires:	zlib-devel
Requires:	at-spi2-atk-libs >= 2.5.3
Requires:	atk >= 1:2.16.0
Requires:	cairo >= 1.16.0
Requires:	fontconfig-libs >= 2.13.0
Requires:	freetype >= 1:2.9.0
Requires:	glib2 >= 1:2.70.0
Requires:	gstreamer >= 1.2.3
Requires:	gstreamer-plugins-base >= 1.2.3
Requires:	harfbuzz >= 1.4.2
Requires:	libepoxy >= 1.5.4
Requires:	libgcrypt >= 1.7.0
Requires:	libjxl >= 0.7.0
Requires:	libsoup >= 2.54.0
Requires:	libwpe >= 1.14.0
Requires:	libxml2 >= 1:2.8.0
Requires:	libxslt >= 1.1.7
Requires:	openjpeg2 >= 2.2.0
Requires:	woff2 >= 1.0.2
Requires:	wpebackend-fdo >= 1.9.0
# Source/JavaScriptCore/CMakeLists.txt /WTF_CPU_
ExclusiveArch:	%{ix86} %{x8664} x32 %{arm} aarch64 hppa mips ppc ppc64 ppc64le s390 s390x sh4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_enable_debug_packages	0

%description
wpe-webkit is a port of the WebKit embeddable web component to WPE.

WPE (Webkit Port for Embedded) is the reference WebKit port for
embedded and low-consumption computer devices.

%description -l pl.UTF-8
wpe-webkit to port osadzalnego komponentu WWW WebKit do WPE.

WPE (Webkit Port for Embedded) to wzorcowy port biblioteki WebKit dla
urządzeń komputerowych wbudowanych oraz o niskim poborze energii.

%package devel
Summary:	Development files for WebKit for WPE
Summary(pl.UTF-8):	Pliki programistyczne komponentu WebKit dla WPE
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.70.0
Requires:	libsoup-devel >= 2.54.0
Requires:	libstdc++-devel >= 6:10.2
Requires:	libwpe-devel >= 1.14.0

%description devel
Development files for WebKit for WPE.

%description devel -l pl.UTF-8
Pliki programistyczne komponentu WebKit dla WPE.

%package apidocs
Summary:	API documentation for WebKit WPE port
Summary(pl.UTF-8):	Dokumentacja API portu WebKitu do WPE
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for WebKit WPE port.

%description apidocs -l pl.UTF-8
Dokumentacja API portu WebKitu do WPE.

%package -n wpe-webkit1.1
Summary:	Port of WebKit embeddable web component to WPE with HTTP/2 support
Summary(pl.UTF-8):	Port osadzalnego komponentu WWW WebKit do WPE z obsługą HTTP/2
Group:		X11/Libraries
Requires:	at-spi2-atk-libs >= 2.5.3
Requires:	atk >= 1:2.16.0
Requires:	cairo >= 1.16.0
Requires:	fontconfig-libs >= 2.13.0
Requires:	freetype >= 1:2.9.0
Requires:	glib2 >= 1:2.67.1
Requires:	gstreamer >= 1.2.3
Requires:	gstreamer-plugins-base >= 1.2.3
Requires:	harfbuzz >= 1.4.2
Requires:	libepoxy >= 1.5.4
Requires:	libgcrypt >= 1.7.0
Requires:	libjxl >= 0.7.0
Requires:	libsoup3 >= 3.0.0
Requires:	libwpe >= 1.14.0
Requires:	libxml2 >= 1:2.8.0
Requires:	libxslt >= 1.1.7
Requires:	openjpeg2 >= 2.2.0
Requires:	woff2 >= 1.0.2
Requires:	wpebackend-fdo >= 1.9.0

%description -n wpe-webkit1.1
wpe-webkit1.1 is a port of the WebKit embeddable web component to WPE
with HTTP/2 (libsoup 3) support.

WPE (Webkit Port for Embedded) is the reference WebKit port for
embedded and low-consumption computer devices.

%description -n wpe-webkit1.1 -l pl.UTF-8
wpe-webkit1.1 to port osadzalnego komponentu WWW WebKit do WPE z
obsługą HTTP/2 (libsoup 3).

WPE (Webkit Port for Embedded) to wzorcowy port biblioteki WebKit dla
urządzeń komputerowych wbudowanych oraz o niskim poborze energii.

%package -n wpe-webkit1.1-devel
Summary:	Development files for WebKit for WPE with HTTP/2 support
Summary(pl.UTF-8):	Pliki programistyczne komponentu WebKit dla WPE z obsługą HTTP/2
Group:		X11/Development/Libraries
Requires:	glib2-devel >= 1:2.67.1
Requires:	libsoup3-devel >= 3.0.0
Requires:	libstdc++-devel >= 6:10.2
Requires:	libwpe-devel >= 1.14.0
Requires:	wpe-webkit1.1 = %{version}-%{release}

%description -n wpe-webkit1.1-devel
Development files for WebKit for WPE with HTTP/2 support.

%description -n wpe-webkit1.1-devel -l pl.UTF-8
Pliki programistyczne komponentu WebKit dla WPE z obsługą HTTP/2.

%package -n wpe-webkit1.1-apidocs
Summary:	API documentation for WebKit WPE port with HTTP/2 support
Summary(pl.UTF-8):	Dokumentacja API portu WebKitu do WPE z obsługą HTTP/2
Group:		Documentation
BuildArch:	noarch

%description -n wpe-webkit1.1-apidocs
API documentation for WebKit WPE port with HTTP/2 support.

%description -n wpe-webkit1.1-apidocs -l pl.UTF-8
Dokumentacja API portu WebKitu do WPE z obsługą HTTP/2.

%package -n wpe-webkit2
Summary:	Port of WebKit embeddable web component to WPE with HTTP/2 support
Summary(pl.UTF-8):	Port osadzalnego komponentu WWW WebKit do WPE z obsługą HTTP/2
Group:		X11/Libraries
Requires:	at-spi2-atk-libs >= 2.5.3
Requires:	atk >= 1:2.16.0
Requires:	cairo >= 1.16.0
Requires:	fontconfig-libs >= 2.13.0
Requires:	freetype >= 1:2.9.0
Requires:	glib2 >= 1:2.70.0
Requires:	gstreamer >= 1.2.3
Requires:	gstreamer-plugins-base >= 1.2.3
Requires:	harfbuzz >= 1.4.2
Requires:	libepoxy >= 1.5.4
Requires:	libgcrypt >= 1.7.0
Requires:	libjxl >= 0.7.0
Requires:	libsoup3 >= 3.0.0
Requires:	libwpe >= 1.14.0
Requires:	libxml2 >= 1:2.8.0
Requires:	libxslt >= 1.1.7
Requires:	openjpeg2 >= 2.2.0
Requires:	woff2 >= 1.0.2
Requires:	wpebackend-fdo >= 1.9.0

%description -n wpe-webkit2
wpe-webkit2 is a port of the WebKit embeddable web component to WPE
with HTTP/2 (libsoup 3) support.

WPE (Webkit Port for Embedded) is the reference WebKit port for
embedded and low-consumption computer devices.

%description -n wpe-webkit2 -l pl.UTF-8
wpe-webkit2 to port osadzalnego komponentu WWW WebKit do WPE z
obsługą HTTP/2 (libsoup 3).

WPE (Webkit Port for Embedded) to wzorcowy port biblioteki WebKit dla
urządzeń komputerowych wbudowanych oraz o niskim poborze energii.

%package -n wpe-webkit2-devel
Summary:	Development files for WebKit for WPE with HTTP/2 support
Summary(pl.UTF-8):	Pliki programistyczne komponentu WebKit dla WPE z obsługą HTTP/2
Group:		X11/Development/Libraries
Requires:	glib2-devel >= 1:2.70.0
Requires:	libsoup3-devel >= 3.0.0
Requires:	libstdc++-devel >= 6:10.2
Requires:	libwpe-devel >= 1.14.0
Requires:	wpe-webkit2 = %{version}-%{release}

%description -n wpe-webkit2-devel
Development files for WebKit for WPE with HTTP/2 support.

%description -n wpe-webkit2-devel -l pl.UTF-8
Pliki programistyczne komponentu WebKit dla WPE z obsługą HTTP/2.

%package -n wpe-webkit2-apidocs
Summary:	API documentation for WebKit WPE port with HTTP/2 support
Summary(pl.UTF-8):	Dokumentacja API portu WebKitu do WPE z obsługą HTTP/2
Group:		Documentation
BuildArch:	noarch

%description -n wpe-webkit2-apidocs
API documentation for WebKit WPE port with HTTP/2 support.

%description -n wpe-webkit2-apidocs -l pl.UTF-8
Dokumentacja API portu WebKitu do WPE z obsługą HTTP/2.

%prep
%setup -q -n wpewebkit-%{version}
%patch0 -p1
%patch2 -p1
%patch3 -p1

%build
%if %{with lowmem}
CXXFLAGS="%{rpmcxxflags} -DNDEBUG --param ggc-min-expand=20 --param ggc-min-heapsize=65536"
%endif
for kind in %{?with_libsoup2:soup2} %{?with_api_1_1:soup3-1.1} %{?with_api_2_0:soup3-2.0} ; do
%cmake -B build-${kind} \
	-DENABLE_GEOLOCATION=ON \
	-DENABLE_GTKDOC=ON \
%ifarch x32
	-DENABLE_C_LOOP=ON \
	-DENABLE_JIT=OFF \
	-DENABLE_SAMPLING_PROFILER=OFF \
%endif
	-DENABLE_VIDEO=ON \
	-DENABLE_WEB_AUDIO=ON \
	-DENABLE_WEBGL=ON \
	$([ "$kind" = "soup3-1.1" ] && echo -DENABLE_WPE_1_1_API=ON) \
%ifarch %{ix86} %{x8664} x32
	-DHAVE_SSE2_EXTENSIONS=ON \
%endif
	-DPORT=WPE \
	-DSHOULD_INSTALL_JS_SHELL=ON \
	-DUSE_LIBBACKTRACE=OFF \
	$([ "$kind" = "soup2" ] && echo -DUSE_SOUP2=ON)

%{__make} -C build-${kind}
done

%install
rm -rf $RPM_BUILD_ROOT

for kind in %{?with_libsoup2:soup2} %{?with_api_1_1:soup3-1.1} %{?with_api_2_0:soup3-2.0} ; do
%{__make} -C build-${kind} install \
	DESTDIR=$RPM_BUILD_ROOT
done

install -d $RPM_BUILD_ROOT%{_gidocdir}
%{__mv} $RPM_BUILD_ROOT%{_docdir}/wpe-* $RPM_BUILD_ROOT%{_gidocdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	-n wpe-webkit1.1 -p /sbin/ldconfig
%postun	-n wpe-webkit1.1 -p /sbin/ldconfig

%post	-n wpe-webkit2 -p /sbin/ldconfig
%postun	-n wpe-webkit2 -p /sbin/ldconfig

%if %{with libsoup2}
%files
%defattr(644,root,root,755)
%doc NEWS
%attr(755,root,root) %{_bindir}/WPEWebDriver-1.0
%attr(755,root,root) %{_libdir}/libWPEWebKit-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libWPEWebKit-1.0.so.3
%{_libdir}/girepository-1.0/WPEJavaScriptCore-1.0.typelib
%{_libdir}/girepository-1.0/WPEWebExtension-1.0.typelib
%{_libdir}/girepository-1.0/WPEWebKit-1.0.typelib
%if "%{_libexecdir}" != "%{_libdir}"
%dir %{_libexecdir}/wpe-webkit-1.0
%endif
%attr(755,root,root) %{_libexecdir}/wpe-webkit-1.0/WPENetworkProcess
%attr(755,root,root) %{_libexecdir}/wpe-webkit-1.0/WPEWebProcess
%attr(755,root,root) %{_libexecdir}/wpe-webkit-1.0/jsc
%dir %{_libdir}/wpe-webkit-1.0
%attr(755,root,root) %{_libdir}/wpe-webkit-1.0/libWPEWebInspectorResources.so
%dir %{_libdir}/wpe-webkit-1.0/injected-bundle
%attr(755,root,root) %{_libdir}/wpe-webkit-1.0/injected-bundle/libWPEInjectedBundle.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libWPEWebKit-1.0.so
%{_includedir}/wpe-webkit-1.0
%{_datadir}/gir-1.0/WPEJavaScriptCore-1.0.gir
%{_datadir}/gir-1.0/WPEWebExtension-1.0.gir
%{_datadir}/gir-1.0/WPEWebKit-1.0.gir
%{_pkgconfigdir}/wpe-web-extension-1.0.pc
%{_pkgconfigdir}/wpe-webkit-1.0.pc

%files apidocs
%defattr(644,root,root,755)
%{_gidocdir}/wpe-javascriptcore-1.0
%{_gidocdir}/wpe-web-extension-1.0
%{_gidocdir}/wpe-webkit-1.0
%endif

%if %{with api_1_1}
%files -n wpe-webkit1.1
%defattr(644,root,root,755)
%doc NEWS
%attr(755,root,root) %{_bindir}/WPEWebDriver-1.1
%attr(755,root,root) %{_libdir}/libWPEWebKit-1.1.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libWPEWebKit-1.1.so.0
%{_libdir}/girepository-1.0/WPEJavaScriptCore-1.1.typelib
%{_libdir}/girepository-1.0/WPEWebExtension-1.1.typelib
%{_libdir}/girepository-1.0/WPEWebKit-1.1.typelib
%if "%{_libexecdir}" != "%{_libdir}"
%dir %{_libexecdir}/wpe-webkit-1.1
%endif
%attr(755,root,root) %{_libexecdir}/wpe-webkit-1.1/WPENetworkProcess
%attr(755,root,root) %{_libexecdir}/wpe-webkit-1.1/WPEWebProcess
%attr(755,root,root) %{_libexecdir}/wpe-webkit-1.1/jsc
%dir %{_libdir}/wpe-webkit-1.1
%attr(755,root,root) %{_libdir}/wpe-webkit-1.1/libWPEWebInspectorResources.so
%dir %{_libdir}/wpe-webkit-1.1/injected-bundle
%attr(755,root,root) %{_libdir}/wpe-webkit-1.1/injected-bundle/libWPEInjectedBundle.so

%files -n wpe-webkit1.1-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libWPEWebKit-1.1.so
%{_includedir}/wpe-webkit-1.1
%{_datadir}/gir-1.0/WPEJavaScriptCore-1.1.gir
%{_datadir}/gir-1.0/WPEWebExtension-1.1.gir
%{_datadir}/gir-1.0/WPEWebKit-1.1.gir
%{_pkgconfigdir}/wpe-web-extension-1.1.pc
%{_pkgconfigdir}/wpe-webkit-1.1.pc

%files -n wpe-webkit1.1-apidocs
%defattr(644,root,root,755)
%{_gidocdir}/wpe-javascriptcore-1.1
%{_gidocdir}/wpe-web-extension-1.1
%{_gidocdir}/wpe-webkit-1.1
%endif

%if %{with api_2_0}
%files -n wpe-webkit2
%defattr(644,root,root,755)
%doc NEWS
%attr(755,root,root) %{_bindir}/WPEWebDriver-2.0
%attr(755,root,root) %{_libdir}/libWPEWebKit-2.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libWPEWebKit-2.0.so.1
%{_libdir}/girepository-1.0/WPEJavaScriptCore-2.0.typelib
%{_libdir}/girepository-1.0/WPEWebKit-2.0.typelib
%{_libdir}/girepository-1.0/WPEWebProcessExtension-2.0.typelib
%if "%{_libexecdir}" != "%{_libdir}"
%dir %{_libexecdir}/wpe-webkit-2.0
%endif
%attr(755,root,root) %{_libexecdir}/wpe-webkit-2.0/WPENetworkProcess
%attr(755,root,root) %{_libexecdir}/wpe-webkit-2.0/WPEWebProcess
%attr(755,root,root) %{_libexecdir}/wpe-webkit-2.0/jsc
%dir %{_libdir}/wpe-webkit-2.0
%attr(755,root,root) %{_libdir}/wpe-webkit-2.0/libWPEWebInspectorResources.so
%dir %{_libdir}/wpe-webkit-2.0/injected-bundle
%attr(755,root,root) %{_libdir}/wpe-webkit-2.0/injected-bundle/libWPEInjectedBundle.so

%files -n wpe-webkit2-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libWPEWebKit-2.0.so
%{_includedir}/wpe-webkit-2.0
%{_datadir}/gir-1.0/WPEJavaScriptCore-2.0.gir
%{_datadir}/gir-1.0/WPEWebKit-2.0.gir
%{_datadir}/gir-1.0/WPEWebProcessExtension-2.0.gir
%{_pkgconfigdir}/wpe-web-process-extension-2.0.pc
%{_pkgconfigdir}/wpe-webkit-2.0.pc

%files -n wpe-webkit2-apidocs
%defattr(644,root,root,755)
%{_gidocdir}/wpe-javascriptcore-2.0
%{_gidocdir}/wpe-web-process-extension-2.0
%{_gidocdir}/wpe-webkit-2.0
%endif
