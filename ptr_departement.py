from osv import osv,fields
# import openerp


class ptr_departement(osv.osv):
    _name= 'ptr.departement'
    _columns={
        'name':fields.char('Nom',size=255) ,
        'code':fields.char('Code',size=255)  ,
        'adresse':fields.char('Adresse',size=255)  ,
        'fixe': fields.char('Telephone Fixe',size=255) ,
        'faxe': fields.char('Faxe',size=255) ,
        'responsable': fields.char('Faxe',size=255) ,
        'idetablissement': fields.many2one('ptr.etablissement','Etablissement',ondelete='cascade'),
        'local_ids': fields.one2many('ptr.local','departement',string='Local')
    }

ptr_departement()