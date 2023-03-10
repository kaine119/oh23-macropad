# oh23-macropad

Thanks for purchasing a oh23-macropad and supporting our Keyboard Warriors interest group here at SUTD! Your support means a lot to us.
<!-- fill this in please, idk man -->

## Configuration

The included firmware is powered by [QMK / Vial](https://get.vial.today/), a fork of QMK that allows for remapping keys on the fly. No `board.json` files here; Vial stores the keyboard configuration on the microcontroller itself.

You may [download the Vial configurator](https://get.vial.today/download/), or [Vial Web](https://vial.rocks/) if you're using Chrome (or Chromium), to remap keys, configure macros, and more. See the [Vial documentation](https://get.vial.today/manual/) for more details.


## Firmware

The board includes a XIAO RP2040 microcontroller unit (MCU), which behaves similarly to a Raspberry Pi Pico. As such, most of the flashing procedure for the Pico also applies to this board. More comprehensive resources for programming the control pins will be coming soon (too many commitments T_T).

Firmware `.uf2` files can be found [here](https://github.com/kaine119/oh23-macropad/tree/master/firmware), and can be directly flashed to the board without any special drivers. You just need a USB-C cable to connect the board to your computer. 

### To flash a `.uf2`:

1. Connect the board to your computer.

2. Hold down the BOOTSEL button at the bottom of the board, then press the reset button.

    The two buttons on the XIAO microcontroller can be accessed via the two holes at the bottom of the case. Use two pens to press the buttons. 

    With the USB port facing up, the BOOTSEL button is the button on the right, and the reset button is the one on the left.

    The board should reboot into bootloader mode, which mounts a USB storage device to your computer. 

3. Copy the `.uf2` into the newly mounted USB storage device. The board will reboot with the new firmware.

    If you flashed one of the `vial` firmware files, you should be able to open Vial and edit the keymap + other settings.

## More info when

More concrete documentation will be available on this page soon(tm), but for now here's a link to the [GitHub repository](https://github.com/kaine119/oh23-macropad). I've put up case files (Autodesk Inventor project files, STEP files), the KiCad files for the PCB and plate (guess where the plate came from), as well as a `.dxf` exported from keyboard-layout-[editor](http://www.keyboard-layout-editor.com/) that I used to build the design.

If you're interested in building a new case, the STEP files for the case and the `.dxf` of the layout file may be helpful.

If you're interested in programming the microcontroller, the schematics may be helpful.