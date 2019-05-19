<?php
$cookie_name = "user";
$usr_string = $_COOKIE[$cookie_name];

$usr_string = $_GET['userID_string'];
$usrSymbol = $usr_string[0];            // odczytanie symbolu użytkownika 
$usrID = (int)substr($usr_string,1);    // odczytanie ID uzytkownika

echo "string: ".$usr_string."<br>";
?>

<div class="container">  
  <form id="contact" action="" method="post" onsubmit="return confirm('Utworzyć konto?');">
    <h3>Witaj w serwisie!</h3>
    <h4>Wypełnij swoje dane w celu dokończenia rejestracji:</h4>

    <hr><h4>Dane personalne:</h4>

    <fieldset>
      <input value="Adam" name="form_imie" placeholder="Imię" type="text" tabindex="1" required autofocus>
    </fieldset>

    <fieldset>
      <input value="Reda" name="form_nazwisko" placeholder="Nazwisko" type="text" tabindex="2" required autofocus>
    </fieldset>

    <fieldset>
    <label> Płeć </label>
        <input type="radio" tabindex="3" name="form_plec" <?php if (isset($usrType) && $usrType=="m") echo "checked";?> value="m">M
        <input type="radio" tabindex="4" name="form_plec" <?php if (isset($usrType) && $usrType=="k") echo "checked";?> value="k">K
    </fieldset>

    <label> Pesel </label>
    <fieldset>
      <input value="1231231" name="form_pesel" placeholder="Pesel" type="number" tabindex="5" required autofocus>
    </fieldset>

    <!--<fieldset>
      <input value="reda@gmail.com" name="form_email" placeholder="Adres e-mail" type="email" tabindex="6" required>
    </fieldset>-->

    <fieldset>
      <input value="123345567" name="form_tel" placeholder="Numer telefonu" type="tel" tabindex="7" required>
    </fieldset>

    <fieldset>
      <label>Data urodzenia</label>
      <input value="" name="form_urodziny" type="date" id="AddEventDate" name="eventDate" min="2018-01-01" tabindex="8" max="2020-12-31">
    </fieldset>

    <hr><h4>Adres:</h4>

    <fieldset>
      <input value="Gdańsk" name="form_miejscowosc" placeholder="Miejscowość" type="text" tabindex="9" required autofocus>
    </fieldset>

    <fieldset>
        <input value="34567" name="form_kod" placeholder="Kod pocztowy" type="text" name="country_code" pattern="[0-9]{2}\-[0-9]{3}" tabindex="10" title="Format xx-xxx">
    </fieldset>

    <fieldset>
      <input value="Rynnicza" name="form_ulica" placeholder="Ulica" type="text" tabindex="11" required autofocus>
    </fieldset>

    <fieldset>
      <input value="12" name="form_nrdomu" placeholder="Numer domu" type="number" tabindex="12" required autofocus>
    </fieldset>

    <fieldset>
      <input value="3" name="form_nrmieszkania" placeholder="Numer mieszkania" type="number" tabindex="13" required autofocus>
    </fieldset>

    <hr><h4>Ustaw nowe hasło:</h4>

    <fieldset>
      <input onkeyup='check();' id="password" value="admin1" id="test10" name="form_nowe_haslo" placeholder="Nowe hasło" type="password" tabindex="14" required autofocus>
    </fieldset>

    <fieldset>
      <input onkeyup='check();' id="confirm_password" value="admin1" name="form_powt_haslo" placeholder="Powtórz hasło" type="password" tabindex="15" required autofocus>
      <span id='message'></span>
    </fieldset>

    <fieldset>
      <button name="submit" type="submit" id="contact-submit" data-submit="...Sending" onclick="passCheck()">Submit</button>
    </fieldset>

  </form>
</div>


<script>

var check = function() 
{
  if (document.getElementById('password').value ==
    document.getElementById('confirm_password').value) {
    document.getElementById('message').style.color = 'green';
    document.getElementById('message').innerHTML = 'Hasła zgadzają się';
  } else {
    document.getElementById('message').style.color = 'red';
    document.getElementById('message').innerHTML = 'Hasła nie zgadzają się';
  }
}

</script>

<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") 
{
    echo "wprowadzono dane<br>";
    if($_REQUEST['form_nowe_haslo'] == $_REQUEST['form_powt_haslo'])
    {
        echo "password correct<br>";

        try { $bdd = new PDO('mysql:host=db4free.net;dbname=dbgabinet', 'root00', 'Mzyk9ftw'); }    // laczenie z baza danych
        catch (Exception $e) { exit('Unable to connect to database.'); }  
        //$sql = "UPDATE pacjenci SET PESEL=123 WHERE ID_PACJENTA=7"; // DZIALA
        //$sql = "INSERT INTO wizyty (ID_PACJENTA, data , cel_wizyty) VALUES (:usrID, :start, :title )";
        //$requestPass = "SELECT * FROM $usrType WHERE adres_email='$email'"; // rekord pacjenta/lekarza szukany po email

        //$sql = "UPDATE pacjenci SET PESEL=".$_REQUEST['form_pesel'] .", imie='".$_REQUEST['form_imie']."' WHERE ID_PACJENTA=".$usrID;
        $data = [
            'pesel' => $_REQUEST['form_pesel'],
            'imie' => $_REQUEST['form_imie'],
            'nazwisko' => $_REQUEST['form_nazwisko'],
            'id_pacjenta' => $usrID,
            'plec' => $_REQUEST['form_plec'],
            'urodziny' => $_REQUEST['form_urodziny'],
            'miejscowosc' => $_REQUEST['form_miejscowosc'],
            'kod' => $_REQUEST['form_kod'],
            'ulica' => $_REQUEST['form_ulica'],
            'nr_domu' => $_REQUEST['form_nrdomu'],
            'nr_mieszkania' => $_REQUEST['form_nrmieszkania'],
            'tel' => $_REQUEST['form_tel'],
            'haslo' => $_REQUEST['form_powt_haslo'],    
        ];

        $sql = "UPDATE pacjenci SET PESEL=:pesel, imie=:imie, nazwisko=:nazwisko, plec=:plec, data_urodzenia=:urodziny, miejscowosc=:miejscowosc, kod_pocztowy=:kod, ulica=:ulica, nr_domu=:nr_domu, nr_mieszkania=:nr_mieszkania, nr_tel=:tel, haslo=:haslo WHERE ID_PACJENTA=:id_pacjenta";
        echo "sgl: ".$sql."<br>";
        
        $bdd->prepare($sql)->execute($data);
        //$q = $bdd->prepare($sql);
        //$q->execute();
        
        header ('Location: index.php');
    }
    else
    {
        echo "password NOT correct<br>";
    }
    /*
    echo "user: ".$usrID."user type: ".$usrSymbol."<br>";
    echo "form_imie: ".$_REQUEST['form_imie']."<br>" ;
    echo "form_nazwisko: ".$_REQUEST['form_nazwisko']."<br>" ;
    echo "form_plec: ".$_REQUEST['form_plec']."<br>" ;
    echo "form_pesel: ".$_REQUEST['form_pesel']."<br>" ;
    echo "form_email: ".$_REQUEST['form_email']."<br>" ;
    echo "form_tel: ".$_REQUEST['form_tel']."<br>" ;
    echo "form_urodziny: ".$_REQUEST['form_urodziny']."<br>" ;
    echo "form_miejscowosc: ".$_REQUEST['form_miejscowosc']."<br>" ;
    echo "form_ulica: ".$_REQUEST['form_ulica']."<br>" ;
    echo "iform_nrdomumie: ".$_REQUEST['form_nrdomu']."<br>" ;
    echo "form_nrmieszkania: ".$_REQUEST['form_nrmieszkania']."<br>" ;
    echo "form_nowe_haslo: ".$_REQUEST['form_nowe_haslo']."<br>" ;
    echo "form_powt_haslo: ".$_REQUEST['form_powt_haslo']."<br>" ;*/
}
?>

<?php
echo "user: ".$usrID."user type: ".$usrSymbol."<br>";
echo "form_imie: ".$_REQUEST['form_imie']."<br>" ;
echo "form_nazwisko: ".$_REQUEST['form_nazwisko']."<br>" ;
echo "form_plec: ".$_REQUEST['form_plec']."<br>" ;
echo "form_pesel: ".$_REQUEST['form_pesel']."<br>" ;
echo "form_email: ".$_REQUEST['form_email']."<br>" ;
echo "form_tel: ".$_REQUEST['form_tel']."<br>" ;
echo "form_urodziny: ".$_REQUEST['form_urodziny']."<br>" ;
echo "form_plec: ".$_REQUEST['form_plec']."<br>" ;
echo "form_miejscowosc: ".$_REQUEST['form_miejscowosc']."<br>" ;
echo "form_ulica: ".$_REQUEST['form_ulica']."<br>" ;
echo "form_kod: ".$_REQUEST['form_kod']."<br>" ;
echo "iform_nrdomumie: ".$_REQUEST['form_nrdomu']."<br>" ;
echo "form_nrmieszkania: ".$_REQUEST['form_nrmieszkania']."<br>" ;
echo "form_nowe_haslo: ".$_REQUEST['form_nowe_haslo']."<br>" ;
echo "form_powt_haslo: ".$_REQUEST['form_powt_haslo']."<br>" ;
?>

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
  background: #4db6ac;
}

.container {
  max-width: 400px;
  width: 100%;
  margin: 0 auto;
  position: relative;
}

#contact input[type="text"],
#contact input[type="email"],
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