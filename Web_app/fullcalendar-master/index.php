
<?php
// Mickiewiczkasia@gmail.com
// kasia

// marek_psychiatra@re.com
// admin1

// ------------- pobieranie danych uzytkownika --------------- //

//$usr_string=$_GET['userID_string'];     // zmienna ID uzytkownika pobierana ze strony logowania (string "symbol+ID")
$cookie_name = "user";
$usr_string = $_COOKIE[$cookie_name];

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
  $tmp = array(
    "id" => $events_array[$i]['ID_WIZYTY'], 
    "title" => $events_array[$i]['wywiad'], 
    "start" => $events_array[$i]['data'], 
    "end" => $events_array[$i]['data']);
  array_push($event_data_raw,$tmp);
}
// ------------- pobieranie danych uzytkownika END --------------- //

// ------------- pobieranie wizyt wybranego lekarza -------------- //

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
    $tmp_sel = array(
      "id" => $events_array_sel[$i]['ID_WIZYTY'], 
      //"title" => "wizyta lekarza: ".$doctors_list_array[$k]['nazwisko'], 
      "title" => "",
      "start" => $events_array_sel[$i]['data'], 
      "end" => $events_array_sel[$i]['data'],
      "color" => 'purple');
    array_push($event_data_raw,$tmp_sel);
  }
}
// ------------- pobieranie wizyt wybranego lekarza END -------------- //


// ------------- pobieranie danych lekarzy --------------- //
$requestDoctorsList = "SELECT * FROM lekarze" ;  
$doctors_list_query = $bdd->query($requestDoctorsList) or die(print_r($bdd->errorInfo()));       
$doctors_list_array = $doctors_list_query->fetchAll(PDO::FETCH_ASSOC); 
// ------------- pobieranie danych lekarzy END --------------- //

?>
<!-- ----------- Kalendarz  ----------------->

<!DOCTYPE html>
<html>

  <meta charset="UTF-8">
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>

  <link href='./lib/fullcalendar.min.css' rel='stylesheet'/>
  <link href='./lib/fullcalendar.min-custom.css' rel='stylesheet'/>
  <link href='./lib/fullcalendar.print.css' rel='stylesheet' media='print'/>
  <script src='./lib/jquery.min.js'></script>
  <script src='./lib/moment.min.js'></script>
  <script src='./lib/jquery-ui.custom.min.js'></script>
  <script src='./lib/fullcalendar.min.js'></script>
  <script>

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
      selectConstraint:'businessHours',

        editable: false,
        header: {
          left: 'prev,next today',
          center: 'title',
          right: 'month,agendaWeek,agendaDay'
        },
        
        //events: "events.php",
        events: <?php echo json_encode($event_data_raw); ?>, 

        // Convert the allDay from string to boolean
        eventRender: function (event, element, view) {
          if (event.allDay === 'true') {
            event.allDay = true;
          } else {
            event.allDay = false;
          }
        },
        selectable: true,                       // dodawanie eventow w kalendarzu 
        selectHelper: true,
        select: function (start, end, allDay) {
          var title = confirm('Dodać nową wizytę?');
          if (title) {
            var start = fmt(start);
            var end = fmt(end);
            
            document.getElementById("AddEventDate").value = start.substr(0,start.length - 6);
            document.getElementById("AddEventTime").value = start.substr(11,start.length);

            $.ajax({
              url: 'add_events.php',
              data: 'title=' + title + '&start=' + start + '&end=' + end,
              type: "POST",
              success: function (json) {
                //alert('Added Successfully');
              }
            });
            calendar.fullCalendar('renderEvent',
                {
                  title: title,
                  start: start,
                  end: end,
                  allDay: allDay
                },
                true // make the event "stick"
            );
          }
          calendar.fullCalendar('unselect');
        },

        editable: false,
        eventDrop: function (event, delta) {
          var start = fmt(event.start);
          var end = fmt(event.end);
          $.ajax({
            url: 'update_events.php',
            data: 'title=' + event.title + '&start=' + start + '&end=' + end + '&id=' + event.id,
            type: "POST",
            success: function (json) {
              //alert("Updated Successfully");
            }
          });
        },
        eventClick: function (event) {
          var decision = confirm("Do you want to remove event?");
          if (decision) {
            $.ajax({
              type: "POST",
              url: "delete_event.php",
              data: "&id=" + event.id,
              success: function (json) {
                $('#calendar').fullCalendar('removeEvents', event.id);
                //alert("Updated Successfully");
              }
            });


          }

        },
        eventResize: function (event) {
          var start = fmt(event.start);
          var end = fmt(event.end);
          $.ajax({
            url: 'update_events.php',
            data: 'title=' + event.title + '&start=' + start + '&end=' + end + '&id=' + event.id,
            type: "POST",
            success: function (json) {
              alert("Updated Successfully");
            }
          });

        }

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
#container {height: 100%; width:80%; font-size: 0; margin: auto;}
#left-menu, #calendar, #right-menu {display: inline-block; *display: inline; zoom: 1; vertical-align: top; font-size: 12px; background: #81e8dd; border-radius: 5px;}
#left-menu {width: 25%; }
#calendar {width: 50%;background-color: white;}
#right-menu {width: 25%; }

#menuBlock {display: block; padding: 10pt; margin: 10px; background: #00857c;border-radius: 25px;}
</style>

<div id="container">
  <!-- -------------------------- left menu -------------------------- -->
    <div id="left-menu">
      <div id="menuBlock">
      <p>Wypełnij formularz wizyty:</p><br>
      
      <form>
        <label for="AddEventDate">Data wizyty:</label>
        <input type="date" id="AddEventDate" name="trip-start"
        value="2018-07-22"
        min="2018-01-01" max="2020-12-31"><br><br>

        <label for="AddEventTime">Godzina wizyty:</label>
        <input type="time" id="AddEventTime" name="eta"> <br>
      
        <br>Cel wizyty:<br>
        <input type="text" name="firstname" id="test1"><br><br>
        
        <button type="submit">todo_Zarejestruj wizytę</button>
      </form>

      </div>
    </div>
  <!-- -------------------------- calendar -------------------------- -->
    <div id="calendar"></div>
  <!-- -------------------------- right menu -------------------------- -->
    <div id="right-menu"> 
      <div id="menuBlock">
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

        <form action="../index.php">
        <input type="submit" value="Wyloguj">
        </form>

        <form action="../pass_change.php">
        <input type="submit" value="todo_Zmień hasło">
        </form>

      </div>

      <div id="menuBlock">
      <p>Wybierz lekarza:</p><br>

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

<head>  <!-- reklama CBA -->
</head>

<body style="background-color:#d8e5ff;">



<script>
  $('#selected_doctor_id').text("ID lekarza: " + "<?php echo $DocID; ?>");
</script>

</body>

<!-- ----------- Uklad glowny strony  END ----------------->

</html>
