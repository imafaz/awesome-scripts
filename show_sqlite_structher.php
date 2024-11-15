<?php

try{
        $pdo = new PDO("sqlite:/etc/x-ui/x-ui.db");
        $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);


        $tablesQuery = $pdo->query("SELECT name FROM sqlite_master WHERE type='table'");
        $tables = $tablesQuery->fetchAll(PDO::FETCH_ASSOC);

        foreach ($tables as $table) {
            echo "Table: " . $table['name'] . "\n";


            $columnsQuery = $pdo->query("PRAGMA table_info(" . $table['name'] . ")");
            $columns = $columnsQuery->fetchAll(PDO::FETCH_ASSOC);

            echo "Columns:\n";
            foreach ($columns as $column) {
                echo " - " . $column['name'] . " (" . $column['type'] . ")\n";
            }

   
            $contentQuery = $pdo->query("SELECT * FROM " . $table['name']);
            $rows = $contentQuery->fetchAll(PDO::FETCH_ASSOC);

            echo "Content:\n";
            foreach ($rows as $row) {
                print_r($row);
            }

            echo "\n";
        }
    } catch (PDOException $e) {
        echo "Error: " . $e->getMessage();
    }

?>
