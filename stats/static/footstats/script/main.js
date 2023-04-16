const script = document.createElement('script');
script.src = 'https://cdn.jsdelivr.net/npm/chart.js';
document.head.appendChild(script);

function displayStats(){
  const xhr = new XMLHttpRequest();
  const url = '/compare/';

  //Get name of selected home team
  const selectHome = document.querySelector("select[name='homeTeam']");
  const selectedHomeIndex = selectHome.selectedIndex;
  const selectedHomeOption = selectHome.options[selectedHomeIndex];
  const homeTeam = selectedHomeOption.text;


  //Get name of selected away team
  const selectAway = document.querySelector("select[name='homeTeam']");
  const selectedAwayIndex = selectHome.selectedIndex;
  const selectedAwayOption = selectAway.options[selectedAwayIndex];
  const awayTeam = selectedAwayOption.text;

  if (homeTeam === "Select Team" || awayTeam === "Select Team"){
    console.log("Select both teams you dumbass ^_^");
    return 0;
  }

    //Unhide hidden divs
    document.getElementById("homeStats").hidden = false;
    document.getElementById("awayStats").hidden = false;
    document.getElementById("prediction").hidden = false;

  const data = { 
    Home: homeTeam,
    Away: awayTeam
  };
  
  xhr.open('POST', url);
  xhr.setRequestHeader('Content-Type', 'application/json');

  // Retrieve the CSRF token from the cookie
  const csrftoken = getCookie('csrftoken');

  // Set the CSRF token as a header in the request
  xhr.setRequestHeader('X-CSRFToken', csrftoken);

  xhr.onload = function() {
      if (xhr.status === 200) {
          const response = JSON.parse(xhr.responseText);
          populateDom(response);
      }
  };
  xhr.send(JSON.stringify(data));
  
}

function populateDom(stats){
  let homeData = JSON.parse(stats).Home;
  let awayData = JSON.parse(stats).Away;

  loadGraps(homeData, awayData);
}     

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}


function loadGraps(a, b){
  let home = a;
  let away = b;
  let homePie = [];
  let homeGraph = [];
  let awayPie = [];
  let awayGraph = [];

  homePie.push(home.WinPercentage);
  homePie.push(home.DrawPercentage);
  homePie.push(home.LosePercentage);

  homeGraph.push(home.Goals);
  homeGraph.push(home.Conceded);

  awayPie.push(away.WinPercentage);
  awayPie.push(away.DrawPercentage);
  awayPie.push(away.LosePercentage);

  awayGraph.push(away.Goals);
  awayGraph.push(away.Conceded);

  showHomePie(homePie);
  showHomeGraph(homeGraph);
  showAwayPie(awayPie);
  showAwayGraph(awayGraph);

}


function showHomePie(x){
  const ctx = document.getElementById('homePie');
  let stats = x;
  
  new Chart(ctx, {
    type: 'doughnut',
    data: {
      labels: ['Win %', 'Draw %', '%Lose %'],
      datasets: [{
        data: stats,
        backgroundColor: ['#68bbb8','#f2c38e','#e55a5a'],
        borderWidth: -2
      }]
    },
    options: {
      scales: {
        y: {
          beginAtZero: false
        }
      }
    }
  });
}


function showHomeGraph(x){
  const ctx = document.getElementById('homeGraph');
  let stats = x;

  new Chart(ctx, {
    type: 'bar',
    data: {
      labels: ['Scored', 'Conceded'],
      datasets: [{
        data: stats,
        backgroundColor: ['#68bbb8','#f2c38e'],
        borderWidth: 0
      }]
    },
    options: {
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  });
}

//Away
function showAwayPie(x){
  const ctx = document.getElementById('awayPie');
  let stats = x;

  new Chart(ctx, {
    type: 'doughnut',
    data: {
      labels: ['Win %', 'Draw %', 'Lose %'],
      datasets: [{
        data: stats,
        backgroundColor: ['#68bbb8','#f2c38e','#e55a5a'],
        borderWidth: -2
      }]
    },
    options: {
      scales: {
        y: {
          beginAtZero: false
        }
      }
    }
  });
}

//Bar
function showAwayGraph(x){
  const ctx = document.getElementById('awayGraph');
  let stats = x;

  new Chart(ctx, {
    type: 'bar',
    data: {
      labels: ['Scored', 'Conceded'],
      datasets: [{
        data: stats,
        backgroundColor: ['#68bbb8','#f2c38e'],
        borderWidth: 0
      }]
    },
    options: {
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  });
}