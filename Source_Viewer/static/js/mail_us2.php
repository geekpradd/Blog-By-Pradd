<!Doctype html>
<html>
<head>
    <title>Programming Whiz</title>
    <!-- Add custom CSS here -->
    <link href="css/bootstrap.css" rel="stylesheet">
    <link href="css/modern-business.css" rel="stylesheet">
    <link href="css/font-awesome.css" rel="stylesheet">
    <link href="css/global_styles.css" rel="stylesheet">
    <link href="css/mail_us.css" rel="stylesheet">
    <script src="javascript/jquery-1.10.2.js"></script>
    <script src="javascript/bootstrap.js"></script>
    <script src="javascript/modern-business.js"></script>
</head>
<body style="padding-top:50px;">
    <?php require("helpers/header.php"); ?>
    <div class="container">
    <?php require("helpers/navigation.php"); ?>
        <div class="col-md-8 col-md-offset-1" style="position:relative;top:30px;left:-6a%;">
            <h1 >E-mail us</h1><hr>
            <ol class="breadcrumb" style="height:5%;">
                    <li><a href="index.php">Home</a>
                    </li>
                    <li class="active">Mail Us</li>
                </ol>
            <p class="text-justify">Mail Us with your queries and we will respond as soon as we can.</p>

            <form method="post" action="mail_us.php" id="mail-form">
            <input class="half-input-box" name="fname" type="text" placeholder="First Name" value =
            <?php
                if (isset($_POST['fname'])) {
                    echo $_POST['fname'];
                }
            ?> ></input>
            <input class="half-input-box" name="lname" type="text" placeholder="Last Name" value =
            <?php
                if (isset($_POST['lname'])) {
                    echo $_POST['lname'];
                }
            ?> ></input>
            <br />
            <input class="full-input-box" name="e_mail" type="text" placeholder="Your E-mail" value =
            <?php
                if (isset($_POST['e_mail'])) {
                    echo $_POST['e_mail'];
                }
            ?> ></input>
            <br />
            <textarea class="message-input" rows="9" cols="60" name="message" placeholder="Your Message"><?php if (isset($_POST['message'])) { echo $_POST['message']; } ?></textarea>
            <br />
            <input class="btn btn-default" id="send-button" type="submit" value="Send" />
            </form>
<?php
    function validate_form($parameter, $max_length, $match, $print_name) {
        if (strlen(trim($parameter)) > $max_length) {
            echo "<div class='error-box'>Make sure that your $print_name is less than $max_length characters</div>";
            return false;
        } else if (empty($parameter)) {
            echo "<div class='error-box'>Make sure that you entered your $print_name.</div>";
            return false;
        } else if (!$match) {
            echo "<div class='error-box'>Make sure that you entered a valid $print_name.</div>";
            return false;
        } else {
            return true;
        }
    }

    if (isset($_POST['fname']) && isset($_POST['lname']) && isset($_POST['e_mail']) && isset($_POST['message'])) {
        if (validate_form($_POST['fname'], 30, preg_match("/^[a-zA-Z ]*$/",$_POST['fname']), 'first name')) {
            $first_name = true;
        } else {
            exit();
        }

        if (validate_form($_POST['lname'], 30, preg_match("/^[a-zA-Z ]*$/",$_POST['lname']), 'last name')) {
            $last_name = true;
        } else {
            exit();
        }

        if (validate_form($_POST['e_mail'], 50, preg_match("/([\w\-]+\@[\w\-]+\.[\w\-]+)/", $_POST['e_mail']), 'email')) {
            $email = true;
        } else {
            exit();
        }

        if (empty($_POST['message'])) {
            echo "<div class='error-box'>Your message must not be empty</div>";
            exit();
        } else if (strlen($_POST['message']) > 5000) {
            echo "<div class='error-box'>Your message must not be greater than 5000 characters.</div>";
            exit();
        } else {
            $message = true;
        }

        if ($first_name && $last_name && $email && $message) {
            mail("programmingwhizz@gmail.com", "From: " . $_POST['fname'] . ' ' . $_POST['lname'], $_POST['message'], "From: " . $_POST['e_mail']);
            echo '<div class="error-box">You message was successfully sent.</div>';
        } else {
            echo '<div class="error-box">Sorry, something went wrong, please try again later.</div>';
        }
    }

    require('helpers/footer.php');
?>
            </div>
        </div>
    </body>
</html>
