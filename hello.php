<?php
$ret = array();
$ret[] = $_POST['foo'];
$ret[] = $_POST['bar'];
echo json_encode($ret);
