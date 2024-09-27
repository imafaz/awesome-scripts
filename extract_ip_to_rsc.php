<?php

function extractIpRanges($inputFile, $outputFile, $listName) {

    $fileContents = file($inputFile, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);
    
    $ipRanges = [];

    foreach ($fileContents as $line) {
        if (preg_match('/(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}(\.\d{1,3})?)(\/\d{1,2})?/', $line, $matches)) {
            $ipRanges[] = $matches[0];
        }
    }

    $output = "/ip firewall address-list\n";
    $output .= ":local listName \"$listName\"\n";
    foreach ($ipRanges as $range) {
        $output .= "add list=\$listName address=\"$range\"\n";
    }

    file_put_contents($outputFile, $output);

    echo "IP addresses have been successfully saved in file $outputFile.\n";
}

$inputFile = 'inputfile'; 
$outputFile = 'output.rsc'; 
$listName = 'extraxted'; 

extractIpRanges($inputFile, $outputFile, $listName);
