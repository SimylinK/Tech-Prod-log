$(function(){

  //setting for the menu on the left
  $("#div-menu").hide();

  $("#menu").on('click', function() {
    $('#menu').hide('fast');
    $("#div-menu").show("fast");
    $("#menu").css("z-index", "1");
    $("#div-menu").css("z-index", "2");
  });

  $("#close-menu").on('click', function() {
    $("#div-menu").hide("fast");
    $('#menu').show('fast');
    $("#div-menu").css("z-index", "1");
    $("#menu").css("z-index", "2");
  });

  //The increment and decrement buttons for the navigation in the table
  //We display 6 elements
  var min = 0;
  var max = 6;
  //When no result, buttons are hidden
  $("#inc_act").css({"display":"none"});
  $("#dec_act").css({"display":"none"});

  function init_button() {
   min = 0;
   max = 6;
   $('#dec_act').prop('disabled', true);
   $('#inc_act').prop('disabled', false);
   $("#inc_act").css({"display":"block"});
   $("#dec_act").css({"display":"block"});
 }
 function incr() {
   $('#dec_act').prop('disabled', false);
   min += 6;
   max += 6;
 }
 function decr() {
   min -= 6;
   max -= 6;
   if(min == 0)
   $('#dec_act').prop('disabled', true);
   $('#inc_act').prop('disabled', false);
 }

 $("#inc_act").on("click", function() {
    incr("act");
    select_activites();
  });
  $("#dec_act").on("click", function() {
    decr("act");
    select_activites();
  });


  //Fill the form fields at the launch of the page
  //champ Commune
  $.ajax({
      // chargement du fichier externe
      url      : "http://localhost:8080/fill_form/commune",
      // Passage des données au fichier externe
      cache    : false,
      dataType : "json",
      error    : function(request, error) { // Info Debuggage si erreur
        alert("Erreur : responseText: "+request.responseText);
      },
      success  : function(data) {
        var result = [];
        var listeCom = [];

        for(var i in data){
          for(var j in data[i]){
            result.push([data[i][j]]);
          }
          listeCom.push(result);
          result = [];
        }

        $.each(listeCom, function(i) {
          //console.log(listeCom[i][0]);
          $('#commune').append('<option value="'+listeCom[i][0]+'">' + listeCom[i][0] + '</option>');
        });
      }
  })
  //champ Activite
    $.ajax({
      // chargement du fichier externe
      url      : "http://localhost:8080/fill_form/activity",
      // Passage des données au fichier externe
      cache    : false,
      dataType : "json",
      error    : function(request, error) { // Info Debuggage si erreur
        alert("Erreur : responseText: "+request.responseText);
      },
      success  : function(data) {
        var result = [];
        var listeAct = [];

        for(var i in data){
          for(var j in data[i]){
            result.push([data[i][j]]);
          }
          listeAct.push(result);
          result = [];
        }

        $.each(listeAct, function(i) {
          //console.log(listeCom[i][0]);
          $('#activite').append('<option value="'+listeAct[i][0]+'">' + listeAct[i][0] + '</option>');
        });
      }
  })


  //requête sur activites
  function select_activites() {
    name_commune = $("#commune").val();
    number_equipment = $("#nb_equipements").val();
    activitie = $("#activite").val();
    activitie = activitie.replace("/", ".");

    special = $("input[name=spe]:checked").val();

    practice = $("input[name=prat]:checked").val();

    $.ajax({
      // chargement du fichier externe
      url      : "http://localhost:8080/request/activites/"+name_commune+"/"+number_equipment+"/"+activitie+"/"+practice+"/"+special,
      // Passage des données au fichier externe
      cache    : false,
      dataType : "json",
      error    : function(request, error) { // Info Debuggage si erreur
        alert("Erreur : responseText: "+request.responseText);
      },
      success  : function(data) {

        //console.log(data);
        var result = [];
        var table = [];
        var html = "";
        var entete = [];
        for (var i in data[0]) {
          //console.log(i);
          entete.push(i);
        }


        var order = [];
        var index = 0;
        $.each(entete, function(i) {
          if (entete[i] == "activite libelle") {
            order[0] = index;
          }
          if (entete[i] == "nom commune") {
            order[1] = index;
          }
          if (entete[i] == "nb equipements identiques") {
            order[2] = index;
          }
          if (entete[i] == "dans salle spe") {
            order[3] = index;
          }
          if (entete[i] == "activite pratiquee") {
            order[4] = index;
          }
          if (entete[i] == "activite praticable") {
            order[5] = index;
          }
          index++;
        });



        html+= "<thead><tr>"
        for(i = 0; i < 6; i++) {
          html += "<th>"+entete[order[i]]+"</th>";
        }
        html+= "</tr></thead>"


        for(var i in data){
          for(j = 0; j < 6; j++) {
            result.push([data[i][entete[order[j]]]]);
          }
          table.push(result);
          result = [];
        }



        var isEmpty = true;

        $.each(table, function(i) {
          isEmpty = false;
          if(i < max && i >= min){
            html += "<tr style=\"cursor:pointer;\" class=\"select_equipement\">";
            $.each(table[i], function(j) {
              html += "<td>"+table[i][j]+"</td>";
            });
            html += "</tr>";
          }
        });

        if(isEmpty) {
          alert("Aucun résultat pour cette recherche");
          html="";
          $("#inc_act").css({"display":"none"});
          $("#dec_act").css({"display":"none"});

        } else {
          if(min == 0) {
            init_button();
          }
        }


        $("#display_activites").html(html);


        //On place un listener sur chaque ligne du tableau
        //il faut le faire ici car la table est créée dans cette fonction et n'existe pas avant son appel
        $.each( $(".select_equipement"), function( i, val ) {
          $(this).on("click", function() {
            activity_code = data[0]["num fiche equipement"];
            console.log(activity_code);
            select_equipement(activity_code);
          });
        });
      }
    });
  }
  //requête activités
  $("#button_select_activitie").on("click", function() {
    select_activites();
  });

  $( "#dialog" ).dialog({
    autoOpen: false,
    resizable: false,
        modal: true,
        width:'auto',
    //on utilise le code suivant pour fixer la fenêtre au centre de l'écran (avec toujours la possibilité de la déplacer)
    open: function(event, ui) {
      $(event.target).dialog('widget')
          .css({ position: 'fixed' })
          .position({ my: 'center', at: 'center', of: window });
  }
  });


  //requête sur equipements
  function select_equipement(activity_code) {

    $("#dialog").html("");

    $.ajax({
      // chargement du fichier externe
      url      : "http://localhost:8080/request/installations/"+activity_code,
      // Passage des données au fichier externe
      cache    : false,
      dataType : "json",
      error    : function(request, error) { // Info Debuggage si erreur
        alert("Erreur : responseText: "+request.responseText);
      },
      success  : function(data) {
        $("#dialog").append("<U>INSTALLATION :</U> <br/>");
        $("#dialog").append("Commune : " + data["0"]["nom commune"] + "<br/>");
        $("#dialog").append("Code postal : " + data["0"]["code postal"] + "<br/><br/>");
      }
    });

    $.ajax({
      // chargement du fichier externe
      url      : "http://localhost:8080/request/equipements/"+activity_code,
      // Passage des données au fichier externe
      cache    : false,
      dataType : "json",
      error    : function(request, error) { // Info Debuggage si erreur
        alert("Erreur : responseText: "+request.responseText);
      },
      success  : function(data) {
        $("#dialog").append("<U>EQUIPEMENT :</U> <br/>");
        $("#dialog").append("Nom : " + data["0"]["eq nom"] + "<br/>");
        $("#dialog").append("Type : " + data["0"]["equipement type lib"] + "<br/> <br/>");
      }
    });

    $("#dialog").dialog( "open" );
  }



});
