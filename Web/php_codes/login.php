<?php
session_start();
if(isset($_SESSION['user'])){
header("location:home.php");
}

	if(isset($_POST))
	{
			if(isset($_POST['btnSubmit']) && $_POST['btnSubmit'] == "Login")
			{
				$data = "";
				$username = $_POST['username'];
				$password = $_POST['password'];
				if(strlen($username) <= 0)
				{
					$data =  "Username cannot be blank";
				}
				else if(strlen($password) <= 0)
				{
					$data =  "Password cannot be blank";
				}
				else if(strlen($password) > 0 && strlen($password) < 8)
				{
					$data = "Password should be greater than 8 digits";
				}
				else
				{
					if($username == "admin" && $password == "admin@12345")
					{
						//echo "User validated successfully";
						$_SESSION['user'] = $username;
						header("location:home.php");
					}
					else
					{
						$data = "Failed to Login, Check user credentials";
					}
				}
				echo "<h2 style='color:red'>" . $data . "</h2>";
			}
	}
?>
<html>
	<head><title>Login</title></head>
	<body>
		<form method="POST" action="">
			Enter Username:
			<input type="text" name="username" placeholder="Enter Username" required />
			<br />
			Enter Password:
			<input type="password" name="password" placeholder="Enter Password" required />
			<br />
			<input type="submit" name="btnSubmit" value="Login" />
		</form>
	</body>
</html>