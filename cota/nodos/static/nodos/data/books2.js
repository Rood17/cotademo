'use strict';
var data2;
var categorias;
var edges;
var k=0;
var e=0;
var aSize = 30;
var bSize = 20;
var cSize = 10;
var LENGTH_MAIN = 2050;
var GRAY = 'gray';
var cat;
var categoria;
var DIR = 'img/';
var nodes = null;
var edges = null;
var network = null;
var titulo;

data2 = new Array();
categorias = new Array();
edges = new Array();

var categorias = JSON.parse(datac);

function draw() {

  var ref;

  ref   = test('Dos')
  nodes = ref[0];
  edges = ref[1];

  var container = document.getElementById('mynetwork');
  var data = {
    nodes: nodes,
    edges: edges
  };
  var options = {
    layout: {
      randomSeed:1
        /*hierarchical: {
            direction: "LR",
            sortMethod: "directed"
        }*/
    },
    interaction:{hover:true},
    nodes: {

      borderWidth:2,
      scaling: {
          min:85,
          max: 650
      },
    color: {
        border: '#D9A099',
        background: 'gray'
      },
      font:{color:'#fff',size:30},
    },
    edges: {
        color: 'blue',
        smooth: false
    },
    physics: {
        barnesHut: {
            gravitationalConstant: -130000
        },
        stabilization: {
            iterations: 2500
        }
    },
  };
  network = new vis.Network(container, data, options);

  //Get the canvas HTML element
  var networkCanvas = document.getElementById("mynetwork").getElementsByTagName("canvas")[0]
  function changeCursor(newCursorStyle){
	networkCanvas.style.cursor = newCursorStyle;
  }

  /*network.on('hoverNode', function () {

   changeCursor('grab');
   console.log('hover' );

 });*/

  network.on("click", function (params) {


    var objz;
    var objc;
    var ctr;
    var modalNodos = document.getElementById('id01');


    params.event = "[original event]";
    var num = params.nodes;
    console.log(num[0]);

    objz = data2.find( libro => libro.id === num[0]);
    //console.log(objz);

    //console.log("OBJETO:",objz);

    document.getElementById('imgn').src
    = objz.image;

    document.getElementById('titulo').innerHTML
    =  objz.libro.titulo  ;

    if (objz.libro !== undefined  ) {
        document.getElementById('autor').innerHTML
        = objz.libro.autor  ;
        
        Object.keys(objz.libro.relaciones).forEach(function(key) {
          if(ctr !== undefined){
            ctr =  ctr + '<a href="category/' + objz.relacion[key] + '/" >'
             + objz.libro.relaciones[key] + '</a> ';
          }else{
            ctr = '<a href="category/'
            + objz.libro.relaciones[key] + '">' + objz.libro.relaciones[key] + '</a> ';
          }
        });

        document.getElementById('relaciones').innerHTML = ctr;
        
        
        document.getElementById('isbn').innerHTML
        = objz.libro.isbn  ;
        


        var link = objz.libro.link;
        if( link != 'null'){
          document.getElementById("link").innerHTML = '<a target="blank" href=' + link + 
          '>[ Leer ]</a>';
        } else {
          "<a href='' >[ Leer ]</a>"
        }


    
        // document.getElementById('link').innerHTML
        // = objz.libro.link ;
        modalNodos.style.display='block';
        window.onclick = function(event) {
          if (event.target == modalNodos) {
              modalNodos.style.display = "none";
          }
        }

      }else{
        objc = categorias.find( categoria => categoria.id === num[0]);
        document.getElementById('categoria').innerHTML = 'Categoria: '  + objc.categoria ;
        document.getElementById('id02').style.display='';
      }

      objz = 0;
      //console.log(objz);

    console.log('click event, getNodeAt returns: ' + this.getNodeAt(params.pointer.DOM));


  });
}

function test(titulo){
  var ref     = new Array();
  var mydata  = JSON.parse(data);
  edges  = [];

  var x;
  var r;
  var w;

  Object.keys(mydata).forEach(function(key) {

    if(!data2.find(libro => libro.id === mydata[key].id) && (mydata[key].nombre == titulo || mydata[key].libro.autor == titulo || mydata[key].label == titulo )){
      //console.log("MAIN PROCESS:",mydata[key].id);
      w = data2.length;
      mydata[key].value=aSize;
      mydata[key].font={"color":"#000"};
      data2[w] = mydata[key];
      //console.log("DATA en el MAIN:",data2);

      for(x=0;x<mydata[key].relacion.length;x++){
        //console.log(mydata[key].relacion[x],mydata[key].id);
        if((!edges.find(edge => edge.from === mydata[key].id && edge.to === mydata[key].relacion[x])) ||
           (!edges.find(edge => edge.from === mydata[key].relacion[x] && edge.to === mydata[key].id)) ){
          var objw = {"from": mydata[key].id, "to":mydata[key].relacion[x], "length": LENGTH_MAIN,  font: {align: 'middle'} };
          edges[e] = objw ;
          e = e + 1;
        }

        if(!data2.find(libro => libro.id === mydata[key].relacion[x])){
          categoria = categorias.find(categoria => categoria.id === mydata[key].relacion[x]) ;
          cat       = {"id":categoria.id,"label":categoria.label,"shape":"box",font:{size:25} };

          w = data2.length;
          data2[w] = cat;
          r = testr(mydata[key].relacion[x], mydata,mydata[key].id,mydata[key].id,x);

        } else{

          console.log(mydata[key].relacion[x]);
          if((!edges.find(edge => edge.from === mydata[key].id && edge.to === mydata[key].relacion[x])) ||
             (!edges.find(edge => edge.from === mydata[key].relacion[x] && edge.to ===  mydata[key].id))){
            var objw = {"from": mydata[key].id, "to":mydata[key].relacion[x], "length": LENGTH_MAIN,font: {align: 'middle'} };
            edges[e] = objw ;
            e = e + 1;
          }
        }
      //  console.log(mydata[key].relacion[x]);

      }
    }
  });

  console.log(edges);

  ref[0] = data2;
  ref[1] = edges;

  console.log("REF",ref);
  return ref;
}


function testr(nodo,nodos,id,main){

  //console.log("NODO:",nodo);
  var obj;
  var index;
  var j;
  var a;
  var objw;

    Object.keys(nodos).forEach(function(key2) {

      index = nodos[key2].relacion.indexOf(nodo);

      if(index > -1 && !data2.find(libro => libro.id === nodos[key2].id)){
        //console.log(nodos[key2].id, nodo);
        //console.log("CATEGORIA:",nodo, "ID:",nodos[key2].id);
        obj  = nodos.find(libro => libro.id === nodos[key2].id);
        obj.font={"color":"#000"};
        if(main == 'x' ){
          obj.value = cSize;
        }else{
          obj.value = cSize;
        }

        if(id == main ){
          obj.value = bSize;
        }else{
          obj.value = cSize;
        }

        j = data2.length;
        data2[j] = obj;

        if((!edges.find(edge => edge.from === id && edge.to === nodo)) ||
           (!edges.find(edge => edge.from === nodo && edge.to === id)) ){
        var objw = { "from": id, "to" : nodo, "length": LENGTH_MAIN };
        edges[e] = objw ;
        e = e + 1;
        }

        if((!edges.find(edge => edge.from === nodo && edge.to === nodos[key2].id)) ||
           (!edges.find(edge => edge.from === nodos[key2].id && edge.to === nodo)) ){
        //console.log("NO PASS ID:",nodo,"PR:",id);
        var objw = { "from": nodo, "to" : nodos[key2].id, "length": LENGTH_MAIN,  font: {align: 'middle'} };
        edges[e] = objw ;
        e = e + 1;
        }

        //console.log(obj.id);
        for(a=0;a<obj.relacion.length;a++){

          if(!data2.find(libro => libro.id === obj.relacion[a])){
            categoria = categorias.find(categoria => categoria.id === obj.relacion[a]) ;
            //console.log(categoria);
            cat  = {"id":categoria.id,"label":categoria.label,"shape":"box","font":{size:25}};

            if((!edges.find(edge => edge.from === obj.id && edge.to === obj.relacion[a])) ||
               (!edges.find(edge => edge.from === obj.relacion[a] && edge.to === obj.id)) ){
            var objw = { "from": obj.id, "to" : obj.relacion[a], "length": LENGTH_MAIN,  font: {align: 'middle'} };
            edges[e] = objw ;
            e = e + 1;
            }

            j = data2.length;
            //console.log(j);
            data2[j] = cat;
          }
            //console.log("CONTADOR:",a,"--CATEGORIA:",obj.relacion[a],"ID:",obj.id)
            //console.log("ID:",obj.id,"CATEGORIA;",obj.relacion[a]);
            testr(obj.relacion[a],nodos,obj.id);

        }
      }else if (index > -1 && data2.find(libro => libro.id === nodos[key2].id)) {

        //console.log(edges);
        if(!edges.find(edge => edge.from === nodo && edge.to === nodos[key2].id) ){
           //console.log(nodo,nodos[key2].id);
          var objw = { "from": nodo, "to" : nodos[key2].id, "length": LENGTH_MAIN,  font: {align: 'middle'} };
          edges[e] = objw ;
          e = e + 1;
        }
      }
    });
}

function buscar(){

      var ref = new Array();
      titulo = document.getElementById("libro").value;
      k=0;
      e=0;
      data2=[];
      edges=[];
      //console.log(titulo);
      ref   = test(titulo);
      // console.log("Referencia:",ref);
      nodes = new vis.DataSet(ref[0]);
      edges = new vis.DataSet(ref[1]);
      console.log('SOY SOLO SEARCH()');
      console.log(nodes.length);
      console.log(titulo.length);
      if (nodes.length > 1){
        network.setData({nodes:nodes, edges:edges})
      } else {
        if(titulo.length == 0){
          window.location = 'http://127.0.0.1:8000/nodos/constelaciones/';
        } else {
          window.location = 'http://127.0.0.1:8000/nodos/lista/';
        }
      }
      // if (nodos.length == 0 ){
      //   window.location = 'http://127.0.0.1:8000/nodos/lista/';
      // } else {
      //   network.setData({nodes:nodes, edges:edges})  
      // }
}

function bInicio(){

  var ref = new Array();
  
  titulo = document.getElementById("qss").value;
  console.log(titulo)
  k=0;
  e=0;
  data2=[];
  edges=[];
  //console.log(titulo);
  ref   = test(titulo);
  // console.log("Referencia:",ref);
  nodes = new vis.DataSet(ref[0]);
  edges = new vis.DataSet(ref[1]);
  console.log(nodes,edges);
  console.log(nodes.length);
  console.log(titulo);

  if (titulo.length == 0 ){
    window.location = 'http://127.0.0.1:8000/nodos/constelaciones/';
  } else {
    if (nodes.length == 0 ){
      window.location = 'http://127.0.0.1:8000/nodos/lista/';
    } else {
      network.setData({nodes:nodes, edges:edges})
      }
  }
}
