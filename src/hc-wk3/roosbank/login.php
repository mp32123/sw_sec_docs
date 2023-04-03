<?php
include "lib/security.php";

if (!isset($_SESSION['authenticated'])) {
    if (isset($_POST['user']) && isset($_POST['pass'])) {
        $login_failed = do_login($_POST['user'], $_POST['pass']);
    }
}
session_start();

include "templates/login.tpl.php";