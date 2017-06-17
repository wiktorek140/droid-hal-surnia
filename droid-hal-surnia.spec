#These and other macros are documented in dhd/droid-hal-device.inc
%define device surnia
%define vendor motorola

%define vendor_pretty Motorola
%define device_pretty Moto E2

%define installable_zip 1

%define straggler_files\
/init.mmi.boot.sh\
/init.mmi.touch.sh\
%{nil}

%define additional_post_scripts \
/usr/bin/groupadd-user inet || :\
%{nil}

%include rpm/dhd/droid-hal-device.inc
