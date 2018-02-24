<?php

include('database.php');
$conn = connect_db();

$results = array();
$category = json_decode($_POST['category'], true);

// data validation
if(empty($category)){
    die(json_encode(array('status' => 'failure')));
}

// fetch names of events with the specified category
$sql = "SELECT ename, description from Events WHERE tags LIKE '%$category%'";
if($result = mysqli_query($conn, $sql)){
    while($row = mysqli_fetch_assoc($result)){
        $results[] = $row;
    }
    echo(json_encode(array('success', json_encode($results))));
}
else{
    echo(json_encode(array('failure', json_encode($results))));
}
