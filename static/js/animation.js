function getEmotionCount() {
	$.ajax({
    url: 'emotion_count',
    success: function(data) {
      $("#angry").html(data.split(",")[0].split("'Angry': ")[1]);
      $("#fear").html(data.split(",")[2].split("'Fear': ")[1]);
      $("#happy").html(data.split(",")[3].split("'Happy': ")[1]);
      $("#sad").html(data.split(",")[4].split("'Sad': ")[1]);
      $("#surprise").html(data.split(",")[5].split("'Surprise': ")[1]);
      $("#neutral").html(data.split(",")[6].split("'Neutral': ")[1]);
    }
  });
}

getEmotionCount(); // This will run on page load
setInterval(function(){
  getEmotionCount() // this will run after every 5 seconds
}, 500);