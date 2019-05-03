<?php

    try                     // laczenie z baza danych
    { 
        $bd = new PDO('mysql:host=db4free.net;dbname=dbgabinet', 'root00', 'Mzyk9ftw'); 
    }    
    catch (Exception $e)    // blad polaczenia z baza danych
    { 
        exit('Unable to connect to database.'); 
    }   

?>