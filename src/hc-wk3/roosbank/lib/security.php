<?php
function redirect($url) {
    ob_start();
    header('Location: ' . $url);
    ob_end_flush();
    exit();
}

function check_login() {
    if (!isset($_COOKIE['ManualAuthCookie']) || $_COOKIE['ManualAuthCookie'] != 'Authenticated') {
        redirect('login.php');
    }
}

function get_cookie_params($time_diff) {
    return array(
        'expires' => time() + $time_diff,
        'path' => '/',
        'domain' => $_SERVER['SERVER_NAME'],
        'secure' => true, // must be true in order for samesite:None to work
        'httponly' => true,
        'samesite' => 'None'
    );
}

function do_login($user, $pass) {
    if ($user == 'erik' && $pass == '1234') {
        $arr_cookie_options = get_cookie_params(60 * 60 * 24 * 30);
        setcookie('ManualAuthCookie', 'Authenticated', $arr_cookie_options);
        redirect('index.php');
    }
    return false;
}

function logout() {
    if (isset($_COOKIE['ManualAuthCookie']) && $_COOKIE['ManualAuthCookie'] == 'Authenticated') {
        $arr_cookie_options = get_cookie_params(-3600);
        setcookie('ManualAuthCookie', '', $arr_cookie_options);
        redirect('logout.php');
    }
}