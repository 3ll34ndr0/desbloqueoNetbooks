#!/usr/bin/env python
# coding: latin-1

import cgi
#import cgitb; cgitb.enable() # for troubleshooting
from desbloqueoNetbook import createKeyUnblock,checkMAC

form = cgi.FieldStorage()
hwid  = form.getvalue("hwid","Ejemplo: 7427EA95FD92 ")
btick = form.getvalue("btick","Ejemplo: 2" )

styleCSS = """<style type="text/css">
html { font-size:100%; } 
img { max-width: 100%; }
body {/* Tablet Landscape */
@media screen and (max-width: 1060px) {
    #primary { width:67%; }
    #secondary { width:30%; margin-left:3%;}  
}

/* Tabled Portrait */
@media screen and (max-width: 768px) {
    #primary { width:100%; }
    #secondary { width:100%; margin:0; border:none; }
}
@media (min-width: 640px) { body {font-size:1rem;} } 
@media (min-width:960px) { body {font-size:1.2rem;} } 
@media (min-width:1100px) { body {font-size:1.5rem;} } 
}
</style>"""


if hwid == "Ejemplo: 7427EA95FD92 ":
	print "Content-type: text/html; charset=utf-8"
	print """
        <!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN">
	<html>
	<head>"""
        print styleCSS
        print """
<meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no">
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
<meta name="HandheldFriendly" content="true">

<title>Instituto de Formación Docente Contínua - Villa Mercedes</title></head>
	<body>

	  <h3> Generación de código de desbloqueo para netbooks </h3>
	   <form method="post" action="ifdcvm.py">
	     <p>ID de Hardware (código unico de hardware): <input type="text" name="hwid" placeholder="{}"/></p>
	     <p>Marca de arranque (Boot tick): <input type="text" name="btick" placeholder="{}"/></p>
	   <input name="hwid,btick" type="submit" class="bt2" value="Aceptar" alt="Aceptar" border=0 >
	   </form>
	<h4>¿Dónde encuentro el ID de Hardware y la marca de arranque?</h4>
<p> Utilizar la siguiente figura como ayuda:</p>
<img src="http://desbloqueo.serverifdcvm.sytes.net/ddata/images/ayuda.jpg"
     data-src-600px="http://desbloqueo.serverifdcvm.sytes.net/ddata/images/ayuda-600px.jpg"
     data-src-800px="http://desbloqueo.serverifdcvm.sytes.net/ddata/images/ayuda-800px.jpg"
     alt="Imagen explicativa de Código Único de Hardware y Marca de Arranque.">
	   </body>
	   </html>""".format(cgi.escape(hwid), cgi.escape(btick))

else:
    try:
        resultado = createKeyUnblock(checkMAC(hwid), btick.upper())
        print "Content-type: text/html; charset=utf-8"
        print resultado
    except ValueError as e:
        print e
