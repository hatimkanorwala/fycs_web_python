<?php
$num1 = 10;
$num2 = 20;
$op = 1;
$result = 0;
switch($op){
	case 1:
		$result = $num1 + $num2;	
		break;
	case 2:
		$result = $num1 - $num2;	
		break;	
	case 3:
		$result = $num1 * $num2;
		break;
	case 4:
		$result = $num1 / $num2;
		break;
	case 5:
		$result = $num1 % $num2;
		break;
	default:
		echo "Operator is not valid";
}
echo "<br />Result: ".$result;
?>