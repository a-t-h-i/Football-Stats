const script = document.createElement('script');
script.src = 'https://cdn.jsdelivr.net/npm/chart.js';
document.head.appendChild(script);


var stats = document.getElementById("compare_stats");
var prediction = document.getElementById("prediction");


function focus_stats(){
  console.log("I have been called up. Yay!");
  stats.focus();
}

function focus_prediction(){
  console.log("I have also been called up. Yay ^_^");
  prediction.focus();
}

function loadGraps(data){
  homePie([12,3,4]);
  homeGraph([2,4,5]);
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
