<?php

define('DB_NAME', 'rtaylor80');
define('DB_USER', 'rtaylor80');
define('DB_PASSWORD', 'rtaylor80');
define('DB_HOST', 'localhost');


// function to verify the user
function verifyUser($user, $pass)
{
    // Create connection
    $conn = mysqli_connect(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME);
    // Check connection
    if (!$conn) {
        die("Connection failed: " . mysqli_connect_error());
    }

    $sql = "SELECT * FROM user WHERE username = '$user' AND password = '$pass'";
    $result = mysqli_query($conn, $sql);

    if (mysqli_num_rows($result) > 0) {
        return true;
    } else {
        return false;
    }

    mysqli_close($conn);
}
?>

<form method="post">
    Username: <input type="text" name="user"><br>
    Password: <input type="text" name="pass"><br>
    <input type="submit" value="Submit">
</form>

<?php

$cookie_name = "login";

if (isset($_POST['user']) && isset($_POST['pass'])) {
    $user = $_POST['user'];
    $pass = $_POST['pass'];

    if (verifyUser($user, $pass)) {
        setcookie($cookie_name, $user, time() + (86400 * 30), "/");
        header("Location: week6.php");
    } else {
        setcookie($cookie_name, "", time() - 3600, "/");
        echo "<h3>Wrong username or password</h3>";
    }
}

?>
