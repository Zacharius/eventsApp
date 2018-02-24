<!DOCTYPE html>
<html>

<head>
    <script src="jquery-3.3.1.min.js"></script>
</head>

<script>
    $('#cat_form').submit(function(event) {
        event.preventDefault();
        alert('hi');
        var foo = document.getElementById('pass');
        $.post("./get-events-by-category.php",
            {
                category: foo
            },
            function(data, status) {
                //alert("Data: " + data + "\nStatus: " + status);
                alert(data);
        });
        /*$.ajax({ // create an AJAX call...
            data: $('#cat_form').serialize(), // get the form data
            type: 'POST', // GET or POST
            url: './get-events-by-category.php', // the file to call
            .done(function(data) {
                var temp = JSON.parse(response);
                if (temp[0] === 'success') {
                    var results = JSON.parse(temp[1]);
                    for (var i = 0; i < results.length; i++) {
                        var ename = results[i]['ename'];
                        var desc = results[i]['description'];
                        $('#event_results').append("<li>"+ename+": " +desc+"</li>"); // update the DIV
                    }
                    alert('success');
                } else {
                    alert("failure");
                }
            });
        });*/
        return false; // cancel original event to prevent form submitting
    });
</script>


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

<form id="cat_form" method="POST">
    Enter name: <input type="text" name="category" id="category">
    <input type="submit" value="Submit">
</form>

<p>Results:</p>
<ul id="event_results">
</ul>

</body>
</html>

