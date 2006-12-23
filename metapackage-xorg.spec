
# TODO:
# X11-driver-glide ??
# X11-driver-glint-dri - ??
# X11-driver-ffb ?

Summary:	Metapackage that allows easier X11->xorg upgrade
Name:		metapackage-xorg
Version:	6.10
Release:	0.1
Epoch:		1
License:	GPL
Group:		X11
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Metapackage that allows easier X11->xorg upgrade.

%package -n X11-Xprint
Summary:	Xprint package that allows easier X11->xorg upgrade
Group:		X11
Requires:	xorg-xserver-Xprt
Provides:	XFree86-Xprint = %{epoch}:%{version}-%{release}

%description -n X11-Xprint

%package -n X11-OpenGL-core
Summary:	OpenGL-core package that allows easier X11->xorg upgrade
Group:		X11
Requires:	xorg-xserver-server
Provides:	XFree86-OpenGL-core = %{epoch}:%{version}-%{release}

%description -n X11-OpenGL-core

%package -n X11-OpenGL-libGL
Summary:	OpenGL-libGL package that allows easier X11->xorg upgrade
Group:		X11
Requires:	Mesa-libGL
Provides:	XFree86-OpenGL-libGL = %{epoch}:%{version}-%{release}

%description -n X11-OpenGL-libGL

%package -n X11-OpenGL-libs
Summary:	OpenGL-libs package that allows easier X11->xorg upgrade
Group:		X11
Requires:	Mesa-libGLU
Requires:	Mesa-utils
Provides:	XFree86-OpenGL-libs = %{epoch}:%{version}-%{release}

%description -n X11-OpenGL-libs

%package -n X11-OpenGL-devel-base
Summary:	OpenGL-devel-base package that allows easier X11->xorg upgrade
Group:		X11
Provides:	XFree86-OpenGL-devel-base = %{epoch}:%{version}-%{release}

%description -n X11-OpenGL-devel-base

%package -n X11-OpenGL-devel
Summary:	OpenGL-devel package that allows easier X11->xorg upgrade
Group:		X11
Requires:	Mesa-libGL-devel
Provides:	XFree86-OpenGL-devel = %{epoch}:%{version}-%{release}

%description -n X11-OpenGL-devel

%package -n X11-OpenGL-static
Summary:	OpenGL-static package that allows easier X11->xorg upgrade
Group:		X11
Requires:	Mesa-libGL-static
Provides:	XFree86-OpenGL-static = %{epoch}:%{version}-%{release}

%description -n X11-OpenGL-static

%package -n X11-Xnest
Summary:	Xnest package that allows easier X11->xorg upgrade
Group:		X11
Requires:	xorg-xserver-Xnest
Provides:	XFree86-Xnest = %{epoch}:%{version}-%{release}

%description -n X11-Xnest

%package -n X11-Xprt
Summary:	Xprt package that allows easier X11->xorg upgrade
Group:		X11
Requires:	xorg-xserver-Xprt
Provides:	XFree86-Xprt = %{epoch}:%{version}-%{release}

%description -n X11-Xprt

%package -n X11-Xserver
Summary:	Xserver package that allows easier X11->xorg upgrade
Group:		X11
Requires:	xorg-xserver-server
Provides:	XFree86-Xserver = %{epoch}:%{version}-%{release}

%description -n X11-Xserver

%package -n X11-Xvfb
Summary:	Xvfb package that allows easier X11->xorg upgrade
Group:		X11
Requires:	xorg-xserver-Xvfb
Provides:	XFree86-Xvfb = %{epoch}:%{version}-%{release}

%description -n X11-Xvfb

%package -n X11-devel
Summary:	devel package that allows easier X11->xorg upgrade
Group:		X11
Requires:	xorg-app-bdftopcf
Requires:	xorg-lib-libFS-devel
Requires:	xorg-lib-libICE-devel
Requires:	xorg-lib-libSM-devel
Requires:	xorg-lib-libX11-devel
Requires:	xorg-lib-libXau-devel
Requires:	xorg-lib-libXaw-devel
Requires:	xorg-lib-libXcomposite-devel
Requires:	xorg-lib-libXcursor-devel
Requires:	xorg-lib-libXdamage-devel
Requires:	xorg-lib-libXdmcp-devel
Requires:	xorg-lib-libXevie-devel
Requires:	xorg-lib-libXfixes-devel
Requires:	xorg-lib-libXfont-devel
Requires:	xorg-lib-libXft-devel
Requires:	xorg-lib-libXmu-devel
Requires:	xorg-lib-libXpm-devel
Requires:	xorg-lib-libXprintAppUtil-devel
Requires:	xorg-lib-libXprintUtil-devel
Requires:	xorg-lib-libXrandr-devel
Requires:	xorg-lib-libXrender-devel
Requires:	xorg-lib-libXres-devel
Requires:	xorg-lib-libXt-devel
Requires:	xorg-lib-libXv-devel
Requires:	xorg-lib-libXvMC-devel
Requires:	xorg-lib-libfontenc-devel
Requires:	xorg-lib-liboldX-devel
Requires:	xorg-lib-libxkbfile-devel
Requires:	xorg-lib-libxkbui-devel
Requires:	xorg-proto-applewmproto-devel
Requires:	xorg-proto-bigreqsproto-devel
Requires:	xorg-proto-compositeproto-devel
Requires:	xorg-proto-damageproto-devel
Requires:	xorg-proto-dmxproto-devel
Requires:	xorg-proto-evieext-devel
Requires:	xorg-proto-fixesproto-devel
Requires:	xorg-proto-fontcacheproto-devel
Requires:	xorg-proto-fontsproto-devel
Requires:	xorg-proto-inputproto-devel
Requires:	xorg-proto-kbproto-devel
Requires:	xorg-proto-printproto-devel
Requires:	xorg-proto-randrproto-devel
Requires:	xorg-proto-recordproto-devel
Requires:	xorg-proto-renderproto-devel
Requires:	xorg-proto-resourceproto-devel
Requires:	xorg-proto-scrnsaverproto-devel
Requires:	xorg-proto-trapproto-devel
Requires:	xorg-proto-videoproto-devel
Requires:	xorg-proto-windowswmproto-devel
Requires:	xorg-proto-xcmiscproto-devel
Requires:	xorg-proto-xextproto-devel
Requires:	xorg-proto-xf86bigfontproto-devel
Requires:	xorg-proto-xf86dgaproto-devel
Requires:	xorg-proto-xf86miscproto-devel
Requires:	xorg-proto-xf86rushproto-devel
Requires:	xorg-proto-xf86vidmodeproto-devel
Requires:	xorg-proto-xineramaproto-devel
Requires:	xorg-proto-xproto-devel
Requires:	xorg-proto-xproxymanagementprotocol-devel
Requires:	xorg-xserver-server
Provides:	XFree86-devel = %{epoch}:%{version}-%{release}

%description -n X11-devel

%package -n X11-Xserver-devel
Summary:	Xserver-devel package that allows easier X11->xorg upgrade
Group:		X11
Requires:	xorg-xserver-server-devel
Provides:	XFree86-Xserver-devel = %{epoch}:%{version}-%{release}

%description -n X11-Xserver-devel

%package -n X11-driver-apm
Summary:	driver-apm package that allows easier X11->xorg upgrade
Group:		X11
Requires:	xorg-driver-video-apm
Provides:	XFree86-driver-apm = %{epoch}:%{version}-%{release}

%description -n X11-driver-apm

%package -n X11-driver-ark
Summary:	driver-ark package that allows easier X11->xorg upgrade
Group:		X11
Requires:	xorg-driver-video-ark
Provides:	XFree86-driver-ark = %{epoch}:%{version}-%{release}

%description -n X11-driver-ark

%package -n X11-driver-ati
Summary:	driver-ati package that allows easier X11->xorg upgrade
Group:		X11
Requires:	xorg-driver-video-ati
Provides:	X11-driver-r128 = %{epoch}:%{version}-%{release}
Provides:	X11-driver-radeon = %{epoch}:%{version}-%{release}
Provides:	XFree86-driver-ati = %{epoch}:%{version}-%{release}
Obsoletes:	X11-driver-r128
Obsoletes:	X11-driver-radeon

%description -n X11-driver-ati

%package -n X11-driver-r128-dri
Summary:	driver-r128-dri package that allows easier X11->xorg upgrade
Group:		X11
Requires:	Mesa-dri-driver-ati-rage128
Provides:	XFree86-driver-r128-dri = %{epoch}:%{version}-%{release}

%description -n X11-driver-r128-dri

%package -n X11-driver-radeon-dri
Summary:	driver-radeon-dri package that allows easier X11->xorg upgrade
Group:		X11
Requires:	Mesa-dri-driver-ati-radeon-R100
Requires:	Mesa-dri-driver-ati-radeon-R200
Requires:	Mesa-dri-driver-ati-radeon-R300
Provides:	XFree86-driver-radeon-dri = %{epoch}:%{version}-%{release}

%description -n X11-driver-radeon-dri

%package -n X11-driver-chips
Summary:	driver-chips package that allows easier X11->xorg upgrade
Group:		X11
Requires:	xorg-driver-video-chips
Provides:	XFree86-driver-chips = %{epoch}:%{version}-%{release}

%description -n X11-driver-chips

%package -n X11-driver-cirrus
Summary:	driver-cirrus package that allows easier X11->xorg upgrade
Group:		X11
Requires:	xorg-driver-video-cirrus
Provides:	XFree86-driver-cirrus = %{epoch}:%{version}-%{release}

%description -n X11-driver-cirrus

%package -n X11-driver-cyrix
Summary:	driver-cyrix package that allows easier X11->xorg upgrade
Group:		X11
Requires:	xorg-driver-video-cyrix
Provides:	XFree86-driver-cyrix = %{epoch}:%{version}-%{release}

%description -n X11-driver-cyrix

%package -n X11-driver-fbdev
Summary:	driver-fbdev package that allows easier X11->xorg upgrade
Group:		X11
Requires:	xorg-driver-video-fbdev
Provides:	XFree86-driver-fbdev = %{epoch}:%{version}-%{release}

%description -n X11-driver-fbdev

%package -n X11-driver-ffb
Summary:	driver-ffb package that allows easier X11->xorg upgrade
Group:		X11
Provides:	XFree86-driver-ffb = %{epoch}:%{version}-%{release}

%description -n X11-driver-ffb

%package -n X11-driver-glide
Summary:	driver-glide package that allows easier X11->xorg upgrade
Group:		X11
Provides:	XFree86-driver-glide = %{epoch}:%{version}-%{release}

%description -n X11-driver-glide

%package -n X11-driver-glint
Summary:	driver-glint package that allows easier X11->xorg upgrade
Group:		X11
Requires:	xorg-driver-video-glint
Provides:	XFree86-driver-glint = %{epoch}:%{version}-%{release}

%description -n X11-driver-glint

%package -n X11-driver-glint-dri
Summary:	driver-glint-dri package that allows easier X11->xorg upgrade
Group:		X11
Provides:	XFree86-driver-glint-dri = %{epoch}:%{version}-%{release}

%description -n X11-driver-glint-dri

%package -n X11-driver-i128
Summary:	driver-i128 package that allows easier X11->xorg upgrade
Group:		X11
Requires:	xorg-driver-video-i128
Provides:	XFree86-driver-i128 = %{epoch}:%{version}-%{release}

%description -n X11-driver-i128

%package -n X11-driver-i2c
Summary:	driver-i2c package that allows easier X11->xorg upgrade
Group:		X11
Requires:	xorg-xserver-server
Provides:	XFree86-driver-i2c = %{epoch}:%{version}-%{release}

%description -n X11-driver-i2c

%package -n X11-driver-i740
Summary:	driver-i740 package that allows easier X11->xorg upgrade
Group:		X11
Requires:	xorg-driver-video-i740
Provides:	XFree86-driver-i740 = %{epoch}:%{version}-%{release}

%description -n X11-driver-i740

%package -n X11-driver-i810
Summary:	driver-i810 package that allows easier X11->xorg upgrade
Group:		X11
Requires:	xorg-driver-video-i810
Provides:	XFree86-driver-i810 = %{epoch}:%{version}-%{release}

%description -n X11-driver-i810

%package -n X11-driver-i810-dri
Summary:	driver-i810-dri package that allows easier X11->xorg upgrade
Group:		X11
Requires:	Mesa-dri-driver-intel-i810
Requires:	Mesa-dri-driver-intel-i915
Requires:	Mesa-dri-driver-intel-i965
Provides:	XFree86-driver-i810-dri = %{epoch}:%{version}-%{release}

%description -n X11-driver-i810-dri

%package -n X11-driver-mga
Summary:	driver-mga package that allows easier X11->xorg upgrade
Group:		X11
Requires:	xorg-driver-video-mga
Provides:	XFree86-driver-mga = %{epoch}:%{version}-%{release}

%description -n X11-driver-mga

%package -n X11-driver-mga-dri
Summary:	driver-mga-dri package that allows easier X11->xorg upgrade
Group:		X11
Requires:	Mesa-dri-driver-matrox
Provides:	XFree86-driver-mga-dri = %{epoch}:%{version}-%{release}

%description -n X11-driver-mga-dri

%package -n X11-driver-neomagic
Summary:	driver-neomagic package that allows easier X11->xorg upgrade
Group:		X11
Requires:	xorg-driver-video-neomagic
Provides:	XFree86-driver-neomagic = %{epoch}:%{version}-%{release}

%description -n X11-driver-neomagic

%package -n X11-driver-newport
Summary:	driver-newport package that allows easier X11->xorg upgrade
Group:		X11
Requires:	xorg-driver-video-newport
Provides:	XFree86-driver-newport = %{epoch}:%{version}-%{release}

%description -n X11-driver-newport

%package -n X11-driver-nsc
Summary:	driver-nsc package that allows easier X11->xorg upgrade
Group:		X11
Requires:	xorg-driver-video-nsc
Provides:	XFree86-driver-nsc = %{epoch}:%{version}-%{release}

%description -n X11-driver-nsc

%package -n X11-driver-nv
Summary:	driver-nv package that allows easier X11->xorg upgrade
Group:		X11
Requires:	xorg-driver-video-nv
Provides:	XFree86-driver-nv = %{epoch}:%{version}-%{release}

%description -n X11-driver-nv

%package -n X11-driver-rendition
Summary:	driver-rendition package that allows easier X11->xorg upgrade
Group:		X11
Requires:	xorg-driver-video-rendition
Provides:	XFree86-driver-rendition = %{epoch}:%{version}-%{release}

%description -n X11-driver-rendition

%package -n X11-driver-s3virge
Summary:	driver-s3virge package that allows easier X11->xorg upgrade
Group:		X11
Requires:	Mesa-dri-driver-s3virge
Requires:	xorg-driver-video-s3virge
Provides:	XFree86-driver-s3virge = %{epoch}:%{version}-%{release}

%description -n X11-driver-s3virge

%package -n X11-driver-s3
Summary:	driver-s3 package that allows easier X11->xorg upgrade
Group:		X11
Requires:	xorg-driver-video-s3
Provides:	XFree86-driver-s3 = %{epoch}:%{version}-%{release}

%description -n X11-driver-s3

%package -n X11-driver-savage
Summary:	driver-savage package that allows easier X11->xorg upgrade
Group:		X11
Requires:	Mesa-dri-driver-savage
Requires:	xorg-driver-video-savage
Provides:	XFree86-driver-savage = %{epoch}:%{version}-%{release}

%description -n X11-driver-savage

%package -n X11-driver-siliconmotion
Summary:	driver-siliconmotion package that allows easier X11->xorg upgrade
Group:		X11
Requires:	xorg-driver-video-siliconmotion
Provides:	XFree86-driver-siliconmotion = %{epoch}:%{version}-%{release}

%description -n X11-driver-siliconmotion

%package -n X11-driver-sis
Summary:	driver-sis package that allows easier X11->xorg upgrade
Group:		X11
Requires:	xorg-driver-video-sis
Provides:	XFree86-driver-sis = %{epoch}:%{version}-%{release}

%description -n X11-driver-sis

%package -n X11-driver-sis-dri
Summary:	driver-sis-dri package that allows easier X11->xorg upgrade
Group:		X11
Requires:	Mesa-dri-driver-sis
Provides:	XFree86-driver-sis-dri = %{epoch}:%{version}-%{release}

%description -n X11-driver-sis-dri

%package -n X11-driver-sisusb
Summary:	driver-sisusb package that allows easier X11->xorg upgrade
Group:		X11
Requires:	xorg-driver-video-sisusb
Provides:	XFree86-driver-sisusb = %{epoch}:%{version}-%{release}

%description -n X11-driver-sisusb

%package -n X11-driver-sunbw2
Summary:	driver-sunbw2 package that allows easier X11->xorg upgrade
Group:		X11
Requires:	xorg-driver-video-sunbw2
Provides:	XFree86-driver-sunbw2 = %{epoch}:%{version}-%{release}

%description -n X11-driver-sunbw2

%package -n X11-driver-suncg14
Summary:	driver-suncg14 package that allows easier X11->xorg upgrade
Group:		X11
Requires:	xorg-driver-video-suncg14
Provides:	XFree86-driver-suncg14 = %{epoch}:%{version}-%{release}

%description -n X11-driver-suncg14

%package -n X11-driver-suncg3
Summary:	driver-suncg3 package that allows easier X11->xorg upgrade
Group:		X11
Requires:	xorg-driver-video-suncg3
Provides:	XFree86-driver-suncg3 = %{epoch}:%{version}-%{release}

%description -n X11-driver-suncg3

%package -n X11-driver-suncg6
Summary:	driver-suncg6 package that allows easier X11->xorg upgrade
Group:		X11
Requires:	xorg-driver-video-suncg6
Provides:	XFree86-driver-suncg6 = %{epoch}:%{version}-%{release}

%description -n X11-driver-suncg6

%package -n X11-driver-sunffb
Summary:	driver-sunffb package that allows easier X11->xorg upgrade
Group:		X11
Requires:	xorg-driver-video-sunffb
Provides:	XFree86-driver-sunffb = %{epoch}:%{version}-%{release}

%description -n X11-driver-sunffb

%package -n X11-driver-sunleo
Summary:	driver-sunleo package that allows easier X11->xorg upgrade
Group:		X11
Requires:	xorg-driver-video-sunleo
Provides:	XFree86-driver-sunleo = %{epoch}:%{version}-%{release}

%description -n X11-driver-sunleo

%package -n X11-driver-suntcx
Summary:	driver-suntcx package that allows easier X11->xorg upgrade
Group:		X11
Requires:	xorg-driver-video-suntcx
Provides:	XFree86-driver-suntcx = %{epoch}:%{version}-%{release}

%description -n X11-driver-suntcx

%package -n X11-driver-tdfx
Summary:	driver-tdfx package that allows easier X11->xorg upgrade
Group:		X11
Requires:	xorg-driver-video-tdfx
Provides:	XFree86-driver-tdfx = %{epoch}:%{version}-%{release}

%description -n X11-driver-tdfx

%package -n X11-driver-tdfx-dri
Summary:	driver-tdfx-dri package that allows easier X11->xorg upgrade
Group:		X11
Requires:	Mesa-dri-driver-tdfx
Provides:	XFree86-driver-tdfx-dri = %{epoch}:%{version}-%{release}

%description -n X11-driver-tdfx-dri

%package -n X11-driver-tga
Summary:	driver-tga package that allows easier X11->xorg upgrade
Group:		X11
Requires:	xorg-driver-video-tga
Provides:	XFree86-driver-tga = %{epoch}:%{version}-%{release}

%description -n X11-driver-tga

%package -n X11-driver-trident
Summary:	driver-trident package that allows easier X11->xorg upgrade
Group:		X11
Requires:	Mesa-dri-driver-trident
Requires:	xorg-driver-video-trident
Provides:	XFree86-driver-trident = %{epoch}:%{version}-%{release}

%description -n X11-driver-trident

%package -n X11-driver-tseng
Summary:	driver-tseng package that allows easier X11->xorg upgrade
Group:		X11
Requires:	xorg-driver-video-tseng
Provides:	XFree86-driver-tseng = %{epoch}:%{version}-%{release}

%description -n X11-driver-tseng

%package -n X11-driver-via
Summary:	driver-via package that allows easier X11->xorg upgrade
Group:		X11
Requires:	Mesa-dri-driver-via-unichrome
Requires:	xorg-driver-video-via
Provides:	XFree86-driver-via = %{epoch}:%{version}-%{release}

%description -n X11-driver-via

%package -n X11-driver-vmware
Summary:	driver-vmware package that allows easier X11->xorg upgrade
Group:		X11
Requires:	xorg-driver-video-vmware
Provides:	XFree86-driver-vmware = %{epoch}:%{version}-%{release}

%description -n X11-driver-vmware

%package -n X11-libs
Summary:	libs package that allows easier X11->xorg upgrade
Group:		X11
Requires:	xorg-app-bitmap
Requires:	xorg-app-xditview
Requires:	xorg-app-xmh
Requires:	xorg-data-xbitmaps
Provides:	XFree86-libs = %{epoch}:%{version}-%{release}
# Rest of libs deps will be fetched on per so-name rule.
# Common obsoletes:
Obsoletes:	DPS
Obsoletes:	DPS-devel
Obsoletes:	DPS-static
Obsoletes:	X11-common
Obsoletes:	XFree86-common

%description -n X11-libs

%package -n X11-modules
Summary:	modules package that allows easier X11->xorg upgrade
Group:		X11
Requires:	xorg-app-xkbcomp
Requires:	xorg-driver-input-keyboard
Requires:	xorg-driver-video-v4l
Requires:	xorg-driver-video-vesa
Requires:	xorg-driver-video-vga
Requires:	xorg-xserver-Xprt
Provides:	XFree86-modules = %{epoch}:%{version}-%{release}
# not all deps here but we don't want to bring all modules on upgrade

%description -n X11-modules

%package -n X11-setup
Summary:	setup package that allows easier X11->xorg upgrade
Group:		X11
Requires:	xorg-xserver-server
Provides:	XFree86-setup = %{epoch}:%{version}-%{release}

%description -n X11-setup

%package -n X11-static
Summary:	static package that allows easier X11->xorg upgrade
Group:		X11
Requires:	xorg-lib-libFS-static
Requires:	xorg-lib-libICE-static
Requires:	xorg-lib-libSM-static
Requires:	xorg-lib-libX11-static
Requires:	xorg-lib-libXScrnSaver-static
Requires:	xorg-lib-libXTrap-static
Requires:	xorg-lib-libXau-static
Requires:	xorg-lib-libXcomposite-static
Requires:	xorg-lib-libXcursor-static
Requires:	xorg-lib-libXdamage-static
Requires:	xorg-lib-libXdmcp-static
Requires:	xorg-lib-libXevie-static
Requires:	xorg-lib-libXext-static
Requires:	xorg-lib-libXfixes-static
Requires:	xorg-lib-libXfont-static
Requires:	xorg-lib-libXfontcache-static
Requires:	xorg-lib-libXft-static
Requires:	xorg-lib-libXi-static
Requires:	xorg-lib-libXinerama-static
Requires:	xorg-lib-libXmu-static
Requires:	xorg-lib-libXp-static
Requires:	xorg-lib-libXpm-static
Requires:	xorg-lib-libXrandr-static
Requires:	xorg-lib-libXrender-static
Requires:	xorg-lib-libXres-static
Requires:	xorg-lib-libXt-static
Requires:	xorg-lib-libXtst-static
Requires:	xorg-lib-libXv-static
Requires:	xorg-lib-libXvMC-static
Requires:	xorg-lib-libXxf86dga-static
Requires:	xorg-lib-libXxf86misc-static
Requires:	xorg-lib-libXxf86vm-static
Requires:	xorg-lib-libfontenc-static
Requires:	xorg-lib-libxkbfile-static
Requires:	xorg-lib-libxkbui-static
Provides:	XFree86-static = %{epoch}:%{version}-%{release}

%description -n X11-static

%package -n X11-tools
Summary:	tools package that allows easier X11->xorg upgrade
Group:		X11
Requires:	xorg-app-beforelight
Requires:	xorg-app-ico
Requires:	xorg-app-listres
Requires:	xorg-app-oclock
Requires:	xorg-app-showfont
Requires:	xorg-app-viewres
Requires:	xorg-app-x11perf
Requires:	xorg-app-xbiff
Requires:	xorg-app-xcalc
Requires:	xorg-app-xclipboard
Requires:	xorg-app-xclock
Requires:	xorg-app-xdbedizzy
Requires:	xorg-app-xditview
Requires:	xorg-app-xdriinfo
Requires:	xorg-app-xedit
Requires:	xorg-app-xev
Requires:	xorg-app-xeyes
Requires:	xorg-app-xfd
Requires:	xorg-app-xfontsel
Requires:	xorg-app-xgc
Requires:	xorg-app-xkill
Requires:	xorg-app-xload
Requires:	xorg-app-xlogo
Requires:	xorg-app-xmag
Requires:	xorg-app-xman
Requires:	xorg-app-xmessage
Requires:	xorg-app-xmh
Requires:	xorg-app-xmore
Requires:	xorg-app-xphelloworld
Requires:	xorg-app-xplsprinters
Requires:	xorg-app-xpr
Requires:	xorg-app-xprehashprinterlist
Requires:	xorg-app-xprop
Requires:	xorg-app-xtrap
Requires:	xorg-app-xwininfo
Provides:	XFree86-tools = %{epoch}:%{version}-%{release}

%description -n X11-tools

%package -n X11-imake
Summary:	imake package that allows easier X11->xorg upgrade
Group:		X11
Requires:	xorg-util-gccmakedep
Requires:	xorg-util-imake
Provides:	XFree86-imake = %{epoch}:%{version}-%{release}

%description -n X11-imake

%package -n X11-sessreg
Summary:	sessreg package that allows easier X11->xorg upgrade
Group:		X11
Requires:	xorg-app-sessreg
Provides:	XFree86-sessreg = %{epoch}:%{version}-%{release}

%description -n X11-sessreg

%package -n X11-twm
Summary:	twm package that allows easier X11->xorg upgrade
Group:		X11
Requires:	xorg-app-twm
Provides:	XFree86-twm = %{epoch}:%{version}-%{release}

%description -n X11-twm

%package -n X11-xauth
Summary:	xauth package that allows easier X11->xorg upgrade
Group:		X11
Requires:	xorg-app-xauth
Provides:	XFree86-xauth = %{epoch}:%{version}-%{release}

%description -n X11-xauth

%package -n X11-xdm
Summary:	xdm package that allows easier X11->xorg upgrade
Group:		X11
Requires:	xorg-app-xdm
Provides:	XFree86-xdm = %{epoch}:%{version}-%{release}

%description -n X11-xdm

%package -n X11-xfs
Summary:	xfs package that allows easier X11->xorg upgrade
Group:		X11
Requires:	xorg-app-xfs
Provides:	XFree86-xfs = %{epoch}:%{version}-%{release}

%description -n X11-xfs

%clean
rm -rf $RPM_BUILD_ROOT

%files -n X11-Xprint
%defattr(644,root,root,755)
%files -n X11-OpenGL-core
%defattr(644,root,root,755)
%files -n X11-OpenGL-libGL
%defattr(644,root,root,755)
%files -n X11-OpenGL-libs
%defattr(644,root,root,755)
%files -n X11-OpenGL-devel-base
%defattr(644,root,root,755)
%files -n X11-OpenGL-devel
%defattr(644,root,root,755)
%files -n X11-OpenGL-static
%defattr(644,root,root,755)
%files -n X11-Xnest
%defattr(644,root,root,755)
%files -n X11-Xprt
%defattr(644,root,root,755)
%files -n X11-Xserver
%defattr(644,root,root,755)
%files -n X11-Xvfb
%defattr(644,root,root,755)
%files -n X11-devel
%defattr(644,root,root,755)
%files -n X11-Xserver-devel
%defattr(644,root,root,755)
%files -n X11-driver-apm
%defattr(644,root,root,755)
%files -n X11-driver-ark
%defattr(644,root,root,755)
%files -n X11-driver-ati
%defattr(644,root,root,755)
%files -n X11-driver-r128-dri
%defattr(644,root,root,755)
%files -n X11-driver-radeon-dri
%defattr(644,root,root,755)
%files -n X11-driver-chips
%defattr(644,root,root,755)
%files -n X11-driver-cirrus
%defattr(644,root,root,755)
%files -n X11-driver-cyrix
%defattr(644,root,root,755)
%files -n X11-driver-fbdev
%defattr(644,root,root,755)
%files -n X11-driver-ffb
%defattr(644,root,root,755)
%files -n X11-driver-glide
%defattr(644,root,root,755)
%files -n X11-driver-glint
%defattr(644,root,root,755)
%files -n X11-driver-glint-dri
%defattr(644,root,root,755)
%files -n X11-driver-i128
%defattr(644,root,root,755)
%files -n X11-driver-i2c
%defattr(644,root,root,755)
%files -n X11-driver-i740
%defattr(644,root,root,755)
%files -n X11-driver-i810
%defattr(644,root,root,755)
%files -n X11-driver-i810-dri
%defattr(644,root,root,755)
%files -n X11-driver-mga
%defattr(644,root,root,755)
%files -n X11-driver-mga-dri
%defattr(644,root,root,755)
%files -n X11-driver-neomagic
%defattr(644,root,root,755)
%files -n X11-driver-newport
%defattr(644,root,root,755)
%files -n X11-driver-nsc
%defattr(644,root,root,755)
%files -n X11-driver-nv
%defattr(644,root,root,755)
%files -n X11-driver-rendition
%defattr(644,root,root,755)
%files -n X11-driver-s3virge
%defattr(644,root,root,755)
%files -n X11-driver-s3
%defattr(644,root,root,755)
%files -n X11-driver-savage
%defattr(644,root,root,755)
%files -n X11-driver-siliconmotion
%defattr(644,root,root,755)
%files -n X11-driver-sis
%defattr(644,root,root,755)
%files -n X11-driver-sis-dri
%defattr(644,root,root,755)
%files -n X11-driver-sisusb
%defattr(644,root,root,755)
%files -n X11-driver-sunbw2
%defattr(644,root,root,755)
%files -n X11-driver-suncg14
%defattr(644,root,root,755)
%files -n X11-driver-suncg3
%defattr(644,root,root,755)
%files -n X11-driver-suncg6
%defattr(644,root,root,755)
%files -n X11-driver-sunffb
%defattr(644,root,root,755)
%files -n X11-driver-sunleo
%defattr(644,root,root,755)
%files -n X11-driver-suntcx
%defattr(644,root,root,755)
%files -n X11-driver-tdfx
%defattr(644,root,root,755)
%files -n X11-driver-tdfx-dri
%defattr(644,root,root,755)
%files -n X11-driver-tga
%defattr(644,root,root,755)
%files -n X11-driver-trident
%defattr(644,root,root,755)
%files -n X11-driver-tseng
%defattr(644,root,root,755)
%files -n X11-driver-via
%defattr(644,root,root,755)
%files -n X11-driver-vmware
%defattr(644,root,root,755)
%files -n X11-libs
%defattr(644,root,root,755)
%files -n X11-modules
%defattr(644,root,root,755)
%files -n X11-setup
%defattr(644,root,root,755)
%files -n X11-static
%defattr(644,root,root,755)
%files -n X11-tools
%defattr(644,root,root,755)
%files -n X11-imake
%defattr(644,root,root,755)
%files -n X11-sessreg
%defattr(644,root,root,755)
%files -n X11-twm
%defattr(644,root,root,755)
%files -n X11-xauth
%defattr(644,root,root,755)
%files -n X11-xdm
%defattr(644,root,root,755)
%files -n X11-xfs
%defattr(644,root,root,755)
