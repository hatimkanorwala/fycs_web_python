<?php
	include('config.php');
	if(isset($_POST))
	{
		if(isset($_POST['btnSubmit']))
		{
			if($_POST['btnSubmit'] == "Register")
			{
				$username = $_POST['username'];
				$password = $_POST['password'];
				$con_password = $_POST['con_password'];
				if($username == "")
				{
					?>
						<script>
							alert("Username is required");
							window.location.href="registration.php";
						</script>
					<?php
				}
				else if($password == "")
				{
					?>
						<script>
							alert("Password is required");
							window.location.href="registration.php";
						</script>
					<?php	
				}
				else if(strlen($password) <= 8)
				{
					?>
						<script>
							alert("Password cannot be less than 8 characters");
							window.location.href="registration.php";
						</script>
					<?php
				}
				else if($con_password == "")
				{
					?>
						<script>
							alert("Confirm Password is required");
							window.location.href="registration.php";
						</script>
					<?php
				}
				else if(strlen($con_password) <= 8)
				{
										?>
						<script>
							alert("Confirm Password Length should be greater than 8 characters");
							window.location.href="registration.php";
						</script>
					<?php
				}
				else if($password != $con_password)
				{
					?>
						<script>
							alert("Password and confirm Password Doesnot match");
							window.location.href="registration.php";
						</script>
					<?php
				}
				$query = "INSERT INTO users(username,password) VALUES('$username','$password')";
				$res = mysqli_query($conn,$query);
				if($res > 0)
				{
					?>
						<script>
							alert("User Registered Successfully");
							window.location.href="registration.php";
						</script>
					<?php
				}
				else
				{
					?>
						<script>
							alert("Failed to Register User, Try Again!");
							window.location.href="registration.php";
						</script>
					<?php
				}
			}

			if($_POST['btnSubmit'] == "Login")
			{
				$username = $_POST['username'];
				$password = $_POST['password'];
				if(strlen($username) > 0 && strlen($password) > 0)
				{
					if(strlen($password) < 8)
					{

					}
					else
					{
						$query = "select id,username,password from users where username='$username' LIMIT 1";
						$res = mysqli_query($conn,$query);
						$cnt = mysqli_num_rows($res);
						if($cnt > 0)
						{
							$row = mysqli_fetch_assoc($res);
							if($row['password'] == $password)
							{
								echo "User Login Successful";
							}
							else
							{
								echo "Username/Password doesnot match";
							}
						}
						else{
							echo "User not Found, Kindly Register";
						}
						
					}
				}
			}		
		}
	}
?>