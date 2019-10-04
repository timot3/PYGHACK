<?php
  if (!empty($_FILES) && isset($_FILES['fileToUpload'])) {
      switch ($_FILES['fileToUpload']["error"]) {
          case UPLOAD_ERR_OK:
              $target = "/var/www/html/files/";
              $target = $target . basename('input.csv');

              if (move_uploaded_file($_FILES['fileToUpload']['tmp_name'], $target)) {
                  $status = "The file " . basename($_FILES['fileToUpload']['name']) . " has been uploaded";
              } else {
                  $status = "Sorry, there was a problem uploading your file.";
              }
              break;
      }

      echo "Status: {$status}<br/>\n";

      header('Location: http://23.99.220.51/run_script.php?success=true');
  }
?>
