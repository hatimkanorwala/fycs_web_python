<?php
session_start();
if(!(isset($_SESSION['user']))){
header("location:logout.php");
}
echo "Welcome: " . $_SESSION['user'] ;
echo "<a href='logout.php'>Logout</a>";

?>