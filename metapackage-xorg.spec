Summary:	Metapackage that installs a set of Xorg packages needed to run on any configuration
Summary(pl.UTF-8):	Metapakiet instalujący zestaw pakietów potrzebnych by uruchomić Xorg na każdym sprzęcie
Name:		metapackage-xorg
Version:	7.7
Release:	11
Epoch:		1
License:	GPL
Group:		X11
Requires:	xcursor-theme-handhelds >= 1.0.3
Requires:	xcursor-theme-redglass >= 1.0.3
Requires:	xcursor-theme-whiteglass >= 1.0.3
Requires:	xkeyboard-config >= 2.6
Requires:	xorg-app-iceauth >= 1.0.5
Requires:	xorg-app-rgb
Requires:	xorg-app-sessreg >= 1.0.7
Requires:	xorg-app-setxkbmap >= 1.3.0
Requires:	xorg-app-twm
Requires:	xorg-app-xauth >= 1.0.7
Requires:	xorg-app-xbacklight >= 1.1.2
Requires:	xorg-app-xdpyinfo >= 1.3.0
Requires:	xorg-app-xinput >= 1.6.0
Requires:	xorg-app-xkbcomp >= 1.2.4
Requires:	xorg-app-xmessage
Requires:	xorg-app-xmodmap >= 1.0.7
Requires:	xorg-app-xprop >= 1.2.1
Requires:	xorg-app-xset >= 1.2.2
Requires:	xorg-app-xsetroot >= 1.1.0
Requires:	xorg-data-xbitmaps >= 1.1.1
Requires:	xorg-driver-input-evdev >= 2.7.0
Requires:	xorg-driver-input-keyboard >= 1.6.1
Requires:	xorg-driver-input-mouse >= 1.7.2
Requires:	xorg-driver-input-synaptics >= 1.6.1
Requires:	xorg-driver-video-vmmouse >= 12.8.0
Requires:	xorg-driver-video-apm
Requires:	xorg-driver-video-ark >= 0.7.4
Requires:	xorg-driver-video-ast >= 0.93.10
Requires:	xorg-driver-video-ati >= 6.14.4
Requires:	xorg-driver-video-chips
Requires:	xorg-driver-video-cirrus >= 1.4.0
Requires:	xorg-driver-video-dummy >= 0.3.5
Requires:	xorg-driver-video-fbdev >= 0.4.2
Requires:	xorg-driver-video-i128 >= 1.3.5
Requires:	xorg-driver-video-i740
Requires:	xorg-driver-video-intel >= 2.19.0
Requires:	xorg-driver-video-mach64 >= 6.9.1
Requires:	xorg-driver-video-mga >= 1.5.0
Requires:	xorg-driver-video-neomagic >= 1.2.6
%ifarch mips
Requires:	xorg-driver-video-newport >= 0.2.4
%endif
Requires:	xorg-driver-video-nv >= 2.1.18
Requires:	xorg-driver-video-openchrome >= 0.2.906
Requires:	xorg-driver-video-r128 >= 6.8.2
Requires:	xorg-driver-video-rendition
Requires:	xorg-driver-video-s3virge
Requires:	xorg-driver-video-savage >= 2.3.4
Requires:	xorg-driver-video-siliconmotion >= 1.7.6
Requires:	xorg-driver-video-sis >= 0.10.4
Requires:	xorg-driver-video-sisusb
Requires:	xorg-driver-video-tdfx >= 1.4.4
Requires:	xorg-driver-video-tseng
Requires:	xorg-driver-video-trident >= 1.3.5
Requires:	xorg-driver-video-v4l >= 0.2.0
Requires:	xorg-driver-video-vesa >= 2.3.1
Requires:	xorg-driver-video-vmware >= 12.0.2
Requires:	xorg-driver-video-voodoo >= 1.2.4
Requires:	xorg-font-encodings >= 1.0.4
Requires:	xorg-font-font-adobe-utopia-type1 >= 1.0.4
Requires:	xorg-font-font-alias >= 1.0.3
Requires:	xorg-font-font-arabic-misc >= 1.0.3
Requires:	xorg-font-font-bh-ttf >= 1.0.3
Requires:	xorg-font-font-bh-type1 >= 1.0.3
Requires:	xorg-font-font-bitstream-type1 >= 1.0.3
Requires:	xorg-font-font-cursor-misc >= 1.0.3
Requires:	xorg-font-font-daewoo-misc >= 1.0.3
Requires:	xorg-font-font-dec-misc >= 1.0.3
Requires:	xorg-font-font-ibm-type1 >= 1.0.3
Requires:	xorg-font-font-isas-misc >= 1.0.3
Requires:	xorg-font-font-micro-misc >= 1.0.3
Requires:	xorg-font-font-misc-ethiopic >= 1.0.3
Requires:	xorg-font-font-misc-meltho >= 1.0.3
Requires:	xorg-font-font-misc-misc >= 1.1.2
Requires:	xorg-font-font-misc-misc-base >= 1.1.2
Requires:	xorg-font-font-mutt-misc >= 1.0.3
Requires:	xorg-font-font-schumacher-misc >= 1.1.2
Requires:	xorg-font-font-sony-misc >= 1.0.3
Requires:	xorg-font-font-sun-misc >= 1.0.3
Requires:	xorg-font-font-xfree86-type1 >= 1.0.4
Requires:	xorg-lib-libICE >= 1.0.8
Requires:	xorg-lib-libSM >= 1.2.1
Requires:	xorg-lib-libX11 >= 1.5.0
Requires:	xorg-lib-libXScrnSaver >= 1.2.2
Requires:	xorg-lib-libXau >= 1.0.7
Requires:	xorg-lib-libXaw >= 1.0.11
Requires:	xorg-lib-libXcomposite >= 0.4.3
Requires:	xorg-lib-libXcursor >= 1.1.13
Requires:	xorg-lib-libXdamage >= 1.1.3
Requires:	xorg-lib-libXdmcp >= 1.1.1
Requires:	xorg-lib-libXext >= 1.3.1
Requires:	xorg-lib-libXfixes >= 5.0
Requires:	xorg-lib-libXfont >= 1.4.5
Requires:	xorg-lib-libXft >= 2.3.1
Requires:	xorg-lib-libXi >= 1.6.1
Requires:	xorg-lib-libXinerama >= 1.1.2
Requires:	xorg-lib-libXmu >= 1.1.1
Requires:	xorg-lib-libXp
Requires:	xorg-lib-libXpm >= 3.5.10
Requires:	xorg-lib-libXrandr >= 1.3.2
Requires:	xorg-lib-libXrender >= 0.9.7
Requires:	xorg-lib-libXres >= 1.0.6
Requires:	xorg-lib-libXt >= 1.1.3
Requires:	xorg-lib-libXtst >= 1.2.1
Requires:	xorg-lib-libXv >= 1.0.7
Requires:	xorg-lib-libXvMC >= 1.0.7
Requires:	xorg-lib-libXxf86dga >= 1.1.3
Requires:	xorg-lib-libXxf86vm >= 1.1.2
Requires:	xorg-lib-libdmx >= 1.1.2
Requires:	xorg-lib-libfontenc >= 1.1.1
Requires:	xorg-lib-libpciaccess >= 0.13.1
Requires:	xorg-lib-libxkbfile >= 1.0.8
Requires:	xorg-xserver-libdri >= 1.12.2
Requires:	xorg-xserver-libglx >= 1.12.2
Requires:	xorg-xserver-server >= 1.12.2
Obsoletes:	X11-driver-apm < 1:7.0.0-13
Obsoletes:	X11-driver-cyrix < 1:7.0.0-5
Obsoletes:	X11-driver-firegl < 1:7.0.0-14
Obsoletes:	X11-driver-glide < 1:7.7-11
Obsoletes:	X11-driver-glint < 1:7.7-9
Obsoletes:	X11-driver-glint-dri < 1:7.7-9
Obsoletes:	X11-driver-i810-dri < 1:7.0.0-23
Obsoletes:	X11-driver-mga-dri < 1:7.0.0-23
Obsoletes:	X11-driver-nsc < 1:7.0.0-8
Obsoletes:	X11-driver-nvidia-legacy < 1:7.0.0-13
Obsoletes:	X11-driver-nvidia-legacy-devel < 1:7.0.0-13
Obsoletes:	X11-driver-nvidia-legacy-progs < 1:7.0.0-13
Obsoletes:	X11-driver-nsc < 1:7.0.0-8
Obsoletes:	X11-driver-r128-dri < 1:7.0.0-23
Obsoletes:	X11-driver-s3 < 1:7.7-9
Obsoletes:	X11-driver-sis-dri < 1:7.0.0-23
Obsoletes:	X11-driver-tdfx-dri < 1:7.0.0-23
Obsoletes:	X11-driver-tga < 1:7.7-9
Obsoletes:	X11-driver-via < 1:7.0.0-5
Obsoletes:	xorg-app-lbxproxy < 1.0.4
Obsoletes:	xorg-app-luit < 1.1.2
Obsoletes:	xorg-app-proxymngr < 1.0.5
Obsoletes:	xorg-app-xfindproxy < 1.0.5
Obsoletes:	xorg-app-xfwp < 1.0.4
Obsoletes:	xorg-app-xrx < 1.0.5
Obsoletes:	xorg-app-xsetpointer < 1.0.2
Obsoletes:	xorg-app-xtrap < 1.0.4
Obsoletes:	xorg-driver-video-glide < 1.2.3
Obsoletes:	xorg-font-font-bitstream-speedo < 1.0.3
Obsoletes:	xorg-lib-liblbxutil < 1.1.1
Obsoletes:	xorg-lib-liboldX < 1.0.2
Obsoletes:	xorg-lib-libXevie < 1.0.4
Obsoletes:	xorg-lib-libXfontcache < 1.0.6
Obsoletes:	xorg-lib-libxkbui < 1.0.3
Obsoletes:	xorg-lib-libXxf86misc < 1.0.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# don't create -debuginfo package
%define		_enable_debug_packages	0

%description
Metapackage that installs a set of Xorg packages needed to run on any
configuration.

%description -l pl.UTF-8
Metapakiet instalujący zestaw pakietóww potrzebnych by uruchomić Xorg
na każdym sprzęcie.

%package -n X11
Summary:	X11 package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet X11 ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		X11
Requires:	xorg-app-bitmap
Requires:	xorg-app-editres
Requires:	xorg-app-iceauth >= 1.0.5
Requires:	xorg-app-mkfontdir >= 1.0.7
Requires:	xorg-app-mkfontscale >= 1.1.0
Requires:	xorg-app-rgb
Requires:	xorg-app-rstart
Requires:	xorg-app-scripts
Requires:	xorg-app-setxkbmap >= 1.3.0
Requires:	xorg-app-smproxy >= 1.0.5
Requires:	xorg-app-x11perf >= 1.5.4
Requires:	xorg-app-xclipboard
Requires:	xorg-app-xcmsdb >= 1.0.4
Requires:	xorg-app-xconsole
Requires:	xorg-app-xcursorgen >= 1.0.5
Requires:	xorg-app-xditview
Requires:	xorg-app-xdpyinfo >= 1.3.0
Requires:	xorg-app-xf86dga
Requires:	xorg-app-xgamma >= 1.0.5
Requires:	xorg-app-xhost >= 1.0.5
Requires:	xorg-app-xinit
Requires:	xorg-app-xkbevd >= 1.1.3
Requires:	xorg-app-xkbprint
Requires:	xorg-app-xkbutils >= 1.0.3
Requires:	xorg-app-xlsatoms >= 1.1.1
Requires:	xorg-app-xlsclients >= 1.1.2
Requires:	xorg-app-xlsfonts
Requires:	xorg-app-xmh
Requires:	xorg-app-xmodmap >= 1.0.7
Requires:	xorg-app-xprop >= 1.2.1
Requires:	xorg-app-xrandr >= 1.3.5
Requires:	xorg-app-xrdb >= 1.0.9
Requires:	xorg-app-xrefresh >= 1.0.4
Requires:	xorg-app-xset >= 1.2.2
Requires:	xorg-app-xsetroot >= 1.1.0
Requires:	xorg-app-xsm
Requires:	xorg-app-xstdcmap
Requires:	xorg-app-xvidtune
Requires:	xorg-app-xvinfo >= 1.1.1
Requires:	xorg-app-xwd >= 1.0.5
Requires:	xorg-app-xwud >= 1.0.4
Requires:	xorg-data-xbitmaps >= 1.1.1
Requires:	xorg-docs >= 1.7
Requires:	xorg-lib-libXpm-utils >= 3.5.10
Requires:	xorg-util-imake
Requires:	xorg-util-lndir
Provides:	XFree86 = %{epoch}:%{version}-%{release}

%description -n X11
X11 package that allows easier monolithic X11->modular xorg upgrade.

%description -n X11 -l pl.UTF-8
Pakiet X11 ułatwiający przejście z monolitycznego X11 na modularne
xorg.

%package -n X11-OpenGL-core
Summary:	OpenGL-core package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet OpenGL-core ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		X11
Requires:	xorg-xserver-server >= 1.12.2
Provides:	XFree86-OpenGL-core = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-OpenGL-core < 1:5

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
# either Mesa-libGL or some vendor-specific binary driver
Requires:	OpenGL
Provides:	XFree86-OpenGL-libGL = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-OpenGL-libGL < 1:5

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
Requires:	mesa-utils
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
Obsoletes:	XFree86-OpenGL-devel-base < 1:5

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
Obsoletes:	XFree86-OpenGL-devel < 1:5

%description -n X11-OpenGL-devel
OpenGL-devel package that allows easier monolithic X11->modular xorg
upgrade.

%description -n X11-OpenGL-devel -l pl.UTF-8
Pakiet OpenGL-devel ułatwiający przejście z monolitycznego X11 na
modularne xorg.

%package -n X11-Xnest
Summary:	Xnest package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet Xnest ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		X11
Requires:	xorg-xserver-Xnest >= 1.12.2
Provides:	XFree86-Xnest = %{epoch}:%{version}-%{release}

%description -n X11-Xnest
Xnest package that allows easier monolithic X11->modular xorg upgrade.

%description -n X11-Xnest -l pl.UTF-8
Pakiet Xnest ułatwiający przejście z monolitycznego X11 na modularne
xorg.

%package -n X11-Xserver
Summary:	Xserver package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet Xserver ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		X11
Requires:	dbus
Requires:	xorg-driver-input-evdev >= 2.7.0
Requires:	xorg-xserver-server >= 1.12.2
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
Requires:	xorg-xserver-Xvfb >= 1.12.2
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
Requires:	xorg-app-bdftopcf >= 1.0.3
Requires:	xorg-lib-libFS-devel >= 1.0.4
Requires:	xorg-lib-libICE-devel >= 1.0.8
Requires:	xorg-lib-libSM-devel >= 1.2.1
Requires:	xorg-lib-libX11-devel >= 1.5.0
Requires:	xorg-lib-libXau-devel >= 1.0.7
Requires:	xorg-lib-libXaw-devel >= 1.0.11
Requires:	xorg-lib-libXcomposite-devel >= 0.4.3
Requires:	xorg-lib-libXcursor-devel >= 1.1.13
Requires:	xorg-lib-libXdamage-devel >= 1.1.3
Requires:	xorg-lib-libXdmcp-devel >= 1.1.1
Requires:	xorg-lib-libXext-devel >= 1.3.1
Requires:	xorg-lib-libXfixes-devel >= 5.0
Requires:	xorg-lib-libXfont-devel >= 1.4.5
Requires:	xorg-lib-libXft-devel >= 2.3.1
Requires:	xorg-lib-libXi-devel >= 1.6.1
Requires:	xorg-lib-libXinerama-devel >= 1.1.2
Requires:	xorg-lib-libXmu-devel >= 1.1.1
Requires:	xorg-lib-libXpm-devel >= 3.5.10
Requires:	xorg-lib-libXprintAppUtil-devel
Requires:	xorg-lib-libXprintUtil-devel
Requires:	xorg-lib-libXrandr-devel >= 1.3.2
Requires:	xorg-lib-libXrender-devel >= 0.9.7
Requires:	xorg-lib-libXres-devel >= 1.0.6
Requires:	xorg-lib-libXt-devel >= 1.1.3
Requires:	xorg-lib-libXv-devel >= 1.0.7
Requires:	xorg-lib-libXvMC-devel >= 1.0.7
Requires:	xorg-lib-libXxf86dga-devel >= 1.1.3
Requires:	xorg-lib-libXxf86vm-devel >= 1.1.2
Requires:	xorg-lib-libdmx-devel >= 1.1.2
Requires:	xorg-lib-libfontenc-devel >= 1.1.1
Requires:	xorg-lib-libpciaccess-devel >= 0.13.1
Requires:	xorg-lib-libxkbfile-devel >= 1.0.8
Requires:	xorg-lib-xtrans-devel >= 1.2.7
Requires:	xorg-proto-bigreqsproto-devel >= 1.1.2
Requires:	xorg-proto-compositeproto-devel >= 0.4.2
Requires:	xorg-proto-damageproto-devel >= 1.2.1
Requires:	xorg-proto-dmxproto-devel >= 2.3.1
Requires:	xorg-proto-dri2proto-devel >= 2.6
Requires:	xorg-proto-fixesproto-devel >= 5.0
Requires:	xorg-proto-fontcacheproto-devel
Requires:	xorg-proto-fontsproto-devel >= 2.1.2
Requires:	xorg-proto-glproto-devel >= 1.4.15
Requires:	xorg-proto-inputproto-devel >= 2.2
Requires:	xorg-proto-kbproto-devel >= 1.0.6
Requires:	xorg-proto-printproto-devel
Requires:	xorg-proto-randrproto-devel >= 1.3.2
Requires:	xorg-proto-recordproto-devel >= 1.14.2
Requires:	xorg-proto-renderproto-devel >= 0.11.1
Requires:	xorg-proto-resourceproto-devel >= 1.2.0
Requires:	xorg-proto-scrnsaverproto-devel >= 1.2.2
Requires:	xorg-proto-videoproto-devel >= 2.3.1
Requires:	xorg-proto-xcmiscproto-devel >= 1.2.2
Requires:	xorg-proto-xextproto-devel >= 7.2.1
Requires:	xorg-proto-xf86bigfontproto-devel >= 1.2.0
Requires:	xorg-proto-xf86dgaproto-devel >= 2.1
Requires:	xorg-proto-xf86driproto-devel >= 2.1.1
Requires:	xorg-proto-xf86miscproto-devel
Requires:	xorg-proto-xf86rushproto-devel
Requires:	xorg-proto-xf86vidmodeproto-devel >= 2.3.1
Requires:	xorg-proto-xineramaproto-devel >= 1.2.1
Requires:	xorg-proto-xproto-devel >= 7.0.23
Requires:	xorg-proto-xproxymngproto-devel
Requires:	xorg-sgml-doctools >= 1.11
Requires:	xorg-util-util-macros >= 1.17
Provides:	XFree86-devel = %{epoch}:%{version}-%{release}
# common obsoletes
Obsoletes:	X11-DPS-devel < 1:7
Obsoletes:	XFree86-DPS-devel < 1:5

%description -n X11-devel
devel package that allows easier monolithic X11->modular xorg upgrade.

%description -n X11-devel -l pl.UTF-8
Pakiet devel ułatwiający przejście z monolitycznego X11 na modularne
xorg.

%package -n X11-Xserver-devel
Summary:	Xserver-devel package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet Xserver-devel ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		X11
Requires:	xorg-xserver-server-devel >= 1.12.2
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
Requires:	xorg-driver-video-ark >= 0.7.4
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
Requires:	xorg-driver-video-ati >= 6.14.4
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
Requires:	xorg-driver-video-ati >= 6.14.4
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
Requires:	xorg-driver-video-r128 >= 6.8.2
Provides:	X11-driver-r128 = %{epoch}:%{version}-%{release}
Provides:	XFree86-driver-r128 = %{epoch}:%{version}-%{release}

%description -n X11-driver-r128
driver-r128 package that allows easier monolithic X11->modular xorg
upgrade.

%description -n X11-driver-r128 -l pl.UTF-8
Pakiet driver-r128 ułatwiający przejście z monolitycznego X11 na
modularne xorg.

%package -n X11-driver-radeon-dri
Summary:	driver-radeon-dri package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet driver-radeon-dri ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		X11
Requires:	Mesa-dri-driver-ati-radeon-R300
Provides:	XFree86-driver-radeon-dri = %{epoch}:%{version}-%{release}

%description -n X11-driver-radeon-dri
driver-radeon-dri package that allows easier monolithic X11->modular
xorg upgrade.

%description -n X11-driver-radeon-dri -l pl.UTF-8
Pakiet driver-radeon-dri ułatwiający przejście z monolitycznego X11 na
modularne xorg.

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
Requires:	xorg-driver-video-cirrus >= 1.4.0
Provides:	XFree86-driver-cirrus = %{epoch}:%{version}-%{release}

%description -n X11-driver-cirrus
driver-cirrus package that allows easier monolithic X11->modular xorg
upgrade.

%description -n X11-driver-cirrus -l pl.UTF-8
Pakiet driver-cirrus ułatwiający przejście z monolitycznego X11 na
modularne xorg.

%package -n X11-driver-fbdev
Summary:	driver-fbdev package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet driver-fbdev ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		X11
Requires:	xorg-driver-video-fbdev >= 0.4.2
Provides:	XFree86-driver-fbdev = %{epoch}:%{version}-%{release}

%description -n X11-driver-fbdev
driver-fbdev package that allows easier monolithic X11->modular xorg
upgrade.

%description -n X11-driver-fbdev -l pl.UTF-8
Pakiet driver-fbdev ułatwiający przejście z monolitycznego X11 na
modularne xorg.

%package -n X11-driver-i128
Summary:	driver-i128 package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet driver-i128 ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		X11
Requires:	xorg-driver-video-i128 >= 1.3.5
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
Requires:	xorg-xserver-server >= 1.12.2
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

%package -n X11-driver-mga
Summary:	driver-mga package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet driver-mga ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		X11
Requires:	xorg-driver-video-mga >= 1.5.0
Provides:	XFree86-driver-mga = %{epoch}:%{version}-%{release}

%description -n X11-driver-mga
driver-mga package that allows easier monolithic X11->modular xorg
upgrade.

%description -n X11-driver-mga -l pl.UTF-8
Pakiet driver-mga ułatwiający przejście z monolitycznego X11 na
modularne xorg.

%package -n X11-driver-neomagic
Summary:	driver-neomagic package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet driver-neomagic ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		X11
Requires:	xorg-driver-video-neomagic >= 1.2.6
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
Requires:	xorg-driver-video-newport >= 0.2.4
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
Requires:	xorg-driver-video-nv >= 2.1.18
Provides:	XFree86-driver-nv = %{epoch}:%{version}-%{release}

%description -n X11-driver-nv
driver-nv package that allows easier monolithic X11->modular xorg
upgrade.

%description -n X11-driver-nv -l pl.UTF-8
Pakiet driver-nv ułatwiający przejście z monolitycznego X11 na
modularne xorg.

%package -n X11-driver-nvidia
Summary:	driver-nvidia package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet driver-nvidia ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		X11
Requires:	xorg-driver-video-nouveau

%description -n X11-driver-nvidia
driver-nvidia package that allows easier monolithic X11->modular xorg
upgrade.

%description -n X11-driver-nvidia -l pl.UTF-8
Pakiet driver-nvidia ułatwiający przejście z monolitycznego X11 na
modularne xorg.

%package -n X11-driver-nvidia-devel
Summary:	driver-nvidia-devel package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet driver-nvidia-devel ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		X11

%description -n X11-driver-nvidia-devel
driver-nvidia-devel package that allows easier monolithic X11->modular
xorg upgrade.

%description -n X11-driver-nvidia-devel -l pl.UTF-8
Pakiet driver-nvidia-devel ułatwiający przejście z monolitycznego X11
na modularne xorg.

%package -n X11-driver-nvidia-progs
Summary:	driver-nvidia-progs package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet driver-nvidia-progs ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		X11

%description -n X11-driver-nvidia-progs
driver-nvidia-progs package that allows easier monolithic X11->modular
xorg upgrade.

%description -n X11-driver-nvidia-progs -l pl.UTF-8
Pakiet driver-nvidia-progs ułatwiający przejście z monolitycznego X11
na modularne xorg.

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
Requires:	xorg-driver-video-s3virge
Provides:	XFree86-driver-s3virge = %{epoch}:%{version}-%{release}

%description -n X11-driver-s3virge
driver-s3virge package that allows easier monolithic X11->modular xorg
upgrade.

%description -n X11-driver-s3virge -l pl.UTF-8
Pakiet driver-s3virge ułatwiający przejście z monolitycznego X11 na
modularne xorg.

%package -n X11-driver-savage
Summary:	driver-savage package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet driver-savage ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		X11
Requires:	xorg-driver-video-savage >= 2.3.4
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
Requires:	xorg-driver-video-siliconmotion >= 1.7.6
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
Requires:	xorg-driver-video-sis >= 0.10.4
Provides:	XFree86-driver-sis = %{epoch}:%{version}-%{release}

%description -n X11-driver-sis
driver-sis package that allows easier monolithic X11->modular xorg
upgrade.

%description -n X11-driver-sis -l pl.UTF-8
Pakiet driver-sis ułatwiający przejście z monolitycznego X11 na
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
driver-suncg3 package that allows easier monolithic X11->modular xorg
upgrade.

%description -n X11-driver-suncg3 -l pl.UTF-8
Pakiet driver-suncg3 ułatwiający przejście z monolitycznego X11 na
modularne xorg.

%package -n X11-driver-suncg6
Summary:	driver-suncg6 package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet driver-suncg6 ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		X11
Requires:	xorg-driver-video-suncg6 >= 1.1.1
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
Requires:	xorg-driver-video-sunffb >= 1.2.1
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
Requires:	xorg-driver-video-tdfx >= 1.4.4
Provides:	XFree86-driver-tdfx = %{epoch}:%{version}-%{release}

%description -n X11-driver-tdfx
driver-tdfx package that allows easier monolithic X11->modular xorg
upgrade.

%description -n X11-driver-tdfx -l pl.UTF-8
Pakiet driver-tdfx ułatwiający przejście z monolitycznego X11 na
modularne xorg.

%package -n X11-driver-trident
Summary:	driver-trident package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet driver-trident ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		X11
Requires:	xorg-driver-video-trident >= 1.3.5
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

%package -n X11-driver-vmware
Summary:	driver-vmware package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet driver-vmware ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		X11
Requires:	xorg-driver-video-vmware >= 12.0.2
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
# help poldek out a bit specifying these packages explicitly
Requires:	xorg-lib-libXi >= 1.6.1
Requires:	xorg-lib-libXtst >= 1.2.1
# Rest of libs deps will be fetched on per so-name rule.
Provides:	X11-DPS
Provides:	XFree86-libs = %{epoch}:%{version}-%{release}
# Common obsoletes:
Obsoletes:	X11-DPS < 1:7
Obsoletes:	X11-Xprint < 1:7.0.0-3
Obsoletes:	X11-Xprt < 1:7.0.0-3
Obsoletes:	X11-common < 1:7
Obsoletes:	XFree86-DPS < 1:5
Obsoletes:	XFree86-common < 1:5

%description -n X11-libs
libs package that allows easier monolithic X11->modular xorg upgrade.

%description -n X11-libs -l pl.UTF-8
Pakiet libs ułatwiający przejście z monolitycznego X11 na modularne
xorg.

%package -n X11-modules
Summary:	modules package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet modules ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		X11
Requires:	xorg-app-xkbcomp >= 1.2.4
Requires:	xorg-driver-input-joystick >= 1.6.1
Requires:	xorg-driver-input-keyboard >= 1.6.1
Requires:	xorg-driver-input-mouse >= 1.7.2
Requires:	xorg-driver-input-void >= 1.4.0
Requires:	xorg-driver-video-v4l >= 0.2.0
Requires:	xorg-driver-video-vesa >= 2.3.1
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
Requires:	xorg-xserver-server >= 1.12.2
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
Requires:	xorg-lib-libFS-static >= 1.0.4
Requires:	xorg-lib-libICE-static >= 1.0.8
Requires:	xorg-lib-libSM-static >= 1.2.1
Requires:	xorg-lib-libX11-static >= 1.5.0
Requires:	xorg-lib-libXScrnSaver-static >= 1.2.2
Requires:	xorg-lib-libXau-static >= 1.0.7
Requires:	xorg-lib-libXcomposite-static >= 0.4.3
Requires:	xorg-lib-libXcursor-static >= 1.1.13
Requires:	xorg-lib-libXdamage-static >= 1.1.3
Requires:	xorg-lib-libXdmcp-static >= 1.1.1
Requires:	xorg-lib-libXext-static >= 1.3.1
Requires:	xorg-lib-libXfixes-static >= 5.0
Requires:	xorg-lib-libXfont-static >= 1.4.5
Requires:	xorg-lib-libXft-static >= 2.3.1
Requires:	xorg-lib-libXi-static >= 1.6.1
Requires:	xorg-lib-libXinerama-static >= 1.1.2
Requires:	xorg-lib-libXmu-static >= 1.1.1
Requires:	xorg-lib-libXp-static
Requires:	xorg-lib-libXpm-static >= 3.5.10
Requires:	xorg-lib-libXrandr-static >= 1.3.2
Requires:	xorg-lib-libXrender-static >= 0.9.7
Requires:	xorg-lib-libXres-static >= 1.0.6
Requires:	xorg-lib-libXt-static >= 1.1.3
Requires:	xorg-lib-libXtst-static >= 1.2.1
Requires:	xorg-lib-libXv-static >= 1.0.7
Requires:	xorg-lib-libXvMC-static >= 1.0.7
Requires:	xorg-lib-libXxf86dga-static >= 1.1.3
Requires:	xorg-lib-libXxf86vm-static >= 1.1.2
Requires:	xorg-lib-libfontenc-static >= 1.1.1
Requires:	xorg-lib-libxkbfile-static >= 1.0.8
Provides:	XFree86-static = %{epoch}:%{version}-%{release}
# common obsoletes
Obsoletes:	X11-DPS-static < 1:7
Obsoletes:	X11-OpenGL-static < 1:7.0.0-13
Obsoletes:	XFree86-DPS-static < 1:5
Obsoletes:	XFree86-OpenGL-static < 1:5

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
Requires:	xorg-app-x11perf >= 1.5.4
Requires:	xorg-app-xbiff
Requires:	xorg-app-xcalc
Requires:	xorg-app-xclipboard
Requires:	xorg-app-xclock
Requires:	xorg-app-xdbedizzy
Requires:	xorg-app-xditview
Requires:	xorg-app-xdriinfo >= 1.0.4
Requires:	xorg-app-xedit
Requires:	xorg-app-xev >= 1.2.0
Requires:	xorg-app-xeyes
Requires:	xorg-app-xfd
Requires:	xorg-app-xfontsel
Requires:	xorg-app-xgc
Requires:	xorg-app-xkill >= 1.0.3
Requires:	xorg-app-xload
Requires:	xorg-app-xlogo
Requires:	xorg-app-xmag
Requires:	xorg-app-xman
Requires:	xorg-app-xmessage
Requires:	xorg-app-xmh
Requires:	xorg-app-xmore
Requires:	xorg-app-xplsprinters
Requires:	xorg-app-xpr >= 1.0.4
Requires:	xorg-app-xprehashprinterlist
Requires:	xorg-app-xprop >= 1.2.1
Requires:	xorg-app-xwininfo >= 1.1.2
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
Requires:	xorg-util-makedepend >= 1.0.4
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
Requires:	xorg-app-sessreg >= 1.0.7
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
Obsoletes:	XFree86-twm < 1:5
Obsoletes:	twm < 1:5

%description -n X11-twm
twm package that allows easier monolithic X11->modular xorg upgrade.

%description -n X11-twm -l pl.UTF-8
Pakiet twm ułatwiający przejście z monolitycznego X11 na modularne
xorg.

%package -n X11-xauth
Summary:	xauth package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet xauth ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		X11
Requires:	xorg-app-xauth >= 1.0.7
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
Provides:	xfs = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-xfs < 1:5
Obsoletes:	xfs < 1:5

%description -n X11-xfs
xfs package that allows easier monolithic X11->modular xorg upgrade.

%description -n X11-xfs -l pl.UTF-8
Pakiet xfs ułatwiający przejście z monolitycznego X11 na modularne
xorg.

%package -n X11-fonts
Summary:	fonts package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet fonts ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		X11
Requires:	xorg-font-encodings >= 1.0.4
Requires:	xorg-font-font-adobe-utopia-type1 >= 1.0.4
Requires:	xorg-font-font-arabic-misc >= 1.0.3
Requires:	xorg-font-font-bh-ttf >= 1.0.3
Requires:	xorg-font-font-bh-type1 >= 1.0.3
Requires:	xorg-font-font-bitstream-type1 >= 1.0.3
Requires:	xorg-font-font-daewoo-misc >= 1.0.3
Requires:	xorg-font-font-dec-misc >= 1.0.3
Requires:	xorg-font-font-ibm-type1 >= 1.0.3
Requires:	xorg-font-font-isas-misc >= 1.0.3
Requires:	xorg-font-font-micro-misc >= 1.0.3
Requires:	xorg-font-font-misc-ethiopic >= 1.0.3
Requires:	xorg-font-font-misc-meltho >= 1.0.3
Requires:	xorg-font-font-misc-misc >= 1.1.2
Requires:	xorg-font-font-mutt-misc >= 1.0.3
Requires:	xorg-font-font-schumacher-misc >= 1.1.2
Requires:	xorg-font-font-sony-misc >= 1.0.3
Requires:	xorg-font-font-sun-misc >= 1.0.3
Requires:	xorg-font-font-xfree86-type1 >= 1.0.4
Provides:	XFree86-fonts = %{epoch}:%{version}-%{release}

%description -n X11-fonts
fonts package that allows easier monolithic X11->modular xorg upgrade.

%description -n X11-fonts -l pl.UTF-8
Pakiet fonts ułatwiający przejście z monolitycznego X11 na modularne
xorg.

%package -n X11-fonts-utils
Summary:	fonts-utils package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet fonts-utils ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		X11
Requires:	xorg-font-font-util >= 1.3.0
Provides:	XFree86-fonts-utils = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-fonts-utils < 5

%description -n X11-fonts-utils
fonts-utils package that allows easier monolithic X11->modular xorg
upgrade.

%description -n X11-fonts-utils -l pl.UTF-8
Pakiet fonts-utils ułatwiający przejście z monolitycznego X11 na
modularne xorg.

%package -n X11-fonts-base
Summary:	fonts-base package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet fonts-base ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		Fonts
Requires:	xorg-font-font-cursor-misc >= 1.0.3
Requires:	xorg-font-font-misc-misc-base >= 1.1.2

%description -n X11-fonts-base
fonts-base package that allows easier monolithic X11->modular xorg
upgrade.

%description -n X11-fonts-base -l pl.UTF-8
Pakiet fonts-base ułatwiający przejście z monolitycznego X11 na
modularne xorg.

%package -n X11-fonts-ISO8859-1
Summary:	fonts-ISO8859-1 package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet fonts-ISO8859-1 ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		Fonts
Requires:	xorg-font-font-misc-misc-ISO8859-1 >= 1.1.2
Provides:	XFree86-fonts-ISO8859-1 = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-fonts-ISO8859-1 < 5

%description -n X11-fonts-ISO8859-1
fonts-ISO8859-1 package that allows easier monolithic X11->modular
xorg upgrade.

%description -n X11-fonts-ISO8859-1 -l pl.UTF-8
Pakiet fonts-ISO8859-1 ułatwiający przejście z monolitycznego X11 na
modularne xorg.

%package -n X11-fonts-ISO8859-2
Summary:	fonts-ISO8859-2 package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet fonts-ISO8859-2 ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		Fonts
Requires:	xorg-font-font-misc-misc-ISO8859-2 >= 1.1.2
Provides:	XFree86-fonts-ISO8859-2 = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-fonts-ISO8859-2 < 5

%description -n X11-fonts-ISO8859-2
fonts-ISO8859-2 package that allows easier monolithic X11->modular
xorg upgrade.

%description -n X11-fonts-ISO8859-2 -l pl.UTF-8
Pakiet fonts-ISO8859-2 ułatwiający przejście z monolitycznego X11 na
modularne xorg.

%package -n X11-fonts-ISO8859-3
Summary:	fonts-ISO8859-3 package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet fonts-ISO8859-3 ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		Fonts
Requires:	xorg-font-font-misc-misc-ISO8859-3 >= 1.1.2
Provides:	XFree86-fonts-ISO8859-3 = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-fonts-ISO8859-3 < 5

%description -n X11-fonts-ISO8859-3
fonts-ISO8859-3 package that allows easier monolithic X11->modular
xorg upgrade.

%description -n X11-fonts-ISO8859-3 -l pl.UTF-8
Pakiet fonts-ISO8859-3 ułatwiający przejście z monolitycznego X11 na
modularne xorg.

%package -n X11-fonts-ISO8859-4
Summary:	fonts-ISO8859-4 package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet fonts-ISO8859-4 ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		Fonts
Requires:	xorg-font-font-misc-misc-ISO8859-4 >= 1.1.2
Provides:	XFree86-fonts-ISO8859-4 = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-fonts-ISO8859-4 < 5

%description -n X11-fonts-ISO8859-4
fonts-ISO8859-4 package that allows easier monolithic X11->modular
xorg upgrade.

%description -n X11-fonts-ISO8859-4 -l pl.UTF-8
Pakiet fonts-ISO8859-4 ułatwiający przejście z monolitycznego X11 na
modularne xorg.

%package -n X11-fonts-ISO8859-5
Summary:	fonts-ISO8859-5 package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet fonts-ISO8859-5 ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		Fonts
Requires:	xorg-font-font-misc-misc-ISO8859-5 >= 1.1.2
Provides:	XFree86-fonts-ISO8859-5 = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-fonts-ISO8859-5 < 5

%description -n X11-fonts-ISO8859-5
fonts-ISO8859-5 package that allows easier monolithic X11->modular
xorg upgrade.

%description -n X11-fonts-ISO8859-5 -l pl.UTF-8
Pakiet fonts-ISO8859-5 ułatwiający przejście z monolitycznego X11 na
modularne xorg.

%package -n X11-fonts-ISO8859-7
Summary:	fonts-ISO8859-7 package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet fonts-ISO8859-7 ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		Fonts
Requires:	xorg-font-font-misc-misc-ISO8859-7 >= 1.1.2
Provides:	XFree86-fonts-ISO8859-7 = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-fonts-ISO8859-7 < 5

%description -n X11-fonts-ISO8859-7
fonts-ISO8859-7 package that allows easier monolithic X11->modular
xorg upgrade.

%description -n X11-fonts-ISO8859-7 -l pl.UTF-8
Pakiet fonts-ISO8859-7 ułatwiający przejście z monolitycznego X11 na
modularne xorg.

%package -n X11-fonts-ISO8859-8
Summary:	fonts-ISO8859-8 package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet fonts-ISO8859-8 ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		Fonts
Requires:	xorg-font-font-misc-misc-ISO8859-8 >= 1.1.2
Provides:	XFree86-fonts-ISO8859-8 = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-fonts-ISO8859-8 < 5

%description -n X11-fonts-ISO8859-8
fonts-ISO8859-8 package that allows easier monolithic X11->modular
xorg upgrade.

%description -n X11-fonts-ISO8859-8 -l pl.UTF-8
Pakiet fonts-ISO8859-8 ułatwiający przejście z monolitycznego X11 na
modularne xorg.

%package -n X11-fonts-ISO8859-9
Summary:	fonts-ISO8859-9 package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet fonts-ISO8859-9 ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		Fonts
Requires:	xorg-font-font-misc-misc-ISO8859-9 >= 1.1.2
Provides:	XFree86-fonts-ISO8859-9 = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-fonts-ISO8859-9 < 5

%description -n X11-fonts-ISO8859-9
fonts-ISO8859-9 package that allows easier monolithic X11->modular
xorg upgrade.

%description -n X11-fonts-ISO8859-9 -l pl.UTF-8
Pakiet fonts-ISO8859-9 ułatwiający przejście z monolitycznego X11 na
modularne xorg.

%package -n X11-fonts-ISO8859-10
Summary:	fonts-ISO8859-10 package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet fonts-ISO8859-10 ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		Fonts
Requires:	xorg-font-font-misc-misc-ISO8859-10 >= 1.1.2
Provides:	XFree86-fonts-ISO8859-10 = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-fonts-ISO8859-10 < 5

%description -n X11-fonts-ISO8859-10
fonts-ISO8859-10 package that allows easier monolithic X11->modular
xorg upgrade.

%description -n X11-fonts-ISO8859-10 -l pl.UTF-8
Pakiet fonts-ISO8859-10 ułatwiający przejście z monolitycznego X11 na
modularne xorg.

%package -n X11-fonts-ISO8859-11
Summary:	fonts-ISO8859-11 package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet fonts-ISO8859-11 ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		Fonts
Requires:	xorg-font-font-misc-misc-ISO8859-11 >= 1.1.2
Provides:	XFree86-fonts-ISO8859-11 = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-fonts-ISO8859-11 < 5

%description -n X11-fonts-ISO8859-11
fonts-ISO8859-11 package that allows easier monolithic X11->modular
xorg upgrade.

%description -n X11-fonts-ISO8859-11 -l pl.UTF-8
Pakiet fonts-ISO8859-11 ułatwiający przejście z monolitycznego X11 na
modularne xorg.

%package -n X11-fonts-ISO8859-13
Summary:	fonts-ISO8859-13 package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet fonts-ISO8859-13 ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		Fonts
Requires:	xorg-font-font-misc-misc-ISO8859-13 >= 1.1.2
Provides:	XFree86-fonts-ISO8859-13 = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-fonts-ISO8859-13 < 5

%description -n X11-fonts-ISO8859-13
fonts-ISO8859-13 package that allows easier monolithic X11->modular
xorg upgrade.

%description -n X11-fonts-ISO8859-13 -l pl.UTF-8
Pakiet fonts-ISO8859-13 ułatwiający przejście z monolitycznego X11 na
modularne xorg.

%package -n X11-fonts-ISO8859-14
Summary:	fonts-ISO8859-14 package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet fonts-ISO8859-14 ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		Fonts
Requires:	xorg-font-font-misc-misc-ISO8859-14 >= 1.1.2
Provides:	XFree86-fonts-ISO8859-14 = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-fonts-ISO8859-14 < 5

%description -n X11-fonts-ISO8859-14
fonts-ISO8859-14 package that allows easier monolithic X11->modular
xorg upgrade.

%description -n X11-fonts-ISO8859-14 -l pl.UTF-8
Pakiet fonts-ISO8859-14 ułatwiający przejście z monolitycznego X11 na
modularne xorg.

%package -n X11-fonts-ISO8859-15
Summary:	fonts-ISO8859-15 package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet fonts-ISO8859-15 ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		Fonts
Requires:	xorg-font-font-misc-misc-ISO8859-15 >= 1.1.2
Provides:	XFree86-fonts-ISO8859-15 = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-fonts-ISO8859-15 < 5

%description -n X11-fonts-ISO8859-15
fonts-ISO8859-15 package that allows easier monolithic X11->modular
xorg upgrade.

%description -n X11-fonts-ISO8859-15 -l pl.UTF-8
Pakiet fonts-ISO8859-15 ułatwiający przejście z monolitycznego X11 na
modularne xorg.

%package -n X11-fonts-ISO8859-16
Summary:	fonts-ISO8859-16 package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet fonts-ISO8859-16 ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		Fonts
Requires:	xorg-font-font-misc-misc-ISO8859-16 >= 1.1.2
Provides:	XFree86-fonts-ISO8859-16 = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-fonts-ISO8859-16 < 5

%description -n X11-fonts-ISO8859-16
fonts-ISO8859-16 package that allows easier monolithic X11->modular
xorg upgrade.

%description -n X11-fonts-ISO8859-16 -l pl.UTF-8
Pakiet fonts-ISO8859-16 ułatwiający przejście z monolitycznego X11 na
modularne xorg.

%package -n X11-fonts-75dpi
Summary:	fonts-75dpi package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet fonts-75dpi ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		Fonts
Requires:	xorg-font-font-adobe-75dpi >= 1.0.3
Requires:	xorg-font-font-adobe-utopia-75dpi >= 1.0.4
Requires:	xorg-font-font-bh-75dpi >= 1.0.3
Requires:	xorg-font-font-bh-lucidatypewriter-75dpi >= 1.0.3
Requires:	xorg-font-font-bitstream-75dpi >= 1.0.3
Provides:	XFree86-fonts-75dpi = %{epoch}:%{version}-%{release}
Obsoletes:	X11-fonts-75dpi-ISO8859-1 < 7
Obsoletes:	X11-fonts-75dpi-ISO8859-10 < 7
Obsoletes:	X11-fonts-75dpi-ISO8859-13 < 7
Obsoletes:	X11-fonts-75dpi-ISO8859-14 < 7
Obsoletes:	X11-fonts-75dpi-ISO8859-15 < 7
Obsoletes:	X11-fonts-75dpi-ISO8859-2 < 7
Obsoletes:	X11-fonts-75dpi-ISO8859-3 < 7
Obsoletes:	X11-fonts-75dpi-ISO8859-4 < 7
Obsoletes:	X11-fonts-75dpi-ISO8859-9 < 7
Obsoletes:	X11R6.1-75dpi-fonts < 3.2
Obsoletes:	XFree86-fonts-75dpi < 5
Obsoletes:	XFree86-fonts-75dpi-ISO8859-1 < 5
Obsoletes:	XFree86-fonts-75dpi-ISO8859-10 < 5
Obsoletes:	XFree86-fonts-75dpi-ISO8859-13 < 5
Obsoletes:	XFree86-fonts-75dpi-ISO8859-14 < 5
Obsoletes:	XFree86-fonts-75dpi-ISO8859-15 < 5
Obsoletes:	XFree86-fonts-75dpi-ISO8859-2 < 5
Obsoletes:	XFree86-fonts-75dpi-ISO8859-3 < 5
Obsoletes:	XFree86-fonts-75dpi-ISO8859-4 < 5
Obsoletes:	XFree86-fonts-75dpi-ISO8859-9 < 5

%description -n X11-fonts-75dpi
fonts-75dpi package that allows easier monolithic X11->modular xorg
upgrade.

%description -n X11-fonts-75dpi -l pl.UTF-8
Pakiet fonts-75dpi ułatwiający przejście z monolitycznego X11 na
modularne xorg.

%package -n X11-fonts-100dpi
Summary:	fonts-100dpi package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet fonts-100dpi ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		Fonts
Requires:	xorg-font-font-adobe-100dpi >= 1.0.3
Requires:	xorg-font-font-adobe-utopia-100dpi >= 1.0.4
Requires:	xorg-font-font-bh-100dpi >= 1.0.3
Requires:	xorg-font-font-bh-lucidatypewriter-100dpi >= 1.0.3
Requires:	xorg-font-font-bitstream-100dpi >= 1.0.3
Provides:	XFree86-fonts-100dpi = %{epoch}:%{version}-%{release}
Obsoletes:	X11-fonts-100dpi-ISO8859-1 < 7
Obsoletes:	X11-fonts-100dpi-ISO8859-10 < 7
Obsoletes:	X11-fonts-100dpi-ISO8859-13 < 7
Obsoletes:	X11-fonts-100dpi-ISO8859-14 < 7
Obsoletes:	X11-fonts-100dpi-ISO8859-15 < 7
Obsoletes:	X11-fonts-100dpi-ISO8859-2 < 7
Obsoletes:	X11-fonts-100dpi-ISO8859-3 < 7
Obsoletes:	X11-fonts-100dpi-ISO8859-4 < 7
Obsoletes:	X11-fonts-100dpi-ISO8859-9 < 7
Obsoletes:	X11R6.1-100dpi-fonts < 3.2
Obsoletes:	XFree86-fonts-100dpi < 5
Obsoletes:	XFree86-fonts-100dpi-ISO8859-1 < 5
Obsoletes:	XFree86-fonts-100dpi-ISO8859-10 < 5
Obsoletes:	XFree86-fonts-100dpi-ISO8859-13 < 5
Obsoletes:	XFree86-fonts-100dpi-ISO8859-14 < 5
Obsoletes:	XFree86-fonts-100dpi-ISO8859-15 < 5
Obsoletes:	XFree86-fonts-100dpi-ISO8859-2 < 5
Obsoletes:	XFree86-fonts-100dpi-ISO8859-3 < 5
Obsoletes:	XFree86-fonts-100dpi-ISO8859-4 < 5
Obsoletes:	XFree86-fonts-100dpi-ISO8859-9 < 5

%description -n X11-fonts-100dpi
fonts-100dpi package that allows easier monolithic X11->modular xorg
upgrade.

%description -n X11-fonts-100dpi -l pl.UTF-8
Pakiet fonts-100dpi ułatwiający przejście z monolitycznego X11 na
modularne xorg.

%package -n X11-fonts-JISX0201.1976-0
Summary:	fonts-JISX0201.1976-0 package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet fonts-JISX0201.1976-0 ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		Fonts
Requires:	xorg-font-font-jis-misc >= 1.0.3
Provides:	XFree86-fonts-JISX0201.1976-0 = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-fonts-JISX0201.1976-0 < 5

%description -n X11-fonts-JISX0201.1976-0
fonts-JISX0201.1976-0 package that allows easier monolithic
X11->modular xorg upgrade.

%description -n X11-fonts-JISX0201.1976-0 -l pl.UTF-8
Pakiet fonts-JISX0201.1976-0 ułatwiający przejście z monolitycznego
X11 na modularne xorg.

%package -n X11-fonts-KOI8-R
Summary:	fonts-KOI8-R package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet fonts-KOI8-R ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		Fonts
Requires:	xorg-font-font-cronyx-cyrillic >= 1.0.3
Requires:	xorg-font-font-misc-cyrillic >= 1.0.3
Requires:	xorg-font-font-screen-cyrillic >= 1.0.4
Requires:	xorg-font-font-winitzki-cyrillic >= 1.0.3
Provides:	XFree86-fonts-KOI8-R = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-fonts-KOI8-R < 5

%description -n X11-fonts-KOI8-R
fonts-KOI8-R package that allows easier monolithic X11->modular xorg
upgrade.

%description -n X11-fonts-KOI8-R -l pl.UTF-8
Pakiet fonts-KOI8-R ułatwiający przejście z monolitycznego X11 na
modularne xorg.

%package -n X11-fonts-Ethiopic
Summary:	fonts-Ethiopic package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet fonts-Ethiopic ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		Fonts
Requires:	xorg-font-font-misc-ethiopic >= 1.0.3
Provides:	XFree86-fonts-Ethiopic = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-fonts-Ethiopic < 5

%description -n X11-fonts-Ethiopic
fonts-Ethiopic package that allows easier monolithic X11->modular xorg
upgrade.

%description -n X11-fonts-Ethiopic -l pl.UTF-8
Pakiet fonts-Ethiopic ułatwiający przejście z monolitycznego X11 na
modularne xorg.

%package -n X11-fonts-Syriac
Summary:	fonts-Syriac package that allows easier monolithic X11->modular xorg upgrade
Summary(pl.UTF-8):	Pakiet fonts-Syriac ułatwiający przejście z monolitycznego X11 na modularne xorg
Group:		Fonts
Requires:	xorg-font-font-misc-meltho >= 1.0.3
Provides:	XFree86-fonts-Syriac = %{epoch}:%{version}-%{release}
Obsoletes:	XFree86-fonts-Syriac < 5

%description -n X11-fonts-Syriac
fonts-Syriac package that allows easier monolithic X11->modular xorg
upgrade.

%description -n X11-fonts-Syriac -l pl.UTF-8
Pakiet fonts-Syriac ułatwiający przejście z monolitycznego X11 na
modularne xorg.

%prep

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%files -n X11
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
%files -n X11-Xnest
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
%files -n X11-driver-radeon-dri
%defattr(644,root,root,755)
%files -n X11-driver-chips
%defattr(644,root,root,755)
%files -n X11-driver-cirrus
%defattr(644,root,root,755)
%files -n X11-driver-fbdev
%defattr(644,root,root,755)
%files -n X11-driver-i128
%defattr(644,root,root,755)
%files -n X11-driver-i2c
%defattr(644,root,root,755)
%files -n X11-driver-i740
%defattr(644,root,root,755)
%files -n X11-driver-i810
%defattr(644,root,root,755)
%files -n X11-driver-mga
%defattr(644,root,root,755)
%files -n X11-driver-neomagic
%defattr(644,root,root,755)
%ifarch mips
%files -n X11-driver-newport
%defattr(644,root,root,755)
%endif
%files -n X11-driver-nv
%defattr(644,root,root,755)
%files -n X11-driver-nvidia
%defattr(644,root,root,755)
%files -n X11-driver-nvidia-devel
%defattr(644,root,root,755)
%files -n X11-driver-nvidia-progs
%defattr(644,root,root,755)
%files -n X11-driver-rendition
%defattr(644,root,root,755)
%files -n X11-driver-s3virge
%defattr(644,root,root,755)
%files -n X11-driver-savage
%defattr(644,root,root,755)
%files -n X11-driver-siliconmotion
%defattr(644,root,root,755)
%files -n X11-driver-sis
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
%files -n X11-driver-trident
%defattr(644,root,root,755)
%files -n X11-driver-tseng
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
%files -n X11-fonts-utils
%defattr(644,root,root,755)
%files -n X11-fonts-base
%defattr(644,root,root,755)
%files -n X11-fonts-JISX0201.1976-0
%defattr(644,root,root,755)
%files -n X11-fonts-KOI8-R
%defattr(644,root,root,755)
%files -n X11-fonts-Ethiopic
%defattr(644,root,root,755)
%files -n X11-fonts-Syriac
%defattr(644,root,root,755)
%files -n X11-fonts-ISO8859-1
%defattr(644,root,root,755)
%files -n X11-fonts-ISO8859-2
%defattr(644,root,root,755)
%files -n X11-fonts-ISO8859-3
%defattr(644,root,root,755)
%files -n X11-fonts-ISO8859-4
%defattr(644,root,root,755)
%files -n X11-fonts-ISO8859-5
%defattr(644,root,root,755)
%files -n X11-fonts-ISO8859-7
%defattr(644,root,root,755)
%files -n X11-fonts-ISO8859-8
%defattr(644,root,root,755)
%files -n X11-fonts-ISO8859-9
%defattr(644,root,root,755)
%files -n X11-fonts-ISO8859-10
%defattr(644,root,root,755)
%files -n X11-fonts-ISO8859-11
%defattr(644,root,root,755)
%files -n X11-fonts-ISO8859-13
%defattr(644,root,root,755)
%files -n X11-fonts-ISO8859-14
%defattr(644,root,root,755)
%files -n X11-fonts-ISO8859-15
%defattr(644,root,root,755)
%files -n X11-fonts-ISO8859-16
%defattr(644,root,root,755)
%files -n X11-fonts-75dpi
%defattr(644,root,root,755)
%files -n X11-fonts-100dpi
%defattr(644,root,root,755)
