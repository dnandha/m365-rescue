# m365-rescue
Python based helper to restore m365 devices. Works on Linux!

The project is based on [https://github.com/CamiAlfa/M365_DRV_STLINK](https://github.com/CamiAlfa/M365_DRV_STLINK).

No firmware files are provided with this tool. You have posess the binary you want to flash.

WARNING: Most of the stuff is untested, be prepared to brick your device and open an issue / PR here :). Thanks!

## Usage
You can flash any firmware suited for the device (that you own!) by providing the path to the file as an CLI argument.

Use the `-s` or `--simulate` flag to generate an output file specified by `-o` or `--outfile`, instead of flashing with STLink.

Use the `ble` subcommand for BLE related functions. Use the `--16k` flag to indicate a M365 / Pro device with 16kb RAM (includes most clones). Default is 32k RAM device (Pro2/1S/3).
Type `ble --help` for more help.

Use the `esc` subcommand for ESC related functions. Use the `--gd32` flag to indicate a GD32 instead of the default STM32 MCU. Use the `--sn` and `--km` options to set the serial number and kilometer counter respectively.
Type `esc --help` for more help.

### STLink / OpenOCD
Connect STLink to the target device and start a openocd session. Then, in a new terminal, enter one of the example commands.

#### Restore 32k (Pro2..) BLE
`python m365resc.py ble BLE134.bin`

#### Restore 16k (Pro..) BLE
`python m365resc.py ble --16k BLE090.bin`

#### Restore STM32 ESC
`python m365resc.py esc --sn "..." --km 123 DRV236.bin`

#### Restore GD32 ESC
`python m365resc.py esc --gd32 --sn "..." --km 123 DRV247.bin`

#### Restore 4Pro ESC
`python m365resc.py esc --nb --sn "..." --km 123 DRV022.bin`

### Simulation
Simulation allows generation of the final output file without STLink connection.

#### Generate full 32k (Pro2..) BLE rescue file
`python m365resc.py -s -o out_ble134.bin ble BLE134.bin`

#### Generate full 16k (Pro..) BLE rescue file
`python m365resc.py -s -o out_ble090.bin ble --16k BLE090.bin`

#### Generate full STM32 ESC rescue file
`python m365resc.py -s -o out_drv236_stm32.bin esc --sn "..." --km 123 DRV236.bin`

#### Generate full GD32 ESC rescue file
`python m365resc.py -s -o out_drv247_gd32.bin esc --gd32 --sn "..." --km 123 DRV247.bin`

#### Generate full 4Pro ESC rescue file
`python m365resc.py -s -o out_drv022.bin esc --nb --sn "..." --km 123 DRV022.bin`

## Disclaimer
I am in no way affiliated with any hardware vendor. All information / files provided in this repo are publically available. The purpose of this project is to allow owners to restore device functionality in case of a software malfunction.
