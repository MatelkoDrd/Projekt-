// var xmlns = "http://www.w3.org/2000/svg",
//   xlinkns = "http://www.w3.org/1999/xlink",
//   select = function(s) {
//     return document.querySelector(s);
//   },
//   selectAll = function(s) {
//     return document.querySelectorAll(s);
//   }
//
//
// TweenMax.set('svg', {
//   visibility: 'visible'
// })
// TweenMax.set('#bonnetStart', {
//   y:75
// })
// TweenMax.set('#bumper', {
//   drawSVG:'50% 50%',
//   alpha:0
// })
//
// TweenMax.set('#shadow', {
//   alpha:0.2
// })
// TweenMax.set('#wholeCar', {
//   transformOrigin:'50% 50%',
//   y:-30
// })
// TweenMax.set('#frame', {
//   transformOrigin:'50% 50%',
//   scaleX:0
// })
// TweenMax.set(['#headlightL', '#headlightR'], {
//   svgOrigin:'410 320',
//   scale:0
// })
// TweenMax.set(['#tyreL', '#tyreR'], {
//   y:-30,
//   transformOrigin:'50% 50%'
// })
//
// TweenMax.set('#mirrorL', {
//   transformOrigin:'100% 100%',
//   scale:0,
//   rotation:90,
//   y:20,
//   x:10
//
// })
// TweenMax.set('#mirrorR', {
//   transformOrigin:'0% 100%',
//   scale:0,
//   rotation:-90,
//   y:20,
//   x:-10
//
// })
//
// var tl = new TimelineMax({repeat:-1, repeatDelay:0});
// tl.set('#bumper', {
//   alpha:1
// })
// .to('#bumper', 1, {
//   drawSVG:'0% 100%',
//   ease:Power1.easeInOut
// })
// .from('#shadow', 1, {
//   attr:{
//     rx:0,
//     ry:'-=6'
//   },
//   ease:Power1.easeInOut
// },'-=1')
//   .to('#bonnetStart', 0.9, {
//   y:0,
//   ease:Power2.easeInOut
// },'-=0.9')
// .to('#bonnetStart', 1, {
//   morphSVG:{shape:'#bonnetEnd'}
// },'-=0.3')
// .to('#frame', 1, {
//   scaleX:1,
//   ease:Power2.easeInOut
// },'-=1')
//
// .to(['#headlightL', '#headlightR'], 1, {
//   scale:1,
//   ease:Power2.easeInOut
// },'-=1')
// .to('#wholeCar', 1.2, {
//   y:0,
//   ease:Anticipate.easeInOut
// },'-=1')
//
// .to(['#tyreL', '#tyreR'], 0.5, {
//   y:0,
//   ease:Power2.easeInOut
// },'-=1')
// .to(['#tyreL', '#tyreR'], 0.2, {
//   scaleX:1.1,
//   ease:Power2.easeOut
// },'-=0.5')
// .to('#chassis', 0.2, {
//   y:5,
//   transformOrigin:'50% 50%',
//   //rotation:3,
//   ease:Power1.easeIn
// },'-=0.5')
// .to('#chassis', 0.4, {
//   y:0
// },'-=0.2')
//
// .to(['#tyreL', '#tyreR'], 2, {
//   scaleX:1,
//   ease:Elastic.easeOut.config(1, 0.8)
// },'-=0.4')
// .to(['#mirrorL', '#mirrorR'], 1, {
//   scale:1,
//   y:0,
//   x:0
// },'-=2.5')
// .to(['#mirrorL', '#mirrorR'], 4, {
//   rotation:0  ,
//   ease:Elastic.easeOut.config(1, 0.2)
// },'-=1.8')
// .set('#shadow', {
//   alpha:0
// })
// .set('#shadow', {
//   alpha:0
// })
// .set('#shadowFollow', {
//   alpha:0.2
// })
// .to('#wholeCar', 2, {
//   scale:1.82,
//   y:600,
//   ease:Power1.easeIn
// })
//
//
//
// tl.timeScale(2)
//
// //ScrubGSAPTimeline(tl)