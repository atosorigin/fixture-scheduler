

let mountains = [
    { Team1: ' ', V:'', Team2: ' ' },
    { Team1: "Everton", V: '', Team2: "Bournemouth" },
    { Team1: "Wolverhampton", V: '', Team2: "Aston Villa" },
    { Team1: "Everton", V: '', Team2: "Man United" },
    { Team1: "Norwich", V: '', Team2: "Man City"},
  ];

  
  document.getElementById('body').innerHTML = '<div class="row"><div class="col s6 m6"><table id = "customers">" - "</div>';


  function generateTableHead(table, data) {
    let tableHead = table.createTHead();
    let row = tableHead.insertRow();
    for (let key of data) {
      let th = document.createElement("th");
      let text = document.createTextNode(key);
      th.appendChild(text);
      row.appendChild(th);
    }
  }
  function generateTable(table, data) {
    for (let element of data) {
      let row = table.insertRow();
      for (key in element) {
       let cell = row.insertCell();
       cell.id = key;
        let text = document.createTextNode(element[key]);
        cell.appendChild(text);
      }
    }
  }

  let table = document.querySelector("table");
  let data = Object.keys(mountains[0]);
  generateTableHead(table, data);
  generateTable(table, mountains);
