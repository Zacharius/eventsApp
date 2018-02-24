<?php

function connect_db(){
	$_SESSION["foo"] = "success";
	$dbhost = "aa1mmfnt965pffo.ccuxndnykfbl.us-east-2.rds.amazonaws.com:3306";
	$dbuser = "zacharius";
	$dbpass = "CompSci2.0";
	$dbname = "viaSocial";

    $conn = mysqli_connect( $dbhost, $dbuser, $dbpass, $dbname);
    if (mysqli_connect_errno($conn)) {
        error_log("Failed to connect to MySQL: " . mysqli_connect_error());
        $_SESSION["foo"] = "fail";
    }

    return $conn;
}

function check_logged_in() {
    session_start();

    if (!isset($_SESSION['loggedin']) || !$_SESSION['loggedin']) {
    	$protocol = empty($_SERVER['HTTPS']) ? 'http://' : 'https://';
    	$target_url = $protocol . $_SERVER['HTTP_HOST'] . $_SERVER['REQUEST_URI'];
    	$redirect_url = 'index.php?target_url=' . rawurlencode($target_url);
        header('Location: ' . $redirect_url);
        die('You must be logged in. If you are not automatically redirected, please click <a href="' . $redirect_url . '">here</a>.');
    }
}
