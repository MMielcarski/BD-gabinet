
<!DOCTYPE HTML>  
<link href='https://fonts.googleapis.com/css?family=Work Sans' rel='stylesheet'>
<html>

<style>
.error {color: #FF0000;}
body {
  font-family: 'Work Sans';
}
</style>


<body style="background-color:#4db6ac;">  

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

<style>
p {

}
#login {
  border-radius: 25px 0 0 25px;
  background-color: #00867d;
  margin: 10px;
  padding: 10px;
}
#formLogin{
  width: 15%;
  text-align: right;
}
</style>
<div id='login'>
  <h2>Witamy w bazie lekarskiej bd-Gabinet!</h2>

  <!-- ---------- formularze danych uzytkownika --------------- -->

  <p><span class="error">* wymagane</span></p>
  <div id='formLogin'>
    <form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">  

      E-mail: <input type="text" name="email" value="<?php echo $email;?>">
      <span class="error">* <?php echo $emailErr;?></span>
      <br><br>

      haslo: <input type="password" name="haslo" value="<?php echo $haslo;?>">
      <span class="error">* <?php echo $hasloErr;?></span>
      <br><br>

      <input type="radio" name="usrType" <?php if (isset($usrType) && $usrType=="pacjenci") echo "checked";?> value="pacjenci">Pacjent
      <input type="radio" name="usrType" <?php if (isset($usrType) && $usrType=="lekarze") echo "checked";?> value="lekarze">Lekarz
      <span class="error">* <?php echo $usrTypeErr;?></span>
      <br><br>

      <input type="submit" name="submit" value="Zaloguj">  

    </form>
  </div>
</div>
<!-- --------------------------------------------------------- -->


<?php
// ------------------- requesty SQL ----------------------------- //

//if (isset($_POST['submit']))

if(!$_GET['userID_string'])
{
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
  

  header ('Location: fullcalendar-master/index.php?userID_string='.$userID_string); 
}
else
{
  echo "Błędny adres e-mail lub hasło!";
}
}

?>

<head>
</head>

</html>

