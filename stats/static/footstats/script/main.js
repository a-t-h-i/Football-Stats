const script = document.createElement('script');
script.src = 'https://cdn.jsdelivr.net/npm/chart.js';
document.head.appendChild(script);

var renderedCharts = []


function getSelection(){
  //Get name of selected home team
  const selectHome = document.querySelector("select[name='homeTeam']");
  const selectedHomeIndex = selectHome.selectedIndex;
  const selectedHomeOption = selectHome.options[selectedHomeIndex];
  const homeTeam = selectedHomeOption.text;

  //Get name of selected away team
  const selectAway = document.querySelector("select[name='awayTeam']");
  const selectedAwayIndex = selectAway.selectedIndex;
  const selectedAwayOption = selectAway.options[selectedAwayIndex];
  const awayTeam = selectedAwayOption.text;

  return [homeTeam, awayTeam]
}

function getAnalysis(){
  const xhr = new XMLHttpRequest();
  const url = '/predict/';

  let homeTeam = getSelection()[0];
  let awayTeam = getSelection()[1];

  
  if (homeTeam === "Select Team" || awayTeam === "Select Team"){
    console.log("Select both teams you idiot ^_^");
    return 0;
  }

  let data = {
    Home: homeTeam,
    Away: awayTeam
  };

  xhr.open('POST', url);
  xhr.setRequestHeader('Content-Type', 'application/json');

  xhr.onload = function() {
      if (xhr.status === 200) {
          const response = JSON.parse(xhr.responseText);
          showPrediction(response);
      }
  };
  xhr.send(JSON.stringify(data));

}


function displayStats(){
  const xhr = new XMLHttpRequest();
  const url = '/compare/';

  let homeTeam = getSelection()[0];
  let awayTeam = getSelection()[1];


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
  
  document.querySelector('#homeName').innerHTML = "(" + homeData.Name + ") (Position: " + homeData.Position + ") (Points: " + homeData.Points + ")";
  document.querySelector('#awayName').innerHTML = "(" + awayData.Name  + ") (Position: " + awayData.Position + ") (Points:  " + awayData.Points + ")";
  
  displayHomeTable(homeData);
  displayAwayTable(awayData);
}

function displayHomeTable(data){
  document.querySelector('#homePlayedHome').innerHTML = data.HomePlayed;
  document.querySelector('#homePlayedAway').innerHTML = data.AwayPlayed;
  document.querySelector('#homePlayedTotal').innerHTML = data.Played;
  
  document.querySelector('#homeWonHome').innerHTML = data.HomeWins;
  document.querySelector('#homeWonAway').innerHTML = data.AwayWins;
  document.querySelector('#homeWonTotal').innerHTML = data.Won;

  document.querySelector('#homeDrawnHome').innerHTML = data.HomeDraws;
  document.querySelector('#homeDrawnAway').innerHTML =  data.AwayDraws;
  document.querySelector('#homeDrawnTotal').innerHTML =  data.Draws;

  document.querySelector('#homeLostHome').innerHTML = data.HomeLoses;
  document.querySelector('#homeLostAway').innerHTML = data.AwayLost;
  document.querySelector('#homeLostTotal').innerHTML = data.Lost;

  document.querySelector('#homeWinPercHome').innerHTML = data.HomeWinPercentage + "%";
  document.querySelector('#homeWinPercAway').innerHTML = data.AwayWinPercentage + "%";
  document.querySelector('#homeWinPercTotal').innerHTML = data.WinPercentage + "%";

  document.querySelector('#homeDrawPercHome').innerHTML = data.HomeDrawsPercentage + "%";
  document.querySelector('#homeDrawPercAway').innerHTML = data.AwayDrawPercentage + "%";
  document.querySelector('#homeDrawPercTotal').innerHTML = data.DrawPercentage + "%";

  document.querySelector('#homeLosePercHome').innerHTML = data.HomeLosePercentage + "%";
  document.querySelector('#homeLosePercAway').innerHTML = data.AwayLosePercentage + "%";
  document.querySelector('#homeLosePercTotal').innerHTML = data.LosePercentage + "%";
}

function displayAwayTable(data){
  document.querySelector('#awayPlayedHome').innerHTML = data.HomePlayed;
  document.querySelector('#awayPlayedAway').innerHTML = data.AwayPlayed;
  document.querySelector('#awayPlayedTotal').innerHTML = data.Played;
  
  document.querySelector('#awayWonHome').innerHTML = data.HomeWins;
  document.querySelector('#awayWonAway').innerHTML = data.AwayWins;
  document.querySelector('#awayWonTotal').innerHTML = data.Won;

  document.querySelector('#awayDrawnHome').innerHTML = data.HomeDraws;
  document.querySelector('#awayDrawnAway').innerHTML =  data.AwayDraws;
  document.querySelector('#awayDrawnTotal').innerHTML =  data.Draws;

  document.querySelector('#awayLostHome').innerHTML = data.HomeLoses;
  document.querySelector('#awayLostAway').innerHTML = data.AwayLost;
  document.querySelector('#awayLostTotal').innerHTML = data.Lost;

  document.querySelector('#awayWinPercHome').innerHTML = data.HomeWinPercentage + "%";
  document.querySelector('#awayWinPercAway').innerHTML = data.AwayWinPercentage + "%";
  document.querySelector('#awayWinPercTotal').innerHTML = data.WinPercentage + "%";

  document.querySelector('#awayDrawPercHome').innerHTML = data.HomeDrawsPercentage + "%";
  document.querySelector('#awayDrawPercAway').innerHTML = data.AwayDrawPercentage + "%";
  document.querySelector('#awayDrawPercTotal').innerHTML = data.DrawPercentage + "%";

  document.querySelector('#awayLosePercHome').innerHTML = data.HomeLosePercentage + "%";
  document.querySelector('#awayLosePercAway').innerHTML = data.AwayLosePercentage + "%";
  document.querySelector('#awayLosePercTotal').innerHTML = data.LosePercentage + "%";
}

function showPrediction(response){
  let prediction = JSON.parse(response).Prediction;
  console.log(JSON.parse(response));
  //Code to show the prediction on the DOM
  document.querySelector('#analysis').innerHTML = prediction;
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

  for (let i = 0; i != renderedCharts.length; i++){
    //Destroy rendered charts if they exist
    renderedCharts[i].destroy();
  }

  renderedCharts.push(showHomePie(homePie));
  renderedCharts.push(showHomeGraph(homeGraph));
  renderedCharts.push(showAwayPie(awayPie));
  renderedCharts.push(showAwayGraph(awayGraph));

}

function showHomePie(x){
  const ctx = document.getElementById('homePie');
  let stats = x;
  
  return new Chart(ctx, {
    type: 'doughnut',
    data: {
      labels: ['Win %', 'Draw %', '%Lose %'],
      datasets: [{
        data: stats,
        backgroundColor: ['#68bbb8','#f2c38e','#e55a5a'],
        borderWidth: 0,
        borderRadius: 5
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


function showHomeGraph(y){
  const ctx = document.getElementById('homeGraph');
  let stats = y;

  return new Chart(ctx, {
    type: 'bar',
    data: {
      labels: ['Scored', 'Conceded'],
      datasets: [{
        label: "Goals",
        data: stats,
        backgroundColor: ['#68bbb8','#f2c38e'],
        borderWidth: 0,
        borderRadius: 20
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
function showAwayPie(y){
  const ctx = document.getElementById('awayPie');
  let stats = y;

  return new Chart(ctx, {
    type: 'doughnut',
    data: {
      labels: ['Win %', 'Draw %', 'Lose %'],
      datasets: [{
        data: stats,
        backgroundColor: ['#68bbb8','#f2c38e','#e55a5a'],
        borderWidth: 0,
        borderRadius: 5
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

  return new Chart(ctx, {
    type: 'bar',
    data: {
      labels: ['Scored', 'Conceded'],
      datasets: [{
        label: "Goals",
        data: stats,
        backgroundColor: ['#68bbb8','#f2c38e'],
        borderWidth: 0,
        borderRadius: 20
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