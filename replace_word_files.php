<?php

function replaceInFile($filePath, $search, $replace) {
    $fileContent = file_get_contents($filePath);
    $newContent = str_replace($search, $replace, $fileContent);
    
    if ($newContent !== $fileContent) {
        file_put_contents($filePath, $newContent);
        return true; 
    }
    return false;
}

$directoryPath = 'sourcefolder';
$searchWord = 'words';
$replaceWord = 'replaced';
$modifiedFiles = []; 

function recursiveSearch($directory, $search, $replace) {
    global $modifiedFiles; 
    $dir = opendir($directory);
    
    while (($file = readdir($dir)) !== false) {
        if ($file != '.' && $file != '..') {
            $filePath = $directory.'/'.$file;
            if (is_dir($filePath)) {
                recursiveSearch($filePath, $search, $replace);
            } else {
                if (replaceInFile($filePath, $search, $replace)) {
                    $modifiedFiles[] = $filePath;
                }
            }
        }
    }
    closedir($dir);
}

recursiveSearch($directoryPath, $searchWord, $replaceWord);


if (!empty($modifiedFiles)) {
    echo "Replacements were made in the following files:\n";
    foreach ($modifiedFiles as $modifiedFile) {
        echo $modifiedFile . "\n";
    }
} else {
    echo "No replacements were made.\n";
}
?>
