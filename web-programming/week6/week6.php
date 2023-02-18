<?PHP

if (!isset($_COOKIE['login'])) {
    header("Location: week6Login.php");
} else {
    echo "Currently logged in as: {$_COOKIE['login']}<br>";
}


define('DB_NAME', 'rtaylor80');
define('DB_USER', 'rtaylor80');
define('DB_PASSWORD', 'rtaylor80');
define('DB_HOST', 'localhost');

function deletePerson($id)
{

    $conn = mysqli_connect(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME);
    // Check connection
    if (!$conn) {
        die("Connection failed: " . mysqli_connect_error());
    }

    $del = "DELETE FROM People WHERE id = '$id' ";

    $result = $conn->query($del);

    mysqli_close($conn);
}

function insertPerson($firstname, $lastname, $telephone)
{

    $conn = mysqli_connect(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME);
    // Check connection
    if (!$conn) {
        die("Connection failed: " . mysqli_connect_error());
    }

    $insert = "INSERT INTO People (firstname, lastname, telephone_number) VALUES ('$firstname', '$lastname', '$telephone')";

    $result = $conn->query($insert);

    mysqli_close($conn);
}



function showPeople()
{
    // Create connection
    $conn = mysqli_connect(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME);
    // Check connection
    if (!$conn) {
        die("Connection failed: " . mysqli_connect_error());
    }

    $sql = "SELECT * FROM People";
    $result = mysqli_query($conn, $sql);

    if (mysqli_num_rows($result) > 0) {
        // output data of each row
        while ($row = mysqli_fetch_assoc($result)) {
            echo "<u><b>" . "id: " . $row["id"] . "</b></u>" . "<br>First Name: " . $row["firstname"] . "<br>Last Name: " . $row["lastname"] . "<br>Telephone #: " . $row["telephone_number"] . "<br><br>";
        }
    } else {
        echo "0 results";
    }

    mysqli_close($conn);
}

?>

<h2>Insert new Person</h2>
<form method="post">
    First Name: <input type="text" name="firstname"><br>

    Last Name: <input type="text" name="lastname"><br>

    Phone #: <input type="text" name="telephone"><br>
    <input type="submit" value="Submit">
</form>

<h2>Delete Person</h2>
<form method="get">
    ID: <input type="text" name="id"><br>
    <input type="submit" value="Submit">
</form>

<?php

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $firstname = $_POST['firstname'];
    $lastname = $_POST['lastname'];
    $telephone = $_POST['telephone'];
    insertPerson($firstname, $lastname, $telephone);
}

if ($_GET['id'] != '') {
    $id = $_GET['id'];
    deletePerson($id);
}

print("<h2>Current Database</h2>");
showPeople();
?>
