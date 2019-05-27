
<meta charset="UTF-8">
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>

<link href='./lib/fullcalendar.min.css' rel='stylesheet'/>
<link href='./lib/fullcalendar.min-custom.css' rel='stylesheet'/>
<link href='./lib/fullcalendar.print.css' rel='stylesheet' media='print'/>
<script src='./lib/jquery.min.js'></script>
<script src='./lib/moment.min.js'></script>
<script src='./lib/jquery-ui.custom.min.js'></script>
<script src='./lib/fullcalendar.min.js'></script>
<link rel="stylesheet" href="styles.css">

<?php
// Mickiewiczkasia@gmail.com
// admin1

// marek_psychiatra@re.com
// admin1

// ------------- SELECT danych uzytkownika --------------- //

//$usr_string=$_GET['userID_string'];     // zmienna ID uzytkownika pobierana ze strony logowania (string "symbol+ID")
$cookie_name_login = "user";
$usr_string = $_COOKIE[$cookie_name_login];
//echo "usr:".$usr_string."<br>";

$usrSymbol = $usr_string[0];            // odczytanie symbolu użytkownika 
$usrID = (int)substr($usr_string,1);    // odczytanie ID uzytkownika

try { $bdd = new PDO('mysql:host=db4free.net;dbname=dbgabinet', 'root00', 'Mzyk9ftw'); }    // laczenie z baza danych
catch (Exception $e) { exit('Unable to connect to database.'); }                            // blad polaczenia z baza danych

$events_array =[];
if($usrSymbol == 'P')       // uzytkownik: pacjent
{
  $requestEvents = "SELECT * FROM wizyty WHERE id_pacjenta=$usrID";                     // zapytanie o rekordy wizyt pacjenta
  $events_query = $bdd->query($requestEvents) or die(print_r($bdd->errorInfo()));       // odebrane rekordy wizyt uzytkownika
  $events_array = $events_query->fetchAll(PDO::FETCH_ASSOC);                            // rekordy wizyt (array)
}
else if($usrSymbol == 'L')  // uzytkownik: lekarz
{
  $requestPatientsID = "SELECT id_pacjenta FROM pacjenci_lekarza WHERE id_lekarza=$usrID";  // zapytanie o ID pacjentow lekarza
  $patients_id_query = $bdd->query($requestPatientsID) or die(print_r($bdd->errorInfo()));
  $patients_id_array = $patients_id_query->fetchAll(PDO::FETCH_ASSOC);

  for($j=0; $j < count($patients_id_array); $j++ )
  {
    $tmp_ID = $patients_id_array[$j]['id_pacjenta'];

    $tmp_requestEvents = "SELECT * FROM wizyty WHERE id_pacjenta=$tmp_ID";                     
    $tmp_events_query = $bdd->query($tmp_requestEvents) or die(print_r($bdd->errorInfo()));       
    $tmp_events_array = $tmp_events_query->fetch(PDO::FETCH_ASSOC); 

    array_push($events_array,$tmp_events_array);
  }
}
else  echo "User Type Error!<br>";

$event_data_raw = array();
for ($i = 0; $i < count($events_array); $i++)   // tworzy tablice z eventami w standardzie fullCalendar
{
  $datetimeP = new DateTime($events_array[$i]['data']);
  $datetimeP->modify('+1 hour');

  if($events_array[$i]['czy_zatwierdzona'] == 1)
  {
    $tmp = array(
      "id" => $events_array[$i]['ID_WIZYTY'], 
      "title" => $events_array[$i]['cel_wizyty'], 
      "start" => $events_array[$i]['data'], 
      "end" => $datetimeP->format('Y-m-d H:i:s'),
      "backgroundColor" => "green");
    array_push($event_data_raw,$tmp);
  }
  else
  {
    $tmp = array(
      "id" => $events_array[$i]['ID_WIZYTY'], 
      "title" => $events_array[$i]['cel_wizyty'], 
      "start" => $events_array[$i]['data'], 
      "end" => $datetimeP->format('Y-m-d H:i:s'),
      "backgroundColor" => "red");
    array_push($event_data_raw,$tmp);
  }
  


}
// ------------- SELECT danych uzytkownika END --------------- //

// ------------- SELECT wizyt wybranego lekarza -------------- //

if($_GET['lekarze'])  // jezeli wybrany lekarz (w url)
{
  $DocID = $_GET['lekarze'];

  $requestPatientsID_sel = "SELECT id_pacjenta FROM pacjenci_lekarza WHERE id_lekarza=$DocID";  // zapytanie o ID pacjentow lekarza
  $patients_id_query_sel = $bdd->query($requestPatientsID_sel) or die(print_r($bdd->errorInfo()));
  $patients_id_array_sel = $patients_id_query_sel->fetchAll(PDO::FETCH_ASSOC);

  $events_array_sel=[];
  for($j=0; $j < count($patients_id_array_sel); $j++ )
  {
    $tmp_ID_sel = $patients_id_array_sel[$j]['id_pacjenta'];

    $tmp_requestEvents_sel = "SELECT * FROM wizyty WHERE id_pacjenta=$tmp_ID_sel";                     
    $tmp_events_query_sel = $bdd->query($tmp_requestEvents_sel) or die(print_r($bdd->errorInfo()));       
    $tmp_events_array_sel = $tmp_events_query_sel->fetch(PDO::FETCH_ASSOC); 

    array_push($events_array_sel,$tmp_events_array_sel);
  }

  for ($i = 0; $i < count($events_array_sel); $i++)   // tworzy tablice z eventami w standardzie fullCalendar
  {
    $datetimeL = new DateTime($events_array_sel[$i]['data']);
    $datetimeL->modify('+1 hour');

    $tmp_sel = array(
      "id" => $events_array_sel[$i]['ID_WIZYTY'], 
      //"title" => "wizyta lekarza: ".$doctors_list_array[$k]['nazwisko'], 
      "title" => $events_array_sel[$i]['cel_wizyty'],
      "start" => $events_array_sel[$i]['data'], 
      //"end" => $events_array_sel[$i]['data'],
      "end" => $datetimeL->format('Y-m-d H:i:s'),
      "color" => 'purple');
    array_push($event_data_raw,$tmp_sel);
  }
}
// ------------- SELECT wizyt wybranego lekarza END -------------- //


// ------------- SELECT danych lekarzy --------------- //
$requestDoctorsList = "SELECT * FROM lekarze" ;  
$doctors_list_query = $bdd->query($requestDoctorsList) or die(print_r($bdd->errorInfo()));       
$doctors_list_array = $doctors_list_query->fetchAll(PDO::FETCH_ASSOC); 
// ------------- SELECT danych lekarzy END --------------- //


// ------------- INSERT request wizyty --------------- //

if($_GET['eventDate'])  // jezeli wybrany lekarz (w url)
{

  $title = $_GET['eventCel'];
  $start_date = $_GET['eventDate'];
  $start_time = $_GET['eventTime'];

  $cookie_name = "insert_event_anti_repeat";
  echo $title.$start_date.$start_time.$usrID. "<br>";

  //if(!isset($_COOKIE[$cookie_name]) && $title.$start_date.$start_time.$usrID != $_COOKIE[$cookie_name]) 
  if($title.$start_date.$start_time.$usrID != $_COOKIE[$cookie_name])
  {
    echo "Cookie named " . $cookie_name . " is not set!";

    $cookie_value = $title.$start_date.$start_time.$usrID;
    //setcookie($cookie_name, $cookie_value, time() + (86400 * 30), "/"); // 86400 = 1 day
    setcookie($cookie_name, $cookie_value, time() + (100), "/"); // 86400 = 1 day


  
    $start = $start_date." ".$start_time;
    $datetimetmp = new DateTime();
    $datetimetmp = date_create_from_format('Y-m-d H:i:s', $start_date." ".$start_time.":00");
    $datetimetmp->modify('+1 hour');
    $end = $datetimetmp->format('Y-m-d H:i:s');
  
    $sql = "INSERT INTO wizyty (ID_PACJENTA, data , cel_wizyty) VALUES (:usrID, :start, :title )";
    $q = $bdd->prepare($sql);
    $q->execute(array(':usrID' => $usrID, ':start' => $start, ':title' => $title));

    header("Refresh:0");    // refresh page to load new new events
  } 
  else 
  {
    echo "same values!<br>";
    //echo "Cookie '" . $cookie_name . "' is set!<br>";
    //echo "Value is: " . $_COOKIE[$cookie_name];
  }
}
// ------------- INSERT request wizyty END --------------- //



?>

<!-- ----------- Kalendarz  ----------------->

<!--
<input type="text" id="test2" name="bla" >
<script>
document.getElementById("test2").value = "445";
document.getElementById("test2").value = end;
</script> -->


  <script type="text/javascript">

    $(document).ready(function () {
      function fmt(date) {
        return date.format("YYYY-MM-DD HH:mm");

      }

      var date = new Date();
      var d = date.getDate();
      var m = date.getMonth();
      var y = date.getFullYear();

      var calendar = $('#calendar').fullCalendar({

        businessHours: {        // days of week. an array of zero-based day of week integers (0=Sunday)      
        dow: [ 1, 2, 3, 4 ],    // Monday - Thursday

        start: '10:00',         // a start time (10am in this example)
        end: '18:00',           // an end time (6pm in this example)
      }, 
      // ----------------- OPTIONS ------------------- //
      selectConstraint:'businessHours',
      editable: false,
      events: <?php echo json_encode($event_data_raw); ?>,
      selectable: true,                        
      selectHelper: true,
      defaultView: 'month',
      eventOverlap: false,
      selectOverlap: false,
      slotEventOverlap: false,
      eventDurationEditable : false,
      eventStartEditable: false,      // not working
      // ----------------- OPTIONS END ------------------- //

        header: {
          left: 'prev,next today',
          center: 'title',
          right: 'month,agendaWeek,agendaDay'
        },
      
        // Convert the allDay from string to boolean
        eventRender: function (event, element, view) {
          if (event.allDay === 'true') {
            event.allDay = true;
          } else {
            event.allDay = false;
          }
        },

        select: function (start, end, allDay) {               // add new event

            var title = confirm('Dodać nową wizytę?');
            if (title) {
              title = "nowa wizyta";
              var start = fmt(start);
              var end = new Date(start);
              end.setHours( end.getHours() + 1 );

              document.getElementById("menuBlock2").style.display = "block"
              document.getElementById("AddEventDate").value = start.substr(0,start.length - 6);
              document.getElementById("AddEventTime").value = start.substr(11,start.length);

              calendar.fullCalendar('renderEvent',
                  {
                    title: title,
                    start: start,
                    end: end,
                    allDay: false,
                    backgroundColor: 'orange'},
                  true // make the event "stick"
              );
            }
            calendar.fullCalendar('unselect');
        },

        /*eventDrop: function (event, delta) {
          var start = fmt(event.start);
          var end = fmt(event.end);
        },*/
        /*eventClick: function (event) {
          var decision = confirm("Do you want to remove event?");
          if (decision) {
          }

        },*/
        /*eventResize: function (event) {
          var start = fmt(event.start);
          var end = fmt(event.end);
        },*/

// ------------------- CUSTOM ---------------------- //

        dayClick: function(date, jsEvent, view) {
          $('#calendar').fullCalendar('changeView', 'agendaDay');
          $("#calendar").fullCalendar('gotoDate', date.format());
        },

        eventClick: function(event) {
          $('#calendar').fullCalendar('changeView', 'agendaDay');
          $("#calendar").fullCalendar('gotoDate', event.start.format());
        }
// ------------------- CUSTOM END---------------------- //

      });

    });

  </script>
  <style>
    body 
    {
      margin-top: 40px;
      text-align: center;
      font-size: 14px;
      font-family: "Lucida Grande", Helvetica, Arial, Verdana, sans-serif;
    }
  </style>
<!-- ----------- Kalendarz  END ----------------->

<!-- ----------- Uklad glowny strony  ----------------->
<div style="background-color:lightblue">
  <h3>DB-Gabinet</h3>
  <p>Harmonogram wizyt</p>
</div> 

<style type="text/css">
* {margin: 0; padding: 0;}
#container {height: 80%; width:100%; font-size: 0; margin: auto; }
#left-menu, #calendar, #right-menu {box-shadow: 0 0 20px 0 rgba(0, 0, 0, 0.2), 0 5px 5px 0 rgba(0, 0, 0, 0.24); margin: 10px; display: inline-block; *display: inline; zoom: 1; vertical-align: top; font-size: 12px; background: #4db6ac;; border-radius: 5px;}
#left-menu {width: 25%; }
#calendar {width: 40%;background-color: white;}
#right-menu {width: 25%; }

#menuBlock {box-shadow: 0 0 20px 0 rgba(0, 0, 0, 0.2), 0 5px 5px 0 rgba(0, 0, 0, 0.24); display: block; padding: 10pt; margin: 10px; background: #F9F9F9; border-radius: 3px;}
#menuBlock2 {box-shadow: 0 0 20px 0 rgba(0, 0, 0, 0.2), 0 5px 5px 0 rgba(0, 0, 0, 0.24); display: block; padding: 10pt; margin: 10px; background: #F9F9F9; border-radius: 3px; display: none}
</style>

<div id="container">
  <!-- -------------------------- left menu -------------------------- -->
    <div id="left-menu">
      <div id="menuBlock2">
      <p><b>Wypełnij formularz wizyty:</b></p><br>
      
      <form id="add_new_event">
        <label for="AddEventDate">Data wizyty:</label>
        <input type="date" id="AddEventDate" name="eventDate"
        value="2018-07-22"
        min="2018-01-01" max="2020-12-31"><br><br>

        <label for="AddEventTime">Godzina wizyty:</label>
        <input type="time" id="AddEventTime" name="eventTime"> <br>
      
        <br>Cel wizyty:<br>
        <input type="text" id="AddEventCel" name="eventCel" id="test1"><br><br>
        
        <button type="submit">Zarejestruj wizytę</button>
      </form>

      </div>
    </div>
  <!-- -------------------------- calendar -------------------------- -->
    <div id="calendar"></div>
  <!-- -------------------------- right menu -------------------------- -->
    <div id="right-menu" class="container"> 
      <div id="menuBlock">
        <b>
        <?php
        if($usrSymbol == 'P')
        {
          echo "Zalogowano jako Pacjent<br>";
          echo "ID: ".$usrID."<br>";
        }
        else if($usrSymbol == 'L')
        {
          echo "Zalogowano jako Lekarz<br>";
          echo "ID: ".$usrID."<br>";
        }
        else echo "Bledny typ uzytkownika!";
        ?>
        </b>

        <form action="../index.php"> 
        <input type="submit" value="Wyloguj">
        </form>

        <form action="../pass_change.php">
        <input type="submit" value="todo_Zmień hasło">
        </form>

      </div>

      <div id="menuBlock">
      <p><b>Wybierz lekarza:</b></p><br>

        <form id="lista-lekarzy">

          <select name="lekarze" form="lista-lekarzy">
            <?php for($k=0; $k < count($doctors_list_array); $k++) { ?>
              <option value="<?php echo $doctors_list_array[$k]['ID_LEKARZA']; ?>"> <?php echo $doctors_list_array[$k]['tytul']." ". $doctors_list_array[$k]['nazwisko']; ?> </option>
            <?php } ?>
          </select> 

          <div id="select_doctor_button">
          <button type="submit">Pokaż terminarz</button>
          </div>

        </form><br>

        <p id="selected_doctor_id"></p>

      </div>
    </div>
</div>




<script>
  $('#selected_doctor_id').text("ID lekarza: " + "<?php echo $DocID; ?>");
</script>

<body style="background-color:#4db6ac;">
</body>
<!-- ----------- Uklad glowny strony  END ----------------->
<!DOCTYPE html>
<html>
</html>

<head>  <!-- reklama CBA -->
</head>