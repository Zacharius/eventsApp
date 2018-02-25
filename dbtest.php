<?php
include('database.php');
$conn = connect_db();

echo $_SESSION["foo"];
echo "<br>";

$result = mysqli_query($conn, "SELECT * FROM Events");
echo "{$_SESSION["foo"]}";
echo "<ul>";
while($row = mysqli_fetch_assoc($result)) {
    echo "<li>{$row['ename']}</li>";
}
echo "</ul>";
