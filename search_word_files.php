<?php

$directoryPath = 'folder';

$searchWord = 'word';


function searchInFile($filePath, $searchWord) {
    $fileContent = file_get_contents($filePath);
    if (stripos($fileContent, $searchWord) !== false) {
        echo "wcd " . $filePath . PHP_EOL;
    }
}


function recursiveSearch($directory, $search) {
    $dir = opendir($directory);
    while (($file = readdir($dir)) !== false) {
        if ($file != '.' && $file != '..') {
            $filePath = $directory.'/'.$file;
            if (is_dir($filePath)) {
                recursiveSearch($filePath, $search);
            } else {

                searchInFile($filePath, $search);
            }
        }
    }
    closedir($dir);
}

recursiveSearch($directoryPath, $searchWord);
?>
