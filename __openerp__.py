{
    'name':'Patrimoines',
    'version':'1.0',
    'author':'GI 3 BI TEAM Workshop',
    'category':'ENSAH ERP',
    'sequence':1,
    'description': """
         Module test de gestion du patrimoines
        *Gestion des locaux
        *Gestion des departements
        *Gestion des etablisements
        *Gestion des reponsable
        *Gestion des personnels
    

    """,
    'website':'http://www.monsite.ma',
    'images':[],
    'depends':['base'],
    'data':['ptr_etablissement_view.xml',
            'ptr_inventaire_view.xml',
            'ptr_departement_view.xml',
            'ptr_inv_wkf_view.xml',
            'ptr_categoriepersonnel_view.xml',
            'ptr_local_view.xml',
            'ptr_responsable_view.xml',
            'ptr_typetrgeo_view.xml'],
    'init_xml' : [],
    'update_xml' : [],
    'js':[],
    'qweb':[],
    'css':[],
    'demo':[],
    'test':[],
    "installable": True,
    "auto_install": False
}