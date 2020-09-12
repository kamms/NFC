#!/usr/bin/python
import usb.core

# find USB devices
dev = usb.core.find(find_all=True)


# loop through devices, printing vendor and product ids in decimal and hex
for cfg in dev:
    print(cfg)
    print('Decimal VendorID=' + str(cfg.idVendor) + ' & ProductID=' + str(cfg.idProduct) + '\n')
    print('Hexadecimal VendorID=' + hex(cfg.idVendor) + ' & ProductID=' + hex(cfg.idProduct) + '\n\n')
