$(function(){


  // Création de la base de donnée
  /*function create_table(fichier) {
    $.ajax({
      // chargement du fichier externe
      url      : "http://localhost:8080/create/"+fichier,
      // Passage des données au fichier externe
      type : 'GET',
      error    : function(request, error) { // Info Debuggage si erreur
        alert("Erreur " + fichier + ": responseText: "+request.responseText);
      },
      success  : function(data) {
        alert("La base de donnée de " + fichier + " est à jour");
      }
    });
  }
  $("#create_installation").on("click", function() {
    create_table("installations");
  });
  $("#create_activitie").on("click", function() {
    create_table("activites");
  });
  $("#create_equipment").on("click", function() {
    create_table("equipements");
  });*/

  min =0;
  max = 10;


  //Remplir les champs du formulaire au lancement de la page
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

  //Affichage sur les tables
  function display_table(fichier) {
    $.ajax({
      // chargement du fichier externe
      url      : "http://localhost:8080/display/"+fichier,
      // Passage des données au fichier externe
      cache    : false,
      dataType : "json",
      error    : function(request, error) { // Info Debuggage si erreur
        alert("Erreur : responseText: "+request.responseText);
      },
      success  : function(data) {

        var result = [];
        var table = [];
        var html = "";
        var entete = [];
        for (var i in data[0])
        entete.push(i);

        for(var i in data){
          for(var j in data[i]){
            result.push([data[i][j]]);
          }
          table.push(result);
          result = [];
        }

        html+= "<thead><tr>"
        html += "<th>indice</th>";
        $.each(entete, function(i) {
          html += "<th>"+entete[i]+"</th>";
        });

        html+= "</tr></thead>"

        $.each(table, function(i) {
          if(i < max && i >= min){
            html += "<tr>";
            html += "<td>"+(i+1)+"</td>";
            $.each(table[i], function(j) {
              html += "<td>"+table[i][j]+"</td>";
            });
            html += "</tr>";
          }
        });

        $("#display_"+fichier).html(html);
      }
    });
  }
  //affichage activités
  $("#button_display_activitie").on("click", function() {
    display_table("activites");
  });
  //affichage installations
  $("#button_display_installation").on("click", function() {
    display_table("installations");
  });
  //affichage équipements
  $("#button_display_equipment").on("click", function() {
    display_table("equipements");
  });



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
        } else {
          init_button();
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

  var min = 0;
  var max = 10;
  $("#inc_act").css({"display":"none"});
  $("#dec_act").css({"display":"none"});

  function init_button() {
   min = 0;
   max = 10;
   $('#dec_act').prop('disabled', true);
   $('#inc_act').prop('disabled', false);
   $("#inc_act").css({"display":"block"});
   $("#dec_act").css({"display":"block"});
 }
 function incr() {
   $('#dec_act').prop('disabled', false);
   min += 100;
   max += 100;
 }
 function decr() {
   min -= 100;
   max -= 100;
   if(min == 0)
   $('#dec_act').prop('disabled', true);
   $('#inc_act').prop('disabled', false);
 }

});
