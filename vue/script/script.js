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

  /*
  //Remplir les champs du formulaire au lancement de la page
  $.ajax({
      // chargement du fichier externe
      url      : "http://localhost:8080/fill_form",
      // Passage des données au fichier externe
      cache    : false,
      dataType : "json",
      error    : function(request, error) { // Info Debuggage si erreur
        alert("Erreur : responseText: "+request.responseText);
      },
      success  : function(data) {
        alert("success");
      }
  })*/


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
        $.each(entete, function(i) {
          html += "<th>"+entete[i]+"</th>";
        });

        html+= "</tr></thead>"

        $.each(table, function(i) {
          if(i < max && i >= min){
            html += "<tr style=\"cursor:pointer;\" class=\"select_equipement\">";
            $.each(table[i], function(j) {
              html += "<td>"+table[i][j]+"</td>";
            });
            html += "</tr>";
          }
        });

        $("#display_activites").html(html);

        //requête activités
        $(".select_equipement").on("click", function() {
          alert("test");
          activity_code = "69882";
          select_equipement(activity_code);
        });
      }
    });
  }
  //requête activités
  $("#button_select_activitie").on("click", function() {
    select_activites();
  });


  //requête sur equipements
  function select_equipement(activity_code) {
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
        alert("success");
      }
    });
  }
  /*le listener des éléments qui déclenchent la fonction select_equipement() 
  sont plus haut à la fin de la fonction select_activites()*/

});
