Summary:	Metapackage that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Metapakiet ułatwiający przejście z monolitycznego X11 na modularne xorg
Name:		metapackage-xorg
Version:	7.0.0
Release:	0.2
Epoch:		1
License:	GPL
Group:		X11
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Metapackage that allows easier monolithic X11->modular xorg upgrade.

%description -l pl.UTF-8
Metapakiet ułatwiający przejście z monolitycznego X11 na modularne xorg.

%package -n X11
Summary:	X11 package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet X11 ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		X11
Requires:	xorg-app-appres
Requires:	xorg-app-bitmap
Requires:	xorg-app-editres
Requires:	xorg-app-iceauth
Requires:	xorg-app-lbxproxy
Requires:	xorg-app-luit
Requires:	xorg-app-mkfontdir
Requires:	xorg-app-mkfontscale
Requires:	xorg-app-proxymngr
Requires:	xorg-app-rgb
Requires:	xorg-app-rstart
Requires:	xorg-app-scripts
Requires:	xorg-app-setxkbmap
Requires:	xorg-app-smproxy
Requires:	xorg-app-x11perf
Requires:	xorg-app-xclipboard
Requires:	xorg-app-xcmsdb
Requires:	xorg-app-xconsole
Requires:	xorg-app-xcursorgen
Requires:	xorg-app-xditview
Requires:	xorg-app-xdpyinfo
Requires:	xorg-app-xf86dga
Requires:	xorg-app-xfindproxy
Requires:	xorg-app-xfwp
Requires:	xorg-app-xgamma
Requires:	xorg-app-xhost
Requires:	xorg-app-xinit
Requires:	xorg-app-xkbevd
Requires:	xorg-app-xkbprint
Requires:	xorg-app-xkbutils
Requires:	xorg-app-xlsatoms
Requires:	xorg-app-xlsclients
Requires:	xorg-app-xlsfonts
Requires:	xorg-app-xmh
Requires:	xorg-app-xmodmap
Requires:	xorg-app-xprop
Requires:	xorg-app-xrandr
Requires:	xorg-app-xrdb
Requires:	xorg-app-xrefresh
Requires:	xorg-app-xrx
Requires:	xorg-app-xset
Requires:	xorg-app-xsetmode
Requires:	xorg-app-xsetpointer
Requires:	xorg-app-xsetroot
Requires:	xorg-app-xsm
Requires:	xorg-app-xstdcmap
Requires:	xorg-app-xvidtune
Requires:	xorg-app-xvinfo
Requires:	xorg-app-xwd
Requires:	xorg-app-xwud
Requires:	xorg-data-xbitmaps
Requires:	xorg-docs
Requires:	xorg-lib-libXpm-utils
Requires:	xorg-util-imake
Requires:	xorg-util-lndir
Provides:	XFree86 = %{epoch}:%{version}-%{release}

%description -n X11
X11 package that allows easier monolithic X11->modular xorg upgrade.

%description -n X11 -l pl.UTF-8
Pakiet X11 ułatwiający przejście z monolitycznego X11 na modularne
xorg.

%package -n X11-Xprint
Summary:	Xprint package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet Xprint ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		X11
Requires:	xorg-xserver-Xprt
Provides:	XFree86-Xprint = %{epoch}:%{version}-%{release}

%description -n X11-Xprint
Xprint package that allows easier monolithic X11->modular xorg
upgrade.

%description -n X11-Xprint -l pl.UTF-8
Pakiet Xprint ułatwiający przejście z monolitycznego X11 na modularne
xorg.

%package -n X11-OpenGL-core
Summary:	OpenGL-core package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet OpenGL-core ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		X11
Requires:	xorg-xserver-server
Provides:	XFree86-OpenGL-core = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-OpenGL-core

%description -n X11-OpenGL-core
OpenGL-core package that allows easier monolithic X11->modular xorg
upgrade.

%description -n X11-OpenGL-core -l pl.UTF-8
Pakiet OpenGL-core ułatwiający przejście z monolitycznego X11 na
modularne xorg.

%package -n X11-OpenGL-libGL
Summary:	OpenGL-libGL package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet OpenGL-libGL ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		X11
Requires:	Mesa-libGL
Provides:	XFree86-OpenGL-libGL = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-OpenGL-libGL

%description -n X11-OpenGL-libGL
OpenGL-libGL package that allows easier monolithic X11->modular xorg
upgrade.

%description -n X11-OpenGL-libGL -l pl.UTF-8
Pakiet OpenGL-libGL ułatwiający przejście z monolitycznego X11 na
modularne xorg.

%package -n X11-OpenGL-libs
Summary:	OpenGL-libs package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet OpenGL-libs ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		X11
Requires:	Mesa-libGLU
Requires:	Mesa-utils
Provides:	XFree86-OpenGL-libs = %{epoch}:%{version}-%{release}

%description -n X11-OpenGL-libs
OpenGL-libs package that allows easier monolithic X11->modular xorg
upgrade.

%description -n X11-OpenGL-libs -l pl.UTF-8
Pakiet OpenGL-libs ułatwiający przejście z monolitycznego X11 na
modularne xorg.

%package -n X11-OpenGL-devel-base
Summary:	OpenGL-devel-base package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet OpenGL-devel-base ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		X11
Provides:	XFree86-OpenGL-devel-base = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-OpenGL-devel-base

%description -n X11-OpenGL-devel-base
OpenGL-devel-base package that allows easier monolithic X11->modular
xorg upgrade.

%description -n X11-OpenGL-devel-base -l pl.UTF-8
Pakiet OpenGL-devel-base ułatwiający przejście z monolitycznego X11 na
modularne xorg.

%package -n X11-OpenGL-devel
Summary:	OpenGL-devel package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet OpenGL-devel ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		X11
Requires:	Mesa-libGL-devel
Provides:	XFree86-OpenGL-devel = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-OpenGL-devel

%description -n X11-OpenGL-devel
OpenGL-devel package that allows easier monolithic X11->modular xorg
upgrade.

%description -n X11-OpenGL-devel -l pl.UTF-8
Pakiet OpenGL-devel ułatwiający przejście z monolitycznego X11 na
modularne xorg.

%package -n X11-OpenGL-static
Summary:	OpenGL-static package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet OpenGL-static ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		X11
Requires:	Mesa-libGL-static
Provides:	XFree86-OpenGL-static = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-OpenGL-static

%description -n X11-OpenGL-static
OpenGL-static package that allows easier monolithic X11->modular xorg
upgrade.

%description -n X11-OpenGL-static -l pl.UTF-8
Pakiet OpenGL-static ułatwiający przejście z monolitycznego X11 na
modularne xorg.

%package -n X11-Xnest
Summary:	Xnest package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet Xnest ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		X11
Requires:	xorg-xserver-Xnest
Provides:	XFree86-Xnest = %{epoch}:%{version}-%{release}

%description -n X11-Xnest
Xnest package that allows easier monolithic X11->modular xorg upgrade.

%description -n X11-Xnest -l pl.UTF-8
Pakiet Xnest ułatwiający przejście z monolitycznego X11 na modularne xorg.

%package -n X11-Xprt
Summary:	Xprt package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet Xprt ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		X11
Requires:	xorg-xserver-Xprt
Provides:	XFree86-Xprt = %{epoch}:%{version}-%{release}

%description -n X11-Xprt
Xprt package that allows easier monolithic X11->modular xorg upgrade.

%description -n X11-Xprt -l pl.UTF-8
Pakiet Xprt ułatwiający przejście z monolitycznego X11 na modularne xorg.

%package -n X11-Xserver
Summary:	Xserver package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet Xserver ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		X11
Requires:	xorg-xserver-server
Provides:	XFree86-Xserver = %{epoch}:%{version}-%{release}

%description -n X11-Xserver
Xserver package that allows easier monolithic X11->modular xorg
upgrade.

%description -n X11-Xserver -l pl.UTF-8
Pakiet Xserver ułatwiający przejście z monolitycznego X11 na modularne
xorg.

%package -n X11-Xvfb
Summary:	Xvfb package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet Xvfb ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		X11
Requires:	xorg-xserver-Xvfb
Provides:	XFree86-Xvfb = %{epoch}:%{version}-%{release}

%description -n X11-Xvfb
Xvfb package that allows easier monolithic X11->modular xorg upgrade.

%description -n X11-Xvfb -l pl.UTF-8
Pakiet Xvfb ułatwiający przejście z monolitycznego X11 na modularne
xorg.

%package -n X11-devel
Summary:	devel package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet devel ułatwiający przejście z monolitycznego X11 na modularne xorg
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
Provides:	XFree86-devel = %{epoch}:%{version}-%{release}
# common obsoletes
Obsoletes:	X11-DPS-devel
Obsoletes:	XFree86-DPS-devel

%description -n X11-devel
devel package that allows easier monolithic X11->modular xorg upgrade.

%description -n X11-devel -l pl.UTF-8
Pakiet devel ułatwiający przejście z monolitycznego X11 na modularne
xorg.

%package -n X11-Xserver-devel
Summary:	Xserver-devel package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet Xserver-devel ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		X11
Requires:	xorg-xserver-server-devel
Provides:	XFree86-Xserver-devel = %{epoch}:%{version}-%{release}

%description -n X11-Xserver-devel
Xserver-devel package that allows easier monolithic X11->modular xorg
upgrade.

%description -n X11-Xserver-devel -l pl.UTF-8
Pakiet Xserver-devel ułatwiający przejście z monolitycznego X11 na
modularne xorg.

%package -n X11-driver-apm
Summary:	driver-apm package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet driver-apm ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		X11
Requires:	xorg-driver-video-apm
Provides:	XFree86-driver-apm = %{epoch}:%{version}-%{release}

%description -n X11-driver-apm
driver-apm package that allows easier monolithic X11->modular xorg
upgrade.

%description -n X11-driver-apm -l pl.UTF-8
Pakiet driver-apm ułatwiający przejście z monolitycznego X11 na
modularne xorg.

%package -n X11-driver-ark
Summary:	driver-ark package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet driver-ark ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		X11
Requires:	xorg-driver-video-ark
Provides:	XFree86-driver-ark = %{epoch}:%{version}-%{release}

%description -n X11-driver-ark
driver-ark package that allows easier monolithic X11->modular xorg
upgrade.

%description -n X11-driver-ark -l pl.UTF-8
Pakiet driver-ark ułatwiający przejście z monolitycznego X11 na
modularne xorg.

%package -n X11-driver-ati
Summary:	driver-ati package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet driver-ati ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		X11
Requires:	xorg-driver-video-ati
Provides:	XFree86-driver-ati = %{epoch}:%{version}-%{release}

%description -n X11-driver-ati
driver-ati package that allows easier monolithic X11->modular xorg
upgrade.

%description -n X11-driver-ati -l pl.UTF-8
Pakiet driver-ati ułatwiający przejście z monolitycznego X11 na
modularne xorg.

%package -n X11-driver-radeon
Summary:	driver-radeon package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet driver-radeon ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		X11
Requires:	xorg-driver-video-ati
Provides:	X11-driver-radeon = %{epoch}:%{version}-%{release}
Provides:	XFree86-driver-radeon = %{epoch}:%{version}-%{release}

%description -n X11-driver-radeon
driver-radeon package that allows easier monolithic X11->modular xorg
upgrade.

%description -n X11-driver-radeon -l pl.UTF-8
Pakiet driver-radeon ułatwiający przejście z monolitycznego X11 na
modularne xorg.

%package -n X11-driver-r128
Summary:	driver-r128 package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet driver-r128 ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		X11
Requires:	xorg-driver-video-ati
Provides:	X11-driver-r128 = %{epoch}:%{version}-%{release}
Provides:	XFree86-driver-r128 = %{epoch}:%{version}-%{release}

%description -n X11-driver-r128
driver-r128 package that allows easier monolithic X11->modular xorg
upgrade.

%description -n X11-driver-r128 -l pl.UTF-8
Pakiet driver-r128 ułatwiający przejście z monolitycznego X11 na
modularne xorg.

%package -n X11-driver-r128-dri
Summary:	driver-r128-dri package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet driver-r128-dri ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		X11
Requires:	Mesa-dri-driver-ati-rage128
Provides:	XFree86-driver-r128-dri = %{epoch}:%{version}-%{release}

%description -n X11-driver-r128-dri
driver-r128-dri package that allows easier monolithic X11->modular
xorg upgrade.

%description -n X11-driver-r128-dri -l pl.UTF-8
Pakiet driver-r128-dri ułatwiający przejście z monolitycznego X11 na
modularne xorg.

%package -n X11-driver-radeon-dri
Summary:	driver-radeon-dri package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet driver-radeon-dri ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		X11
Requires:	Mesa-dri-driver-ati-radeon-R100
Requires:	Mesa-dri-driver-ati-radeon-R200
Requires:	Mesa-dri-driver-ati-radeon-R300
Provides:	XFree86-driver-radeon-dri = %{epoch}:%{version}-%{release}

%description -n X11-driver-radeon-dri
driver-radeon-dri package that allows easier monolithic X11->modular xorg upgrade.

%description -n X11-driver-radeon-dri -l pl.UTF-8
Pakiet driver-radeon-dri ułatwiający przejście z monolitycznego X11 na modularne xorg.

%package -n X11-driver-chips
Summary:	driver-chips package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet driver-chips ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		X11
Requires:	xorg-driver-video-chips
Provides:	XFree86-driver-chips = %{epoch}:%{version}-%{release}

%description -n X11-driver-chips
driver-chips package that allows easier monolithic X11->modular xorg
upgrade.

%description -n X11-driver-chips -l pl.UTF-8
Pakiet driver-chips ułatwiający przejście z monolitycznego X11 na
modularne xorg.

%package -n X11-driver-cirrus
Summary:	driver-cirrus package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet driver-cirrus ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		X11
Requires:	xorg-driver-video-cirrus
Provides:	XFree86-driver-cirrus = %{epoch}:%{version}-%{release}

%description -n X11-driver-cirrus
driver-cirrus package that allows easier monolithic X11->modular xorg
upgrade.

%description -n X11-driver-cirrus -l pl.UTF-8
Pakiet driver-cirrus ułatwiający przejście z monolitycznego X11 na
modularne xorg.

%package -n X11-driver-cyrix
Summary:	driver-cyrix package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet driver-cyrix ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		X11
Requires:	xorg-driver-video-cyrix
Provides:	XFree86-driver-cyrix = %{epoch}:%{version}-%{release}

%description -n X11-driver-cyrix
driver-cyrix package that allows easier monolithic X11->modular xorg
upgrade.

%description -n X11-driver-cyrix -l pl.UTF-8
Pakiet driver-cyrix ułatwiający przejście z monolitycznego X11 na
modularne xorg.

%package -n X11-driver-fbdev
Summary:	driver-fbdev package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet driver-fbdev ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		X11
Requires:	xorg-driver-video-fbdev
Provides:	XFree86-driver-fbdev = %{epoch}:%{version}-%{release}

%description -n X11-driver-fbdev
driver-fbdev package that allows easier monolithic X11->modular xorg
upgrade.

%description -n X11-driver-fbdev -l pl.UTF-8
Pakiet driver-fbdev ułatwiający przejście z monolitycznego X11 na
modularne xorg.

%package -n X11-driver-glide
Summary:	driver-glide package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet driver-glide ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		X11
Requires:	xorg-driver-video-voodoo
Provides:	XFree86-driver-glide = %{epoch}:%{version}-%{release}

%description -n X11-driver-glide
driver-glide package that allows easier monolithic X11->modular xorg
upgrade.

%description -n X11-driver-glide -l pl.UTF-8
Pakiet driver-glide ułatwiający przejście z monolitycznego X11 na
modularne xorg.

%package -n X11-driver-glint
Summary:	driver-glint package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet driver-glint ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		X11
Requires:	xorg-driver-video-glint
Provides:	XFree86-driver-glint = %{epoch}:%{version}-%{release}

%description -n X11-driver-glint
driver-glint package that allows easier monolithic X11->modular xorg
upgrade.

%description -n X11-driver-glint -l pl.UTF-8
Pakiet driver-glint ułatwiający przejście z monolitycznego X11 na
modularne xorg.

%package -n X11-driver-glint-dri
Summary:	driver-glint-dri package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet driver-glint-dri ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		X11
Requires:	Mesa-dri-driver-glint
Provides:	XFree86-driver-glint-dri = %{epoch}:%{version}-%{release}

%description -n X11-driver-glint-dri
driver-glint-dri package that allows easier monolithic X11->modular
xorg upgrade.

%description -n X11-driver-glint-dri -l pl.UTF-8
Pakiet driver-glint-dri ułatwiający przejście z monolitycznego X11 na
modularne xorg.

%package -n X11-driver-i128
Summary:	driver-i128 package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet driver-i128 ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		X11
Requires:	xorg-driver-video-i128
Provides:	XFree86-driver-i128 = %{epoch}:%{version}-%{release}

%description -n X11-driver-i128
driver-i128 package that allows easier monolithic X11->modular xorg
upgrade.

%description -n X11-driver-i128 -l pl.UTF-8
Pakiet driver-i128 ułatwiający przejście z monolitycznego X11 na
modularne xorg.

%package -n X11-driver-i2c
Summary:	driver-i2c package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet driver-i2c ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		X11
Requires:	xorg-xserver-server
Provides:	XFree86-driver-i2c = %{epoch}:%{version}-%{release}

%description -n X11-driver-i2c
driver-i2c package that allows easier monolithic X11->modular xorg
upgrade.

%description -n X11-driver-i2c -l pl.UTF-8
Pakiet driver-i2c ułatwiający przejście z monolitycznego X11 na
modularne xorg.

%package -n X11-driver-i740
Summary:	driver-i740 package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet driver-i740 ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		X11
Requires:	xorg-driver-video-i740
Provides:	XFree86-driver-i740 = %{epoch}:%{version}-%{release}

%description -n X11-driver-i740
driver-i740 package that allows easier monolithic X11->modular xorg
upgrade.

%description -n X11-driver-i740 -l pl.UTF-8
Pakiet driver-i740 ułatwiający przejście z monolitycznego X11 na
modularne xorg.

%package -n X11-driver-i810
Summary:	driver-i810 package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet driver-i810 ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		X11
Requires:	xorg-driver-video-i810
Provides:	XFree86-driver-i810 = %{epoch}:%{version}-%{release}

%description -n X11-driver-i810
driver-i810 package that allows easier monolithic X11->modular xorg
upgrade.

%description -n X11-driver-i810 -l pl.UTF-8
Pakiet driver-i810 ułatwiający przejście z monolitycznego X11 na
modularne xorg.

%package -n X11-driver-i810-dri
Summary:	driver-i810-dri package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet driver-i810-dri ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		X11
Requires:	Mesa-dri-driver-intel-i810
Requires:	Mesa-dri-driver-intel-i915
Requires:	Mesa-dri-driver-intel-i965
Provides:	XFree86-driver-i810-dri = %{epoch}:%{version}-%{release}

%description -n X11-driver-i810-dri
driver-i810-dri package that allows easier monolithic X11->modular
xorg upgrade.

%description -n X11-driver-i810-dri -l pl.UTF-8
Pakiet driver-i810-dri ułatwiający przejście z monolitycznego X11 na
modularne xorg.

%package -n X11-driver-mga
Summary:	driver-mga package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet driver-mga ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		X11
Requires:	xorg-driver-video-mga
Provides:	XFree86-driver-mga = %{epoch}:%{version}-%{release}

%description -n X11-driver-mga
driver-mga package that allows easier monolithic X11->modular xorg
upgrade.

%description -n X11-driver-mga -l pl.UTF-8
Pakiet driver-mga ułatwiający przejście z monolitycznego X11 na
modularne xorg.

%package -n X11-driver-mga-dri
Summary:	driver-mga-dri package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet driver-mga-dri ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		X11
Requires:	Mesa-dri-driver-matrox
Provides:	XFree86-driver-mga-dri = %{epoch}:%{version}-%{release}

%description -n X11-driver-mga-dri
driver-mga-dri package that allows easier monolithic X11->modular xorg
upgrade.

%description -n X11-driver-mga-dri -l pl.UTF-8
Pakiet driver-mga-dri ułatwiający przejście z monolitycznego X11 na
modularne xorg.

%package -n X11-driver-neomagic
Summary:	driver-neomagic package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet driver-neomagic ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		X11
Requires:	xorg-driver-video-neomagic
Provides:	XFree86-driver-neomagic = %{epoch}:%{version}-%{release}

%description -n X11-driver-neomagic
driver-neomagic package that allows easier monolithic X11->modular
xorg upgrade.

%description -n X11-driver-neomagic -l pl.UTF-8
Pakiet driver-neomagic ułatwiający przejście z monolitycznego X11 na
modularne xorg.

%package -n X11-driver-newport
Summary:	driver-newport package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet driver-newport ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		X11
Requires:	xorg-driver-video-newport
Provides:	XFree86-driver-newport = %{epoch}:%{version}-%{release}

%description -n X11-driver-newport
driver-newport package that allows easier monolithic X11->modular xorg
upgrade.

%description -n X11-driver-newport -l pl.UTF-8
Pakiet driver-newport ułatwiający przejście z monolitycznego X11 na
modularne xorg.

%package -n X11-driver-nsc
Summary:	driver-nsc package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet driver-nsc ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		X11
Requires:	xorg-driver-video-nsc
Provides:	XFree86-driver-nsc = %{epoch}:%{version}-%{release}

%description -n X11-driver-nsc
driver-nsc package that allows easier monolithic X11->modular xorg
upgrade.

%description -n X11-driver-nsc -l pl.UTF-8
Pakiet driver-nsc ułatwiający przejście z monolitycznego X11 na
modularne xorg.

%package -n X11-driver-nv
Summary:	driver-nv package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet driver-nv ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		X11
Requires:	xorg-driver-video-nv
Provides:	XFree86-driver-nv = %{epoch}:%{version}-%{release}

%description -n X11-driver-nv
driver-nv package that allows easier monolithic X11->modular xorg
upgrade.

%description -n X11-driver-nv -l pl.UTF-8
Pakiet driver-nv ułatwiający przejście z monolitycznego X11 na
modularne xorg.

%package -n X11-driver-rendition
Summary:	driver-rendition package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet driver-rendition ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		X11
Requires:	xorg-driver-video-rendition
Provides:	XFree86-driver-rendition = %{epoch}:%{version}-%{release}

%description -n X11-driver-rendition
driver-rendition package that allows easier monolithic X11->modular
xorg upgrade.

%description -n X11-driver-rendition -l pl.UTF-8
Pakiet driver-rendition ułatwiający przejście z monolitycznego X11 na
modularne xorg.

%package -n X11-driver-s3virge
Summary:	driver-s3virge package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet driver-s3virge ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		X11
Requires:	Mesa-dri-driver-s3virge
Requires:	xorg-driver-video-s3virge
Provides:	XFree86-driver-s3virge = %{epoch}:%{version}-%{release}

%description -n X11-driver-s3virge
driver-s3virge package that allows easier monolithic X11->modular xorg
upgrade.

%description -n X11-driver-s3virge -l pl.UTF-8
Pakiet driver-s3virge ułatwiający przejście z monolitycznego X11 na
modularne xorg.

%package -n X11-driver-s3
Summary:	driver-s3 package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet driver-s3 ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		X11
Requires:	xorg-driver-video-s3
Provides:	XFree86-driver-s3 = %{epoch}:%{version}-%{release}

%description -n X11-driver-s3
driver-s3 package that allows easier monolithic X11->modular xorg
upgrade.

%description -n X11-driver-s3 -l pl.UTF-8
Pakiet driver-s3 ułatwiający przejście z monolitycznego X11 na
modularne xorg.

%package -n X11-driver-savage
Summary:	driver-savage package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet driver-savage ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		X11
Requires:	Mesa-dri-driver-savage
Requires:	xorg-driver-video-savage
Provides:	XFree86-driver-savage = %{epoch}:%{version}-%{release}

%description -n X11-driver-savage
driver-savage package that allows easier monolithic X11->modular xorg
upgrade.

%description -n X11-driver-savage -l pl.UTF-8
Pakiet driver-savage ułatwiający przejście z monolitycznego X11 na
modularne xorg.

%package -n X11-driver-siliconmotion
Summary:	driver-siliconmotion package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet driver-siliconmotion ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		X11
Requires:	xorg-driver-video-siliconmotion
Provides:	XFree86-driver-siliconmotion = %{epoch}:%{version}-%{release}

%description -n X11-driver-siliconmotion
driver-siliconmotion package that allows easier monolithic
X11->modular xorg upgrade.

%description -n X11-driver-siliconmotion -l pl.UTF-8
Pakiet driver-siliconmotion ułatwiający przejście z monolitycznego X11
na modularne xorg.

%package -n X11-driver-sis
Summary:	driver-sis package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet driver-sis ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		X11
Requires:	xorg-driver-video-sis
Provides:	XFree86-driver-sis = %{epoch}:%{version}-%{release}

%description -n X11-driver-sis
driver-sis package that allows easier monolithic X11->modular xorg
upgrade.

%description -n X11-driver-sis -l pl.UTF-8
Pakiet driver-sis ułatwiający przejście z monolitycznego X11 na
modularne xorg.

%package -n X11-driver-sis-dri
Summary:	driver-sis-dri package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet driver-sis-dri ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		X11
Requires:	Mesa-dri-driver-sis
Provides:	XFree86-driver-sis-dri = %{epoch}:%{version}-%{release}

%description -n X11-driver-sis-dri
driver-sis-dri package that allows easier monolithic X11->modular xorg
upgrade.

%description -n X11-driver-sis-dri -l pl.UTF-8
Pakiet driver-sis-dri ułatwiający przejście z monolitycznego X11 na
modularne xorg.

%package -n X11-driver-sisusb
Summary:	driver-sisusb package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet driver-sisusb ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		X11
Requires:	xorg-driver-video-sisusb
Provides:	XFree86-driver-sisusb = %{epoch}:%{version}-%{release}

%description -n X11-driver-sisusb
driver-sisusb package that allows easier monolithic X11->modular xorg
upgrade.

%description -n X11-driver-sisusb -l pl.UTF-8
Pakiet driver-sisusb ułatwiający przejście z monolitycznego X11 na
modularne xorg.

%package -n X11-driver-sunbw2
Summary:	driver-sunbw2 package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet driver-sunbw2 ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		X11
Requires:	xorg-driver-video-sunbw2
Provides:	XFree86-driver-sunbw2 = %{epoch}:%{version}-%{release}

%description -n X11-driver-sunbw2
driver-sunbw2 package that allows easier monolithic X11->modular xorg
upgrade.

%description -n X11-driver-sunbw2 -l pl.UTF-8
Pakiet driver-sunbw2 ułatwiający przejście z monolitycznego X11 na
modularne xorg.

%package -n X11-driver-suncg14
Summary:	driver-suncg14 package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet driver-suncg14 ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		X11
Requires:	xorg-driver-video-suncg14
Provides:	XFree86-driver-suncg14 = %{epoch}:%{version}-%{release}

%description -n X11-driver-suncg14
driver-suncg14 package that allows easier monolithic X11->modular xorg
upgrade.

%description -n X11-driver-suncg14 -l pl.UTF-8
Pakiet driver-suncg14 ułatwiający przejście z monolitycznego X11 na
modularne xorg.

%package -n X11-driver-suncg3
Summary:	driver-suncg3 package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet driver-suncg3 ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		X11
Requires:	xorg-driver-video-suncg3
Provides:	XFree86-driver-suncg3 = %{epoch}:%{version}-%{release}

%description -n X11-driver-suncg3
driver-suncg3 package that allows easier monolithic X11->modular xorg upgrade.

%description -n X11-driver-suncg3 -l pl.UTF-8
Pakiet driver-suncg3 ułatwiający przejście z monolitycznego X11 na modularne xorg.

%package -n X11-driver-suncg6
Summary:	driver-suncg6 package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet driver-suncg6 ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		X11
Requires:	xorg-driver-video-suncg6
Provides:	XFree86-driver-suncg6 = %{epoch}:%{version}-%{release}

%description -n X11-driver-suncg6
driver-suncg6 package that allows easier monolithic X11->modular xorg
upgrade.

%description -n X11-driver-suncg6 -l pl.UTF-8
Pakiet driver-suncg6 ułatwiający przejście z monolitycznego X11 na
modularne xorg.

%package -n X11-driver-sunffb
Summary:	driver-sunffb package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet driver-sunffb ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		X11
Requires:	Mesa-dri-driver-ffb
Requires:	xorg-driver-video-sunffb
Provides:	XFree86-driver-sunffb = %{epoch}:%{version}-%{release}

%description -n X11-driver-sunffb
driver-sunffb package that allows easier monolithic X11->modular xorg
upgrade.

%description -n X11-driver-sunffb -l pl.UTF-8
Pakiet driver-sunffb ułatwiający przejście z monolitycznego X11 na
modularne xorg.

%package -n X11-driver-sunleo
Summary:	driver-sunleo package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet driver-sunleo ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		X11
Requires:	xorg-driver-video-sunleo
Provides:	XFree86-driver-sunleo = %{epoch}:%{version}-%{release}

%description -n X11-driver-sunleo
driver-sunleo package that allows easier monolithic X11->modular xorg
upgrade.

%description -n X11-driver-sunleo -l pl.UTF-8
Pakiet driver-sunleo ułatwiający przejście z monolitycznego X11 na
modularne xorg.

%package -n X11-driver-suntcx
Summary:	driver-suntcx package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet driver-suntcx ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		X11
Requires:	xorg-driver-video-suntcx
Provides:	XFree86-driver-suntcx = %{epoch}:%{version}-%{release}

%description -n X11-driver-suntcx
driver-suntcx package that allows easier monolithic X11->modular xorg
upgrade.

%description -n X11-driver-suntcx -l pl.UTF-8
Pakiet driver-suntcx ułatwiający przejście z monolitycznego X11 na
modularne xorg.

%package -n X11-driver-tdfx
Summary:	driver-tdfx package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet driver-tdfx ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		X11
Requires:	xorg-driver-video-tdfx
Provides:	XFree86-driver-tdfx = %{epoch}:%{version}-%{release}

%description -n X11-driver-tdfx
driver-tdfx package that allows easier monolithic X11->modular xorg
upgrade.

%description -n X11-driver-tdfx -l pl.UTF-8
Pakiet driver-tdfx ułatwiający przejście z monolitycznego X11 na
modularne xorg.

%package -n X11-driver-tdfx-dri
Summary:	driver-tdfx-dri package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet driver-tdfx-dri ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		X11
Requires:	Mesa-dri-driver-tdfx
Provides:	XFree86-driver-tdfx-dri = %{epoch}:%{version}-%{release}

%description -n X11-driver-tdfx-dri
driver-tdfx-dri package that allows easier monolithic X11->modular
xorg upgrade.

%description -n X11-driver-tdfx-dri -l pl.UTF-8
Pakiet driver-tdfx-dri ułatwiający przejście z monolitycznego X11 na
modularne xorg.

%package -n X11-driver-tga
Summary:	driver-tga package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet driver-tga ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		X11
Requires:	xorg-driver-video-tga
Provides:	XFree86-driver-tga = %{epoch}:%{version}-%{release}

%description -n X11-driver-tga
driver-tga package that allows easier monolithic X11->modular xorg
upgrade.

%description -n X11-driver-tga -l pl.UTF-8
Pakiet driver-tga ułatwiający przejście z monolitycznego X11 na
modularne xorg.

%package -n X11-driver-trident
Summary:	driver-trident package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet driver-trident ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		X11
Requires:	Mesa-dri-driver-trident
Requires:	xorg-driver-video-trident
Provides:	XFree86-driver-trident = %{epoch}:%{version}-%{release}

%description -n X11-driver-trident
driver-trident package that allows easier monolithic X11->modular xorg
upgrade.

%description -n X11-driver-trident -l pl.UTF-8
Pakiet driver-trident ułatwiający przejście z monolitycznego X11 na
modularne xorg.

%package -n X11-driver-tseng
Summary:	driver-tseng package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet driver-tseng ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		X11
Requires:	xorg-driver-video-tseng
Provides:	XFree86-driver-tseng = %{epoch}:%{version}-%{release}

%description -n X11-driver-tseng
driver-tseng package that allows easier monolithic X11->modular xorg
upgrade.

%description -n X11-driver-tseng -l pl.UTF-8
Pakiet driver-tseng ułatwiający przejście z monolitycznego X11 na
modularne xorg.

%package -n X11-driver-via
Summary:	driver-via package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet driver-via ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		X11
Requires:	Mesa-dri-driver-via-unichrome
Requires:	xorg-driver-video-via
Provides:	XFree86-driver-via = %{epoch}:%{version}-%{release}

%description -n X11-driver-via
driver-via package that allows easier monolithic X11->modular xorg
upgrade.

%description -n X11-driver-via -l pl.UTF-8
Pakiet driver-via ułatwiający przejście z monolitycznego X11 na
modularne xorg.

%package -n X11-driver-vmware
Summary:	driver-vmware package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet driver-vmware ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		X11
Requires:	xorg-driver-video-vmware
Provides:	XFree86-driver-vmware = %{epoch}:%{version}-%{release}

%description -n X11-driver-vmware
driver-vmware package that allows easier monolithic X11->modular xorg
upgrade.

%description -n X11-driver-vmware -l pl.UTF-8
Pakiet driver-vmware ułatwiający przejście z monolitycznego X11 na
modularne xorg.

%package -n X11-libs
Summary:	libs package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet libs ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		X11
Requires:	xorg-app-bitmap
Requires:	xorg-app-xditview
Requires:	xorg-app-xmh
Requires:	xorg-data-xbitmaps
Provides:	XFree86-libs = %{epoch}:%{version}-%{release}
# Rest of libs deps will be fetched on per so-name rule.
# Common obsoletes:
Provides:	X11-DPS
Obsoletes:	X11-DPS
Obsoletes:	X11-common
Obsoletes:	XFree86-DPS
Obsoletes:	XFree86-common

%description -n X11-libs
libs package that allows easier monolithic X11->modular xorg upgrade.

%description -n X11-libs -l pl.UTF-8
Pakiet libs ułatwiający przejście z monolitycznego X11 na modularne
xorg.

%package -n X11-modules
Summary:	modules package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet modules ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		X11
Requires:	xorg-app-xkbcomp
Requires:	xorg-driver-input-keyboard
Requires:	xorg-driver-input-mouse
Requires:	xorg-driver-video-v4l
Requires:	xorg-driver-video-vesa
Requires:	xorg-driver-video-vga
Provides:	XFree86-modules = %{epoch}:%{version}-%{release}
# not all deps here but we don't want to bring all modules on upgrade

%description -n X11-modules
modules package that allows easier monolithic X11->modular xorg
upgrade.

%description -n X11-modules -l pl.UTF-8
Pakiet modules ułatwiający przejście z monolitycznego X11 na modularne
xorg.

%package -n X11-setup
Summary:	setup package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet setup ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		X11
Requires:	xorg-xserver-server
Provides:	XFree86-setup = %{epoch}:%{version}-%{release}

%description -n X11-setup
setup package that allows easier monolithic X11->modular xorg upgrade.

%description -n X11-setup -l pl.UTF-8
Pakiet setup ułatwiający przejście z monolitycznego X11 na modularne
xorg.

%package -n X11-static
Summary:	static package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet static ułatwiający przejście z monolitycznego X11 na modularne xorg
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
# common obsoletes
Obsoletes:	X11-DPS-static
Obsoletes:	XFree86-DPS-static

%description -n X11-static
static package that allows easier monolithic X11->modular xorg
upgrade.

%description -n X11-static -l pl.UTF-8
Pakiet static ułatwiający przejście z monolitycznego X11 na modularne
xorg.

%package -n X11-tools
Summary:	tools package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet tools ułatwiający przejście z monolitycznego X11 na modularne xorg
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
tools package that allows easier monolithic X11->modular xorg upgrade.

%description -n X11-tools -l pl.UTF-8
Pakiet tools ułatwiający przejście z monolitycznego X11 na modularne
xorg.

%package -n X11-imake
Summary:	imake package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet imake ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		X11
Requires:	xorg-util-gccmakedep
Requires:	xorg-util-imake
Provides:	XFree86-imake = %{epoch}:%{version}-%{release}

%description -n X11-imake
imake package that allows easier monolithic X11->modular xorg upgrade.

%description -n X11-imake -l pl.UTF-8
Pakiet imake ułatwiający przejście z monolitycznego X11 na modularne
xorg.

%package -n X11-sessreg
Summary:	sessreg package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet sessreg ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		X11
Requires:	xorg-app-sessreg
Provides:	XFree86-sessreg = %{epoch}:%{version}-%{release}

%description -n X11-sessreg
sessreg package that allows easier monolithic X11->modular xorg
upgrade.

%description -n X11-sessreg -l pl.UTF-8
Pakiet sessreg ułatwiający przejście z monolitycznego X11 na modularne
xorg.

%package -n X11-twm
Summary:	twm package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet twm ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		X11
Requires:	xorg-app-twm
Provides:	twm = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-twm
Obsoletes:	twm

%description -n X11-twm
twm package that allows easier monolithic X11->modular xorg upgrade.

%description -n X11-twm -l pl.UTF-8
Pakiet twm ułatwiający przejście z monolitycznego X11 na modularne
xorg.

%package -n X11-xauth
Summary:	xauth package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet xauth ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		X11
Requires:	xorg-app-xauth
Provides:	XFree86-xauth = %{epoch}:%{version}-%{release}

%description -n X11-xauth
xauth package that allows easier monolithic X11->modular xorg upgrade.

%description -n X11-xauth -l pl.UTF-8
Pakiet xauth ułatwiający przejście z monolitycznego X11 na modularne
xorg.

%package -n X11-xdm
Summary:	xdm package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet xdm ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		X11
Requires:	xorg-app-xdm
Provides:	XFree86-xdm = %{epoch}:%{version}-%{release}

%description -n X11-xdm
xdm package that allows easier monolithic X11->modular xorg upgrade.

%description -n X11-xdm -l pl.UTF-8
Pakiet xdm ułatwiający przejście z monolitycznego X11 na modularne
xorg.

%package -n X11-xfs
Summary:	xfs package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet xfs ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		X11
Requires:	xorg-app-xfs
Provides:	XFree86-xfs = %{epoch}:%{version}-%{release}

%description -n X11-xfs
xfs package that allows easier monolithic X11->modular xorg upgrade.

%description -n X11-xfs -l pl.UTF-8
Pakiet xfs ułatwiający przejście z monolitycznego X11 na modularne
xorg.

%package -n X11-fonts
Summary:	fonts package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet fonts ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		X11
Requires:	xorg-font-encodings
Requires:	xorg-font-font-adobe-utopia-type1
Requires:	xorg-font-font-arabic-misc
Requires:	xorg-font-font-bh-ttf
Requires:	xorg-font-font-bh-type1
Requires:	xorg-font-font-bitstream-type1
Requires:	xorg-font-font-daewoo-misc
Requires:	xorg-font-font-dec-misc
Requires:	xorg-font-font-ibm-type1
Requires:	xorg-font-font-isas-misc
Requires:	xorg-font-font-micro-misc
Requires:	xorg-font-font-misc-ethiopic
Requires:	xorg-font-font-misc-meltho
Requires:	xorg-font-font-misc-misc
Requires:	xorg-font-font-mutt-misc
Requires:	xorg-font-font-schumacher-misc
Requires:	xorg-font-font-sony-misc
Requires:	xorg-font-font-sun-misc
Requires:	xorg-font-font-xfree86-type1
Provides:	XFree86-fonts = %{epoch}:%{version}-%{release}

%description -n X11-fonts
fonts package that allows easier monolithic X11->modular xorg upgrade.

%description -n X11-fonts -l pl.UTF-8
Pakiet fonts ułatwiający przejście z monolitycznego X11 na modularne
xorg.

%package -n X11-fonts-base
Summary:	fonts-base package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet fonts-base ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		X11
Requires:	xorg-font-font-cursor-misc
Requires:	xorg-font-font-misc-misc-base

%description -n X11-fonts-base
fonts-base package that allows easier monolithic X11->modular xorg upgrade.

%description -n X11-fonts-base -l pl.UTF-8
Pakiet fonts-base ułatwiający przejście z monolitycznego X11 na modularne xorg.

%clean
rm -rf $RPM_BUILD_ROOT

%files -n X11
%defattr(644,root,root,755)
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
%files -n X11-driver-radeon
%defattr(644,root,root,755)
%files -n X11-driver-r128
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
%ifarch mips
%files -n X11-driver-newport
%defattr(644,root,root,755)
%endif
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
%ifarch sparc sparcv9 sparc64
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
%endif
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
%files -n X11-fonts
%defattr(644,root,root,755)
%files -n X11-fonts-base
%defattr(644,root,root,755)
