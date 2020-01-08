# -*- coding: utf-8 -*-
# from odoo import http


# class Library-app(http.Controller):
#     @http.route('/library-app/library-app/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/library-app/library-app/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('library-app.listing', {
#             'root': '/library-app/library-app',
#             'objects': http.request.env['library-app.library-app'].search([]),
#         })

#     @http.route('/library-app/library-app/objects/<model("library-app.library-app"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('library-app.object', {
#             'object': obj
#         })
