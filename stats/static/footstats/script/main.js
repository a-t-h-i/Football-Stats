const script = document.createElement('script');
script.src = 'https://cdn.jsdelivr.net/npm/chart.js';
document.head.appendChild(script);

let home; 
let away;

function getStats(home, away){
  home, away = [JSON.parse(home), JSON.parse(away)]
  loadGraps();
}


function focuStats(){
  console.log("I have been called up. Yay!");
  stats.focus();
}

function focusPrediction(){
  console.log("I have also been called up. Yay ^_^");
  prediction.focus();
}

function loadGraps(){
  var homePie = [];
  var homeGraph = [];
  var awayPie = [];
  var awayGraph = [];

  homePie.push(home["Win Percentage"]);
  homePie.push(home["Draw Percentage"]);
  homePie.push(home["Lose Percentage"]);

  homeGraph.push(home["Goals"]);
  homeGraph.push(home["Conceded"]);

  awayPie.push(away["Win Percentage"]);
  awayPie.push(away["Draw Percentage"]);
  awayPie.push(away["Lose Percentage"]);

  awayGraph.push(away["Goals"]);
  awayGraph.push(away["Conceded"]);

  homePie(homePie);
  homeGraph(homeGraph);
}

//Pie
function homePie(x){
  const ctx = document.getElementById('homePie');
  let stats = x
  new Chart(ctx, {
    type: 'doughnut',
    data: {
      labels: ['% of wins', '% of draws', '% of loses'],
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
function homeGraph(x){
  const ctx = document.getElementById('homeGraph');
  let stats = x
  new Chart(ctx, {
    type: 'bar',
    data: {
      labels: ['Scored', 'Conceded'],
      datasets: [{
        label: 'Goals',
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
