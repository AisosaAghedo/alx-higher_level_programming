// script that fetches and lists the title for all movies by using this URL

$.get("https://swapi-api.hbtn.io/api/films/?format=json", function (data) {
 let body = data.results;
 for (let i = 0; i < body.length; i++){
   $("UL#list_movies").append('<li>' + body[i].title +'</li>');
 }
});
