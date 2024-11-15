<?php

function replaceInFile($filePath, $search, $replace) {
    $fileContent = file_get_contents($filePath);
    

    if (strpos($fileContent, $search) !== false) {
        $newContent = str_replace($search, $replace, $fileContent);
        
        if ($newContent !== $fileContent) {
            file_put_contents($filePath, $newContent);
            return true; 
        }
    }
    return false;
}

function recursiveSearch($directory, $search, $replace) {
    $modifiedFiles = []; 
    $dir = opendir($directory);
    
    while (($file = readdir($dir)) !== false) {
        if ($file != '.' && $file != '..') {
            $filePath = $directory . '/' . $file;
            if (is_dir($filePath)) {
                $modifiedFiles = array_merge($modifiedFiles, recursiveSearch($filePath, $search, $replace));
            } else {
                if (replaceInFile($filePath, $search, $replace)) {
                    $modifiedFiles[] = $filePath;
                }
            }
        }
    }
    closedir($dir);
    return $modifiedFiles;
}


$directoryPath = readline("Enter the directory path: ");
$searchWord = readline("Enter the word to search: ");
$replaceWord = readline("Enter the word to replace with: ");


if (!is_dir($directoryPath)) {
    echo "The specified directory does not exist.\n";
    exit(1);
}

$modifiedFiles = recursiveSearch($directoryPath, $searchWord, $replaceWord);

if (!empty($modifiedFiles)) {
    echo "Replacements were made in the following files:\n";
    foreach ($modifiedFiles as $modifiedFile) {
        echo $modifiedFile . "\n";
    }
} else {
    echo "No replacements were made.\n";
}
?>
