from osv import osv,fields
# import openerp


class ptr_etablissement(osv.osv):
    _name= 'ptr.etablissement'
    _columns={
        'name':fields.char('Nom',size=255) ,
        'code':fields.char('Code',size=64)  ,
        'adresse':fields.char('Adresse')  ,
        'fixe': fields.char('Telephone Fixe') ,
        'faxe': fields.char('Faxe') ,
        'departement_ids': fields.one2many('ptr.departement','idetablissement',string='Departement'),
        'inv_ids': fields.one2many('ptr.inventaire','idi_nv',string='Inventaire')
   
    }

ptr_etablissement()