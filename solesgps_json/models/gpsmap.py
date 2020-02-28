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
        vehicle_obj     =self.env['fleet.vehicle']
        
        vehicle_args    =[]
        vehicle_data    =vehicle_obj.search(vehicle_args, offset=0, limit=None, order=None)

        url = "http://solesgps.com/sitio_web/ajax/odoo.php?key=asfasfasf"
        req = requests.get(url)
        req.raise_for_status()
        json_positions = req.json()
        for position_row in json_positions: 
            print("===========================")
            print(position_row)           
            for vehicle in vehicle_data:        
                print("VEHICULO=================",vehicle['imei'])
            
                if(position_row['uniqueid']==vehicle['imei']):
                    print("CREANDO POSITIONS")
                    data_create={}        
                    data_create['protocol']     =position_row['protocol']
                    data_create['deviceid']     =vehicle['id']
                    data_create['servertime']   =position_row['servertime']
                    data_create['devicetime']   =position_row['devicetime']
                    data_create['fixtime']      =position_row['fixtime']
                    data_create['valid']        =position_row['valid']
                    data_create['latitude']     =position_row['latitude']
                    data_create['longitude']    =position_row['longitude']
                    data_create['altitude']     =position_row['altitude']
                    data_create['speed']        =position_row['speed']
                    data_create['course']       =position_row['course']
                    data_create['address']      =position_row['address']
                    data_create['attributes']   =position_row['attributes']
                    data_create['other']        =position_row['other']
                    data_create['leido']        =position_row['leido']
                    data_create['event']        =position_row['event']
                    
                    self.create(data_create)    

