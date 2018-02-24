<!DOCTYPE html>
<html>
<body>

<p>Search for events tagged with the specified category</p>

These are all the categories currently in the database:
<?php
include('database.php');
$conn = connect_db();
$result = mysqli_query($conn, "SELECT DISTINCT tags FROM Events ORDER BY tags DESC");
echo "<ul id='current_cats'>";
while($row = mysqli_fetch_assoc($result)) {
    echo "<li>{$row['tags']}</li>";
}
echo "</ul>";
?>

<form action="/get-events-by-category.php" method="POST" onsubmit="myFunction(this)">
    Enter name: <input type="text" name="category">
    <input type="submit" value="Submit">
</form>

<p>Results:</p>
<ul id="event_results">
</ul>

<script>
    function myFunction(myForm) {
        $.ajax({ // create an AJAX call...
            data: $(myForm).serialize(), // get the form data
            type: 'post', // GET or POST
            url: $(myForm).attr('action'), // the file to call
            success: function(response) { // on success..
                var temp = JSON.parse(response);
                if (temp[0] === 'success') {
                    var results = JSON.parse(temp[1]);
                    for (var i = 0; i < results.length; i++) {
                        var ename = results[i]['ename'];
                        var desc = results[i]['description'];
                        $('#event_results').append("<li>"+ename+": " +desc+"</li>"); // update the DIV
                    }
                } else {
                    alert("failure");
                }
            }
        });
        return false; // cancel original event to prevent form submitting
    }
</script>

</body>
</html>
