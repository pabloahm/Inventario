# -*- coding: utf-8 -*-

from odoo import models, fields, api

class TipoInsumos(models.Model):
	_name= 'inventario.tipo_insumos'

	name = fields.Char(string = "Nombre", required=True)


class Insumos(models.Model):
	_name = 'inventario.insumos'

	name = fields.Char(string = "Nombre Insumo", requiered = True)

	codigo_insumo = fields.Integer(string = "Codigo Insumo", required = True)
	cantidad_insumo = fields.Integer(string = "Cantidad de insumo", requiered = True)
	codigo_proveedor = fields.Integer(string = "Codigo proveedor", required = True)
	fecha = fields.Date("Fecha operacion")

	tipo_insumos_id = fields.Many2one(
		'inventario.tipo_insumos', string="Tipo de Insumo")
