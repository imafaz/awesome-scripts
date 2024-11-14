<?php

$directoryPath = readline("pliase inter directory name:");
$searchWord = readline("pliase inter word to search:");

function searchInFile($filePath, $searchWord) {
    $fileContent = file_get_contents($filePath);
    if (stripos($fileContent, $searchWord) !== false) {
        echo "Found in: " . $filePath . PHP_EOL;
    }
}

function recursiveSearch($directory, $search) {
    $items = scandir($directory);
    foreach ($items as $item) {
        if ($item === '.' || $item === '..') {
            continue;
        }

        $filePath = $directory . '/' . $item;
        if (is_dir($filePath)) {
            recursiveSearch($filePath, $search);
        } else {
            searchInFile($filePath, $search);
        }
    }
}

recursiveSearch($directoryPath, $searchWord);
?>
