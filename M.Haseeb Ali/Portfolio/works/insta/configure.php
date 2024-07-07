<?php
session_start();
$conn = mysqli_connect("localhost", "root", "", "scam");

if ($conn -> connect_errno) {
    echo
    "<script> alert('not connected') </script>";
    
  }
else{
}