<?php
$ret = array();
$ret['foo'] = $_POST['foo'] . '2';
$ret['bar'] = $_POST['bar'] . '2';
echo json_encode($ret);
