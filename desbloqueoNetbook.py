#!/usr/bin/env python
# coding: latin-1


import string
import requests
import re
from configuration import adminPass, adminUser

##############################################
#
# CSS and HTML template
#
##############################################
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


@media (min-device-width:600px) {
    img[data-src-600px] {
        content: attr(data-src-600px, url);
    }
}

@media (min-device-width:800px) {
    img[data-src-800px] {
        content: attr(data-src-800px, url);
    }
}

}
</style>
"""
##########################################################
# HTML Template
##########################################################
headHTML = """Content-type: text/html; charset=utf-8

<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//ES">
<html>
<head>
"""
        
metaHTML = """<meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no">
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
<meta name="HandheldFriendly" content="true">"""

titleHTML = """<title>Instituto de Formación Docente Contínua - Villa Mercedes</title></head>"""

contentAndClosing = """<body>
REPLACE_CONTENT
<h4>¿Dónde encuentro el ID de Hardware y la marca de arranque?</h4>
<p> Utilizar la siguiente figura como ayuda:</p>
<img src="http://desbloqueo.serverifdcvm.sytes.net/ddata/images/ayuda.jpg"
     data-src-600px="http://desbloqueo.serverifdcvm.sytes.net/ddata/images/ayuda-600px.jpg"
     data-src-800px="http://desbloqueo.serverifdcvm.sytes.net/ddata/images/ayuda-800px.jpg"
     alt="Imagen explicativa de Código Único de Hardware y Marca de Arranque.">
</body>
</html>"""
################################################################
# Use it as:htmlOutput('REPLACE_CONTENT','new content ...')
htmlOutput =  headHTML + styleCSS + metaHTML + titleHTML + contentAndClosing    
################################################################

#hwid=raw_input("Ingrese Codigo de hardware: ")
#btick=raw_input("ingrese marca de arranque: ")
def createKeyUnblock(hwid, btick):
    notExistRegex = re.compile(r'error_notexist')
    url='http://172.16.0.2/tdserver/login_deal.jsp'
    urlHID = 'http://172.16.0.2/tdserver/Device Admin/boot_tick.jsp'
    urlKey = 'http://172.16.0.2/tdserver/Device Admin/fetch_key_deal.jsp'
    payload = {'password': '{}'.format(adminPass), 'operatorName': '{}'.format(adminUser)}
    hwidBootick={'HWID':hwid, 'bootTick': btick}
    s = requests.Session()
    p = s.post(url, data=payload)
    # print the html returned or something more intelligent to see if it's a successful login page.
    #print p.text
    # An authorised request.
    p = s.post('http://172.16.0.2/tdserver/Device Admin/boot_tick.jsp', data=hwidBootick)
    r = s.post(urlKey,data=hwidBootick)
    if len(notExistRegex.findall(r.content)) > 0:
	content = "No se encuentran registros para el ID de hardware {}".format(hwid)
	output = htmlOutput.replace('REPLACE_CONTENT',content)
    else:
        output = r.content

    with open('/var/www/ddata/codigo{}.html'.format(hwid),'w') as f:
        f.write(output)

    return output

##########################################################
# HTML Template
##########################################################
headHTML = """Content-type: text/html; charset=utf-8

<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//ES">
<html>
<head>
"""
        
metaHTML = """<meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no">
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
<meta name="HandheldFriendly" content="true">"""

titleHTML = """<title>Instituto de Formación Docente Contínua - Villa Mercedes</title></head>"""

contentAndClosing = """<body>
REPLACE_CONTENT
<h4>¿Dónde encuentro el ID de Hardware y la marca de arranque?</h4>
<p> Utilizar la siguiente figura como ayuda:</p>
<img src="http://desbloqueo.serverifdcvm.sytes.net/ddata/images/ayuda.jpg"
     data-src-600px="http://desbloqueo.serverifdcvm.sytes.net/ddata/images/ayuda-600px.jpg"
     data-src-800px="http://desbloqueo.serverifdcvm.sytes.net/ddata/images/ayuda-800px.jpg"
     alt="Imagen explicativa de Código Único de Hardware y Marca de Arranque.">
</body>
</html>"""
################################################################
# Use it as:htmlOutput('REPLACE_CONTENT','new content ...')
htmlOutput =  headHTML + styleCSS + metaHTML + titleHTML + contentAndClosing    
################################################################

#hwid=raw_input("Ingrese Codigo de hardware: ")
#btick=raw_input("ingrese marca de arranque: ")
def createKeyUnblock(hwid, btick):
    notExistRegex = re.compile(r'error_notexist')
    url='http://172.16.0.2/tdserver/login_deal.jsp'
    urlHID = 'http://172.16.0.2/tdserver/Device Admin/boot_tick.jsp'
    urlKey = 'http://172.16.0.2/tdserver/Device Admin/fetch_key_deal.jsp'
    payload = {'password': '{}'.format(adminPass), 'operatorName': '{}'.format(adminUser)}
    hwidBootick={'HWID':hwid, 'bootTick': btick}
    s = requests.Session()
    p = s.post(url, data=payload)
    # print the html returned or something more intelligent to see if it's a successful login page.
    #print p.text
    # An authorised request.
    p = s.post('http://172.16.0.2/tdserver/Device Admin/boot_tick.jsp', data=hwidBootick)
    r = s.post(urlKey,data=hwidBootick)
    if len(notExistRegex.findall(r.content)) > 0:
	content = "No se encuentran registros para el ID de hardware {}".format(hwid)
	output = htmlOutput.replace('REPLACE_CONTENT',content)
    else:
        output = r.content

    with open('/var/www/ddata/codigo{}.html'.format(hwid),'w') as f:
        f.write(output)

    return output
