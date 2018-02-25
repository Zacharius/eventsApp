<?php

include('../database.php');
$conn = connect_db();

$results = array();
$month = "02";//date("n",strtotime($_POST['month']));
$year = "2018";//$_POST['year'];


// data validation
if (empty($month)) { die("Month is blank."); }
if (empty($year)) { die("Year is blank."); }

// fetch names of events with the specified category
$sql = "SELECT * from Events WHERE YEAR(date) = $year AND MONTH(date) = $month";
if($result = mysqli_query($conn, $sql)){
    while($row = mysqli_fetch_assoc($result)){
        $results[] = json_encode($row);
    }
    echo(json_encode($results));
} else {
    die('failure');
}
