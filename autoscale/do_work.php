<html>
<head><title>CPU load example</title></head>
<body>
<br/><br/>
<?php
if ($_SERVER['REQUEST_METHOD'] == "POST")
{
    $num = $_POST["num"];
	for ($x = 0; $x <= $num * 5000000; $x++) 
	{
      $var = $num+1;
	}
} 
?>
<center>
<h2>Processing complete</h2>
</center>
</body>
</html>