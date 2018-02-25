<?php

include('../database.php');
$conn = connect_db();

// fetch names of events with the specified category
for ($i = 0; $i < 30; $i++) {
    $hr = rand(0,23);
    $min1 = rand(0,5);
    $min2 = rand(0,8);
    $start = '' . $hr . ':' . $min1 . $min2;

    $hrEnd = $hr+1;
    $end1 = $min1+1;
    $end2 = $min2+1;
    $end = '' . $hrEnd . ':' . $end1 . $end2;

    $sql = "insert into Events (ename, hname, dow, tags, address, cost, description, url, date, startTime, endTime) values ('AAAename$i', 'host$i', 'M', 'kids', 'location$i', 10.00, 'desc$i', 'www.website$i.com', '2018-02-$i', '$start', '$end')";
    mysqli_query($conn, $sql);
}