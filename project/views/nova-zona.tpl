<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="Bottle web project template">
    <meta name="author" content="datamate">
     
    <title>UPI - Busevi</title>
    <link rel="stylesheet" type="text/css" href="/static/bootstrap.min.css">
    <link rel="stylesheet" type="text/css" href="/static/custom.css">
    <link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.11.2/css/all.min.css">
    
    <script type="text/javascript" src="/static/jquery.js"></script>
	<script type="text/javascript" src="/static/assets/js/custom.js"></script>
    <script type="text/javascript" src="/static/bootstrap.min.js"></script> 
</head>
<body>

	
	  <!-- Navigation -->
  <nav class="navbar navbar-expand-lg navbar-custom static-top">
    <div class="container">
      <a class="navbar-brand" style="color:#FFEC00" href="/">Autobusne karte</a>
      <button class="navbar-toggler custom-toggler" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon custom-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarResponsive">
        <ul class="navbar-nav ml-auto">
          <li class="nav-item active">
            <a class="nav-link" style="color:#FFEC00" href="/">Početna</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" style="color:#FFEC00" href="/crud-primjer">Karte</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" style="color:#FFEC00" href="/info">Kontakt</a>
		  </li>
	  <li class="nav-item">
            <a class="nav-link" style="color:#FFEC00" href="/odjava">Odjava</a>
		  </li>
		  <li class="nav-item">
			<a class="nav-link" style="color:#FFEC00" href="/novi-korisnik">Novi korisnik<span class="sr-only">(current)</span></a>
		  </li>
        </ul>
      </div>
    </div>
  </nav>

  <!-- Page Content -->
  <div class="container">
	<div class="row" style="margin-top: 50px;">
        <form style="width: 100%" action='{{form_akcija}}' method='POST'>
			<div class="form-group">
                <label for="zona">Nova zona</label>
                <input type="number" class="form-control" id="zona" name='zona' aria-describedby="zona-help" placeholder="Unesite zonu" required>
            </div>
			
            <button type="submit" class="btn btn-dark">Sačuvaj</button>
        </form> 
    </div>

</body>
</html>
