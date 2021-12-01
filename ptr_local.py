from osv import osv,fields
# import openerp


class ptr_local(osv.osv):
    _name= 'ptr.local'
    _columns={
        'code':fields.char('Code',size=255)  ,
        'designation':fields.char('Designation',size=255),
        'crocquis':fields.char('Crocquis',size=255),
        'superficie': fields.float('SuperFicie',digits=None) ,
        'capacite_acceuil': fields.char('Capacite Acceuil',size=255) ,
        'fiche_immeuble': fields.char('Fiche Immeuble',size=255) ,
        'fiche_etage': fields.char('Fiche Tage',size=255) ,
        'fiche_local': fields.char('Fiche local',size=255) ,
        'departement': fields.many2one('ptr.departement','Departement',ondelete='cascade'), 
        'responsable': fields.many2one('ptr.responsable','Responsable',ondelete='cascade')
    }


ptr_local()