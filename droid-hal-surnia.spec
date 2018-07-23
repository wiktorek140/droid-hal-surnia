#These and other macros are documented in dhd/droid-hal-device.inc
%define device surnia
%define vendor motorola

%define vendor_pretty Motorola
%define device_pretty Moto E2 LTE

%define installable_zip 1

%define community_adaptation 1

%define straggler_files\
/file_contexts.bin\
/property_contexts\
/selinux_version\
/service_contexts\
/bugreports\
/d\
/sdcard\
/vendor\
%{nil}

%define android_config \
#define QCOM_BSP 1\
%{nil}


%define additional_post_scripts \
/usr/bin/groupadd-user inet || :\
%{nil}

%include rpm/dhd/droid-hal-device.inc
