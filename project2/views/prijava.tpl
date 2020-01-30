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
    <script type="text/javascript" src="/static/jquery.js"></script>
	  <script type="text/javascript" src="/static/custom.js"></script>
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
            <a class="nav-link" style="color:#FFFFFF">Prijava<span class="sr-only">(current)</span></a>
          </li>
	  <li class="nav-item">
            <a class="nav-link" style="color:#FFEC00" href="/odjava">Odjava</a>
		  </li>
        </ul>
      </div>
    </div>
  </nav>

  <!-- Page Content -->
      <div class="container">
	<form style="width: 100%" action='{{form_akcija}}' method="POST">
	 <h1>Prijava</h1>
	 <hr>
	 <div class="form-group">
	 <label for="login_username"><b>Korisničko ime</b></label>
	 <input type="text" placeholder="Korisničko ime" name="login_username" required>
	 </div>
	 <div class="form-group">
	 <label for="login_password"><b>Zaporka</b></label>
	 <input type="password" placeholder="Zaporka" name="login_password" required>
     	 </div>
	<button type="submit" class="btn btn-dark">Prijava</button>
      </form>
      <span 
    </div>
  </body>
</html>
