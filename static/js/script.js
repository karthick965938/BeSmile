EmotionIncrementAnimation = {
  tlDuration: 300,
  emotion: null,
  emotionCount: null,
  count_element: null,
  animationTimeline: null,

  triangleBurst: function(){
    new mojs.Burst({
      parent: EmotionIncrementAnimation.clap,
      radius: { 50: 95 },
      count: 5,
      angle: 30,
      children: {
        shape: 'cross',
        radius: { 10: 0 },
        scale: 1,
        stroke: 'rgba(211,84,0 ,0.5)',
        strokeWidth: 2,
        angle: 210,
        delay: 30,
        speed: 0.2,
        easing: mojs.easing.bezier(0.1, 1, 0.3, 1),
        duration: EmotionIncrementAnimation.tlDuration
      } 
    });
  },

  circleBurst: function(){
    new mojs.Burst({
      parent: EmotionIncrementAnimation.emotion,
      radius: { 50: 75 },
      angle: 25,
      duration: EmotionIncrementAnimation.tlDuration,
      children: {
        shape: 'circle',
        fill: 'rgba(149,165,166 ,0.5)',
        delay: 30,
        speed: 0.2,
        radius: { 3: 0 },
        easing: mojs.easing.bezier(0.1, 1, 0.3, 1)
      }
    });
  },

  countAnimation: function(){
    new mojs.Html({
    el: EmotionIncrementAnimation.count_element,
    isShowStart: false,
    isShowEnd: true,
    y: { 0: -30 },
    opacity: { 0: 1 },
    duration: EmotionIncrementAnimation.tlDuration }).then({
      opacity: { 1: 0 },
      y: -80,
      delay: EmotionIncrementAnimation.tlDuration / 2
    });
  },

  addTransform: function(){
    EmotionIncrementAnimation.emotion.style.transform = "scale(1, 1)";
  },

  assignValues: function(emotion, emotionCount){
    EmotionIncrementAnimation.emotion = document.getElementById(emotion);
    EmotionIncrementAnimation.emotionCount = document.getElementById(emotionCount);
    EmotionIncrementAnimation.count_element = '#'+emotionCount
    EmotionIncrementAnimation.emotionCount.innerHTML = "😐"
    EmotionIncrementAnimation.addTransform()
  },

  start: function(emotion, emotionCount){
    EmotionIncrementAnimation.assignValues(emotion, emotionCount);
    EmotionIncrementAnimation.animationTimeline = new mojs.Timeline();
    EmotionIncrementAnimation.animationTimeline.add([
      EmotionIncrementAnimation.triangleBurst(),
      EmotionIncrementAnimation.circleBurst(),
      EmotionIncrementAnimation.countAnimation()
    ]);
    EmotionIncrementAnimation.animationTimeline.replay();
  }
}