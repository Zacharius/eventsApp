<?php

include('../database.php');
$conn = connect_db();

$results = array();
$month = date_parse($_POST['month']);
$year = $_POST['year'];

$results[] = $month;
echo json_encode($results);
// data validation
if (empty($month)) { die("Month is blank."); }
if (empty($year)) { die("Year is blank."); }

// fetch names of events with the specified category
$sql = "SELECT * from Events WHERE YEAR(date) = $year AND MONTH(date) = $month";
if($result = mysqli_query($conn, $sql)){
    while($row = mysqli_fetch_assoc($result)){
        $results[] = $row;
    }
    echo(json_encode($results));
}
