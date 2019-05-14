
<style>
.error {color: #FF0000;}
body {
  font-family: 'Work Sans';
}
</style>

<?php

include 'header.php';

$hasloErr = $emailErr = $usrTypeErr = "";
$haslo = $email = $usrType =  "";

if ($_SERVER["REQUEST_METHOD"] == "POST") 
{
  // ------ poprawnosc wprowadzanych danych ---------- //
  if (empty($_POST["email"])) 
  {
    $emailErr = "Adres e-mail jest wymagany";
  } 
  else 
  {
    $email = test_input($_POST["email"]);
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) 
    {
      $emailErr = "Nieprawidłowy format adresu e-mail";
    }
  }

  if (empty($_POST["haslo"])) 
  {
    $hasloErr = "Hasło jest wymagane";
  } else 
  {
    $haslo = test_input($_POST["haslo"]);
  }

  if (empty($_POST["usrType"])) {
    $usrTypeErr = "Typ użytkownika jest wymagany";
  } else {
    $usrType = test_input($_POST["usrType"]);
  }

} // ------ ------------------------- ---------- //

function test_input($data) 
{
  $data = trim($data);
  $data = stripslashes($data);
  $data = htmlspecialchars($data);
  return $data;
}
?>

<div class="container">  
  <form id="contact" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>" method="post" >
    <h3>Witaj w serwisie!</h3>
    <h4>Zaloguj się:</h4>

    <fieldset>
      <input type="text" name="email" placeholder="e-mail" value="<?php echo $email;?>">
      <span class="error">* <?php echo $emailErr;?></span>
    </fieldset>

    <fieldset>
      <input type="password" placeholder="hasło" name="haslo" value="<?php echo $haslo;?>">
      <span class="error">* <?php echo $hasloErr;?></span>
    </fieldset>

    <fieldset>
      <input type="radio" name="usrType" <?php if (isset($usrType) && $usrType=="pacjenci") echo "checked";?> value="pacjenci">Pacjent
      <input type="radio" name="usrType" <?php if (isset($usrType) && $usrType=="lekarze") echo "checked";?> value="lekarze">Lekarz
      <span class="error">* <?php echo $usrTypeErr;?></span>
    </fieldset>

    <fieldset>
      <button name="submit" type="submit" id="contact-submit" data-submit="...Sending" onclick="passCheck()">Zaloguj</button>
    </fieldset>

  </form>
</div>

<style>
@import url(https://fonts.googleapis.com/css?family=Roboto:400,300,600,400italic);
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-font-smoothing: antialiased;
  -moz-font-smoothing: antialiased;
  -o-font-smoothing: antialiased;
  font-smoothing: antialiased;
  text-rendering: optimizeLegibility;
}

body {
  font-family: "Roboto", Helvetica, Arial, sans-serif;
  font-weight: 100;
  font-size: 12px;
  line-height: 30px;
  color: #777;
  background: #4CAF50;
}

.container {
  max-width: 400px;
  width: 100%;
  margin: 0 auto;
  position: relative;
}

#contact input[type="text"],
#contact input[type="email"],
#contact input[type="password"],
#contact input[type="tel"],
#contact input[type="url"],
#contact textarea,
#contact button[type="submit"] {
  font: 400 12px/16px "Roboto", Helvetica, Arial, sans-serif;
}

#contact {
  background: #F9F9F9;
  padding: 25px;
  margin: 150px 0;
  box-shadow: 0 0 20px 0 rgba(0, 0, 0, 0.2), 0 5px 5px 0 rgba(0, 0, 0, 0.24);
}

#contact h3 {
  display: block;
  font-size: 30px;
  font-weight: 300;
  margin-bottom: 10px;
}

#contact h4 {
  margin: 5px 0 15px;
  display: block;
  font-size: 13px;
  font-weight: 400;
}

fieldset {
  border: medium none !important;
  margin: 0 0 10px;
  min-width: 100%;
  padding: 0;
  width: 100%;
}

#contact input[type="text"],
#contact input[type="email"],
#contact input[type="tel"],
#contact input[type="url"],
#contact input[type="password"],
#contact textarea {
  width: 100%;
  border: 1px solid #ccc;
  background: #FFF;
  margin: 0 0 5px;
  padding: 10px;
}

#contact input[type="text"]:hover,
#contact input[type="email"]:hover,
#contact input[type="tel"]:hover,
#contact input[type="url"]:hover,
#contact input[type="password"],
#contact textarea:hover {
  -webkit-transition: border-color 0.3s ease-in-out;
  -moz-transition: border-color 0.3s ease-in-out;
  transition: border-color 0.3s ease-in-out;
  border: 1px solid #aaa;
}

#contact textarea {
  height: 100px;
  max-width: 100%;
  resize: none;
}

#contact button[type="submit"] {
  cursor: pointer;
  width: 100%;
  border: none;
  background: #4CAF50;
  color: #FFF;
  margin: 0 0 5px;
  padding: 10px;
  font-size: 15px;
}

#contact button[type="submit"]:hover {
  background: #43A047;
  -webkit-transition: background 0.3s ease-in-out;
  -moz-transition: background 0.3s ease-in-out;
  transition: background-color 0.3s ease-in-out;
}

#contact button[type="submit"]:active {
  box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.5);
}

.copyright {
  text-align: center;
}

#contact input:focus,
#contact textarea:focus {
  outline: 0;
  border: 1px solid #aaa;
}

::-webkit-input-placeholder {
  color: #888;
}

:-moz-placeholder {
  color: #888;
}

::-moz-placeholder {
  color: #888;
}

:-ms-input-placeholder {
  color: #888;
}
</style>

<body style="background-color:#4db6ac;">  

<?php

include 'header.php';

 // ------ ------------------------- ---------- //


?>

  <!-- ---------- formularze danych uzytkownika --------------- --> 
<!-- --------------------------------------------------------- -->

<?php
// ------------------- requesty SQL ----------------------------- //

if(!$_GET['userID_string'])
{
  echo "zaczynam połączenie<br>";

  $json = array();
  $requestPass = "SELECT * FROM $usrType WHERE adres_email='$email'"; // rekord pacjenta/lekarza szukany po email
  try { $bdd = new PDO('mysql:host=db4free.net;dbname=dbgabinet', 'root00', 'Mzyk9ftw'); } 
  catch (Exception $e) { exit('Unable to connect to database.'); }
  $result = $bd->query($requestPass) or die(print_r($bdd->errorInfo()));
  $userData = $result->fetch(PDO::FETCH_ASSOC); // tablica rekordu uzytkownika  

  if($haslo == $userData['haslo'] )
  {
        /* ----------------- event data from wizyty table ------------------------- */

    if($usrType == 'pacjenci')
    {
      $usrType_request = 'id_pacjenta';
      $usrID = $userData['ID_PACJENTA'];
      $usrSymbol = 'P';
    }
    else if($usrType == 'lekarze')
    {
      $usrType_request = 'id_lekarza';
      $usrID = $userData['ID_LEKARZA'];
      $usrSymbol = 'L';
    }
    /* ----------------- end ------------------------- */ 

      $userID_string = $usrSymbol.(string)$usrID;

      if($userData['PESEL'] == 0)     // first login case
      {
        header ('Location: first_login.php?userID_string='.$userID_string);
      }
      else
      {
        $cookie_name = "user";
        if(!isset($_COOKIE[$cookie_name])) {
            echo "Cookie named " . $cookie_name . " is not set!";
        
            $cookie_value = $userID_string;
            //setcookie($cookie_name, $cookie_value, time() + (86400 * 30), "/"); // 86400 = 1 day
            setcookie($cookie_name, $cookie_value, time() + (100), "/"); // 86400 = 1 day
          } else {
            echo "Cookie '" . $cookie_name . "' is set!<br>";
            echo "Value is: " . $_COOKIE[$cookie_name];
        }
        //echo "goging to calendar with string: ".$userID_string."<br>";
        header ('Location: fullcalendar-master/index.php?userID_string='.$userID_string); 
      }
  }
  else
  {
    echo "Błędny adres e-mail, hasło, lub rodzaj użytkownika!";
  }
}

?>

<head>
</head>

</html>

