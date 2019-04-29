<!DOCTYPE html>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.4/jquery.min.js"></script>
<html>
<body>

    <form id="carform">    
        <select name="carlist" form="carform">
            <option value="jeden">jeden</option>
            <option value="dwa">dwa</option>
            <option value="trzy">trzy</option>
        </select>
        <button type="submit">Submit</button>
    </form> 

    <form id="carform2">    
        <select name="carlist2" form="carform2">
            <option value="jeden2">jeden2</option>
            <option value="dwa2">dwa2</option>
            <option value="trzy2">trzy2</option>
        </select>
    </form> 

    <p id="text-output"></p>

    <script> 
        $('form[id=carform]').on('submit', function(event) 
        {
            event.preventDefault();
            var $input = $(this).find('select[name=carlist]');
            var input = $input.val();
            $('#text-output').text("You typed: " + input);
        });
    </script>
    
    </body>
</html>
