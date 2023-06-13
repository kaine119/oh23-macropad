# Firmware

This folder contains .uf2's for the macropad, as well as a submodule link to my fork of `vial-qmk`, where the source code for the macropad firmware lives.

## To flash a `.uf2`:

1. Connect the board to your computer.

2. Hold down the BOOTSEL button at the bottom of the board, then press the reset button.

    The two buttons on the XIAO microcontroller can be accessed via the two holes at the bottom of the case. Use two pens to press the buttons. 

    With the USB port facing up, the BOOTSEL button is the button on the right, and the reset button is the one on the left.

    The board should reboot into bootloader mode, which mounts a USB storage device to your computer. 

3. Copy the `.uf2` into the newly mounted USB storage device. The board will reboot with the new firmware.

    If you flashed one of the `vial` firmware files, you should be able to open Vial and edit the keymap + other settings.

## Developing QMK for the macropad

The source code for the firmware lives in `vial-qmk/keyboards/kaine119/oh23-macropad`; it's just barebones setup for the three keys, Vial configuration, and RGB lighting.

If you'd like to connect your own hardware via the GPIO pins, please consult the QMK docs. Vial also has a feature for [custom keycodes](https://get.vial.today/manual/custom_keycode.html), which presumably lets you define your own keycodes that show up in Vial. This can be used to perform custom actions on the GPIO pins. In practice, I couldn't get this working in time for Open House; I used CircuitPython instead. You may want to give CircuitPython a shot first; [KMK project](http://kmkfw.io/docs/) is a similar keyboard firmware project that runs on CircuitPython.