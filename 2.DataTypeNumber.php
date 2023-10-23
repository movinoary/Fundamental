<?php
// Di php ada 2 jenis tipe data
// 1. int = bilangan bulat (10,20,30,50)
// 2. float = bilangan pecahan (1.5, 1.7)


echo "Decimal :";
var_dump(1234);

echo "Octal :";
var_dump(0123); // didepannya ditambahin 0

echo "Hexadecimal :";
var_dump(0x1A); // didepannya ditambahin 0x

echo "Binary :";
var_dump(0b01101); // didepannya ditambahin 0b

echo "Underscore in number :"; // _ dibaca undifind
var_dump(1_231_231_123);

echo "Floting Point :";
var_dump(1.234);

echo "Floting Point dengan E notation Plus (1.2 x 1000) :";
var_dump(1.2e4);

echo "Floting Point dengan E notation Minus (7 x 1000) :";
var_dump(7e-3);

echo "Underscore in Floting Point :";
var_dump(1_13.234);


// integer overflow
// decara default di 32 bit bisa sampai 2137483647
// decara default di 64 bit bisa sampai 9223372036854775807
// jika lebih dari batasan maka akan di konversi menjadi floating point

echo "Integer Overflow 32 Bit :";
var_dump(2137483647);

echo "Integer Overflow 64 Bit :";
var_dump(9223372036854775807);
