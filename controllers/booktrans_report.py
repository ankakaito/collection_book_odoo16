from odoo import http
from odoo.http import content_disposition, request
import io
import xlsxwriter

class ReportExelTransBook(http.Controller):
    @http.route(['/collection_book/book_transaction_report_execl/<model("book.transaction"):data>',],type='http', auth="user", csrf=False)
    def get_booktrans_excel_report(self, data=None, **args):
        response = request.make_respondse(
            none,
            headers=[
                ('Content-Type', 'application/vnd.ms-excel'),
                ('Content-Disposition', content_disposition('Transaction Book Report' + '.xlsx'))
            ]
        )
        # For Object WorkBook from Xlsxwriter Library
        output = io.BytesIO()
        workbook = xlswriter.Workbook(output, {'in_memmory: True'})

        # For sytle to managing Font and aligment
        upper_style = workbook.add_format({'font_name': 'Times', 'bold': True, 'align': 'left'})
        upper_content_style = workbook.add_format({'font_name': 'Times', 'bold': False, 'align': 'left'})
        header_style = workbook.add_format({'font_name': 'Times', 'bold': True, 'left': 1, 'bottom': 1, 'right': 1, 'top': 1, 'align': 'center'})
        text_style = workbook.add_format({'font_name': 'Times', 'bold': False, 'left': 1, 'bottom': 1, 'right': 1, 'top':1, 'align':'left'})

        # Looping the choosing from model
        for upper in data:
            # for worksheet / tab
            sheet = workbook.add_worksheet(upper.name)

            # set orientation becoming landscape
            sheet.set_lanscape()
            # Papper setup
            sheet.set_paper(9)
            #set paper margin in inchi
            sheet.set_margins(0.5, 0.5, 0.5, 0.50)
            #set witdh column
            sheet.set_column('A:A', 10)
            sheet.set_column('B:B', 55)
            sheet.set_column('C:C', 5)
            # Title Setup
            sheet.merge_range('A1:B1', 'Name', upper_style)
            sheet.merge_range('A2:B2', 'Date', upper_content_style)

            # set for upper content
            sheet.write(0, 2, upper.name, upper_style)
            sheet.write(1, 2, upper.date, upper_style)

            # set title table
            sheet.write(3, 0, 'No', header_style)
            sheet.write(3, 1, 'Serial Number', header_style)
            sheet.write(3, 2, 'Book Title', header_style)
            sheet.write(3, 3, 'Qty', header_style)

            rom = 4
            number = 1

            # find transaction line
            recod_line = request.env['book.transaction.line'].search([('management_id', '=', upper.id)])
            for line in record_line:
                sheet.write(row, 0, number, text_style)
                sheet.write(row, 1, line.management_id, text_style)
                sheet.write(row, 2, line.book_title, text_style)
                sheet.write(row, 3, line.qty, text_style)

                row += 1
                number += 1
        workbook.close()
        output.seek(0)
        response.stream.write(output.read())
        output.close()
        return response

