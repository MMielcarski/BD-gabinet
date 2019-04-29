
<?php

// ------------- pobieranie danych uzytkownika --------------- //

$usr_string=$_GET['userID_string'];     // zmienna ID uzytkownika pobierana ze strony logowania (string "symbol+ID")
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
else
{
    echo "User Type Error!<br>";
}

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

// ------------- pobieranie danych lekarzy --------------- //
$requestDoctorsList = "SELECT * FROM lekarze" ;  
$doctors_list_query = $bdd->query($requestDoctorsList) or die(print_r($bdd->errorInfo()));       
$doctors_list_array = $doctors_list_query->fetchAll(PDO::FETCH_ASSOC); 
// ------------- pobieranie danych lekarzy END --------------- //

?>

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

        editable: false,
        header: {
          left: 'prev,next today',
          center: 'title',
          right: 'month,agendaWeek,agendaDay'
        },
        
        events: "events.php",
        //events: <?php echo json_encode($event_data_raw); ?>, 

        // Convert the allDay from string to boolean
        eventRender: function (event, element, view) {
          if (event.allDay === 'true') {
            event.allDay = true;
          } else {
            event.allDay = false;
          }
        },
        selectable: false,
        selectHelper: false,
        select: function (start, end, allDay) {
          var title = prompt('Event Title:');
          var badanie = prompt('Badanie:');
          if (title) {
            var start = fmt(start);
            var end = fmt(end);
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

    body {
      margin-top: 40px;
      text-align: center;
      font-size: 14px;
      font-family: "Lucida Grande", Helvetica, Arial, Verdana, sans-serif;

    }
/*
    #calendar {
      width: 900px;
      margin: 0 auto;
    }*/

  </style>

<!--
<div id='calendar'></div>
  -->

<div style="background-color:lightblue">
  <h3>DB-Gabinet</h3>
  <p>Harmonogram wizyt</p>
</div> 

<style type="text/css">
* {margin: 0; padding: 0;}
#container {height: 100%; width:80%; font-size: 0; margin: auto;}
#left-menu, #calendar, #right-menu {display: inline-block; *display: inline; zoom: 1; vertical-align: top; font-size: 12px; }
#left-menu {width: 25%; background: blue;}
#calendar {width: 50%;}
#right-menu {width: 25%; background: yellow;}

#menuBlock {display: block; padding: 10pt; margin: 10px; background: red;}
</style>

<div id="container">
    <div id="left-menu"></div>
    <div id="calendar"></div>
    <div id="right-menu">
      <div id="menuBlock">
        <?php
        if($usrSymbol == 'P')
        {
          echo "Zalogowano jako Pacjent";
          echo "Identyfikator: ".$usrID."<br>";
        }
        else if($usrSymbol == 'L')
        {
          echo "Zalogowano jako Lekarz<br>";
          echo "ID: ".$usrID."<br>";
        }
        else echo "Bledny typ uzytkownika!";
        ?>
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

<head>
</head>
<body>

<script> 
  $('form[id=lista-lekarzy]').on('submit', function(event) 
  {
      event.preventDefault();
      var $input = $(this).find('select[name=lekarze]');
      var input = $input.val();
      $('#selected_doctor_id').text("ID lekarza: " + input);
      
  });
</script>

</body>
</html>
