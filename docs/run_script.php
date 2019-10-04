<?php
ini_set('set_time_limit', 300000);
	$dir = '/var/www/html/files';
	if(!file_exists($dir)) {
		mkdir($dir, 0744);
	}

  $command = escapeshellcmd('/usr/bin/python3 /var/www/html/test.py');
//	sleep(10);
$output = shell_exec($command);
echo "test";
  echo $output;
echo "test2";
	file_put_contents('/var/www/html/files/output.txt', $output);
 header('Location: http://23.99.220.51/displayUserGraph.html?success=true');
?>
