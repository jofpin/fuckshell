#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       fwshell.py
#       
#       Copyright 2013 Fraph <jfraph@gmail.com>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#    This program is free software: you can redistribute it and/or modify 
#    it under the terms of the GNU General Public License as published by   
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version. 
#   
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of 
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.         
#                                                         
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>
#  
#                                   ###################
#                                   #     Fraph       #
############################################X###########               
#                                                     ##
#  ___________         _____        .__                #
#  \_   _____/______  /  |  |______ |  |__             #
#   |    __) \_  __ \/   |  |\____ \|  |  \            #
#   |     \   |  | \/    ^   /  |_> >   Y  \           #
#   \___  /   |__|  \____   ||   __/|___|  /           #
#       \/               |__||__|        \/            ##                 
#                                                       ##
# Independent Security Researcher                        ##
# Copyright - Fraph                                      ##
# @Fr4phc0r3                                             #########
#                                                       ## V1.0  #
##################################################################    
#
##                                    #----->>>|Fwshell|===============>
 #######################################                                 ==> Detected.
##                                    #----->>>(Escaner De Shell)====>
# 
#
#
#
#
#################
Autor = "Fraph" #
Version = "1.0" #
#################
import os     #
import sys    #
import robots #
import urllib2#
import re     #
###############
if "linux" in sys.platform:
    os.system("clear")
elif "win" in sys.platform:
    os.system("cls")
else:
    pass
    #Colores
class color:
    azul = '\033[94m'
    verde = '\033[92m'
    blanco = '\033[0m'
def escaneo():
        global url
        global coneccion_url 
        motor=[]  
        avanze=[] 
        flowviolento=[] 
        with open('diccionario.txt') as f:
                lines = f.readlines()
                for line in lines:
                        try:
                                coneccion_url=url+line
                                r = urllib2.Request(coneccion_url)
                                r.add_unredirected_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 6.0;en-US; rv:1.9.2) Gecko/20100115 Firefox/3.6')#UserAgent
                                r.add_unredirected_header('Referer', 'http://www.google.com/')#Referer
                                req=urllib2.urlopen(r)
                                resp=req.read()
                                if req.getcode()==200:
                                        print '\033[1;32m[+] Posible WebShell Detectada =>\033[1;m ' + coneccion_url,
                                        motor.append(coneccion_url+str(len(resp)))
                                else:
                                        print '\033[1;32m[+] Redirecciones\033[1;m ' + coneccion_url,
                                        flowviolento.append(coneccion_url) 
                        except urllib2.HTTPError as e:
                                if e.code == 401:
                                        print '\033[1;32m[+] Posible Sospecha =>\033[1;m ' + coneccion_url,
                                        avanze.append(coneccion_url)
                                elif e.code == 404:
                                        print '\033[1;31m[-] Shell no Encontrada =>\033[1;m ' + coneccion_url,
                                elif e.code == 503:
                                        print '\033[1;31m[-] Servicio no disponible\033[1;m ' + coneccion_url,
                                else:
                                        print '\033[1;32m[+] Redirecciones\033[1;m ' + coneccion_url,
                                        flowviolento.append(coneccion_url)
                print ''                        
                print color.azul + "\t\t########################>\033[1;33mFWEBSHELL\033[94m<##########################" + color.blanco
                print color.azul + "\t\t#               Developed By: @Fr4phc0r3                    #" + color.blanco
                print color.azul + "\t\t##+                        V1.0                           +##" + color.blanco
                print color.azul + "\t\t##+         #################################             +##" + color.blanco
                print color.azul + "\t\t#           #      Escaneo Finalizado       #               #" + color.blanco
                print color.azul + "\t\t#############################################################\n" + color.blanco               
                print ''
                print  '\033[1;32mResultados: \033[1;m '
                print '\033[94m==================================================================\033[1;m '
                if motor:
                        print "\033[1;33mPosibles Archivos Maliciosos\033[1;m"
                        for c0r3 in motor:
                                print c0r3,
                        print '\033[94m================================================================\033[1;m '
                if avanze:
                        print "\033[1;33mPosibles WebShell Detectadas:\033[1;m"
                        for botella in avanze:
                                print botella,
                        print '\033[94m==================================================================\033[1;m'
                if flowviolento:
                        print "Estados de otros resultados (robots.txt)"
                        for reconecciones in flowviolento:
                                print reconecciones,
                        print '\033[94m===================================================================\033[1;m'
def validacion():
        global url
        url=raw_input("Ingresa La Direccion URL==> ")
        if url.endswith("/"):
                print ""
                print color.azul + "\t\t########################>FWEBSHELL<##########################" + color.blanco
                print color.azul + "\t\t#                                                           #" + color.blanco
                print color.azul + "\t\t#               Developed By: @Fr4phc0r3                    #" + color.blanco
                print color.azul + "\t\t##+                        V1.0                           +##" + color.blanco
                print color.azul + "\t\t##+            Cwhp Lab`s  www.ccat.edu.mx                +##" + color.blanco
                print color.azul + "\t\t#           #################################               #" + color.blanco
                print color.azul + "\t\t#           #  Escaner Detector de WebShell #               #" + color.blanco
                print color.azul + "\t\t#############################################################" + color.blanco
                print ""
                print color.verde + "=> Escaneando: Web...\n" + color.blanco
                pass 
        else:
                url=url+"/"
        if re.match('((https?):((//)|(\\\\))+([\w\d:#@%/;$()~_?\+-=\\\.&](#!)?)*)',url): #Expresiones Regulares (regexp)
                pass
        else:
                validacion()
                
if __name__ == '__main__':
        try:
                validacion()
                escaneo()
                robots.robots(url)
        except KeyboardInterrupt:
                pass
        except Exception as e:
                print "Un Fallo en la Tool: %s" % e #Invalidez


