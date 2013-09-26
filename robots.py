#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       robots.py
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
#############
#Visualizacion del archivo robots.txt
import urllib2
def robots(url):
	request_robots= urllib2.urlopen(url+"robots.txt")
	respuesta= request_robots.read()
	print "\033[1;33mContenido del Robots.txt:\033[1;m"
	print respuesta
