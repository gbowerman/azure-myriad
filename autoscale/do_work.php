<html>
  <head><title>CPU load example</title></head>
  <body>
    <br/><br/>
    <center>
    <h2><?php $hostname = gethostname(); ?> &nbsp;Doing work..</h2>
    <br/><br/>
    <?php
    set_time_limit(0);

    if ($_SERVER['REQUEST_METHOD'] == "POST")
    {
      $num = $_POST["num"];
	    for ($x = 0; $x <= $num * 5000000; $x++)
	    {
        $var = $num+1;
	    }
    }
    ?>
    <h2>Processing complete</h2>
    </center>
  </body>
</html>
