<?PHP

define('DB_NAME', 'rtaylor80');
define('DB_USER', 'rtaylor80');
define('DB_PASSWORD', 'rtaylor80');
define('DB_HOST', 'localhost');

$conn = mysqli_connect(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME);
// Check connection
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}

function deletePerson($id)
{
    global $conn;

    $del = "DELETE FROM People WHERE id = '$id' ";
    $result = $conn->query($del);
}

function insertPerson($firstname, $lastname, $telephone)
{
    global $conn;

    $insert = "INSERT INTO People (firstname, lastname, telephone_number) VALUES ('$firstname', '$lastname', '$telephone')";

    $result = $conn->query($insert);
}

function showPeople()
{
    global $conn;

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
}

$cmd = $_GET['cmd'];

if ($cmd == 'create') {
    $firstname = $_GET['firstname'];
    $lastname = $_GET['lastname'];
    $telephone = $_GET['telephone'];
    insertPerson($firstname, $lastname, $telephone);
} elseif ($cmd == 'delete') {
    $id = $_GET['id'];
    deletePerson($id);
}

print("<h2>Current Database</h2>");
showPeople();

mysqli_close($conn);
