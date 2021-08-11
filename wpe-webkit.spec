# TODO: review configure options:
# - ENABLE_WEBXR (BR: OpenXR >= 1.0.9, openxr.pc)?
# - ENABLE_THUNDER (https://github.com/rdkcentral/Thunder)?
# - FTL_JIT on !x86_64?
# - WEB_RTC+MEDIA_STREAM (BR: openwebrtc)
#
# it's not possible to build this with debuginfo on 32bit archs due to
# memory constraints during linking
%ifarch %{ix86} x32
%define		_enable_debug_packages		0
%endif
Summary:	Port of WebKit embeddable web component to WPE
Summary(pl.UTF-8):	Port osadzalnego komponentu WWW WebKit do WPE
Name:		wpe-webkit
# NOTE: 2.32.x is stable, 2.33.x devel
Version:	2.32.3
Release:	1
License:	BSD-like
Group:		X11/Libraries
Source0:	https://wpewebkit.org/releases/wpewebkit-%{version}.tar.xz
# Source0-md5:	1e34412c50fe8d1ff084738477ecad7e
Patch0:		%{name}-x32.patch
URL:		https://wpewebkit.org/
BuildRequires:	/usr/bin/ld.gold
BuildRequires:	EGL-devel
BuildRequires:	OpenGLESv2-devel
BuildRequires:	at-spi2-atk-devel >= 2.5.3
BuildRequires:	atk-devel >= 1:2.16.0
BuildRequires:	bubblewrap >= 0.3.1
BuildRequires:	cairo-devel >= 1.16.0
BuildRequires:	cmake >= 3.10
BuildRequires:	docbook-dtd412-xml
BuildRequires:	fontconfig-devel >= 2.13.0
BuildRequires:	freetype-devel >= 1:2.9.0
BuildRequires:	gcc-c++ >= 6:7.3.0
BuildRequires:	glib2-devel >= 1:2.67.1
BuildRequires:	glibc-misc
BuildRequires:	gperf >= 3.0.1
BuildRequires:	gstreamer-devel >= 1.14
BuildRequires:	gstreamer-gl-devel >= 1.10.0
# codecparsers,mpegts with -DUSE_GSTREAMER_MPEGTS=ON
#BuildRequires:	gstreamer-plugins-bad-devel >= 1.10.0
# app,audio,fft,pbutils,tag,video
BuildRequires:	gstreamer-plugins-base-devel >= 1.10.0
BuildRequires:	gtk-doc >= 1.10
BuildRequires:	harfbuzz-devel >= 1.4.2
BuildRequires:	harfbuzz-icu-devel >= 1.4.2
BuildRequires:	libepoxy-devel >= 1.4.0
BuildRequires:	libgcrypt-devel >= 1.7.0
BuildRequires:	libicu-devel >= 60.2
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libseccomp-devel
BuildRequires:	libsoup-devel >= 2.54.0
BuildRequires:	libstdc++-devel >= 6:7.3.0
BuildRequires:	libtasn1-devel
BuildRequires:	libwebp-devel
BuildRequires:	libwpe-devel >= 1.8.0
BuildRequires:	libxml2-devel >= 1:2.8.0
BuildRequires:	libxslt-devel >= 1.1.7
BuildRequires:	openjpeg2-devel >= 2.2.0
BuildRequires:	perl-base >= 1:5.10.0
BuildRequires:	pkgconfig
BuildRequires:	python >= 1:2.7.0
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.699
BuildRequires:	ruby >= 1:1.9
BuildRequires:	ruby-modules >= 1:1.9
BuildRequires:	sqlite3-devel >= 3
BuildRequires:	systemd-devel
BuildRequires:	tar >= 1:1.22
BuildRequires:	wayland-devel
BuildRequires:	wayland-egl-devel
BuildRequires:	wpebackend-fdo-devel >= 1.8.0
BuildRequires:	woff2-devel >= 1.0.2
BuildRequires:	xdg-dbus-proxy
BuildRequires:	xorg-lib-libICE-devel
BuildRequires:	xorg-lib-libXcomposite-devel
BuildRequires:	xorg-lib-libXdamage-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXrender-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	xz
BuildRequires:	zlib-devel
Requires:	at-spi2-atk-libs >= 2.5.3
Requires:	atk >= 1:2.16.0
Requires:	cairo >= 1.16.0
Requires:	fontconfig-libs >= 2.13.0
Requires:	freetype >= 1:2.9.0
Requires:	glib2 >= 1:2.67.1
Requires:	gstreamer >= 1.2.3
Requires:	gstreamer-plugins-base >= 1.2.3
Requires:	harfbuzz >= 1.4.2
Requires:	libepoxy >= 1.4.0
Requires:	libgcrypt >= 1.7.0
Requires:	libsoup >= 2.54.0
Requires:	libxml2 >= 1:2.8.0
Requires:	libxslt >= 1.1.7
Requires:	openjpeg2 >= 2.2.0
Requires:	woff2 >= 1.0.2
Requires:	wpebackend-fdo >= 1.8.0
# Source/JavaScriptCore/CMakeLists.txt /WTF_CPU_
ExclusiveArch:	%{ix86} %{x8664} x32 %{arm} aarch64 hppa mips ppc ppc64 ppc64le s390 s390x sh4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
Requires:	glib2-devel >= 1:2.67.1
Requires:	libsoup-devel >= 2.54.0
Requires:	libstdc++-devel >= 6:7.3.0
Requires:	libwpe-devel >= 1.5.0

%description devel
Development files for WebKit for WPE.

%description devel -l pl.UTF-8
Pliki programistyczne komponentu WebKit dla WPE.

%package apidocs
Summary:	WebKit API documentation
Summary(pl.UTF-8):	Dokumentacja API WebKita
Group:		Documentation
Requires:	gtk-doc-common
BuildArch:	noarch

%description apidocs
WebKit API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API WebKita.

%prep
%setup -q -n wpewebkit-%{version}
%patch0 -p1

%build
install -d build
cd build
%cmake .. \
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
%ifarch %{ix86} %{x8664} x32
	-DHAVE_SSE2_EXTENSIONS=ON \
%endif
	-DPORT=WPE \
	-DSHOULD_INSTALL_JS_SHELL=ON

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%if "%{_gtkdocdir}" != "%{_datadir}/gtk-doc/html"
install -d $RPM_BUILD_ROOT%{_gtkdocdir}
%{__mv} $RPM_BUILD_ROOT%{_datadir}/gtk-doc/html/* $RPM_BUILD_ROOT%{_gtkdocdir}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc NEWS
%attr(755,root,root) %{_bindir}/WPEWebDriver
%attr(755,root,root) %{_libdir}/libWPEWebKit-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libWPEWebKit-1.0.so.3
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
%{_pkgconfigdir}/wpe-web-extension-1.0.pc
%{_pkgconfigdir}/wpe-webkit-1.0.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/wpe-1.0
%{_gtkdocdir}/wpe-webextensions-1.0
