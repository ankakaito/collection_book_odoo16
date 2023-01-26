# -*- coding: utf-8 -*-
# from odoo import http


# class CollectionBook(http.Controller):
#     @http.route('/collection_book/collection_book/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/collection_book/collection_book/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('collection_book.listing', {
#             'root': '/collection_book/collection_book',
#             'objects': http.request.env['collection_book.collection_book'].search([]),
#         })

#     @http.route('/collection_book/collection_book/objects/<model("collection_book.collection_book"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('collection_book.object', {
#             'object': obj
#         })
