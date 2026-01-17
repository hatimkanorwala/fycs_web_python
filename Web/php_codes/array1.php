<?php
$var1 = ["Hatim","Kanorwala","Burhani","College"];
print_r($var1);
$len_var1 = count($var1);

for($i=0;$i<$len_var1;$i++)
{
	echo "<br />"."Index ". $i . " Value: ". $var1[$i];
}


//foreach loop -> used only for arrays
foreach($var1 as $key => $data){
	echo "<br />Key: ". $key. " Data: " . $data;
}

$cars = array(
	'Brand' => 'Tata',
	'Model' => 'Nexon',
	'Year' => 2021
);
echo "<br />";
print_r($cars);
echo "<br />".$cars['Brand'];
echo "<br />".$cars['Model'];
echo "<br />".$cars['Year'];

foreach($cars as $key => $data)
{
	echo "<br />$key as $data";
}

?>