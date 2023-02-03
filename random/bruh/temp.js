$(document).ready(function(){
    $('#quote-box').myfunction();
});
$("button").click(function(){
    $('#quote-box').myfunction();
});
	
(function( $ ){
   $.fn.myfunction = function() {
       $.getJSON('https://gist.githubusercontent.com/camperbot/5a022b72e96c4c9585c32bf6a75f62d9/raw/e3c6895ce42069f0ee7e991229064f167fe8ccdc/quotes.json', function (data) {
           let x = Math.floor(Math.random() * 100);
           let quote = JSON.stringify(data['quotes'][x]['quote']);
           let author = JSON.stringify(data['quotes'][x]['author']);
           $('#text').text(quote);
           $('#author').text(author);
       });
   }; 
})( jQuery );