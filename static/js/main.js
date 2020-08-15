BeSmile = {
  reportData: null,
  reportOptions: null,
  reportChart: null,
  emotionResult: null,

  start: function(){
    BeSmile.emotionCount('POST', 'emotion_count', 'today', "json");
    $("#neutral").html(BeSmile.emotionResult["Neutral"]);
    $("#happy").html(BeSmile.emotionResult["Happy"]);
    $("#sad").html(BeSmile.emotionResult["Sad"]);
    $("#angry").html(BeSmile.emotionResult["Angry"]);
    $("#fear").html(BeSmile.emotionResult["Fear"]);
    $("#surprise").html(BeSmile.emotionResult["Surprise"]);
  },
  emotionCount: function(type, url, date, data_type){
    $.ajax({
      type: type,
      url: url,
      data : {'data': date},
      dataType: data_type,
      success: function(data) {
        BeSmile.emotionResult = data
      }
    });
    return BeSmile.emotionResult
  },
  report: function(){
    BeSmile.emotionCount('POST', 'emotion_count', 'today', "json");
    $('#reportModal').modal('show');
    google.charts.load("current", {packages:["corechart"]});
    google.charts.setOnLoadCallback(drawChart);
    function drawChart() {
      reportData = google.visualization.arrayToDataTable([
        ['Emotions', 'Counts per Day'],
        ['Neutral', Number(BeSmile.emotionResult['Neutral'])],
        ['Angry', Number(BeSmile.emotionResult['Angry'])],
        ['Happy', Number(BeSmile.emotionResult['Happy'])],
        ['Sad', Number(BeSmile.emotionResult['Sad'])],
        ['Fear', Number(BeSmile.emotionResult['Fear'])],
        ['Surprise', Number(BeSmile.emotionResult['Surprise'])]
      ]);

      reportOptions = {
        is3D: true,
        width: 800,
        height: 500,
        slices: {  
          2: {offset: 0.3}
        }
      };

      reportChart = new google.visualization.PieChart(document.getElementById('piechart_3d'));
      reportChart.draw(reportData, reportOptions);
    }
  }
}

$(document).ready(function() {
  $('#btn-section').on('click', '.report-btn', BeSmile.report);
  setInterval(function(){
    BeSmile.start()
  }, 1000);
});