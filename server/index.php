<?php 
include "config.php";
 ?>

 <!DOCTYPE html>
 <html lang="en">
 <head>
     <meta charset="UTF-8">
     <meta name="viewport" content="width=device-width, initial-scale=1.0">
     <title>Daftar Foto</title>
     <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa" crossorigin="anonymous"></script>
    
 </head>
 <body>
    <div class="container">
    <div class="text-center mt-5">
        <h1>Daftar Foto Deteksi Rokok</h1>
    </div>
    <div class="table-responsive mt-5 mb-3">
     <table class="table table-striped table-hover table-bordered">
         <thead align="center" class="bg-info">
             <tr>
                 <th>No</th>
                 <!-- <th>Comment</th> -->
                 <th>Timestamp</th>
                 <th>Foto</th>
             </tr>
         </thead>
<?php 
$query="SELECT * FROM log_data";
foreach($dbo->query($query) as $row){
 ?>
         <tbody>
             <tr>
             <td class="text-center" width="50"><?=$row['id']?></td>
             <!-- <td class="text-center"><?=$row['comment']?></td> -->
             <td class="text-center" width="100"><?=$row['timestamp']?></td>
             <td class="text-center" width="200"><?="<img width='300' class='rounded' src='data:image/jpeg;base64,".base64_encode($row['image'])."'/>"?></td>
         </tr>
         </tbody>
<?php 
    }
 ?>
     </table>
    </div>
</div>
<div class="footer text-center bg-light fixed-bottom">
    <footer class="m-2">&copy; 2022 | <b>Santri</b> Innovator 6</footer>
</div>
 </body>
 </html>