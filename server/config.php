<?php
$host_name = "localhost";
$database = "project_sic"; // Change your database name
$username = "root";          // Your database user id 
$password = "root";          // Your password

//////// Do not Edit below /////////
try {
$dbo = new PDO('mysql:host='.$host_name.';dbname='.$database, $username, $password);
} catch (PDOException $e) {
print "Error!: " . $e->getMessage() . "<br/>";
die();
}
?>