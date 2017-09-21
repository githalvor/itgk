Python 3.5.3 (default, Jan 19 2017, 14:11:04) 
[GCC 6.3.0 20170118] on linux
Type "copyright", "credits" or "license()" for more information.
>>> 



<%@include file="headermeny.jsp"%>

<%
String navn = request.getParameter("Navn");
String epost = request.getParameter("E-post");
String karakter = request.getParameter("Karakter");
String melding = request.getParameter("Melding");

String name;

if ( navn.equals("Christian")) {
	name = "Næmmen, Christian! Dææven schteike, så kult navn!";
}
else if ( navn.equals("") ) {
	name = "Har du ikke noe navn du da? Stakkars liten!";
}
else  {
	name = navn;
}

String grade;

if ( karakter.equals("1") ) {
	grade = "1! Hæ?! Skjer med å være gjerrig a?!<br> (OK, siden det var en oppgave i ITGK: 'Beklager at siden var dårlig...')";
}
else if ( karakter.equals("5") ) {
	grade = "5! Tusen takk, alltid kos med ros!";
}
else  {
	grade = karakter;
}

String message;

if ( (melding.equals("Hei Christian! Jeg digget denne siden, fordiii...")) ){
	message = "Det hadde jo vært hyggelig om du skrev noe selv da...";
}

else {
	message = melding;
}
%>

<h1> Takk for hilsen, <%= navn %>!</h1>
<p>
<table border="0" cellspacing="0" cellpadding="10">
 <tr>
	<th>Navn:</th>
	<td><%= name %></td>
 </tr>
 <tr>
	<th>E-post:</th>
	<td><%= epost %></td>
 </tr>
 <tr>
	<th>Karakter:</th>
	<td><%= grade %></td>
 </tr>
 <tr>
	<th>Melding:</th>
	<td><%= message %></td>
 </tr>
</table>

<%@include file="tail.jsp"%>
