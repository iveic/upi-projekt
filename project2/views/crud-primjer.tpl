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
            <a class="nav-link" style="color:#FFFFFF" href="/crud-primjer">Karte
              <span class="sr-only">(current)</span>
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link" style="color:#FFEC00" href="/info">Kontakt</a>
          </li>
		  <li class="nav-item">
            <a class="nav-link" style="color:#FFEC00" href="/prijava">Prijava</a>
		  </li>
	  <li class="nav-item">
            <a class="nav-link" style="color:#FFEC00" href="/odjava">Odjava</a>
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
                <th scope="col">E-mail</th>
                <th scope="col">Vrsta</th>
		<th scope="col">Datum</th>
                <th scope="col">Uredi</th>
                <th scope="col">Izbriši</th>
                </tr>
            </thead>
            <tbody style="background-color:#e9ecef">

                %for item in data:

                    <tr>
                        <th scope="row"> {{item[1].id}} </th>
                        <td> {{item[0].ime_prezime}} </td>
			<td> {{item[0].email}} </td>
			<td> {{item[2].vrsta}} </td>
			<td> {{item[1].datum}} </td>
                        
                        <td> 
                            <a href='/crud-primjer-azuriraj-kartu?kartaid={{item[1].id}}'>
                                <i class="fas fa-edit"></i>
                            </a>
                        </td>
                        <td> 
                            <a href='/crud-primjer-izbrisi-kartu?kartaid={{item[1].id}}'>
                                <i class="fas fa-trash-alt"></i>
                            </a>
                        </td>
                    </tr>

                %end
            </tbody>
        </table>
	<div class="col-md-2 text-center" style="padding: 0">
		<a href='/ispis-karata' class="btn btn-dark">Ispis karata</a>
	</div>
        </div>
  </div>
  

</body>
</html>
