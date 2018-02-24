<?php

include('../database.php');
$conn = connect_db();

$results = array();
$category = $_POST['category'];

// data validation
if(empty($category)){
    die();
}

// fetch names of events with the specified category
$sql = "SELECT ename, description from Events WHERE tags LIKE '%$category%'";
if($result = mysqli_query($conn, $sql)){
    while($row = mysqli_fetch_assoc($result)){
        $results[] = $row;
    }
    echo(json_encode($results));
}