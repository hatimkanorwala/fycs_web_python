<html>
	<head><title>Login</title></head>
	<body>
		<h1>Registration</h1>
		<form onsubmit="return checkData()" method="POST" action="authentication.php">
		Enter Username:
		<input type="text" name="username" id="un" placeholder="Enter Username" required /><br>
		Enter Password:
		<input type="password" name="password" id="pass" placeholder="Enter Password" required /><br>
		Confirm Password:
		<input type="password" name="con_password" id="c_pass" placeholder="Confirm Password" required /><br>
		<input type="submit" name="btnSubmit" value="Register" />
		</form>
		<script>
			function checkData(){
				var username = document.getElementById("un").value;
				var password = document.getElementById("pass").value;
				var con_password = document.getElementById("c_pass").value;
				if(username == "")
					return false;
				else if(password == "")
					return false;
				else if(password.length < 8)
					return false;
				else if(con_password == "")
					return false;
				else if(con_password.length < 8)
					return false;
				else if(password != con_password)
					return false;
				else
					return true;
			}
		</script>
	</body>
</html>
