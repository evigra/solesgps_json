# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
import json
import requests
from dateutil.relativedelta import relativedelta
from odoo import api, fields, models, _
class positions(models.Model):
    _inherit = "gpsmap.positions"

    def run_scheduler_get_position(self):
        #positions_obj   =self.env['gpsmap.positions']        
        vehicle_obj                             =self.env['fleet.vehicle']
        
        vehicle_args                            =[]
        vehicle_data                            =vehicle_obj.search(vehicle_args, offset=0, limit=None, order=None)

        url                                     = "http://solesgps.com/sitio_web/ajax/odoo.php?key=asfasfasf"
        req                                     = requests.get(url)
        req.raise_for_status()
        json_positions                          = req.json()
        for position_row in json_positions: 
            #print(position_row)           
            for vehicle in vehicle_data:        
                #print("VEHICULO=================",vehicle)
                if(position_row['uniqueid']==vehicle['imei']):
                    print("CREANDO POSITIONS")
                    position_create={}        
                    position_create['protocol']     =position_row['protocol']
                    position_create['deviceid']     =vehicle['id']
                    position_create['servertime']   =position_row['servertime']
                    position_create['devicetime']   =position_row['devicetime']
                    position_create['fixtime']      =position_row['fixtime']
                    position_create['valid']        =position_row['valid']
                    position_create['latitude']     =position_row['latitude']
                    position_create['longitude']    =position_row['longitude']
                    position_create['altitude']     =position_row['altitude']
                    position_create['speed']        =position_row['speed']
                    position_create['course']       =position_row['course']
                    position_create['address']      =position_row['address']
                    position_create['attributes']   =position_row['attributes']
                    position_create['other']        =position_row['other']
                    position_create['leido']        =position_row['leido']
                    position_create['event']        =position_row['event']
                    
                    self.create(position_create)    
                    
                    positions_data                         =self.search([], offset=0, limit=1, order='devicetime DESC')        
                    print(positions_data)
