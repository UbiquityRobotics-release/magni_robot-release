Name:           ros-kinetic-magni-description
Version:        0.2.1
Release:        0%{?dist}
Summary:        ROS magni_description package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-joint-state-publisher
Requires:       ros-kinetic-robot-state-publisher
Requires:       ros-kinetic-urdf
Requires:       ros-kinetic-xacro
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-joint-state-publisher
BuildRequires:  ros-kinetic-robot-state-publisher
BuildRequires:  ros-kinetic-urdf
BuildRequires:  ros-kinetic-xacro

%description
The magni_description package

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Sat Oct 28 2017 Rohan Agrawal <send2arohan@gmail.com> - 0.2.1-0
- Autogenerated by Bloom

* Sat Aug 19 2017 Rohan Agrawal <send2arohan@gmail.com> - 0.2.0-0
- Autogenerated by Bloom

* Tue Jul 04 2017 Rohan Agrawal <send2arohan@gmail.com> - 0.1.1-0
- Autogenerated by Bloom

* Sat Jun 17 2017 Rohan Agrawal <send2arohan@gmail.com> - 0.1.0-0
- Autogenerated by Bloom

