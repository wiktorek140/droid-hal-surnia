#These and other macros are documented in dhd/droid-hal-device.inc
%define device surnia
%define vendor motorola

%define vendor_pretty Motorola
%define device_pretty Moto E2 LTE

%define installable_zip 1

%define community_adaptation 1

%define straggler_files\
/nonplat_file_contexts\
/nonplat_hwservice_contexts\
/nonplat_property_contexts\
/nonplat_seapp_contexts\
/nonplat_service_contexts\
/plat_file_contexts\
/plat_hwservice_contexts\
/plat_property_contexts\
/plat_seapp_contexts\
/plat_service_contexts\
/vndservice_contexts\
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

%define droid_target_armv7hl 1

%include rpm/dhd/droid-hal-device.inc
