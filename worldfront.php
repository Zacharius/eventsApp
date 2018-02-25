These are all the categories currently in the database:
<?php
include('database.php');
$conn = connect_db();

$sql = "SELECT * from Events WHERE YEAR(date) = 2018 AND MONTH(date) = 02";
$result = mysqli_query($conn, $sql);

echo json_encode($result);
/*echo "<ul id='current_cats'>";
while($row = mysqli_fetch_assoc($result)) {
    echo "<li>{$row['tags']}</li>";
}
echo "</ul>";*/
?>