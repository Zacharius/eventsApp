<?php

include('../database.php');
$conn = connect_db();

$ret = array();
$id = $_POST['id'];

// data validation
if (empty($id)) { die("id is blank"); }

// fetch names of events with the specified category
$sql = "SELECT * from Events WHERE id = $id";
if($result = mysqli_query($conn, $sql)){
    $row = mysqli_fetch_assoc($result);
    //echo(json_encode($row));
}

//$file = file_get_contents('../route.php');
$file = include "../route.php";
/*$content = eval("?>$file");*/

$ret[] = $row;
$ret[] = $file;
echo json_encode($ret);
