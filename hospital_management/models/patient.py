
from odoo import fields, models


class Patient(models.Model):
    _name = "patient.patient"
    _description = 'My Patient Module'
    _rec_name = 'patient_name'

    patient_name = fields.Char(string="Patient Name", required=True)
    patient_surname = fields.Text(string='Patient_Surname')
    patient_address = fields.Text(string='Patient_Address')
    patient_sex = fields.Selection(
        [('M', 'Male'), ('F', 'Female')], string='Gender Selection')

    patient_nationality = fields.Char(string="Nationality")
    patient_age = fields.Integer(string="Age")
    patient_photo = fields.Image(string="Patient Photo")
    patient_phone = fields.Integer(string="Phone Number", size="10")
    patient_height = fields.Integer(string="Patient height(cm)")
    patient_weight = fields.Integer(string="Phone Weight(kg)")
    patient_DOB = fields.Date(string="Patient Birthdate")
    patient_joindate = fields.Date(string="Patient Joindate")
    treatment_ids = fields.One2many(
        'treatment.treatment', 'patient_id', string="Treatment ID")
    my_treatment_id = fields.Many2one(
        'treatment.treatment', string="Treatment Id")

    def smartbutton(self):
        return {
            'name': ('Treatment'),
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'treatment.treatment',
            'view_id': False,
            'type': 'ir.actions.act_window',
            'target': 'new'
        }

    def smartbutton1(self):
        return {
            'name': ('Doctor'),
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'doctor.doctor',
            'view_id': False,
            'type': 'ir.actions.act_window',
            'target': 'new'
        }

    def _find_mail_template(self, force_confirmation_template=False):
        template_id = False
        if force_confirmation_template:
            template_id = int(self.env['ir.config_parameter'].sudo(
            ).get_param('sale.default_confirmation_template'))
            template_id = self.env['mail.template'].search(
                [('id', '=', template_id)]).id
            if not template_id:
                template_id = self.env['ir.model.data'].xmlid_to_res_id(
                    'sale.mail_template_sale_confirmation', raise_if_not_found=False)
        if not template_id:
            template_id = self.env['ir.model.data'].xmlid_to_res_id(
                'sale.email_template_edi_sale', raise_if_not_found=False)

        return template_id

    def action_quotation_send(self):
        self.ensure_one()
        template_id = self._find_mail_template()
        lang = self.env.context.get('lang')
        template = self.env['mail.template'].browse(template_id)
        if template.lang:
            lang = template._render_template(
                template.lang, 'sale.order', self.ids[0])
        ctx = {
            'default_model': 'sale.order',
            'default_res_id': self.ids[0],
            'default_use_template': bool(template_id),
            'default_template_id': template_id,
            'default_composition_mode': 'comment',
            'mark_so_as_sent': True,
            'custom_layout': "mail.mail_notification_paynow",
            'proforma': self.env.context.get('proforma', False),
            'force_email': True,
            'model_description': self.with_context(lang=lang).type_name,
        }
        return {
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'mail.compose.message',
            'views': [(False, 'form')],
            'view_id': False,
            'target': 'new',
            'context': ctx,
        }
