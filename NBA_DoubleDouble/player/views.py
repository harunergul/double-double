#Http repsone related imports
from django.shortcuts import render
from django.http import HttpResponse

#imports for datescrapping
from lxml import html
from lxml.etree import XPath
import requests

#import for model
from models import Player

#welcome_page view generates initial view for the first time requests
def welcome_page(request):
    context ={}
    return render(request,"index.html",context)

#list_result view generates html page which includes double-dobule data
def list_result(request):
    if request.GET.get("date"):
        #Getting day, month and year values from request to prepare a new request url
        requested_date = request.GET.get("date")
        day, month, year = requested_date.split("/")

        url ="http://www.basketball-reference.com/play-index/pgl_finder.cgi?request=1&match=game&year_min=2016&year_max=2016&age_min=0&age_max=99&pos_is_g=Y&pos_is_gf=Y&pos_is_f=Y&pos_is_fg=Y&pos_is_fc=Y&pos_is_c=Y&pos_is_cf=Y&is_dbl_dbl=Y&order_by=pts"
        day_parameters="&game_day=%s&game_month=%s" %(day,month)
        url=url+day_parameters

        #Defining and initializing xpath values for incoming html response
        all_table_xpath     = XPath('//table/tbody/tr')
        player_name_xpath   = XPath('td[1]/a/text()')
        player_team_xpath   = XPath('td[5]/a/text()')
        opponent_team_xpath = XPath('td[7]/a/text()')
        team_result_xpath   = XPath('td[8]/text()')

        #To get html contents from mentioned website name
        html_result = html.parse(url)

        #Adding required row values to player_list
        player_list = []
        for row in  all_table_xpath(html_result):
            if player_name_xpath(row):
                player = Player()
                player.name   = player_name_xpath(row)[0]
                player.team   = player_team_xpath(row)[0]
                player.opponent_team = opponent_team_xpath(row)[0]
                player.team_result   = team_result_xpath(row)[0]
                player_list.append(player)

        #context is a dictionary which includes data for generating page
        context ={
            "date" : requested_date,
            "player_list" : player_list,

        }
        return render(request,"result.html",context)
    else:
        context ={}
        return render(request,"result.html",context)
