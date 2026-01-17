<?php
if($_SERVER['REQUEST_METHOD'] == "POST")
{
	print_r($_POST);
	if(isset($_POST['btnSubmit']))
	{
		if($_POST['btnSubmit'] == "calculate")
		{
			$num1 = $_POST['num1'];
			$num2 = $_POST['num2'];
			$op = $_POST['op'];
			$result = 0;
			switch($op){
				case "Addition":
					$result = $num1 + $num2;
					break;
				case "Subtraction":
					$result = $num1 - $num2;
					break;
				case "Multiplication":
					$result = $num1 * $num2;
					break;
				case "Division":
					$result = $num1 / $num2;
					break;
				case "Modulus":
					$result = $num1 % $num2;
					break;
				default:
					echo "Please select proper operator";
			}
			echo "Result of $op is $result";
		}
	}
}

?>