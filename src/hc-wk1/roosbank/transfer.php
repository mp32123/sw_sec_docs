<?php
include "lib/security.php";
check_login();

$result = false;
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $result = $_POST; // XSS vulnerability!
}
?>

<?php include "templates/transfer.tpl.php";