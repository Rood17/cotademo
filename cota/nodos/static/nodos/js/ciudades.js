var text2  = new Object ();
 $(function () {

   var property;
   // Se cambia datacd por dataacd
   var dataacd = document.getElementById('json_map').value;
   console.log(dataacd);
   var ciudad2 = JSON.parse(dataacd);
   var myJSON = JSON.stringify(ciudad2[0]);

   Object.keys(ciudad2).forEach(function(key){

      var property = key;
      text2[property] = ciudad2[key];

   });



   console.log("TEXTO",text2);

   /*var property = 'String2';

   text2[property] = {
           type: "image",
           url: "http://www.neveldo.fr/mapael/assets/img/marker.png",
           width: 6,
           height: 24 ,
           latitude: 60.4978,
           longitude: -99.1269,
           attrs: {
               opacity: 1
           },
           attrsHover: {
               transform: "s1.8"
           },myText: "Coordenda 2 "
         };*/
});
