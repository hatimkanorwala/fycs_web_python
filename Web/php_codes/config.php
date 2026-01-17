<?php
	$conn = new mysqli("localhost","root","admin","burhani_fy_web");
	if(mysqli_connect_error())
	{
		echo "Connection failed";
	}
?>