from osv import osv,fields
# import openerp


class ptr_typeptrgeo(osv.osv):
    _name= 'ptr.typeptrgeo'
    _columns={
        'code':fields.char('Code',size=255)  ,
        'libelle':fields.char('Libelle',size=255)
    }


ptr_typeptrgeo()