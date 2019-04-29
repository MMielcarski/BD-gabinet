<?php

// List of events
$json = array();

// Query that retrieves events
$request = "SELECT * FROM events ORDER BY id";
        
// connection to the database
try {
    $bdd = new PDO('mysql:host=db4free.net;dbname=dbgabinet', 'root00', 'Mzyk9ftw');
} catch (Exception $e) {
    exit('Unable to connect to database.');
}
// Execute the query
$result = $bdd->query($request) or die(print_r($bdd->errorInfo()));

// sending the encoded result to success page
echo json_encode($result->fetchAll(PDO::FETCH_ASSOC));

?>
