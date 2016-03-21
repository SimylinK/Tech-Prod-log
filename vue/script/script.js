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
        var target= $("#"+fichier);
        $('html, body').animate({
          scrollTop: target.offset().top
        }, 1);

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

  $("#button_display_installation").on("click", function() {
    alert("Test1");
    display_table("installations");
    alert("Test2");
  });
  $("#button_display_activitie").on("click", function() {
    display_table("activites");
  });
  $("#button_display_equipment").on("click", function() {
    display_table("equipements");
  });


});
