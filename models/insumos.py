# -*- coding: utf-8 -*-

from odoo import models, fields, api


class TipoInsumos(models.Model):
    _name = 'inventario.tipo_insumos'

    name = fields.Char(string="Nombre", required=True)


class Proveedor(models.Model):
    _name = 'inventario.proveedor'

    name = fields.Char(string="Nombre Proveedor", requiered=True)
    codigo_proveedor = fields.Integer(string="Codigo proveedor", required=True)
    insumos_ids = fields.One2many(
        'inventario.insumos', 'proveedor_id', string="Proveedor")


class Insumos(models.Model):
    _name = 'inventario.insumos'

    name = fields.Char(string="Nombre Insumo", requiered=True)

    codigo_insumo = fields.Integer(string="Codigo Insumo", required=True)
    cantidad_insumo = fields.Integer(string="Cantidad de insumo", requiered=True)
    fecha = fields.Date("Fecha operacion")

    tipo_insumos_id = fields.Many2one(
        'inventario.tipo_insumos', string="Tipo de Insumo")
    proveedor_id = fields.Many2one(
        'inventario.proveedor', string="Codigo Proveedor")
