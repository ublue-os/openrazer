# SPDX-License-Identifier: GPL-2.0-or-later

obj-m := razerkbd.o razermouse.o razerkraken.o razeraccessory.o

razerkbd-y := razerkbd_driver.o razercommon.o razerchromacommon.o
razermouse-y := razermouse_driver.o razercommon.o razerchromacommon.o
razerkraken-y := razerkraken_driver.o razercommon.o
razeraccessory-y := razeraccessory_driver.o razercommon.o razerchromacommon.o

ccflags-y := -std=gnu99 -Wno-declaration-after-statement
KERNEL_SOURCE_DIR := /lib/modules/$(shell uname -r)/build

all:
	make -C "$(KERNEL_SOURCE_DIR)" M="$(PWD)" modules

clean:
	make -C "$(KERNEL_SOURCE_DIR)" M="$(PWD)" clean
