
<!DOCTYPE HTML>  
<html>
<head>
<style>
.error {color: #FF0000;}
</style>
</head>
<body>  

<?php

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

<h2>Witamy w bazie lekarskiej bd-Gabinet!</h2>

<!-- ---------- formularze danych uzytkownika --------------- -->

<p><span class="error">* wymagane</span></p>
<form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">  

  E-mail: <input type="text" name="email" value="<?php echo $email;?>">
  <span class="error">* <?php echo $emailErr;?></span>
  <br><br>

  haslo: <input type="password" name="haslo" value="<?php echo $haslo;?>">
  <span class="error">* <?php echo $hasloErr;?></span>
  <br><br>

  uzytkownik:
  <input type="radio" name="usrType" <?php if (isset($usrType) && $usrType=="pacjenci") echo "checked";?> value="pacjenci">Pacjent
  <input type="radio" name="usrType" <?php if (isset($usrType) && $usrType=="lekarze") echo "checked";?> value="lekarze">Lekarz
  <span class="error">* <?php echo $usrTypeErr;?></span>
  <br><br>

  <input type="submit" name="submit" value="Zaloguj">  

</form>
<!-- --------------------------------------------------------- -->


<?php
// ------------------- requesty SQL ----------------------------- //
$json = array();
$requestPass = "SELECT * FROM $usrType WHERE adres_email='$email'"; // rekord pacjenta/lekarza szukany po email
if (isset($_POST['submit']))
{
  try { $bdd = new PDO('mysql:host=db4free.net;dbname=dbgabinet', 'root00', 'Mzyk9ftw'); } 
  catch (Exception $e) { exit('Unable to connect to database.'); }
  $result = $bdd->query($requestPass) or die(print_r($bdd->errorInfo()));

}
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
  header ('Location: fullcalendar-master/index.php?userID_string='.$userID_string); 
}
else
{
  echo "Błędny adres e-mail lub hasło!";
}

?>




