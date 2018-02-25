These are all the categories currently in the database:
<?php
include('database.php');
$conn = connect_db();

$results = array();
$year = "2018";
$sql = "SELECT * from Events WHERE YEAR(date) = $year";
$result = mysqli_query($conn, $sql);
while($row = mysqli_fetch_assoc($result)){
    $results[] = $row;
}

echo json_encode($results[34]);
/*echo "<ul id='current_cats'>";
while($row = mysqli_fetch_assoc($result)) {
    echo "<li>{$row['tags']}</li>";
}
echo "</ul>";*/
?>