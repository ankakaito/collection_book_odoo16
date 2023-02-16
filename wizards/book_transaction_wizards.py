from datetime import date
from io import BytesIO
from tokenize import group
import xlsxwriter
from xlsxwriter.utility import xl_col_to_name as xcol
from odoo import api, fields, models
from odoo import api, fields, models
from odoo.exceptions import ValidationError


class WizardBookTransaction(models.TransientModel):
    _name = 'wizard.book.transaction'
    _description = 'Sales Consolidation Report'

    date_from = fields.Date('Date From')
    date_to = fields.Date('Date To')

    def button_print(self):
        """ function to print report """
        self.ensure_one()
        date_from = self.date_from.strftime("%d/%m/%Y")
        date_to = self.date_to.strftime("%d/%m/%Y")
        # url http://localhost:8001/xls_report/wizard.book.transaction/9/Report%20Book%20Transaction
        name = 'Report Book Transaction'
        return {
            'type': 'ir.actions.act_url',
            'url': '/xls_report/%s/%s/%s' % (self._name, self.id, name),
            'target': 'new',
        }

    def _generate_headers(self):
        """ function to get list of headers """
        return [
            'No','Transaction Number', 'Member', 'Borrowing Date', 'Returning Date'
        ]

    def _prepare_report_data(self):
        """ function to prepare report data containing list of dict """
        result = []
        data = self.env['book.transaction'].search([
            ('borrowing_date', '>=', self.date_from),
            ('borrowing_date', '<=', self.date_to)
        ])
        i = 0
        for record in data:
            i += 1
            values = {
                'no': i,
                'name': record.name,
                'member': record.member_id.name,
                'borrowing_date': record.borrowing_date.strftime("%d/%m/%Y"),
                'returning_date': record.returning_date.strftime("%d/%m/%Y")
            }
            result.append(values)
        return result

    def get_xlsx(self, response, data={}):
        """ function to generate xls report """
        fp = BytesIO()
        wb = xlsxwriter.Workbook(fp)
        ws = wb.add_worksheet('Book Transaction')

        # styles
        table_header = wb.add_format({
            'valign': 'vcenter', 'font_size': 10, 'font_name': 'Calibri',
            'align': 'center', 'bg_color': 'white', 'bold': True, 'border': 1,
        })

        table_normal = wb.add_format({
            'valign': 'vcenter', 'font_size': 10, 'font_name': 'Calibri',
            'align': 'left', 'bg_color': 'white', 'border': 1,
        })

        headers = self._generate_headers()
        row = col = 0

        for idx, header in enumerate(headers):
            ws.write(row, col + idx, header, table_header)

        row += 1
        for dt in data:
            for idx, value in enumerate(dt.values()):
                ws.write(row, col + idx, value, table_normal)
            row += 1

        wb.close()
        fp.seek(0)
        response.stream.write(fp.read())
        fp.close()
