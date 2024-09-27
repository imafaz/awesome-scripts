<?php
include('mikrotik-api\src\MikrotikMng.php');

use MikrotikMng\Api;

$router = new Api();
$router->connect('ip', 'user', 'pass', 8989);
$traffic = $router->exec('/interface/monitor-traffic', ['ether7' => '', 'once' => '', 'without-paging' => '']);
var_dump($traffic);