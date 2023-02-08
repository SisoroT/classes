<?php

function PrintDateTime()
{
    date_default_timezone_set('America/New_York');
    $date = date('F-d-Y h:i:s');
    print($date . "<br>");
}
