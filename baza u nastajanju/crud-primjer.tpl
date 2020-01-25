<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="Bottle web project template">
    <meta name="author" content="datamate">
     
    <title>My UPI Project</title>
    <link rel="stylesheet" type="text/css" href="/static/bootstrap.min.css">
    <link rel="stylesheet" type="text/css" href="/static/custom.css">
    <link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.11.2/css/all.min.css">

    <script type="text/javascript" src="/static/jquery.js"></script>
	  <script type="text/javascript" src="/static/custom.js"></script>
    <script type="text/javascript" src="/static/bootstrap.min.js"></script> 

</head>
<body>

	
	  <!-- Navigation -->
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark static-top">
    <div class="container">
      <a class="navbar-brand" href="/">My UPI project</a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarResponsive">
        <ul class="navbar-nav ml-auto">
          <li class="nav-item">
            <a class="nav-link" href="/">Home
            </a>
          </li>
		  <li class="nav-item active">
            <a class="nav-link" href="/crud-primjer">CRUD example</a>
			<span class="sr-only">(current)</span>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">About</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Services</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Contact</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>

  <!-- Page Content -->
  <div class="container">
    <div class="row" style="padding: 25px 0;">
      <div class="col-md-2 text-center" style="padding: 0">
        <a href='/crud-primjer-nova-karta' class="btn btn-dark">Dodaj novu kartu</a>
      </div>
    </div>
	<div class="row">
        <table class="table">
            <thead>
                <tr>
                <th scope="col">#</th>
                <th scope="col">Ime Prezime</th>
                <th scope="col">Godište</th>
                <th scope="col">Mjesto stanovanja</th>
                <th scope="col">Datum izrade karte</th>
				<th scope="col">Vrsta karte</th>
				<th scope="col">Područje</th>
				<th scope="col">Zona</th>
                </tr>
            </thead>
            <tbody>

                %for item in data:

                    <tr>
                        <th scope="row"> {{item[0]}} </th>
                        <td> {{item[1]}} </td>
                        <td> {{item[2]}} </td>
						<td> {{item[3]}} </td>
						<td> {{item[4]}} </td>
						<td> {{item[5]}} </td>
						<td> {{item[6]}} </td>
						<td> {{item[7]}} </td>
						
                        <td> 
                            <a href='/crud-primjer-azuriraj-kartu?kartaid={{item[0]}}'>
                                <i class="fas fa-edit"></i>
                            </a>
                        </td>
                        <td> 
                            <a href='/crud-primjer-izbrisi-kartu?kartaid={{item[0]}'>
                                <i class="fas fa-trash-alt"></i>
                            </a>
                        </td>
                    </tr>

                %end
            </tbody>
        </table>       
        </div>
  </div>
  
	<script>
		//example of calling custom function
		helloWorld();
	</script>
</body>
</html>