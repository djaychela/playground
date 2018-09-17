import barcode

print(barcode.PROVIDED_BARCODES)

EAN = barcode.get_barcode_class('ean13')

ean = EAN('5901234123457')

print(ean)

ean.save('test_barcode_1')

UPC = barcode.get_barcode_class('upc')

upc = UPC('5901234123457')

upc.save('test_barcode_2')