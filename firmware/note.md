I'll be sharing the actual `qmk_firmware` folder eventually, for now this folder will hold the built `.uf2` files, which should be ready to flash to the board.

## To flash a `.uf2`:

1. Connect the board to your computer.

2. Hold down the BOOTSEL button at the bottom of the board, then press the reset button.

    The two buttons on the XIAO microcontroller can be accessed via the two holes at the bottom of the case. Use two pens to press the buttons. 

    With the USB port facing up, the BOOTSEL button is the button on the right, and the reset button is the one on the left.

    The board should reboot into bootloader mode, which mounts a USB storage device to your computer. 

3. Copy the `.uf2` into the newly mounted USB storage device. The board will reboot with the new firmware.

    If you flashed one of the `vial` firmware files, you should be able to open Vial and edit the keymap + other settings.