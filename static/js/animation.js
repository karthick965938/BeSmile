function getEmotionCount() {
	$.ajax({
    type: 'POST',
    url: 'emotion_count',
    data : {'data': 'today'},
    dataType: "json",
    success: function(data) {
      $("#neutral").html(data['Neutral']);
      $("#happy").html(data['Happy']);
      $("#sad").html(data['Sad']);
      $("#angry").html(data['Angry']);
      $("#fear").html(data['Fear']);
      $("#surprise").html(data['Surprise']);
    }
  });
}

getEmotionCount(); // This will run on page load
setInterval(function(){
  getEmotionCount() // this will run after every 1 seconds
}, 1000);