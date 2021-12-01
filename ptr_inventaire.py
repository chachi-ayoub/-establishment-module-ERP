from osv import osv,fields



class ptr_inventaire(osv.osv):
    def _draft_func(self, cr, uid, ids):
        self.write(cr, uid, ids, {'state': 'draft'})
        return True
    def _redaction_pv_lancement_func(self, cr, uid, ids):
        self.write(cr, uid, ids, {'state': 'redaction_pv_lancement'})
        return True
    def _signature_courrier_func(self, cr, uid, ids):
        self.write(cr, uid, ids, {'state': 'signature_courrier'})
        return True
    def _designation_equipe_func(self, cr, uid, ids):
        self.write(cr, uid, ids, {'state': 'designation_equipe'})
        return True
    def _maj_plan_action_func(self, cr, uid, ids):
        self.write(cr, uid, ids, {'state': 'maj_plan_action'})
        return True
    def _diffusion_rpe_func(self, cr, uid, ids):
        self.write(cr, uid, ids, {'state': 'diffusion_rpe'})
        return True
    def _pv_reunion_ouverture_func(self, cr, uid, ids):
        self.write(cr, uid, ids, {'state': 'pv_reunion_ouverture'})
        return True
    def _demarrage_inventaire_func(self, cr, uid, ids):
        self.write(cr, uid, ids, {'state': 'demarrage_inventaire'})
        return True
  
    
    _name= 'ptr.inventaire'
    _columns={
        'name':fields.char('Nom',size=255) ,
        'date_inv_dec':fields.date('Date Inventaire Dec')  ,
        'date_inv_ar':fields.date('Date Inventaire Ar')  ,
        'duree':fields.float('Duree', digits=None)  ,
        'idi_nv': fields.many2one('ptr.etablissement','Etablissement',ondelete='cascade'),
        'state': fields.selection([
            ('draft','Brouillant'),
            ('redaction_pv_lancement','Redaction du pv de lancement'),
            ('signature_courrier','Validation et signature du courrier'),
            ('designation_equipe','Designation de l equipe d inventaire'),
            ('maj_plan_action','MAJ plan d action'),
            ('diffusion_rpe','Diffusion RPE'),
            ('pv_reunion_ouverture','PV de reunion ouverture'),
            ('demarrage_inventaire','Demarrage inventaire')
        ], 'State',readonly=True)
    }

ptr_inventaire()