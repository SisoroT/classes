<?php

require "printfunc.php";
require "function.php";

?>
<!DOCTYPE html>
<html>

<head>
    <title>Week 4 Assignment</title>
    <script src="./jquery/jquery-3.6.0.min.js"></script>
    <link rel="stylesheet" href="./foundation/css/foundation.css" />
    <script src="./foundation/js/vendor/foundation.js"></script>
    <link rel="stylesheet" href="style.css" />

    <script>
        $(document).ready(function() {
            $('#alert').on('click', callAlert)
            $('#change').on('click', callChange)

            function callAlert() {
                alert('Hello World!')
            }

            function callChange() {
                $('#body').html(
                    'Here is new text for the body! These words are never before seen!'
                )
            }
        })
    </script>
</head>

<body>
    <main>
        <div class="grid-x">
            <header class="cell small-12 medium-12 large-12 text-right">
                <button id="change" class="button nav">Change Info</button>
                <button id="alert" class="button nav">Hello</button>
            </header>
        </div>

        <div class="grid-x">
            <div id="sidebar" class="cell small-12 medium-4 large-4">
                <b>Lorem Ipsum</b> is simply dummy text of the printing and
                typesetting industry. Lorem Ipsum has been the industry's
                standard dummy text ever since the 1500s, when an unknown
                printer took a galley of type and scrambled it to make a
                type specimen book. It has survived not only five centuries,
                but also the leap into electronic typesetting, remaining
                essentially unchanged. It was popularised in the 1960s with
                the release of Letraset sheets containing Lorem Ipsum
                passages, and more recently with desktop publishing software
                like Aldus PageMaker including versions of Lorem Ipsum.
            </div>

            <div id="body" class="cell small-12 medium-8 large-8">
                <b><u>Today's date and time is:</u></b> <?php PrintDateTime(); ?>
            </div>
        </div>
    </main>

    <footer class="grid-x">
        <p id="footer-left">© 2023 Ryan Taylor, All Rights Reserved</p>
        <p id="footer-right">Design by Ryan Taylor</p>
    </footer>
</body>

</html>
