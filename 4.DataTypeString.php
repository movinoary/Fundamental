<?php

echo 'Nama :';
echo 'Vino Arystio';
echo "\n";

echo 'Nama :';
echo "Vino\t Arystio\n";

// Heredoc 
// TEXT = nama tag bebas
echo <<<TEXT
ini adalah contoh string yang panjang
dan juga gak perlu ngetik ENTER secara manual, 
"bisa qoute" juga

TEXT;

// Heredoc 
// sama seperti heredoc namun tidak memiliku kemampuan double qoute
echo <<<'TEXT'

ini adalah contoh  yang panjang
dan juga gak perlu ngetik ENTER secara manual juga
TEXT;
