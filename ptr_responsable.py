from osv import osv,fields
# import openerp


class ptr_responsable(osv.osv):
    _name= 'ptr.responsable'
    _columns={
        'matricule':fields.char('Matricule',size=255) ,
        'name':fields.char('Nom',size=255) ,
        'prenom':fields.char('Prenom',size=255) ,
        'fonction':fields.char('Fonction',size=64)  ,
        'tel':fields.char('Telephone')  ,
        'faxe': fields.char('Faxe') ,
        'email': fields.char('Email') ,
        'local_id': fields.many2one('ptr.local','Local',ondelete='cascade'),
        'categoriepersonnel': fields.many2one('ptr.categoriepersonnel','Categorie Personnel',ondelete='cascade')

    }

ptr_responsable()