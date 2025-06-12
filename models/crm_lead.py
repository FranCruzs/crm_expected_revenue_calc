from odoo import models, fields, api

class CrmLead(models.Model):
    _inherit = 'crm.lead'
    
    expected_revenue = fields.Monetary(
        string="Expected Revenue",
        currency_field='company_currency',
        tracking=True,
        help="Ingrese manualmente o se calculará automáticamente al presionar Actualizar en etapa 41"
    )

    def action_update_expected_revenue(self):
        """Calcula automáticamente el expected_revenue cuando stage_id == 41"""
        for lead in self:
            if lead.stage_id.id == 41:
                total = 0.0
                for order in lead.order_ids.filtered(lambda o: o.state in ['sale', 'done']):
                    if order.tax_totals:
                        total += order.tax_totals.get('amount_untaxed', 0.0)
                lead.expected_revenue = total
        return True
