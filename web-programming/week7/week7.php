<!doctype html>
<html>

<head>
    <script src="./jquery/jquery-3.6.3.min.js"></script>
</head>

<body>

    <h2>Insert new Person</h2>
    <form onsubmit="return(insertPerson())">
        First Name: <input type="text" id="firstname"><br>

        Last Name: <input type="text" id="lastname"><br>

        Phone #: <input type="text" id="telephone"><br>
        <input type="submit" value="Submit">
    </form>

    <h2>Delete Person</h2>
    <form onsubmit="return(deletePerson())">
        ID: <input type="text" id="id"><br>
        <input type="submit" value="Submit">
    </form>

    <div id=showpeople></div>
    <script>
        function insertPerson() {
            firstname = $("#firstname").val();
            lastname = $("#lastname").val();
            telephone = $("#telephone").val();
            if (firstname == "" && lastname == "" && telephone == "") {
                alert("Please fill at least one of the fields");
                return (false);
            }
            $.get("./week7ajax.php", {
                "cmd": "create",
                "firstname": firstname,
                "lastname": lastname,
                "telephone": telephone,
            }, function(data) {
                $("#showpeople").html(data);
            });
            return (false);
        }

        function deletePerson(id) {
            id = $("#id").val();
            $.get("./week7ajax.php", {
                "cmd": "delete",
                "id": id
            }, function(data) {
                $("#showpeople").html(data);
            });
            return (false);
        }

        function showPeople() {
            $.get("./week7ajax.php", {
                "cmd": ""
            }, function(data) {
                $("#showpeople").html(data);
            });
            return (false);
        }
        showPeople();
    </script>

    <body>

</html>
