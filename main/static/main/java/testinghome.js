function stampa() {

    var Teams = ["<td>Juventus<img class='Test-Logo2' src='https://cdn.freebiesupply.com/images/large/2x/juventus-logo-png-transparent.png'>",
    "<td>Inter Milan<img class='Test-Logo2' src='https://c7.uihere.com/files/149/536/895/inter-milan-football-serie-a-a-c-milan-uefa-champions-league-football.jpg'>",
    "<td>Lazio<img class='Test-Logo2' src='https://upload.wikimedia.org/wikipedia/en/thumb/e/e4/SS_Lazio.svg/1200px-SS_Lazio.svg.png'>",
    "<td>Cagliari<img class='Test-Logo2' src='https://upload.wikimedia.org/wikipedia/en/thumb/6/61/Cagliari_Calcio_1920.svg/1200px-Cagliari_Calcio_1920.svg.png'>",
    "<td>Roma<img class='Test-Logo2' src='https://upload.wikimedia.org/wikipedia/en/thumb/f/f7/AS_Roma_logo_%282017%29.svg/180px-AS_Roma_logo_%282017%29.svg.png'>",
    "<td>Atalanta<img class='Test-Logo2' src='https://upload.wikimedia.org/wikipedia/en/thumb/6/66/AtalantaBC.svg/1200px-AtalantaBC.svg.png'></td>",
    "<td>Napoli<img class='Test-Logo2' src='https://upload.wikimedia.org/wikipedia/commons/thumb/2/28/S.S.C._Napoli_logo.svg/240px-S.S.C._Napoli_logo.svg.png'>",
    "<td>Parma<img class='Test-Logo2' src='https://upload.wikimedia.org/wikipedia/commons/4/4a/ParmaCalcio1913_logo-400x400.png'>",
    "<td>Verona<img class='Test-Logo2' src='https://upload.wikimedia.org/wikipedia/en/thumb/c/cc/Hellas_Verona_FC_logo.svg/1200px-Hellas_Verona_FC_logo.svg.png'>",
    "<td>Fiorentina<img class='Test-Logo2' src='https://www.logofootball.net/wp-content/uploads/AC-Fiorentina-HD-Logo-750x750.png'>",
    "<td>Torino<img class='Test-Logo2' src='https://upload.wikimedia.org/wikipedia/en/thumb/2/2e/Torino_FC_Logo.svg/1200px-Torino_FC_Logo.svg.png'>",
    "<td>Milan<img class='Test-Logo2' src='https://cdn.freebiesupply.com/logos/large/2x/ac-milan-logo-png-transparent.png'>",
    "<td>Udinese<img class='Test-Logo2' src='https://upload.wikimedia.org/wikipedia/en/f/f2/Udinese_calcio.png'>",
    "<td>Sassuolo<img class='Test-Logo2' src='https://upload.wikimedia.org/wikipedia/ro/thumb/a/a3/US_Sassuolo_Calcio.svg/1200px-US_Sassuolo_Calcio.svg.png'>",
    "<td>Bologna<img class='Test-Logo2' src='https://upload.wikimedia.org/wikipedia/en/d/db/Bologna_F.C._1909_logo.png'>",
    "<td>Sampdoria<img class='Test-Logo2' src='https://upload.wikimedia.org/wikipedia/en/thumb/d/d2/U.C._Sampdoria_logo.svg/1200px-U.C._Sampdoria_logo.svg.png'>",
    "<td>Lecce<img class='Test-Logo2' src='https://upload.wikimedia.org/wikipedia/it/a/a0/Leccestemma.png'>",
    "<td>Genoa<img class='Test-Logo2' src='https://upload.wikimedia.org/wikipedia/ro/thumb/7/76/Genoa_CFC.svg/1200px-Genoa_CFC.svg.png'>",
    "<td>SPAL<img class='Test-Logo2' src='https://upload.wikimedia.org/wikipedia/en/thumb/3/3c/Spal2013_logo.svg/1200px-Spal2013_logo.svg.png'>",
    "<td>Brescia<img class='Test-Logo2' src='https://upload.wikimedia.org/wikipedia/fr/9/94/Brescia_Calcio_logo.png'>"
    ];

    var Teams2 = ["<td>Juventus<img class='Test-Logo' src='https://cdn.freebiesupply.com/images/large/2x/juventus-logo-png-transparent.png'>",
    "<td>Inter Milan<img class='Test-Logo' src='https://c7.uihere.com/files/149/536/895/inter-milan-football-serie-a-a-c-milan-uefa-champions-league-football.jpg'>",
    "<td>Lazio<img class='Test-Logo' src='https://upload.wikimedia.org/wikipedia/en/thumb/e/e4/SS_Lazio.svg/1200px-SS_Lazio.svg.png'>",
    "<td>Cagliari<img class='Test-Logo' src='https://upload.wikimedia.org/wikipedia/en/thumb/6/61/Cagliari_Calcio_1920.svg/1200px-Cagliari_Calcio_1920.svg.png'>",
    "<td>Roma<img class='Test-Logo' src='https://upload.wikimedia.org/wikipedia/sco/0/02/Burnley_FC_badge.png'>",
    "<td>Atalanta<img class='Test-Logo' src='https://upload.wikimedia.org/wikipedia/en/thumb/6/66/AtalantaBC.svg/1200px-AtalantaBC.svg.png'></td>",
    "<td>Napoli<img class='Test-Logo' src='https://upload.wikimedia.org/wikipedia/commons/thumb/2/28/S.S.C._Napoli_logo.svg/240px-S.S.C._Napoli_logo.svg.png'>",
    "<td>Parma<img class='Test-Logo' src='https://upload.wikimedia.org/wikipedia/commons/4/4a/ParmaCalcio1913_logo-400x400.png'>",
    "<td>Verona<img class='Test-Logo' src='https://upload.wikimedia.org/wikipedia/en/thumb/c/cc/Hellas_Verona_FC_logo.svg/1200px-Hellas_Verona_FC_logo.svg.png'>",
    "<td>Fiorentina<img class='Test-Logo' src='https://www.logofootball.net/wp-content/uploads/AC-Fiorentina-HD-Logo-750x750.png'>",
    "<td>Torino<img class='Test-Logo' src='https://upload.wikimedia.org/wikipedia/en/thumb/2/2e/Torino_FC_Logo.svg/1200px-Torino_FC_Logo.svg.png'>",
    "<td>Milan<img class='Test-Logo' src='https://cdn.freebiesupply.com/logos/large/2x/ac-milan-logo-png-transparent.png'>",
    "<td>Udinese<img class='Test-Logo' src='https://upload.wikimedia.org/wikipedia/en/f/f2/Udinese_calcio.png'>",
    "<td>Sassuolo<img class='Test-Logo' src='https://upload.wikimedia.org/wikipedia/ro/thumb/a/a3/US_Sassuolo_Calcio.svg/1200px-US_Sassuolo_Calcio.svg.png'>",
    "<td>Bologna<img class='Test-Logo' src='https://upload.wikimedia.org/wikipedia/en/d/db/Bologna_F.C._1909_logo.png'>",
    "<td>Sampdoria<img class='Test-Logo' src='https://upload.wikimedia.org/wikipedia/en/thumb/d/d2/U.C._Sampdoria_logo.svg/1200px-U.C._Sampdoria_logo.svg.png'>",
    "<td>Lecce<img class='Test-Logo' src='https://upload.wikimedia.org/wikipedia/it/a/a0/Leccestemma.png'>",
    "<td>Genoa<img class='Test-Logo' src='https://upload.wikimedia.org/wikipedia/ro/thumb/7/76/Genoa_CFC.svg/1200px-Genoa_CFC.svg.png'>",
    "<td>SPAL<img class='Test-Logo' src='https://upload.wikimedia.org/wikipedia/en/thumb/3/3c/Spal2013_logo.svg/1200px-Spal2013_logo.svg.png'>",
    "<td>Brescia<img class='Test-Logo' src='https://upload.wikimedia.org/wikipedia/fr/9/94/Brescia_Calcio_logo.png'>"
    ];


    for (i = 1; i < 21; i++) {
      if (i === 1) { continue; }
      if (i === 3) { continue; }
      if (i === 3) { continue; }
      if (i === 5) { continue; }
      if (i === 7) { continue; }
      if (i === 9) { continue; }
      if (i === 11) { continue; }
      if (i === 13) { continue; }
      if (i === 15) { continue; }
      if (i === 17) { continue; }
      if (i === 19) { continue; }
      var Team1= Teams[Math.floor(Math.random() * Teams.length)];
      document.getElementById(i).innerHTML = Team1;
  }

    for (i = 1; i < 21; i++) {
      if (i === 2) { continue; }
      if (i === 4) { continue; }
      if (i === 6) { continue; }
      if (i === 8) { continue; }
      if (i === 10) { continue; }
      if (i === 12) { continue; }
      if (i === 14) { continue; }
      if (i === 16) { continue; }
      if (i === 18) { continue; }
      if (i === 20) { continue; }
      var Team1= Teams2[Math.floor(Math.random() * Teams2.length)];
      document.getElementById(i).innerHTML = Team1;
      
  }


}
