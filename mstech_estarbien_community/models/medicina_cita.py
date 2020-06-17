# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class MedicinaPacientePerfilTipo(models.Model) :
    _name = 'medicina.paciente.perfil.tipo'
    _description = 'Tipo de perfil'
    
    perfil_id = fields.Many2one(comodel_name='''medicina.paciente.perfil''', string='''Perfil''')
    tipo_cita = fields.Selection(string='''Tipo''',selection=[("diagnostico","Diagnóstico"),
                                                              ("triaje","Triaje"),
                                                              ("antecedentes_personales","Antecedentes Personales"),
                                                              ("historia_ocupacional","Historia Ocupacional"),
                                                              ("medicina","Medicina general"),
                                                              ("dermatologia","Dermatología"),
                                                              ("grandes_alturas","Anexo N°16 A"),
                                                              ("altura","Certificación de trabajo en altura"),
                                                              ("confinados","Trabajo en espacios confinados"),
                                                              ("electrocardiograma","Electrocardiograma"),
                                                              ("oftalmologia","Oftalmología"),
                                                              ("audiometria","Audiometría"),
                                                              ("psicologia","Psicología"),
                                                              ("odontograma","Odontograma"),
                                                              ("musculo_esqueletico","Músculo Esquelético"),
                                                              ("radiologia","Radiología"),
                                                              ("espirometria","Espirometría"),
                                                              ("tsr","Test de Sintomático Respiratorio"),
                                                              ("laboratorio","Laboratorio"),
                                                              ("consentimiento","Consentimiento"),
                                                              ("interconsultas","Interconsultas"),
                                                              ("encuesta","Encuesta")])

class MedicinaPacientePerfil(models.Model) :
    _name = 'medicina.paciente.perfil'
    _description = 'Perfil de paciente'
    
    name = fields.Char(string='''Perfil''')
    tipo_cita_ids = fields.One2many(comodel_name='''medicina.paciente.perfil.tipo''', inverse_name='''cita_id''', string='''Tipo de cita''')

class MedicalPatient(models.Model) :
    _inherit = 'medical.patient'
    
    perfil_id = fields.Many2one(comodel_name='''medicina.paciente.perfil''',string='''Perfil''')

class MedicinaCita(models.Model) :
    _name = 'medicina.cita'
    _description = 'Cita'
    
    altura_acrofobia = fields.Boolean(string='''Acrofobia (Temor a las alturas)''')
    altura_alcoholismo_adiccion = fields.Boolean(string='''Alcholismo o abuso de sustancias (adicción)''')
    altura_alteracion_coordinacion = fields.Boolean(string='''Alteración de la coordinación presente''')
    altura_anormalidades_fuerza_miembros = fields.Boolean(string='''Anormalidades en la fuerza de miembros''')
    altura_anormalidades_movimiento_ocular = fields.Boolean(string='''Anormalidades en movimiento ocular''')
    altura_antecedentes_entrevista_medicinas = fields.Text(string='''Medicinas que está tomando''')
    altura_antecedentes_medicos_comentario = fields.Text(string='''Comentario/Detalle''')
    altura_asimetria_facial = fields.Boolean(string='''Asimetría facial''')
    altura_cefalea_frecuencia = fields.Boolean(string='''Frecuencia de cefaleas''')
    altura_certificacion_aptitud = fields.Selection(string='''Aptitud para laborar por encima de 1.8 metros sobre el suelo''', selection=[("apto","Apto"),("no_apto","No apto"),("apto_restricciones","Apto con restricciones")])
    altura_certificacion_lentes = fields.Boolean(string='''Uso permanente de lentes correctores''')
    altura_certificacion_observaciones = fields.Text(string='''Observaciones / Recomendaciones''')
    altura_certificacion_otras_restricciones = fields.Char(string='''Otras restricciones''')
    altura_certificacion_protectores = fields.Boolean(string='''Uso permanente de protectores auditivos''')
    altura_certificacion_tipo = fields.Selection(string='''Tipo Certificación''', selection=[("primera_aptitud","Primera Aptitud"),("revalidacion","Revalidación")])
    altura_crisis_asmatica = fields.Boolean(string='''Crisis asmática''')
    altura_diabetes_hipoglicemia = fields.Boolean(string='''Diabetes mellitus o hipoglicemia no controlada''')
    altura_enfermedad_psiquiatrica = fields.Boolean(string='''Portador de enfermedad psiquiátrica''')
    altura_enfermedades_corazon = fields.Boolean(string='''Enfermedades del corazón''')
    altura_epilepsia_convulsiones_otros = fields.Boolean(string='''Pérdida de consciencia (epilepsia/convulsiones, otros)''')
    altura_equilibrio_alteracion = fields.Boolean(string='''Alteración del equilibrio''')
    altura_estereopsis_agudeza_visual = fields.Boolean(string='''Alteración de la agudeza visual (de lejos) y/o estereopsis''')
    altura_examen_fisico_detalles = fields.Text(string='''Detalles del examen físico''')
    altura_frecuencia_cardiaca = fields.Integer(string='''Frecuencia cardiaca''')
    altura_frecuencia_respiratoria = fields.Integer(string='''Frecuencia respiratoria''')
    altura_hipertension_arterial = fields.Boolean(string='''Hipertensión arterial no controlada''')
    altura_hipoacusia_severa = fields.Boolean(string='''Hipoacusia severa''')
    altura_inapto_labor_altura_previo = fields.Boolean(string='''INAPTO para labor de altura (según resultados previos)''')
    altura_indice_masa_corporal = fields.Float(string='''Índice de masa corporal''', compute='''_compute_altura_indice_masa_corporal''', store=True, readonly=False)
    altura_lenguaje_anormal = fields.Boolean(string='''Lenguaje anormal''')
    altura_licor_24_horas = fields.Boolean(string='''Consumió licor en las últimas 24 horas''')
    altura_limitacion_extremidades_fuerza_movilidad = fields.Boolean(string='''Limitación en fuerza y/o movilidad de extremidades''')
    altura_marcha_anormalidades = fields.Boolean(string='''Anormalidades en la marcha''')
    altura_migrana = fields.Boolean(string='''Migraña''')
    altura_nistagmus = fields.Boolean(string='''Nistagmus''')
    altura_peso = fields.Float(string='''Peso''')
    altura_presion_arterial = fields.Char(string='''Presión Arterial''')
    altura_pupilas_cirla = fields.Boolean(string='''Pupilas CIRLA''')
    altura_resfrio_cuadro_respiratorio = fields.Boolean(string='''Resfrío / Cuadro respiratorio''')
    altura_saturacion_oxigeno = fields.Float(string='''Saturación de Oxígeno''')
    altura_talla = fields.Float(string='''Talla''')
    altura_vertigo_mareo = fields.Boolean(string='''Vértigo / Mareos recientes''')
    
    @api.depends('altura_talla','altura_peso')
    def _compute_altura_indice_masa_corporal(self):
        for rec in self:
            rec.altura_indice_masa_corporal = rec.altura_talla and rec.altura_peso / (rec.altura_talla ** 2) or 0.0
    
    archivo_adjunto_audiometria_1 = fields.Binary(string='''New Archivo''')
    archivo_adjunto_audiometria_1_filename = fields.Char(string='''Filename for archivo_adjunto_audiometria_1''')
    archivo_adjunto_audiometria_2 = fields.Binary(string='''New Archivo''')
    archivo_adjunto_audiometria_2_filename = fields.Char(string='''Filename for archivo_adjunto_audiometria_2''')
    archivo_adjunto_audiometria_3 = fields.Binary(string='''New Archivo''')
    archivo_adjunto_audiometria_3_filename = fields.Char(string='''Filename for archivo_adjunto_audiometria_3''')
    archivo_adjunto_audiometria_4 = fields.Binary(string='''New Archivo''')
    archivo_adjunto_audiometria_4_filename = fields.Char(string='''Filename for archivo_adjunto_audiometria_4''')
    
    archivo_adjunto_cardiologico = fields.Binary(string='''Archivo''')
    archivo_adjunto_cardiologico_filename = fields.Char(string='''Filename for archivo_adjunto_informe_cardiologico''')
    
    archivo_adjunto_espirometrico_1 = fields.Binary(string='''New Archivo''')
    archivo_adjunto_espirometrico_1_filename = fields.Char(string='''Filename for archivo_adjunto_espirometrico_1''')
    archivo_adjunto_espirometrico_2 = fields.Binary(string='''New Archivo''')
    archivo_adjunto_espirometrico_2_filename = fields.Char(string='''Filename for archivo_adjunto_espirometrico_2''')
    
    archivo_adjunto_laboratorio_1 = fields.Binary(string='''Archivo adjunto 1 (laboratorio)''')
    archivo_adjunto_laboratorio_1_filename = fields.Char(string='''Filename for archivo_adjunto_laboratorio_1''')
    archivo_adjunto_laboratorio_2 = fields.Binary(string='''Archivo adjunto 2 (laboratorio)''')
    archivo_adjunto_laboratorio_2_filename = fields.Char(string='''Filename for archivo_adjunto_laboratorio_2''')
    
    archivo_adjunto_musculo_esqueletico_1 = fields.Binary(string='''Archivo''')
    archivo_adjunto_musculo_esqueletico_1_filename = fields.Char(string='''Filename for archivo_adjunto_musculo_esqueletico_1''')
    archivo_adjunto_musculo_esqueletico_2 = fields.Binary(string='''Archivo''')
    archivo_adjunto_musculo_esqueletico_2_filename = fields.Char(string='''Filename for archivo_adjunto_musculo_esqueletico_2''')
    
    archivo_adjunto_oftalmologico_1 = fields.Binary(string='''Archivo adjunto 1 (oftalmológico)''')
    archivo_adjunto_oftalmologico_1_filename = fields.Char(string='''Filename for archivo_adjunto_oftalmologico_1''')
    archivo_adjunto_oftalmologico_2 = fields.Binary(string='''Archivo adjunto 2 (oftalmológico)''')
    archivo_adjunto_oftalmologico_2_filename = fields.Char(string='''Filename for archivo_adjunto_oftalmologico_2''')
    
    archivo_adjunto_psicologico_1 = fields.Binary(string='''New Archivo''')
    archivo_adjunto_psicologico_1_filename = fields.Char(string='''Filename for archivo_adjunto_psicologia_1''')
    archivo_adjunto_psicologico_2 = fields.Binary(string='''New Archivo''')
    archivo_adjunto_psicologico_2_filename = fields.Char(string='''Filename for archivo_adjunto_psicologia_2''')
    
    archivo_adjunto_radiologia_1 = fields.Binary(string='''New Archivo''')
    archivo_adjunto_radiologia_1_filename = fields.Char(string='''Filename for archivo_adjunto_radiologia_1''')
    
    audiometria_antecedentes_consumo_tabaco = fields.Boolean(string='''Tabaco (ficha audiológica)''')
    audiometria_antecedentes_hobbies_ruido = fields.Boolean(string='''Hobbies ruidosos (ficha audiológica)''')
    audiometria_antecedentes_infeccion_oido = fields.Boolean(string='''Infecciones de oído previas (ficha audiológica)''')
    audiometria_antecedentes_laboral_quimico = fields.Boolean(string='''Exposición laboral a químicos (ficha audiológica)''')
    audiometria_antecedentes_meningitis_traumatismo = fields.Boolean(string='''Traumatismo encéfalo-craneano o meningitis (ficha audiológica)''')
    audiometria_antecedentes_ototoxicos = fields.Boolean(string='''Uso de ototóxicos (ficha audiológica)''')
    audiometria_antecedentes_servicio_militar = fields.Boolean(string='''Servicio militar (ficha audiológica)''')
    audiometria_antecedentes_trauma_acustico = fields.Boolean(string='''Trauma acústico (ficha audiológica)''')
    audiometria_bilateral = fields.Boolean(string='''Audiometría bilateral''', default=True)
    audiometria_derecho_aerea_1000_nr = fields.Boolean(string='''Audiometría de tipo aérea del oído derecho a 1000 (NR)''')
    audiometria_derecho_aerea_1000_valor = fields.Char(string='''Audiometría de tipo aérea del oído derecho a 1000 (valor)''')
    audiometria_derecho_aerea_125_nr = fields.Boolean(string='''Audiometría de tipo aérea del oído derecho a 125 (NR)''')
    audiometria_derecho_aerea_125_valor = fields.Char(string='''Audiometría de tipo aérea del oído derecho a 125 (valor)''')
    audiometria_derecho_aerea_2000_nr = fields.Boolean(string='''Audiometría de tipo aérea del oído derecho a 2000 (NR)''')
    audiometria_derecho_aerea_2000_valor = fields.Char(string='''Audiometría de tipo aérea del oído derecho a 2000 (valor)''')
    audiometria_derecho_aerea_250_nr = fields.Boolean(string='''Audiometría de tipo aérea del oído derecho a 250 (NR)''')
    audiometria_derecho_aerea_250_valor = fields.Char(string='''Audiometría de tipo aérea del oído derecho a 250 (valor)''')
    audiometria_derecho_aerea_3000_nr = fields.Boolean(string='''Audiometría de tipo aérea del oído derecho a 3000 (NR)''')
    audiometria_derecho_aerea_3000_valor = fields.Char(string='''Audiometría de tipo aérea del oído derecho a 3000 (valor)''')
    audiometria_derecho_aerea_4000_nr = fields.Boolean(string='''Audiometría de tipo aérea del oído derecho a 4000 (NR)''')
    audiometria_derecho_aerea_4000_valor = fields.Char(string='''Audiometría de tipo aérea del oído derecho a 4000 (valor)''')
    audiometria_derecho_aerea_500_nr = fields.Boolean(string='''Audiometría de tipo aérea del oído derecho a 500 (NR)''')
    audiometria_derecho_aerea_500_valor = fields.Char(string='''Audiometría de tipo aérea del oído derecho a 500 (valor)''')
    audiometria_derecho_aerea_6000_nr = fields.Boolean(string='''Audiometría de tipo aérea del oído derecho a 6000 (NR)''')
    audiometria_derecho_aerea_6000_valor = fields.Char(string='''Audiometría de tipo aérea del oído derecho a 6000 (valor)''')
    audiometria_derecho_aerea_8000_nr = fields.Boolean(string='''Audiometría de tipo aérea del oído derecho a 8000 (NR)''')
    audiometria_derecho_aerea_8000_valor = fields.Char(string='''Audiometría de tipo aérea del oído derecho a 8000 (valor)''')
    audiometria_derecho_enmasc_aerea_1000_nr = fields.Boolean(string='''Audiometría de tipo enmasc. aérea. del oído derecho a 1000 (NR)''')
    audiometria_derecho_enmasc_aerea_1000_valor = fields.Char(string='''Audiometría de tipo enmasc. aérea. del oído derecho a 1000 (valor)''')
    audiometria_derecho_enmasc_aerea_125_nr = fields.Boolean(string='''Audiometría de tipo enmasc. aérea. del oído derecho a 125 (NR)''')
    audiometria_derecho_enmasc_aerea_125_valor = fields.Char(string='''Audiometría de tipo enmasc. aérea. del oído derecho a 125 (valor)''')
    audiometria_derecho_enmasc_aerea_2000_nr = fields.Boolean(string='''Audiometría de tipo enmasc. aérea. del oído derecho a 2000 (NR)''')
    audiometria_derecho_enmasc_aerea_2000_valor = fields.Char(string='''Audiometría de tipo enmasc. aérea. del oído derecho a 2000 (valor)''')
    audiometria_derecho_enmasc_aerea_250_nr = fields.Boolean(string='''Audiometría de tipo enmasc. aérea. del oído derecho a 250 (NR)''')
    audiometria_derecho_enmasc_aerea_250_valor = fields.Char(string='''Audiometría de tipo enmasc. aérea. del oído derecho a 250 (valor)''')
    audiometria_derecho_enmasc_aerea_3000_nr = fields.Boolean(string='''Audiometría de tipo enmasc. aérea. del oído derecho a 3000 (NR)''')
    audiometria_derecho_enmasc_aerea_3000_valor = fields.Char(string='''Audiometría de tipo enmasc. aérea. del oído derecho a 3000 (valor)''')
    audiometria_derecho_enmasc_aerea_4000_nr = fields.Boolean(string='''Audiometría de tipo enmasc. aérea. del oído derecho a 4000 (NR)''')
    audiometria_derecho_enmasc_aerea_4000_valor = fields.Char(string='''Audiometría de tipo enmasc. aérea. del oído derecho a 4000 (valor)''')
    audiometria_derecho_enmasc_aerea_500_nr = fields.Boolean(string='''Audiometría de tipo enmasc. aérea. del oído derecho a 500 (NR)''')
    audiometria_derecho_enmasc_aerea_500_valor = fields.Char(string='''Audiometría de tipo enmasc. aérea. del oído derecho a 500 (valor)''')
    audiometria_derecho_enmasc_aerea_6000_nr = fields.Boolean(string='''Audiometría de tipo enmasc. aérea. del oído derecho a 6000 (NR)''')
    audiometria_derecho_enmasc_aerea_6000_valor = fields.Char(string='''Audiometría de tipo enmasc. aérea. del oído derecho a 6000 (valor)''')
    audiometria_derecho_enmasc_aerea_8000_nr = fields.Boolean(string='''Audiometría de tipo enmasc. aérea. del oído derecho a 8000 (NR)''')
    audiometria_derecho_enmasc_aerea_8000_valor = fields.Char(string='''Audiometría de tipo enmasc. aérea. del oído derecho a 8000 (valor)''')
    audiometria_derecho_enmasc_osea_1000_nr = fields.Boolean(string='''Audiometría de tipo enmasc. ósea del oído derecho a 1000 (NR)''')
    audiometria_derecho_enmasc_osea_1000_valor = fields.Char(string='''Audiometría de tipo enmasc. ósea del oído derecho a 1000 (valor)''')
    audiometria_derecho_enmasc_osea_125_nr = fields.Boolean(string='''Audiometría de tipo enmasc. ósea del oído derecho a 125 (NR)''')
    audiometria_derecho_enmasc_osea_125_valor = fields.Char(string='''Audiometría de tipo enmasc. ósea del oído derecho a 125 (valor)''')
    audiometria_derecho_enmasc_osea_2000_nr = fields.Boolean(string='''Audiometría de tipo enmasc. ósea del oído derecho a 2000 (NR)''')
    audiometria_derecho_enmasc_osea_2000_valor = fields.Char(string='''Audiometría de tipo enmasc. ósea del oído derecho a 2000 (valor)''')
    audiometria_derecho_enmasc_osea_250_nr = fields.Boolean(string='''Audiometría de tipo enmasc. ósea del oído derecho a 250 (NR)''')
    audiometria_derecho_enmasc_osea_250_valor = fields.Char(string='''Audiometría de tipo enmasc. ósea del oído derecho a 250 (valor)''')
    audiometria_derecho_enmasc_osea_3000_nr = fields.Boolean(string='''Audiometría de tipo enmasc. ósea del oído derecho a 3000 (NR)''')
    audiometria_derecho_enmasc_osea_3000_valor = fields.Char(string='''Audiometría de tipo enmasc. ósea del oído derecho a 3000 (valor)''')
    audiometria_derecho_enmasc_osea_4000_nr = fields.Boolean(string='''Audiometría de tipo enmasc. ósea del oído derecho a 4000 (NR)''')
    audiometria_derecho_enmasc_osea_4000_valor = fields.Char(string='''Audiometría de tipo enmasc. ósea del oído derecho a 4000 (valor)''')
    audiometria_derecho_enmasc_osea_500_nr = fields.Boolean(string='''Audiometría de tipo enmasc. ósea del oído derecho a 500 (NR)''')
    audiometria_derecho_enmasc_osea_500_valor = fields.Char(string='''Audiometría de tipo enmasc. ósea del oído derecho a 500 (valor)''')
    audiometria_derecho_enmasc_osea_6000_nr = fields.Boolean(string='''Audiometría de tipo enmasc. ósea del oído derecho a 6000 (NR)''')
    audiometria_derecho_enmasc_osea_6000_valor = fields.Char(string='''Audiometría de tipo enmasc. ósea del oído derecho a 6000 (valor)''')
    audiometria_derecho_enmasc_osea_8000_nr = fields.Boolean(string='''Audiometría de tipo enmasc. ósea del oído derecho a 8000 (NR)''')
    audiometria_derecho_enmasc_osea_8000_valor = fields.Char(string='''Audiometría de tipo enmasc. ósea del oído derecho a 8000 (valor)''')
    audiometria_derecho_osea_1000_nr = fields.Boolean(string='''Audiometría de tipo ósea del oído derecho a 1000 (NR)''')
    audiometria_derecho_osea_1000_valor = fields.Char(string='''Audiometría de tipo ósea del oído derecho a 1000 (valor)''')
    audiometria_derecho_osea_125_nr = fields.Boolean(string='''Audiometría de tipo ósea del oído derecho a 125 (NR)''')
    audiometria_derecho_osea_125_valor = fields.Char(string='''Audiometría de tipo ósea del oído derecho a 125 (valor)''')
    audiometria_derecho_osea_2000_nr = fields.Boolean(string='''Audiometría de tipo ósea del oído derecho a 2000 (NR)''')
    audiometria_derecho_osea_2000_valor = fields.Char(string='''Audiometría de tipo ósea del oído derecho a 2000 (valor)''')
    audiometria_derecho_osea_250_nr = fields.Boolean(string='''Audiometría de tipo ósea del oído derecho a 250 (NR)''')
    audiometria_derecho_osea_250_valor = fields.Char(string='''Audiometría de tipo ósea del oído derecho a 250 (valor)''')
    audiometria_derecho_osea_3000_nr = fields.Boolean(string='''Audiometría de tipo ósea del oído derecho a 3000 (NR)''')
    audiometria_derecho_osea_3000_valor = fields.Char(string='''Audiometría de tipo ósea del oído derecho a 3000 (valor)''')
    audiometria_derecho_osea_4000_nr = fields.Boolean(string='''Audiometría de tipo ósea del oído derecho a 4000 (NR)''')
    audiometria_derecho_osea_4000_valor = fields.Char(string='''Audiometría de tipo ósea del oído derecho a 4000 (valor)''')
    audiometria_derecho_osea_500_nr = fields.Boolean(string='''Audiometría de tipo ósea del oído derecho a 500 (NR)''')
    audiometria_derecho_osea_500_valor = fields.Char(string='''Audiometría de tipo ósea del oído derecho a 500 (valor)''')
    audiometria_derecho_osea_6000_nr = fields.Boolean(string='''Audiometría de tipo ósea del oído derecho a 6000 (NR)''')
    audiometria_derecho_osea_6000_valor = fields.Char(string='''Audiometría de tipo ósea del oído derecho a 6000 (valor)''')
    audiometria_derecho_osea_8000_nr = fields.Boolean(string='''Audiometría de tipo ósea del oído derecho a 8000 (NR)''')
    audiometria_derecho_osea_8000_valor = fields.Char(string='''Audiometría de tipo ósea del oído derecho a 8000 (valor)''')
    audiometria_diagnostico = fields.Selection(string='''Diagnóstico (audiometría)''',selection=[("diagnostico_medicina_ocupacional","DiagMO"),("otros_diagnosticos","OtrosD")])
    audiometria_izquierdo_aerea_1000_nr = fields.Boolean(string='''Audiometría de tipo aérea del oído izquierdo a 1000 (NR)''')
    audiometria_izquierdo_aerea_1000_valor = fields.Char(string='''Audiometría de tipo aérea del oído izquierdo a 1000 (valor)''')
    audiometria_izquierdo_aerea_125_nr = fields.Boolean(string='''Audiometría de tipo aérea del oído izquierdo a 125 (NR)''')
    audiometria_izquierdo_aerea_125_valor = fields.Char(string='''Audiometría de tipo aérea del oído izquierdo a 125 (valor)''')
    audiometria_izquierdo_aerea_2000_nr = fields.Boolean(string='''Audiometría de tipo aérea del oído izquierdo a 2000 (NR)''')
    audiometria_izquierdo_aerea_2000_valor = fields.Char(string='''Audiometría de tipo aérea del oído izquierdo a 2000 (valor)''')
    audiometria_izquierdo_aerea_250_nr = fields.Boolean(string='''Audiometría de tipo aérea del oído izquierdo a 250 (NR)''')
    audiometria_izquierdo_aerea_250_valor = fields.Char(string='''Audiometría de tipo aérea del oído izquierdo a 250 (valor)''')
    audiometria_izquierdo_aerea_3000_nr = fields.Boolean(string='''Audiometría de tipo aérea del oído izquierdo a 3000 (NR)''')
    audiometria_izquierdo_aerea_3000_valor = fields.Char(string='''Audiometría de tipo aérea del oído izquierdo a 3000 (valor)''')
    audiometria_izquierdo_aerea_4000_nr = fields.Boolean(string='''Audiometría de tipo aérea del oído izquierdo a 4000 (NR)''')
    audiometria_izquierdo_aerea_4000_valor = fields.Char(string='''Audiometría de tipo aérea del oído izquierdo a 4000 (valor)''')
    audiometria_izquierdo_aerea_500_nr = fields.Boolean(string='''Audiometría de tipo aérea del oído izquierdo a 500 (NR)''')
    audiometria_izquierdo_aerea_500_valor = fields.Char(string='''Audiometría de tipo aérea del oído izquierdo a 500 (valor)''')
    audiometria_izquierdo_aerea_6000_nr = fields.Boolean(string='''Audiometría de tipo aérea del oído izquierdo a 6000 (NR)''')
    audiometria_izquierdo_aerea_6000_valor = fields.Char(string='''Audiometría de tipo aérea del oído izquierdo a 6000 (valor)''')
    audiometria_izquierdo_aerea_8000_nr = fields.Boolean(string='''Audiometría de tipo aérea del oído izquierdo a 8000 (NR)''')
    audiometria_izquierdo_aerea_8000_valor = fields.Char(string='''Audiometría de tipo aérea del oído izquierdo a 8000 (valor)''')
    audiometria_izquierdo_enmasc_aerea_1000_nr = fields.Boolean(string='''Audiometría de tipo enmasc. aérea. del oído izquierdo a 1000 (NR)''')
    audiometria_izquierdo_enmasc_aerea_1000_valor = fields.Char(string='''Audiometría de tipo enmasc. aérea. del oído izquierdo a 1000 (valor)''')
    audiometria_izquierdo_enmasc_aerea_125_nr = fields.Boolean(string='''Audiometría de tipo enmasc. aérea. del oído izquierdo a 125 (NR)''')
    audiometria_izquierdo_enmasc_aerea_125_valor = fields.Char(string='''Audiometría de tipo enmasc. aérea. del oído izquierdo a 125 (valor)''')
    audiometria_izquierdo_enmasc_aerea_2000_nr = fields.Boolean(string='''Audiometría de tipo enmasc. aérea. del oído izquierdo a 2000 (NR)''')
    audiometria_izquierdo_enmasc_aerea_2000_valor = fields.Char(string='''Audiometría de tipo enmasc. aérea. del oído izquierdo a 2000 (valor)''')
    audiometria_izquierdo_enmasc_aerea_250_nr = fields.Boolean(string='''Audiometría de tipo enmasc. aérea. del oído izquierdo a 250 (NR)''')
    audiometria_izquierdo_enmasc_aerea_250_valor = fields.Char(string='''Audiometría de tipo enmasc. aérea. del oído izquierdo a 250 (valor)''')
    audiometria_izquierdo_enmasc_aerea_3000_nr = fields.Boolean(string='''Audiometría de tipo enmasc. aérea. del oído izquierdo a 3000 (NR)''')
    audiometria_izquierdo_enmasc_aerea_3000_valor = fields.Char(string='''Audiometría de tipo enmasc. aérea. del oído izquierdo a 3000 (valor)''')
    audiometria_izquierdo_enmasc_aerea_4000_nr = fields.Boolean(string='''Audiometría de tipo enmasc. aérea. del oído izquierdo a 4000 (NR)''')
    audiometria_izquierdo_enmasc_aerea_4000_valor = fields.Char(string='''Audiometría de tipo enmasc. aérea. del oído izquierdo a 4000 (valor)''')
    audiometria_izquierdo_enmasc_aerea_500_nr = fields.Boolean(string='''Audiometría de tipo enmasc. aérea. del oído izquierdo a 500 (NR)''')
    audiometria_izquierdo_enmasc_aerea_500_valor = fields.Char(string='''Audiometría de tipo enmasc. aérea. del oído izquierdo a 500 (valor)''')
    audiometria_izquierdo_enmasc_aerea_6000_nr = fields.Boolean(string='''Audiometría de tipo enmasc. aérea. del oído izquierdo a 6000 (NR)''')
    audiometria_izquierdo_enmasc_aerea_6000_valor = fields.Char(string='''Audiometría de tipo enmasc. aérea. del oído izquierdo a 6000 (valor)''')
    audiometria_izquierdo_enmasc_aerea_8000_nr = fields.Boolean(string='''Audiometría de tipo enmasc. aérea. del oído izquierdo a 8000 (NR)''')
    audiometria_izquierdo_enmasc_aerea_8000_valor = fields.Char(string='''Audiometría de tipo enmasc. aérea. del oído izquierdo a 8000 (valor)''')
    audiometria_izquierdo_enmasc_osea_1000_nr = fields.Boolean(string='''Audiometría de tipo enmasc. ósea del oído izquierdo a 1000 (NR)''')
    audiometria_izquierdo_enmasc_osea_1000_valor = fields.Char(string='''Audiometría de tipo enmasc. ósea del oído izquierdo a 1000 (valor)''')
    audiometria_izquierdo_enmasc_osea_125_nr = fields.Boolean(string='''Audiometría de tipo enmasc. ósea del oído izquierdo a 125 (NR)''')
    audiometria_izquierdo_enmasc_osea_125_valor = fields.Char(string='''Audiometría de tipo enmasc. ósea del oído izquierdo a 125 (valor)''')
    audiometria_izquierdo_enmasc_osea_2000_nr = fields.Boolean(string='''Audiometría de tipo enmasc. ósea del oído izquierdo a 2000 (NR)''')
    audiometria_izquierdo_enmasc_osea_2000_valor = fields.Char(string='''Audiometría de tipo enmasc. ósea del oído izquierdo a 2000 (valor)''')
    audiometria_izquierdo_enmasc_osea_250_nr = fields.Boolean(string='''Audiometría de tipo enmasc. ósea del oído izquierdo a 250 (NR)''')
    audiometria_izquierdo_enmasc_osea_250_valor = fields.Char(string='''Audiometría de tipo enmasc. ósea del oído izquierdo a 250 (valor)''')
    audiometria_izquierdo_enmasc_osea_3000_nr = fields.Boolean(string='''Audiometría de tipo enmasc. ósea del oído izquierdo a 3000 (NR)''')
    audiometria_izquierdo_enmasc_osea_3000_valor = fields.Char(string='''Audiometría de tipo enmasc. ósea del oído izquierdo a 3000 (valor)''')
    audiometria_izquierdo_enmasc_osea_4000_nr = fields.Boolean(string='''Audiometría de tipo enmasc. ósea del oído izquierdo a 4000 (NR)''')
    audiometria_izquierdo_enmasc_osea_4000_valor = fields.Char(string='''Audiometría de tipo enmasc. ósea del oído izquierdo a 4000 (valor)''')
    audiometria_izquierdo_enmasc_osea_500_nr = fields.Boolean(string='''Audiometría de tipo enmasc. ósea del oído izquierdo a 500 (NR)''')
    audiometria_izquierdo_enmasc_osea_500_valor = fields.Char(string='''Audiometría de tipo enmasc. ósea del oído izquierdo a 500 (valor)''')
    audiometria_izquierdo_enmasc_osea_6000_nr = fields.Boolean(string='''Audiometría de tipo enmasc. ósea del oído izquierdo a 6000 (NR)''')
    audiometria_izquierdo_enmasc_osea_6000_valor = fields.Char(string='''Audiometría de tipo enmasc. ósea del oído izquierdo a 6000 (valor)''')
    audiometria_izquierdo_enmasc_osea_8000_nr = fields.Boolean(string='''Audiometría de tipo enmasc. ósea del oído izquierdo a 8000 (NR)''')
    audiometria_izquierdo_enmasc_osea_8000_valor = fields.Char(string='''Audiometría de tipo enmasc. ósea del oído izquierdo a 8000 (valor)''')
    audiometria_izquierdo_osea_1000_nr = fields.Boolean(string='''Audiometría de tipo ósea del oído izquierdo a 1000 (NR)''')
    audiometria_izquierdo_osea_1000_valor = fields.Char(string='''Audiometría de tipo ósea del oído izquierdo a 1000 (valor)''')
    audiometria_izquierdo_osea_125_nr = fields.Boolean(string='''Audiometría de tipo ósea del oído izquierdo a 125 (NR)''')
    audiometria_izquierdo_osea_125_valor = fields.Char(string='''Audiometría de tipo ósea del oído izquierdo a 125 (valor)''')
    audiometria_izquierdo_osea_2000_nr = fields.Boolean(string='''Audiometría de tipo ósea del oído izquierdo a 2000 (NR)''')
    audiometria_izquierdo_osea_2000_valor = fields.Char(string='''Audiometría de tipo ósea del oído izquierdo a 2000 (valor)''')
    audiometria_izquierdo_osea_250_nr = fields.Boolean(string='''Audiometría de tipo ósea del oído izquierdo a 250 (NR)''')
    audiometria_izquierdo_osea_250_valor = fields.Char(string='''Audiometría de tipo ósea del oído izquierdo a 250 (valor)''')
    audiometria_izquierdo_osea_3000_nr = fields.Boolean(string='''Audiometría de tipo ósea del oído izquierdo a 3000 (NR)''')
    audiometria_izquierdo_osea_3000_valor = fields.Char(string='''Audiometría de tipo ósea del oído izquierdo a 3000 (valor)''')
    audiometria_izquierdo_osea_4000_nr = fields.Boolean(string='''Audiometría de tipo ósea del oído izquierdo a 4000 (NR)''')
    audiometria_izquierdo_osea_4000_valor = fields.Char(string='''Audiometría de tipo ósea del oído izquierdo a 4000 (valor)''')
    audiometria_izquierdo_osea_500_nr = fields.Boolean(string='''Audiometría de tipo ósea del oído izquierdo a 500 (NR)''')
    audiometria_izquierdo_osea_500_valor = fields.Char(string='''Audiometría de tipo ósea del oído izquierdo a 500 (valor)''')
    audiometria_izquierdo_osea_6000_nr = fields.Boolean(string='''Audiometría de tipo ósea del oído izquierdo a 6000 (NR)''')
    audiometria_izquierdo_osea_6000_valor = fields.Char(string='''Audiometría de tipo ósea del oído izquierdo a 6000 (valor)''')
    audiometria_izquierdo_osea_8000_nr = fields.Boolean(string='''Audiometría de tipo ósea del oído izquierdo a 8000 (NR)''')
    audiometria_izquierdo_osea_8000_valor = fields.Char(string='''Audiometría de tipo ósea del oído izquierdo a 8000 (valor)''')
    audiometria_orejeras = fields.Boolean(string='''Orejeras (ficha audiológica)''')
    audiometria_otoscopia_derecho = fields.Char(string='''Otoscopía del oído derecho''')
    audiometria_otoscopia_izquierdo = fields.Char(string='''Otoscopía del oído izquierdo''')
    audiometria_ruido_moderado = fields.Boolean(string='''Ruido moderado''')
    audiometria_ruido_muy_intenso = fields.Boolean(string='''Ruido muy intenso''')
    audiometria_ruido_no_molesto = fields.Boolean(string='''Ruido no molesto''')
    audiometria_sintomas_disminucion_audicion = fields.Boolean(string='''Disminución de la audición (ficha audiológica)''')
    audiometria_sintomas_dolor_oidos = fields.Boolean(string='''Dolor de oídos (ficha audiológica)''')
    audiometria_sintomas_exposicion_ruido_18_horas = fields.Boolean(string='''Exposición a ruidos en las últimas 18 horas (ficha audiológica)''')
    audiometria_sintomas_infeccion_oido = fields.Boolean(string='''Infección de oído (ficha audiológica)''')
    audiometria_sintomas_mareos = fields.Boolean(string='''Mareos (ficha audiológica)''')
    audiometria_sintomas_otros = fields.Char(string='''Otros síntomas (ficha audiológica)''')
    audiometria_sintomas_otros_hay = fields.Boolean(string='''¿Hay otros síntomas? (ficha audiológica)''')
    audiometria_sintomas_zumbidos = fields.Boolean(string='''Zumbidos (ficha audiológica)''')
    audiometria_suma_decibeles_umbral_auditivo_porcentaje = fields.Float(string='''Porcentaje de la suma de decibeles del umbral auditivo''')
    audiometria_suma_decibeles_umbral_auditivo_resultado = fields.Selection(string='''Resultado de la suma de decibeles del umbral auditivo''',selection=[("normal","Normal"),("anormal","Anormal")])
    audiometria_suma_decibeles_umbral_auditivo_valor = fields.Integer(string='''Valor de la suma de decibeles del umbral auditivo''')
    audiometria_tapones = fields.Boolean(string='''Tapones (ficha audiológica)''')
    
    cie_10_audiometria_codigo_bilateral = fields.Char(string='''Código CIE-10 de la audiometría bilateral''')
    cie_10_audiometria_codigo_derecho = fields.Char(string='''Código CIE-10 de la audiometría del oído derecho''')
    cie_10_audiometria_codigo_izquierdo = fields.Char(string='''Código CIE-10 de la audiometría del oído izquierdo''')
    cie_10_audiometria_descripcion_bilateral = fields.Char(string='''Descripción CIE-10 de la audiometría bilateral''')
    cie_10_audiometria_descripcion_derecho = fields.Char(string='''Descripción CIE-10 de la audiometría del oído derecho''')
    cie_10_audiometria_descripcion_izquierdo = fields.Char(string='''Descripción CIE-10 de la audiometría del oído izquierdo''')
    cie_10_audiometria_recomendaciones_bilateral = fields.Text(string='''Recomendaciones CIE-10 de la audiometría bilateral''')
    cie_10_audiometria_recomendaciones_derecho = fields.Text(string='''Recomendaciones CIE-10 de la audiometría del oído derecho''')
    cie_10_audiometria_recomendaciones_izquierdo = fields.Text(string='''Recomendaciones CIE-10 de la audiometría del oído izquierdo''')
    cie_10_oftalmologia_tipo_diagnostico = fields.Selection(string='''Tipo de diagnóstico CIE-10 oftalmológico''',selection=[("normal","Normal"),("anormal","Anormal")])
    
    confinados_alcoholismo_cronico = fields.Boolean(string='''Alcoholismo crónico''')
    confinados_alteracion_agudeza_visual = fields.Boolean(string='''Alteración de la agudeza visual''')
    confinados_alteracion_coordinacion = fields.Boolean(string='''Alteración de la coordinación presente (dedo, nariz)''')
    confinados_alteracion_equilibrio = fields.Boolean(string='''Alteración presente del equilibrio (Roemeberg)''')
    confinados_anemia = fields.Boolean(string='''Anemia según criterios OMS 2011''')
    confinados_anormalidad_marcha = fields.Boolean(string='''Anormalidad en la marcha con los ojos cerrados y/o abiertos''')
    confinados_anormalidad_musculo_esqueletico = fields.Boolean(string='''Anormalidad en la evaluación musculo-esquelética''')
    confinados_apnea = fields.Boolean(string='''Síndrome de apnea obstructiva del sueño''')
    confinados_aptitud_trabajo = fields.Selection(string='''Aptitud para trabajo en espacios confinados''',selection=[("no_apto","No apto"),("observado","Observado"),("apto_con_restriccion","Apto con restricción"),("apto","Apto")])
    confinados_arritmia_soplos = fields.Boolean(string='''Arritmia cardiaca o soplos''')
    confinados_campimetria_anormal = fields.Boolean(string='''Campimetría anormal (Test de confrontación alterada)''')
    confinados_claustrofobia = fields.Boolean(string='''Evaluación psicológica anormal (claustrofobia)''')
    confinados_comentarios_anamnesis = fields.Text(string='''Comentarios (anamnesis de espacios confinados)''')
    confinados_consume_estupefacientes = fields.Boolean(string='''Consume estupefacientes''')
    confinados_consume_estupefacientes_tratamiento = fields.Boolean(string='''Consume estupefacientes, pero está en tratamiento''')
    confinados_detalle_examen_fisico = fields.Text(string='''Detalle (examen físico de espacios confinados)''')
    confinados_detalle_medicinas = fields.Text(string='''Detalle de medicinas (espacios confinados)''')
    confinados_enfermedades_alteracion_consciencia = fields.Boolean(string='''Todas las enfermedades que produzcan alteración de la consciencia''')
    confinados_enfermedades_movimientos_involuntarios = fields.Boolean(string='''Movimientos involuntarios por enfermedad''')
    confinados_frecuencia_cardiaca = fields.Integer(string='''Frecuencia cardiaca (espacios confinados)''')
    confinados_frecuencia_respiratoria = fields.Integer(string='''Frecuencia respiratoria (espacios confinados)''')
    confinados_hipoacusia = fields.Boolean(string='''Hipoacusia''')
    confinados_indice_masa_corporal = fields.Float(string='''Índice de masa corporal (espacios confinados)''', compute='''_compute_confinados_indice_masa_corporal''', store=True, readonly=False)
    confinados_lassegue_positivo = fields.Boolean(string='''Lassegue positivo''')
    confinados_limitacion_extremidades = fields.Boolean(string='''Limitación en fuerza y/o movilidad de extremidades''')
    confinados_nisfagmus = fields.Boolean(string='''Nisfagmus''')
    confinados_obesidad = fields.Boolean(string='''Obesidad''')
    confinados_otros_datos = fields.Text(string='''Otros datos relevantes (espacios confinados)''')
    confinados_perdida_recurrente_consciencia = fields.Boolean(string='''Pérdida recurrente de la consciencia''')
    confinados_peso = fields.Float(string='''Peso (espacios confinados)''')
    confinados_presion_arterial = fields.Char(string='''Presión arterial (espacios confinados)''')
    confinados_talla = fields.Integer(string='''Talla (espacios confinados)''')
    confinados_tratamiento_efectos_secundarios = fields.Boolean(string='''Efectos secundarios a causa de algún tratamiento''')
    confinados_validez_fin = fields.Date(string='''Fin de la validez de la aptitud (espacios confinados)''')
    confinados_validez_inicio = fields.Date(string='''Inicio de la validez de la aptitud (espacios confinados)''')
    confinados_vision_profundidad_alterada = fields.Boolean(string='''Prueba de visión de profundidad alterada''')
    
    @api.depends('confinados_talla','confinados_peso')
    def _compute_confinados_indice_masa_corporal(self):
        for rec in self:
            rec.confinados_indice_masa_corporal = rec.confinados_talla and rec.confinados_peso / ((rec.confinados_talla / 100.0) ** 2) or 0.0
    
    dermatologia_cambio_coloracion_cuestionario = fields.Boolean(string='''¿Presenta algún cambio de coloración en la piel?''')
    dermatologia_cambios_unas_cuestionario = fields.Boolean(string='''¿Presenta cambios en las uñas?''')
    dermatologia_comentarios_cuestionario = fields.Text(string='''Comentarios (cuestionario de dermatología)''')
    dermatologia_comezon_cuestionario = fields.Boolean(string='''¿Tiene comezón?''')
    dermatologia_comezon_localizacion = fields.Char(string='''¿Dónde se localiza la comezón?''')
    dermatologia_dermatopatia_medico = fields.Boolean(string='''Al examen físico, ¿presenta el paciente alguna lesión sugerente a dermatopatía?''')
    dermatologia_enfermedades_piel_cuestionario = fields.Boolean(string='''¿Sufre Ud. enfermedades de la piel?''')
    dermatologia_enfermedades_piel_diagnostico = fields.Char(string='''¿Qué diagnóstico le han dado de dichas enfermedades?''')
    dermatologia_enrojecimiento_cuestionario = fields.Boolean(string='''¿Ud. tiene enrojecimiento de alguna zona del cuerpo?''')
    dermatologia_enrojecimiento_localizacion = fields.Char(string='''¿Dónde se localiza el enrojecimiento?''')
    dermatologia_equipo_proteccion_personal_cuestionario = fields.Boolean(string='''¿Usa EPP (equipo de protección personal)?''')
    dermatologia_equipo_proteccion_personal_especifico = fields.Char(string='''¿Qué tipo de EPP usa?''')
    dermatologia_fotoprotector_recomendado = fields.Char(string='''Fotoprotector recomendado''')
    dermatologia_fototipo_piel = fields.Selection(string='''Tipo de fototipo de piel''',selection=[("fototipo_i","Fototipo I"),("fototipo_ii","Fototipo II"),("fototipo_iii","Fototipo III"),("fototipo_iv","Fototipo IV"),("fototipo_v","Fototipo V"),("fototipo_vi","Fototipo VI")])
    dermatologia_hinchazon_cuestionario = fields.Boolean(string='''¿Presenta hinchazón en parte de su cuerpo?''')
    dermatologia_hinchazon_localizacion = fields.Char(string='''¿Dónde se localiza la hinchazón?''')
    dermatologia_interconsulta_medico = fields.Boolean(string='''¿Necesita el paciente interconsulta con la especialidad de dermatología?''')
    dermatologia_lesion_cuestionario = fields.Boolean(string='''¿Tiene alguna lesión?''')
    dermatologia_lesion_duracion = fields.Char(string='''¿Desde cuándo tiene la lesión?''')
    dermatologia_lesion_frecuente_cuestionario = fields.Boolean(string='''¿Estas lesiones se repiten varias veces al año?''')
    dermatologia_lesion_localizacion = fields.Char(string='''¿Dónde se localiza la lesión?''')
    dermatologia_mas_pruebas_medico = fields.Boolean(string='''El paciente necesita ser evaluado por médico dermatologico para la realización de las siguientes pruebas : Pruebas de sensibilidad subcotánea, Luz de Wood y Maniobra de Nikolsky''')
    dermatologia_medicacion_cuestionario = fields.Boolean(string='''¿Está tomando alguna medicación?''')
    dermatologia_rinitis_asma_cuestionario = fields.Boolean(string='''¿Sufre de rinitis alérgica o asma?''')
    dermatologia_tamizaje_observaciones = fields.Text(string='''Observaciones de tamizaje (dermatología)''')
    
    ekg_antecedentes_familiares = fields.Char(string='''Antecedentes familiares''')
    ekg_aptitud_trabajo_altura = fields.Selection(string='''Aptitud para trabajos en altura mayor a 2500m''',selection=[("apto","Apto"),("no_apto","No apto")])
    ekg_aptitud_trabajo_forzado = fields.Selection(string='''Aptitud para trabajo forzado''',selection=[("apto","Apto"),("no_apto","No apto")])
    ekg_asintomatico = fields.Boolean(string='''Asintomático''')
    ekg_cansancio_rapido = fields.Boolean(string='''Cansancio rápido''')
    ekg_choque_punta = fields.Char(string='''Choque de la punta (interpretación EKG)''')
    ekg_claudicacion_intermitente = fields.Boolean(string='''Claudicación intermitente''')
    ekg_diabetes = fields.Boolean(string='''Diabetes''')
    ekg_diagnostico = fields.Selection(string='''Diagnóstico (electrocardiograma)''',selection=[("diagnostico_medicina_ocupacional","DiagMO"),("otros_diagnosticos","OtrosD")])
    ekg_dinitrofenol = fields.Boolean(string='''Dinitrofenol''')
    ekg_dislipidemias = fields.Boolean(string='''Dislipidemias''')
    ekg_dolor_precordial_antecedentes = fields.Boolean(string='''Dolor precordial''')
    ekg_dolor_precordial_sintomas_actuales = fields.Boolean(string='''Dolor precordial (síntomas actuales)''')
    ekg_eje_qrs = fields.Float(string='''Eje QRS (interpretación EKG)''')
    ekg_examen_corazon = fields.Char(string='''Examen del corazón''')
    ekg_frecuencia_cardiaca = fields.Integer(string='''Frecuencia cardiaca (interpretación EKG)''')
    ekg_frecuencia_cardiaca_preferencial = fields.Integer(string='''Frecuencia cardiaca preferencial''')
    ekg_infarto_agudo_miocardio = fields.Boolean(string='''IMAs''')
    ekg_intervalo_pr = fields.Float(string='''Intervalo PR (interpretación EKG)''')
    ekg_intervalo_qrs = fields.Float(string='''Intervalo QRS (interpretación EKG)''')
    ekg_intervalo_qt = fields.Float(string='''Intervalo QT (interpretación EKG)''')
    ekg_lipotimias = fields.Boolean(string='''Lipotimias''')
    ekg_mareos = fields.Boolean(string='''Mareos''')
    ekg_mareos_sintomas_actuales = fields.Boolean(string='''Mareos (síntomas actuales)''')
    ekg_obesidad = fields.Boolean(string='''Obesidad''')
    ekg_onda_p = fields.Float(string='''Onda P (interpretación EKG)''')
    ekg_onda_q = fields.Float(string='''Onda Q (interpretación EKG)''')
    ekg_onda_r = fields.Float(string='''Onda R (interpretación EKG)''')
    ekg_onda_s = fields.Float(string='''Onda S (interpretación EKG)''')
    ekg_onda_t = fields.Float(string='''Onda T (interpretación EKG)''')
    ekg_onda_u = fields.Float(string='''Onda U (interpretación EKG)''')
    ekg_otros_antecedentes_cardiologicos = fields.Char(string='''Otros antecedentes cardiológicos''')
    ekg_otros_hallazgos_corazon = fields.Char(string='''Otros hallazgos en el corazón''')
    ekg_otros_sintomas_cardiologicos = fields.Char(string='''Otros síntomas cardiológicos''')
    ekg_palpitaciones = fields.Boolean(string='''Palpitaciones''')
    ekg_palpitaciones_sintomas_actuales = fields.Boolean(string='''Palpitaciones (síntomas actuales)''')
    ekg_perdida_de_conciencia = fields.Boolean(string='''Pérdida de conciencia''')
    ekg_presion_alta = fields.Boolean(string='''Presión alta''')
    ekg_presion_arterial = fields.Char(string='''Presión arterial (interpretación EKG)''')
    ekg_presion_arterial_preferencial = fields.Char(string='''Presión arterial preferencial''')
    ekg_ritmo = fields.Char(string='''Ritmo (interpretación EKG)''')
    ekg_segmento_st = fields.Float(string='''Segmento ST (interpretación EKG)''')
    ekg_soplo_cardiaco = fields.Boolean(string='''Soplo cardiaco''')
    ekg_tabaquismo = fields.Boolean(string='''Tabaquismo''')
    ekg_varices_miembros_inferiores = fields.Boolean(string='''Várices en miembros inferiores''')
    
    espirometria_informe_medico = fields.Text(string='''Informe médico''')
    espirometria_diagnostico = fields.Selection(string='''Diagnóstico (espirometría)''',selection=[("diagnostico_medicina_ocupacional","DiagMO"),("otros_diagnosticos","OtrosD")])
    espirometria_informe_medico_recomendaciones = fields.Text(string='''Recomendaciones de informe médico (espirometría)''')
    espirometria_fvc_teor = fields.Char(string='''Capacidad vital forzada (teórica) (FVC)''')
    espirometria_fev1_teor = fields.Char(string='''Volumen espiratorio forzado en el primer segundo (teórico) (FEV1)''')
    espirometria_fev1_fvc_teor = fields.Char(string='''Cociente FEV1/FVC (teórico)''')
    espirometria_pef_teor = fields.Char(string='''Flujo espiratorio máximo (teórico) (PEF)''')
    espirometria_fef2575_teor = fields.Char(string='''Flujo espiratorio medio (teórico) (FEF 25-75%)''')
    espirometria_fvc_pre = fields.Char(string='''Capacidad vital forzada (pre) (FVC''')
    espirometria_fev1_pre = fields.Char(string='''Volumen espiratorio forzado en el primer segundo (pre) (FEV1)''')
    espirometria_fev1_fvc_pre = fields.Char(string='''Cociente FEV1/FVC (pre)''')
    espirometria_pef_pre = fields.Char(string='''Flujo espiratorio máximo (pre) (PEF)''')
    espirometria_fef2575_pre = fields.Char(string='''Flujo espiratorio medio (pre) (FEF 25-75%)''')
    espirometria_conclusion = fields.Selection(string='''Conclusión (espirometría)''',selection=[("patron_normal_espirometrico","Patrón normal espirométrico"),("con_alteracion_funcional","Con alteración funcional")])
    espirometria_conclusion_razon = fields.Text(string='''Razón de la conclusión''')
    espirometria_desprendimiento_retina_cirugia = fields.Boolean(string='''¿Tuvo algún desprendimiento de retina o una operación (cirugía) de los ojos, tórax o abdomen en los últimos 3 meses?''')
    espirometria_ataque_cardiaco_infarto = fields.Boolean(string='''¿Ha tenido algún ataque al cardíaco o infarto al corazón en los últimos 3 meses?''')
    espirometria_hospitalizado_problemas_corazon = fields.Boolean(string='''¿Ha estado hospitalizado(a) por cualquier otro problema del corazón en los últimos 3 meses?''')
    espirometria_medicamentos_tuberculosis = fields.Boolean(string='''¿Está usando medicamentos para la tuberculosis, en este momento?''')
    espirometria_embarazo = fields.Boolean(string='''¿Está usted embarazada actualmente?''')
    espirometria_hemoptisis = fields.Boolean(string='''Hemoptisis''')
    espirometria_neumotorax = fields.Boolean(string='''Neumotórax''')
    espirometria_traqueostomia = fields.Boolean(string='''Traqueostomía''')
    espirometria_sonda_pleural = fields.Boolean(string='''Sonda pleural''')
    espirometria_aneurisma = fields.Boolean(string='''Aneurisma (cerebral, abdominal o tórax)''')
    espirometria_embolia_pulmonar = fields.Boolean(string='''Embolia pulmonar''')
    espirometria_infarto_reciente = fields.Boolean(string='''Infarto reciente''')
    espirometria_inestabilidad_cardiovascular = fields.Boolean(string='''Inestabilidad cardiovascular''')
    espirometria_fiebre_nausea_vomito = fields.Boolean(string='''Fiebre, náuseas y/o vómito''')
    espirometria_embarazo_avanzado = fields.Boolean(string='''Embarazo avanzado''')
    espirometria_embarazo_complicado = fields.Boolean(string='''Embarazo complicado''')
    espirometria_infeccion_respiratoria_3_semanas = fields.Boolean(string='''¿Tuvo una infección respiratoria (resfriado) en las últimas 3 semanas?''')
    espirometria_infeccion_oido_3_semanas = fields.Boolean(string='''¿Tuvo una infección en el oído en las últimas 3 semanas?''')
    espirometria_aerosoles_nebulizaciones_3_horas = fields.Boolean(string='''¿Uso aerosoles (sprays inhalados) o nebulizaciones con broncodilatadores, en las últimas 3 horas?''')
    espirometria_brondocilatador_8_horas = fields.Boolean(string='''¿Ha usado algún medicamento broncodilatador en las últimas 8 horas?''')
    espirometria_fuma_2_horas = fields.Boolean(string='''¿Fumó (cualquier tipo de cigarro) en las últimas dos horas?''')
    espirometria_fuma_2_horas_descripcion = fields.Char(string='''¿Cuántos cigarros fumó (cualquier tipo de cigarro) en las últimas dos horas?''')
    espirometria_ejercicio_fisico_ultima_hora = fields.Boolean(string='''¿Realizó algún ejercicio físico fuerte (gimnasia, caminata, trote) en la última hora?''')
    espirometria_comida_ultima_hora = fields.Boolean(string='''¿Comió en la úlltima hora?''')
    
    grandes_alturas_alergias = fields.Boolean(string='''Alergias''')
    grandes_alturas_alergias_descripcion = fields.Char(string='''Alergias (descripción)''')
    grandes_alturas_apnea_sueno = fields.Boolean(string='''Apnea del sueño''')
    grandes_alturas_aptitud_trabajo = fields.Selection(string='''Aptitud para trabajo en grandes alturas''',selection=[("apto","Apto"),("apto_con_restriccion","Apto con restricción"),("no_apto","No apto")])
    grandes_alturas_cirugia_mayor_reciente = fields.Boolean(string='''Cirugía mayor reciente''')
    grandes_alturas_desordenes_coagulacion = fields.Boolean(string='''Desórdenes de la coagulación: trombosis, otros''')
    grandes_alturas_diabetes_mellitus = fields.Boolean(string='''Diabetes mellitus''')
    grandes_alturas_embarazo = fields.Boolean(string='''Embarazo''')
    grandes_alturas_frecuencia_cardiaca = fields.Integer(string='''Frecuencia cardiaca (grandes alturas)''')
    grandes_alturas_frecuencia_respiratoria = fields.Integer(string='''Frecuencia respiratoria (grandes alturas)''')
    grandes_alturas_hipertension_arterial = fields.Boolean(string='''Hipertensión arterial''')
    grandes_alturas_indice_masa_corporal = fields.Float(string='''Índice de masa corporal (grandes alturas)''')
    grandes_alturas_infecciones_recientes = fields.Boolean(string='''Infecciones recientes (de moderadas a severas)''')
    grandes_alturas_medicacion_actual = fields.Boolean(string='''Uso de medicación actual''')
    grandes_alturas_medicacion_actual_descripcion = fields.Text(string='''Uso de medicación actual (descripción)''')
    grandes_alturas_obesidad = fields.Boolean(string='''Obesidad''')
    grandes_alturas_observaciones = fields.Text(string='''Observaciones (grandes alturas)''')
    grandes_alturas_otra_contraindicacion = fields.Boolean(string='''Otra contraindicación médica importante''')
    grandes_alturas_otra_contraindicacion_descripcion = fields.Char(string='''Otra contraindicación médica importante (descripción)''')
    grandes_alturas_presion_arterial = fields.Char(string='''Presión arterial (grandes alturas)''')
    grandes_alturas_problemas_cardiacos = fields.Boolean(string='''Problemas cardiacos: marcapasos, coronariopatía, otros''')
    grandes_alturas_problemas_digestivos = fields.Boolean(string='''Problemas digestivos: sangrado digestivo, hepatitis, cirrosis hepática, otros''')
    grandes_alturas_problemas_neurologicos = fields.Boolean(string='''Problemas neurológicos: epilepsia, vértigos, otros''')
    grandes_alturas_problemas_oftalmologicos = fields.Boolean(string='''Problemas oftalmológicos: retinopatía, glaucoma, otros''')
    grandes_alturas_problemas_respiratorios = fields.Boolean(string='''Problemas respiratorios: asma, EPOC, otros''')
    grandes_alturas_saturacion_oxigeno = fields.Float(string='''Saturación de oxígeno (grandes alturas)''')
    
    laboratorio_abastonados_mm3 = fields.Float(string='''Abastonados (mm3)''')
    laboratorio_abastonados_porcentaje = fields.Float(string='''Abastonados (%)''')
    laboratorio_basofilos_mm3 = fields.Float(string='''Basofilos (mm3)''')
    laboratorio_basofilos_porcentaje = fields.Float(string='''Basofilos (%)''')
    laboratorio_bioquimica = fields.Boolean(string='''Bioquímica''')
    laboratorio_ccmh = fields.Integer(string='''CCMH (laboratorio)''')
    laboratorio_celulas_inmaduras = fields.Integer(string='''Celulas inmaduras''')
    laboratorio_colesterol_total = fields.Float(string='''Colesterol total''')
    laboratorio_comentarios = fields.Text(string='''Comentarios (laboratorio)''')
    laboratorio_eosinofilos_mm3 = fields.Float(string='''Eosinofilos (mm3)''')
    laboratorio_eosinofilos_porcentaje = fields.Float(string='''Eosinofilos (%)''')
    laboratorio_eritrocitos = fields.Integer(string='''Eritrocitos''')
    laboratorio_eritrosedimentacion = fields.Float(string='''Eritrosedimentacion (VSG)''')
    laboratorio_examen_quimico_acido_ascorbico = fields.Char(string='''Ácido ascórbico (examen químico)''')
    laboratorio_examen_quimico_bilirrubinas = fields.Char(string='''Bilirrubinas (examen químico)''')
    laboratorio_examen_quimico_cetonas = fields.Char(string='''Cetonas (examen químico)''')
    laboratorio_examen_quimico_nitritos = fields.Char(string='''Nitritos (examen químico)''')
    laboratorio_examen_quimico_ph = fields.Float(string='''pH (examen químico)''')
    laboratorio_examen_quimico_proteinas = fields.Char(string='''Proteínas (examen químico)''')
    laboratorio_examen_quimico_sangre = fields.Char(string='''Sangre (examen químico)''')
    laboratorio_examen_quimico_urobilinogeno = fields.Char(string='''Urobilinógeno (examen químico)''')
    laboratorio_factor_rh = fields.Selection(string='''Factor RH''',selection=[("positivo","+"),("negativo","-")])
    laboratorio_filamentos_mucosos = fields.Text(string='''Filamentos mucosos''')
    laboratorio_glucosa = fields.Float(string='''Glucosa''')
    laboratorio_grupo_sanguineo = fields.Selection(string='''Grupo sanguíneo''',selection=[("o","O"),("a","A"),("b","B"),("ab","AB")])
    laboratorio_hcm = fields.Integer(string='''HCM (laboratorio)''')
    laboratorio_hematocrito = fields.Float(string='''Hematocrito''')
    laboratorio_hemoglobina = fields.Float(string='''Hemoglobina''')
    laboratorio_leucocitos = fields.Integer(string='''Leucocitos''')
    laboratorio_linfocitos_mm3 = fields.Float(string='''Linfocitos (mm3)''')
    laboratorio_linfocitos_porcentaje = fields.Float(string='''Linfocitos (%)''')
    laboratorio_monocitos_mm3 = fields.Float(string='''Monocitos (mm3)''')
    laboratorio_monocitos_porcentaje = fields.Float(string='''Monocitos (%)''')
    laboratorio_orina_aspecto = fields.Char(string='''Aspecto de orina''')
    laboratorio_orina_color = fields.Char(string='''Color de orina''')
    laboratorio_orina_densidad = fields.Float(string='''Densidad de orina''')
    laboratorio_orina_examen_completo = fields.Boolean(string='''Examen completo de orina''')
    laboratorio_orina_examen_completo_resultado = fields.Selection(string='''Resultados del examen completo de orina''',selection=[("normal","Normal"),("anormal","Anormal")])
    laboratorio_recuento_plaquetas = fields.Integer(string='''Recuento de plaquetas''')
    laboratorio_resultados_glicemia = fields.Char(string='''Resultados de glicemia''')
    laboratorio_resultados_perfil_lipidico = fields.Char(string='''Resultados de perfil lipídico''')
    laboratorio_sedimento_bacterias = fields.Char(string='''Bacterias (sedimento)''')
    laboratorio_sedimento_celulas_epiteliales = fields.Char(string='''Células epiteliales (sedimento)''')
    laboratorio_sedimento_cilindros = fields.Char(string='''Cilindros (sedimento)''')
    laboratorio_sedimento_cristales = fields.Char(string='''Cristales (sedimento)''')
    laboratorio_sedimento_hematies = fields.Char(string='''Hematíes (sedimento)''')
    laboratorio_sedimento_leucocitos = fields.Char(string='''Leucocitos (sedimento)''')
    laboratorio_segmentados_mm3 = fields.Float(string='''Segmentados (mm3)''')
    laboratorio_segmentados_porcentaje = fields.Float(string='''Segmentados (%)''')
    laboratorio_trigliceridos = fields.Float(string='''Triglicéridos''')
    laboratorio_vcm = fields.Integer(string='''VCM (laboratorio)''')
    
    laboratorio_hematologia_carboxihemoglobina = fields.Float(string='Carboxihemoglobina (hematología)')
    laboratorio_hematologia_tiempo_coagulacion< = fields.Float(string='Tiempo de coagulación (hematología)')
    laboratorio_antigeno_prostatico_especifico_psa = fields.Float(string='Antígeno prostático específico (PSA)')
    laboratorio_hisopado_hematies = fields.Float(string='Hematíes (hisopado nasofaringeo)')
    laboratorio_hisopado_gram = fields.Float(string='Coloración gram (hisopado nasofaringeo)')
    laboratorio_bioquimica_colesterol_hdl = fields.Float(string='Colesterol HDL (bioquímica)')
    laboratorio_bioquimica_colesterol_ldl = fields.Float(string='Colesterol LDL (bioquímica)')
    laboratorio_bioquimica_colesterol_vldl = fields.Float(string='Colesterol VLDL (bioquímica)')
    laboratorio_bioquimica_urea = fields.Float(string='Úrea (bioquímica)')
    laboratorio_bioquimica_creatinina = fields.Float(string='Creatinina (bioquímica)')
    laboratorio_bioquimica_acido_urico = fields.Float(string='Ácido úrico (bioquímica)')
    laboratorio_bioquimica_tgo = fields.Float(string='Transaminasa glutámico oxalacética (bioquímica)')
    laboratorio_bioquimica_tgp = fields.Float(string='Transaminasa glutámico pirúvica (bioquímica)')
    laboratorio_bioquimica_vdrl = fields.Boolean(string='Prueba venérea (bioquímica)')
    laboratorio_bioquimica_sodio = fields.Float(string='Sodio (bioquímica)')
    laboratorio_bioquimica_cloro = fields.Float(string='Cloro (bioquímica)')
    laboratorio_bioquimica_potasio = fields.Float(string='Potasio (bioquímica)')
    laboratorio_bioquimica_hemoglobina_glicosilada = fields.Float(string='Hemoglobina glicosilada (HbA1c) - Electroforesis Capilar (bioquímica)')
    laboratorio_bioquimica_proteinas_totales = fields.Float(string='Proteínas totales (bioquímica)')
    laboratorio_bioquimica_albumina_serica = fields.Float(string='Albúmina sérica (bioquímica)')
    laboratorio_bioquimica_globulinas = fields.Float(string='Globulinas (bioquímica)')
    laboratorio_bioquimica_relacion_albumina_globulina = fields.Float(string='Relación albúmina / globulina (bioquímica)')
    laboratorio_bioquimica_proteina_c_reactiva = fields.Float(string='Proteína C reactiva (bioquímica)')
    laboratorio_bioquimica_deshidrogenasa_lactica = fields.Float(string='Deshidrogenasa láctica (bioquímica)')
    laboratorio_perfil_hepatico_transaminasa_tgo = fields.Float(string='Transaminasa TGO (AST) (perfil hepático)')
    laboratorio_perfil_hepatico_transaminasa_tgp = fields.Float(string='Transaminasa TGP (ALT) (perfil hepático)')
    laboratorio_perfil_hepatico_proteinas_totales = fields.Float(string='Proteínas totales (perfil hepático)')
    laboratorio_perfil_hepatico_albumina = fields.Float(string='Albúmina (perfil hepático)')
    laboratorio_perfil_hepatico_bilirrubinas_total = fields.Float(string='Bilirrubinas total (perfil hepático)')
    laboratorio_perfil_hepatico_bilirrubinas_directas = fields.Float(string='Bilirrubinas directas (perfil hepático)')
    laboratorio_perfil_hepatico_bilirrubinas_indirectas = fields.Float(string='Bilirrubinas indirectas (perfil hepático)')
    laboratorio_perfil_hepatico_fosfatasa_alcalina = fields.Float(string='Fosfatasa alcalina (perfil hepático)')
    laboratorio_perfil_hepatico_acido_urico = fields.Float(string='Ácido úrico (perfil hepático)')
    laboratorio_perfil_hepatico_ldh = fields.Float(string='Lactato deshidrogenasa (LDH) (perfil hepático)')
    laboratorio_perfil_hepatico_ggtp = fields.Float(string='Gamma Glutamil Transpeptidasa (GGTP) (perfil hepático)')
    laboratorio_parasitologico_1_muestra = fields.Float(string='Examen macroscópico (examen parasitológico seriado)')
    laboratorio_parasitologico_1_examen = fields.Float(string='Examen macroscópico (examen parasitológico seriado)')
    laboratorio_parasitologico_1_color = fields.Float(string='Color (examen parasitológico seriado)')
    laboratorio_parasitologico_1_consistencia = fields.Float(string='Consistencia (examen parasitológico seriado)')
    laboratorio_parasitologico_1_moco = fields.Float(string='Moco (examen parasitológico seriado)')
    laboratorio_parasitologico_1_sangre = fields.Float(string='Sangre (examen parasitológico seriado)')
    laboratorio_parasitologico_1_parasitos = fields.Float(string='Parásitos (examen parasitológico seriado)')
    laboratorio_parasitologico_2_examen = fields.Float(string='Examen macroscópico (examen parasitológico seriado)')
    laboratorio_parasitologico_2_color = fields.Float(string='Color (examen parasitológico seriado)')
    laboratorio_parasitologico_2_consistencia = fields.Float(string='Consistencia (examen parasitológico seriado)')
    laboratorio_parasitologico_2_moco = fields.Float(string='Moco (examen parasitológico seriado)')
    laboratorio_parasitologico_2_sangre = fields.Float(string='Sangre (examen parasitológico seriado)')
    laboratorio_parasitologico_2_parasitos = fields.Float(string='Parásitos (examen parasitológico seriado)')
    laboratorio_serologia_rpr = fields.Float(string='Reagina plasmática rápida (RPR) (serología)')
    laboratorio_serologia_subunidad_beta_cualitativo = fields.Float(string='Sub-unidad beta cualitativo (serología)')
    laboratorio_serologia_hbsag_eclia = fields.Float(string='Antígeno de superficie del VHB (HBsAg) mediante ECLIA (serología)')
    laboratorio_serologia_hcv_eclia = fields.Float(string='HCV (Hepatitis C) - ECLIA (serología)')
    laboratorio_serologia_hiv_1_2 = fields.Float(string='HIV (1 - 2) (serología)')
    laboratorio_serologia_examen = fields.Float(string='Examen macroscópico (serología)')
    laboratorio_serologia_examen = fields.Float(string='Examen macroscópico (serología)')
    laboratorio_serologia_examen = fields.Float(string='Examen macroscópico (serología)')
    laboratorio_serologia_examen = fields.Float(string='Examen macroscópico (serología)')
    laboratorio_serologia_examen = fields.Float(string='Examen macroscópico (serología)')
    laboratorio_serologia_examen = fields.Float(string='Examen macroscópico (serología)')
    laboratorio_serologia_examen = fields.Float(string='Examen macroscópico (serología)')
    laboratorio_serologia_examen = fields.Float(string='Examen macroscópico (serología)')
    laboratorio_serologia_examen = fields.Float(string='Examen macroscópico (serología)')
    laboratorio_serologia_examen = fields.Float(string='Examen macroscópico (serología)')
    laboratorio_serologia_examen = fields.Float(string='Examen macroscópico (serología)')
    laboratorio_serologia_examen = fields.Float(string='Examen macroscópico (serología)')
    laboratorio_serologia_examen = fields.Float(string='Examen macroscópico (serología)')
    laboratorio_serologia_examen = fields.Float(string='Examen macroscópico (serología)')
    laboratorio_serologia_examen = fields.Float(string='Examen macroscópico (serología)')
    laboratorio_serologia_examen = fields.Float(string='Examen macroscópico (serología)')
    laboratorio_serologia_examen = fields.Float(string='Examen macroscópico (serología)')
    laboratorio_serologia_examen = fields.Float(string='Examen macroscópico (serología)')
    laboratorio_serologia_examen = fields.Float(string='Examen macroscópico (serología)')
    laboratorio_serologia_examen = fields.Float(string='Examen macroscópico (serología)')
    laboratorio_serologia_examen = fields.Float(string='Examen macroscópico (serología)')
    laboratorio_serologia_examen = fields.Float(string='Examen macroscópico (serología)')
    laboratorio_serologia_examen = fields.Float(string='Examen macroscópico (serología)')
    laboratorio_serologia_examen = fields.Float(string='Examen macroscópico (serología)')
    
    medicina_abdomen = fields.Selection(string='''Abdomen''',selection=[("normal","Normal"),("anormal","Anormal"),("diferido","Diferido")])
    medicina_abdomen_razon = fields.Text(string='''Razón''')
    medicina_abeg = fields.Boolean(string='''ABEG''')
    medicina_abeh = fields.Boolean(string='''ABEH''')
    medicina_aben = fields.Boolean(string='''ABEN''')
    medicina_anamnesis = fields.Text(string='''Anamnesis''')
    medicina_anillos_inguinales = fields.Selection(string='''Anillos Inguinales''',selection=[("normal","Normal"),("anormal","Anormal"),("diferido","Diferido")])
    medicina_anillos_inguinales_razon = fields.Text(string='''Razón''')
    medicina_anormalidades_regional = fields.Char(string='''Anormalidades''')
    medicina_ap_locomotor = fields.Selection(string='''Ap. Locomotor''',selection=[("conservado","Conservado"),("disminuido","Disminuido")])
    medicina_ap_locomotor_razon = fields.Char(string='''Razón''')
    medicina_boca = fields.Selection(string='''Boca''',selection=[("normal","Normal"),("anormal","Anormal"),("diferido","Diferido")])
    medicina_boca_razon = fields.Text(string='''Razón''')
    medicina_cabeza_cabello = fields.Selection(string='''Cabeza y Cabello''',selection=[("normal","Normal"),("anormal","Anormal")])
    medicina_cabeza_cabello_razon = fields.Text(string='''Razón''')
    medicina_columna = fields.Selection(string='''Columna''',selection=[("normal","Normal"),("anormal","Anormal"),("diferido","Diferido")])
    medicina_columna_razon = fields.Text(string='''Razón''')
    medicina_corazon = fields.Selection(string='''Corazón''',selection=[("normal","Normal"),("anormal","Anormal")])
    medicina_corazon_razon = fields.Char(string='''Razón''')
    medicina_cuello_garganta = fields.Selection(string='''Cuello y Garganta''',selection=[("normal","Normal"),("anormal","Anormal"),("diferido","Diferido")])
    medicina_cuello_garganta_razon = fields.Text(string='''Razón''')
    medicina_ectoscopia = fields.Selection(string='''Ectoscopía''',selection=[("normal","Normal"),("anormal","Anormal"),("diferido","Diferido")])
    medicina_ectoscopia_razon = fields.Char(string='''Razón''')
    medicina_faringe = fields.Selection(string='''Faringe''',selection=[("normal","Normal"),("anormal","Anormal"),("diferido","Diferido")])
    medicina_faringe_razon = fields.Text(string='''Razón''')
    medicina_genitales = fields.Selection(string='''Genitales''',selection=[("normal","Normal"),("anormal","Anormal"),("diferido","Diferido")])
    medicina_genitales_razon = fields.Text(string='''Razón''')
    medicina_genito_urinario = fields.Selection(string='''Genito-Urinario''',selection=[("normal","Normal"),("anormal","Anormal"),("diferido","Diferido")])
    medicina_genito_urinario_razon = fields.Text(string='''Razón''')
    medicina_hernias = fields.Boolean(string='''Hernias''')
    medicina_hernias_razon = fields.Text(string='''Razón''')
    medicina_lotep = fields.Boolean(string='''LOTEP''')
    medicina_mama_derecha = fields.Selection(string='''Mama Derecha''',selection=[("normal","Normal"),("anormal","Anormal"),("diferido","Diferido")])
    medicina_mama_derecha_razon = fields.Char(string='''Razón''')
    medicina_mama_izquierda = fields.Selection(string='''Mama Izquierda''',selection=[("normal","Normal"),("anormal","Anormal"),("diferido","Diferido")])
    medicina_mama_izquierda_razon = fields.Char(string='''Razón''')
    medicina_marcha_tandem = fields.Selection(string='''Marcha Tandem''',selection=[("conservado","Conservado"),("anormal","Anormal"),("no_realizado","No Realizado")])
    medicina_marcha_tandem_razon = fields.Char(string='''Razón''')
    medicina_miembro_inferior_derecho = fields.Selection(string='''Miembro Inferior Derecho''',selection=[("normal","Normal"),("anormal","Anormal"),("diferido","Diferido")])
    medicina_miembro_inferior_derecho_razon = fields.Char(string='''Razón''')
    medicina_miembro_inferior_izquierdo = fields.Selection(string='''Miembro Inferior Izquierdo''',selection=[("normal","Normal"),("anormal","Anormal"),("diferido","Diferido")])
    medicina_miembro_inferior_izquierdo_razon = fields.Char(string='''Razón''')
    medicina_miembro_superior_derecho = fields.Selection(string='''Miembro Superior Derecho''',selection=[("normal","Normal"),("anormal","Anormal"),("diferido","Diferido")])
    medicina_miembro_superior_derecho_razon = fields.Char(string='''Razón''')
    medicina_miembro_superior_izquierdo = fields.Selection(string='''Miembro Superior Izquierdo''',selection=[("normal","Normal"),("anormal","Anormal"),("diferido","Diferido")])
    medicina_miembro_superior_izquierdo_razon = fields.Char(string='''Razón''')
    medicina_nariz = fields.Selection(string='''Nariz''',selection=[("normal","Normal"),("anormal","Anormal"),("diferido","Diferido")])
    medicina_nariz_razon = fields.Text(string='''Razón''')
    medicina_piel_faneras = fields.Selection(string='''Piel y Faneras''',selection=[("normal","Normal"),("anormal","Anormal"),("diferido","Diferido")])
    medicina_piel_faneras_razon = fields.Text(string='''Razón''')
    medicina_pulmones = fields.Selection(string='''Pulmones''',selection=[("normal","Normal"),("anormal","Anormal"),("diferido","Diferido")])
    medicina_pulmones_razon = fields.Char(string='''Razón''')
    medicina_sistema_linfatico = fields.Selection(string='''Sistema Linfático''',selection=[("normal","Normal"),("anormal","Anormal"),("diferido","Diferido")])
    medicina_sistema_linfatico_razon = fields.Text(string='''Razón''')
    medicina_sistema_nervioso = fields.Selection(string='''Sistema Nervioso''',selection=[("normal","Normal"),("anormal","Anormal"),("diferido","Diferido")])
    medicina_sistema_nervioso_razon = fields.Text(string='''Razón''')
    
    @api.model
    def _get_default_musculo_esqueletico_abdomen_1(self):
        return b'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'
    
    @api.model
    def _get_default_musculo_esqueletico_abdomen_2(self):
        return b'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'
    
    @api.model
    def _get_default_musculo_esqueletico_abdomen_3(self):
        return b'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'
    
    @api.model
    def _get_default_musculo_esqueletico_abdomen_4(self):
        return b'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'
    
    @api.model
    def _get_default_musculo_esqueletico_cadera_1(self):
        return b'/9j/4AAQSkZJRgABAQEAYABgAAD/2wBDAAIBAQIBAQICAgICAgICAwUDAwMDAwYEBAMFBwYHBwcGBwcICQsJCAgKCAcHCg0KCgsMDAwMBwkODw0MDgsMDAz/2wBDAQICAgMDAwYDAwYMCAcIDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAz/wAARCABJAGcDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD9/KBxwBgCiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAGYKMnoKTePehzxTGOB60AP3j3o3j3qN5FiBZ2VVHXPHtSTyi3iaRyQqDJoBku8e9G8e9c/8NviHp3xT8Jwa3pRn+xXMksUfnJsYmOVo24/3lbHqK2I72GWSRFljLxHDDPINAXLG8e9KDkZrA8dfEXRvhv4cn1bWr+Gx0+3Kh5WywBYgKMLySTW7Gcg85FNoVx1FGc9OaKQwooooAKKKKAGy8lef/r18ofEr9sC2i8R+L7fUvjP4J+F6eFdSNlJZXlrFdXDxBFZZsvIpIcE8KDgg819YN29q821f9j34VeItQuLzUfh54Qv7y7dpJZ7nTIppHZvvHcyk5PtVRa6gt7nwj4I+OOjftLfEfxnPqfxh8M+KdW8OzwJaWuv+ILnwzpHlOgZZIraDJkGOfMYklicDC1z3xk1fwvpE4h8QfET4leHVjuz9nk8J/EH+29MvmdBuJiMizqmcAA4AHav0X079lD4Y6bYR2kXw/wDBzQw/cWTSYJSuR0BZScVT1r9kP4eal4nsNWi8H+FbS4020uLWHydGtxs80IN4IXIKhOMeppppCaPhv4J/HD4Mf8Ke8IXXjr48+N4LGKD/AEWwhvpdLshIrMvkkw4eSUn5iGc5Oepr0Xwho2ifFCW/vvhvoNhYaSH2pqvjHxhf2UutOR8zxRIzybBnG5wMmvoDwz/wT4+E2l+BdM0LU/BXh/Xk0wEia8slYyOXL7yOm7Lda15P2HfhHO6tJ4A8PSMvQtASR9Mmpb1uPoeAaf8AsbN48nMeu+KPh5pMBkR7a2sb+51oOynmTNzIgVwcYIU4P4V9pW4Kxgc/KMc9a8wsv2KPhPpd7Bc2/gPw/DPbuJY3WAgowIII59QD+Feoou0YGcCnJ3B73FC7emeaKKKkAooooAKKKKACiiigQfhR+FFFAwwPQUUUUAFFFFABRRRQAUUUUABGRjJFABGeSQaKKACiiigAooooAKKKKACiiigAooooAKKKKAP/2Q=='
    
    @api.model
    def _get_default_musculo_esqueletico_cadera_2(self):
        return b'/9j/4AAQSkZJRgABAQEAYABgAAD/2wBDAAIBAQIBAQICAgICAgICAwUDAwMDAwYEBAMFBwYHBwcGBwcICQsJCAgKCAcHCg0KCgsMDAwMBwkODw0MDgsMDAz/2wBDAQICAgMDAwYDAwYMCAcIDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAz/wAARCABMAGoDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD9/KPTk8UUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRUZOOtAElFR/QE/pRn6ihMSZJRWNrfjfSvDms6Zp19fWtrfazM0FlBJIA9y4UsVUHqQoJ/CtMyoOroPxoGTUVm+IPElh4V0W51LULu3tLCziM000jhVRADk/p/Sud+BXxy0b9oT4aaZ4t8Ppff2Pq7yLbPdW7Qu6o7rv2nkKdhIJ65FAHaUUCigAooooAKKKKAEL4z0JrzD4l/tL2fgnxynhbSvD3iLxb4haBbiW30q18yKyV2KoZ5SQkYYq2Cf7pr01upz3r538efsQ+J/iB40l8QSfGHxbo+pSW7WnmaTY21qZICxZYpCF/eKpJwTzyfWiw4vU5nx/wDt2eP08TQaRpHw2k8OBZZI7vUfEErTRwrHjdIkNvudkBP3jgYI7nFc/wCJf2jPi54sutDsPDPjX4K3uvi7ivW0+3vpLae4tgSHUxz7SQQe2Dn8qu6b/wAEkrfRfFt3rem/Fn4g6BqOoqVu59GlS0ku+MZcndn14Ayea8u+Lv8AwRtnv/HVzeWd3d+LUn0a7lOrXot49WXUFTNsi3BdWAZ+pAxg5JFVoQ79jrwvxa/ag/awm8ZabqXhDwN4d+H4m0CCS8uU1AvdYK3NzCqFQcJJsG84yp+tZHjTwdp95r2oaZ4e+Jvx4+JOu2Eqx3o8K2mntY20rHlGmNq0anqcbzgcE5FW/C3/AAQk8E3Hw807Ttc8W+N5btoFlu9uoFW+0un7071b5huJwORgDk1698Ov+CeM3wg8E6V4d8K/FXx7oejaTEIo7eD7ORJj+JiUyWz3JJoTsi4+Zwtr+zZ8WfG2inQprS4tNDsdk0cvinXLe6k1JgwYB0s4V2gYHBK5x1r6s+F/hKXwD8PdJ0ieSOe4soAs8sa7I5JGO5yoPRSxbHXivPND/ZR1aweY3/xW+ImpJI2Qpu44Qg9PlTn8a73wN8L4vA+mxWyaz4h1QRXDXHm6hfG4kfchXYTgZQZ3BfXmpsI6hfujrRQOOAMAUUAFFFFABRRRQAm0ZJyeaXHpxiiigAwPek2DIPpS0UAG0UAYoooAMAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAf/9k='
    
    @api.model
    def _get_default_musculo_esqueletico_cadera_3(self):
        return b'/9j/4AAQSkZJRgABAQEAYABgAAD/2wBDAAIBAQIBAQICAgICAgICAwUDAwMDAwYEBAMFBwYHBwcGBwcICQsJCAgKCAcHCg0KCgsMDAwMBwkODw0MDgsMDAz/2wBDAQICAgMDAwYDAwYMCAcIDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAz/wAARCABHAGcDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD9/CARggEUAYoooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACikY8dcU0u2QOefbpSbAfRVK/1220ywkuri4iit4cl3LAKuOv5V4341/4KK/CT4fa3bafqniqOG4ubt7FdtrK+JVXcwOFzjBGD0NWot62Jcktz3Giuei+J2jTeKNM0VL5H1LWbF9StIgpzLbqVBfOMAfOvU5Oa3t7ZPXH6VFyh9FMLN6k/hVHw94osvE63LWNwlylpMbeUrnCyAAlfqARTA0aKKKACiiigAooooARunPSvi/9qH47+Kb39qnw5bWfg/4v3ngbw+L2y1yLSbU29vfy9I5kYHMqA4IIK9q+0aTaPQcU07CZ+W3iv4yXvh9vEUfin4A/Gez0rU7wyaNHpcsniCxtwN2ZpLZ2XZKwCllYspPHrnyv4qftPrd6Vp82vfBi+8XQ3hkMFn4l8E/8I9fnC5KQSWx3MQBnByMfSv2dKDHAJNc94o+G2l+MPFHh/V72N5Lzw1PLcWRBAVWkjMbZBBJ+Vj0xzVymuxKh713qflr+xD+0/o+sRXfxA/4RP4u+HrMWC6LoumnW4JpdBgictdQ7rjDIjShCBk8IK9k8Uf8ABUD4Y+Frm3WXxR8Vp9cvEP8AxL4tWsWWBA4Xc0gOxTznHXGa+4fBnwj8P+CPDNvpFpp1tJaW5dgZ4lkdy7l2LEjkkn+VWj8L/DJBB8O6GQxyc2ERyfX7vWouNJ3ufB/gD47+Kvjlq13ceFfFni8+FWDC7PiLxPp9mGODuhhdAWIA6txgV9S/sL/DNvhd8ILq2N7pd1FqWq3F9Elhe/bYbZWCL5Ym6yHKklj/AHvTFdXq/wCyz8N9e1CS7vPA3hee5lzukbTogWz16DvXTeCfAOifDbQU0vw/pVjo2nRsXW2tIRFEpPUhRxk0210BJmvRRRUlBRRRQAUUUUAFFFFAB14IyKCoOcgHNFFAABjpRRRQAUUUUAFFFFABRRRQAH8qKKKACiiigAooooAKKKKACiiigAooooAKKKKAP//Z'
    
    @api.model
    def _get_default_musculo_esqueletico_cadera_4(self):
        return b'/9j/4AAQSkZJRgABAQEAYABgAAD/2wBDAAIBAQIBAQICAgICAgICAwUDAwMDAwYEBAMFBwYHBwcGBwcICQsJCAgKCAcHCg0KCgsMDAwMBwkODw0MDgsMDAz/2wBDAQICAgMDAwYDAwYMCAcIDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAz/wAARCABHAGgDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD9+mTcwOSKdRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFIXA45o3ckYJxTM7skAkZouA/ePejePeua8cfFzwv8NjGuv69pmkvMwRFuJ1RmJBIAHXsan8F/Ejw/8RbWSfQdY0/VoonMbm2mWQow6ggdKSYG75gzil3j0NcX8I/jHa/GB/FAs9P1CyTwxrtzoUjXSBRdPBtDSR4JJQs2ATg8HiuxyOgzn9apq24XH7x70oOeRURcA4Oc/rTkkAHcikA+igHIB9aKACiiigAooooAOB6DNfEnxw/a3+H1trnjePxT8Z/EGkX3hzVb3T08P6Swtpo5I22xAYBLn7p5Izmvts8157r/AOyR8KvFeuXuqar8M/h/qWp6lMbm7u7vw9Zzz3UpxmR3aMlm4HzHJpxS6iaZ8G+EP24Pg3onwsj8XDxLp994h3rYz2vibR/7V1/ULwvtaOQniNGx8vlcAHkV0ev/ALT0Wj+Fo/FHjv8AZ18ReEY7RWkvfEPha+ige1izgTGJNrk4K8OCRmvsL/hiX4Nbw/8AwqT4ZbhMLnP/AAi9jkSjpJ/qvvD1612Wt/DLw74n0W40zU9A0TUdNuk8ua1ubKKWCZP7rIylSvTggjimmr3JtLufnd+yV8W/BXiX9naXxJqPjv4z6FZy6vqFy2ox3BW0to5bqQxTStt+Y7NpYnPOa3vAn/BSbRX8QXGn+Cf2i/BfjXzI2SCz8W6dLbNG64GTcQA7+TnlR1r7csf2cfh9pfhCTw/a+BPBltoMylH02LRbZLN1PYxBNhHsR3rmtG/YL+B3hu9W5074MfCexuFyRLb+EdPicE9eVhB54/KnKd3cagkrI8Y8Lf8ABQDxn4z0caZa6J4DfxMqyvNPb6+09nbxxj5pNvlh2IPIGK9R/Yr8b+OvGXhzXF8dz2M97a3ET2xiULII5Y/MAbHy7drKVAORyDXf6P8As++A/D161zp/grwlY3DqyNLb6RbxOwb7wJVASD3HQ10WleHLDQzIbKys7PzQofyIVj37V2rnaBnC8DPQAYxWaeg0Xh0FFA449KKYwooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKADPsaKKKACiiigAooooAKKKKACiiigAooooAKKKKAP/9k='
    
    @api.model
    def _get_default_musculo_esqueletico_muslo_1(self):
        return b'/9j/4AAQSkZJRgABAQEAYABgAAD/2wBDAAIBAQIBAQICAgICAgICAwUDAwMDAwYEBAMFBwYHBwcGBwcICQsJCAgKCAcHCg0KCgsMDAwMBwkODw0MDgsMDAz/2wBDAQICAgMDAwYDAwYMCAcIDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAz/wAARCABGAGYDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD9/KQIASQOTS0UAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABnHWjcPUU2TgA+hpjHbjJAzxycUXAkZgBkcmk80ZHIIxmvEf2if26vh/8AAm01vTb/AMS2lt4lstPkngtTbSzDzNhMedo24JxwWH4V8e/D7/gob4w8G3/hn+1PH+veI7vxhYt5sC+HreS2tb0DzlZDuRlheDOBzgoc00iXI/TDzODnHHXHOKUPzg4Ga+QvCsvxv/aN17whDfaxqvhfwv8AaYNbvb6006C0a9tk+cWufMkbMhKggAfLnmvriJBDGFG47QBk8k8DrQ1YdybcPUUZqINkE44p6HgDBH1pDTHUUUUAFFFFABRRRQBR8T63B4b8PXuoXMqQwWULzu752qFUnJxzjivzf1L9uDwJ8UNG0yz13TvjD4h8UaossV1qH2q40XTtKYuy5gdWRGCnlTtJxgk88fpayhxggEGo/sUXlqnlpsXou0YFNNdQSPya8N/Ei01Kxls/C/w51/TdRjfyJNS1xbWcXR+bM0t1MsktyGOGJAAGcdqzvh98Wbj4MfE/wFrHin4ew+I9Qm1iW/kvNEvIpEXFtNB5PkFEVcrITtUkYU5x0r9eFgRE2hQF54AwOao6p4T07WrvT7i6tY5ZtKn+1Wr5KmGXYybhjr8rMOcjmi+pPL1PzJT9rDwlp3xy1PUr/S/jz4N8IDTornSrLQZLi6t7S6SZleJIYyVQOrK+3G0Y49K7Uft/ahomn3N/4L8ZfE7VQz4TTPF/gOeVgcZ4liVXVTwMlTzmv0QMYPqKXYPei+t7Dld7H5rWH7XPxO/aT+Lvwqs77xJrPhjSbnxbAdS03SfDN5aCW2iG/wD0iedQ3lvJtTaFA5J6V+lCdiQCT6UpQHrnApQuDnmnKVwWwUUUVIwooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACjnviiigAooooAKKKKACiiigAooooAKKKKACiiigD//2Q=='
    
    @api.model
    def _get_default_musculo_esqueletico_muslo_2(self):
        return b'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'
    
    @api.model
    def _get_default_musculo_esqueletico_muslo_3(self):
        return b'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'
    
    @api.model
    def _get_default_musculo_esqueletico_muslo_4(self):
        return b'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'
    
    @api.model
    def _get_default_musculo_esqueletico_abdomen_lateral_1(self):
        return b'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'
    
    @api.model
    def _get_default_musculo_esqueletico_abdomen_lateral_2(self):
        return b'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'
    
    @api.model
    def _get_default_musculo_esqueletico_abdomen_lateral_3(self):
        return b'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'
    
    @api.model
    def _get_default_musculo_esqueletico_abdomen_lateral_4(self):
        return b'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'
    
    @api.model
    def _get_default_musculo_esqueletico_abducacion_0_180_1(self):
        return b'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'
    
    @api.model
    def _get_default_musculo_esqueletico_abducacion_0_180_2(self):
        return b'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'
    
    @api.model
    def _get_default_musculo_esqueletico_abducacion_0_180_3(self):
        return b'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'
    
    @api.model
    def _get_default_musculo_esqueletico_abducacion_0_60_1(self):
        return b'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'
    
    @api.model
    def _get_default_musculo_esqueletico_abducacion_0_60_2(self):
        return b'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'
    
    @api.model
    def _get_default_musculo_esqueletico_abducacion_0_60_3(self):
        return b'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'
    
    @api.model
    def _get_default_musculo_esqueletico_rotacion_0_90_1(self):
        return b'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'
    
    @api.model
    def _get_default_musculo_esqueletico_rotacion_0_90_2(self):
        return b'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'
    
    @api.model
    def _get_default_musculo_esqueletico_rotacion_0_90_3(self):
        return b'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'
    
    @api.model
    def _get_default_musculo_esqueletico_rotacion_interna_1(self):
        return b'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'
    
    @api.model
    def _get_default_musculo_esqueletico_rotacion_interna_2(self):
        return b'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'
    
    @api.model
    def _get_default_musculo_esqueletico_rotacion_interna_3(self):
        return b'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'
    
    musculo_esqueletico_abdomen_1 = fields.Binary(string='''Abdomen (excelente)''', default=lambda self: self._get_default_musculo_esqueletico_abdomen_1())
    musculo_esqueletico_abdomen_2 = fields.Binary(string='''Abdomen (promedio)''', default=lambda self: self._get_default_musculo_esqueletico_abdomen_2())
    musculo_esqueletico_abdomen_3 = fields.Binary(string='''Abdomen (regular)''', default=lambda self: self._get_default_musculo_esqueletico_abdomen_3())
    musculo_esqueletico_abdomen_4 = fields.Binary(string='''Abdomen (pobre)''', default=lambda self: self._get_default_musculo_esqueletico_abdomen_4())
    musculo_esqueletico_abdomen_lateral_1 = fields.Binary(string='''Abdomen lateral (excelente)''', default=lambda self: self._get_default_musculo_esqueletico_abdomen_lateral_1())
    musculo_esqueletico_abdomen_lateral_2 = fields.Binary(string='''Abdomen lateral (promedio)''', default=lambda self: self._get_default_musculo_esqueletico_abdomen_lateral_2())
    musculo_esqueletico_abdomen_lateral_3 = fields.Binary(string='''Abdomen lateral (regular)''', default=lambda self: self._get_default_musculo_esqueletico_abdomen_lateral_3())
    musculo_esqueletico_abdomen_lateral_4 = fields.Binary(string='''Abdomen lateral (pobre)''', default=lambda self: self._get_default_musculo_esqueletico_abdomen_lateral_4())
    musculo_esqueletico_abdomen_lateral_observaciones = fields.Text(string='''Abdomen (observaciones)''')
    musculo_esqueletico_abdomen_lateral_puntos = fields.Selection(string='''Abdomen (puntuación)''',selection=[("1","1"),("2","2"),("3","3"),("4","4")], default='''1''')
    musculo_esqueletico_abdomen_observaciones = fields.Text(string='''Flexibilidad (observaciones)''')
    musculo_esqueletico_abdomen_puntos = fields.Selection(string='''Flexibilidad (puntuación)''',selection=[("1","1"),("2","2"),("3","3"),("4","4")], default='''1''')
    musculo_esqueletico_abducacion_0_180_1 = fields.Binary(string='''Abducación 0° - 180° del hombro (óptimo)''', default=lambda self: self._get_default_musculo_esqueletico_abducacion_0_180_1())
    musculo_esqueletico_abducacion_0_180_2 = fields.Binary(string='''Abducación 0° - 180° del hombro (limitado)''', default=lambda self: self._get_default_musculo_esqueletico_abducacion_0_180_2())
    musculo_esqueletico_abducacion_0_180_3 = fields.Binary(string='''Abducación 0° - 180° del hombro (muy limitado)''', default=lambda self: self._get_default_musculo_esqueletico_abducacion_0_180_3())
    musculo_esqueletico_abducacion_0_180_dolor = fields.Boolean(string='''Abducación 0° - 180° del hombro (dolor contra resistencia)''')
    musculo_esqueletico_abducacion_0_180_puntos = fields.Selection(string='''Abducación 0° - 180° del hombro (puntuación)''',selection=[("1","1"),("2","2"),("3","3")], default='''1''')
    musculo_esqueletico_abducacion_0_60_1 = fields.Binary(string='''Abducación 0° - 60° del hombro (óptimo)''', default=lambda self: self._get_default_musculo_esqueletico_abducacion_0_60_1())
    musculo_esqueletico_abducacion_0_60_2 = fields.Binary(string='''Abducación 0° - 60° del hombro (limitado)''', default=lambda self: self._get_default_musculo_esqueletico_abducacion_0_60_2())
    musculo_esqueletico_abducacion_0_60_3 = fields.Binary(string='''Abducación 0° - 60° del hombro (muy limitado)''', default=lambda self: self._get_default_musculo_esqueletico_abducacion_0_60_3())
    musculo_esqueletico_abducacion_0_60_dolor = fields.Boolean(string='''Abducación 0° - 60° del hombro (dolor contra resistencia)''')
    musculo_esqueletico_abducacion_0_60_puntos = fields.Selection(string='''Abducación 0° - 60° del hombro (puntuación)''',selection=[("1","1"),("2","2"),("3","3")], default='''1''')
    musculo_esqueletico_cadera_1 = fields.Binary(string='''Cadera (excelente)''', default=lambda self: self._get_default_musculo_esqueletico_cadera_1())
    musculo_esqueletico_cadera_2 = fields.Binary(string='''Cadera (promedio)''', default=lambda self: self._get_default_musculo_esqueletico_cadera_2())
    musculo_esqueletico_cadera_3 = fields.Binary(string='''Cadera (regular)''', default=lambda self: self._get_default_musculo_esqueletico_cadera_3())
    musculo_esqueletico_cadera_4 = fields.Binary(string='''Cadera (pobre)''', default=lambda self: self._get_default_musculo_esqueletico_cadera_4())
    musculo_esqueletico_cadera_observaciones = fields.Text(string='''Cadera (observaciones)''')
    musculo_esqueletico_cadera_puntos = fields.Selection(string='''Cadera (puntuación)''',selection=[("1","1"),("2","2"),("3","3"),("4","4")], default='''1''')
    musculo_esqueletico_cervical_extension = fields.Boolean(string='''Extensión cervical normal''')
    musculo_esqueletico_cervical_flexion = fields.Boolean(string='''Flexión cervical normal''')
    musculo_esqueletico_cervical_lateralidad = fields.Boolean(string='''Lateralidad cervical normal''')
    musculo_esqueletico_cervical_rotacion = fields.Boolean(string='''Rotación cervical normal''')
    musculo_esqueletico_codo_extension = fields.Boolean(string='''Extensión codo normal''')
    musculo_esqueletico_codo_flexion = fields.Boolean(string='''Flexión codo normal''')
    musculo_esqueletico_codo_pronosupinacion = fields.Boolean(string='''Pronosupinación codo normal''')
    musculo_esqueletico_codo_supinacion = fields.Boolean(string='''Supinación codo normal''')
    musculo_esqueletico_epicondilitis = fields.Boolean(string='''Epicondilitis''')
    musculo_esqueletico_epitrocleitis = fields.Boolean(string='''Epitrocleitis''')
    musculo_esqueletico_flexibilidad_fuerza_total = fields.Integer(string='''Flexibilidad / fuerza (puntuación total)''', compute='''_compute_musculo_esqueletico_flexibilidad_fuerza_total''', store=True, readonly=True)
    musculo_esqueletico_hombro_abduccion = fields.Boolean(string='''Abducción hombro normal''')
    musculo_esqueletico_hombro_extension = fields.Boolean(string='''Extensión hombro normal''')
    musculo_esqueletico_hombro_flexion = fields.Boolean(string='''Flexión hombro normal''')
    musculo_esqueletico_hombro_rotacion_externa = fields.Boolean(string='''Rotación externa hombro normal''')
    musculo_esqueletico_hombro_rotacion_interna = fields.Boolean(string='''Rotación interna hombro normal''')
    musculo_esqueletico_maniobra_finkelstein = fields.Boolean(string='''Maniobra Finkelstein''')
    musculo_esqueletico_maniobra_phalen = fields.Boolean(string='''Maniobra Phalen''')
    musculo_esqueletico_muneca_extension = fields.Boolean(string='''Extensión muñeca normal''')
    musculo_esqueletico_muneca_flexion = fields.Boolean(string='''Flexión muñeca normal''')
    musculo_esqueletico_muslo_1 = fields.Binary(string='''Muslo (excelente)''', default=lambda self: self._get_default_musculo_esqueletico_muslo_1())
    musculo_esqueletico_muslo_2 = fields.Binary(string='''Muslo (promedio)''', default=lambda self: self._get_default_musculo_esqueletico_muslo_2())
    musculo_esqueletico_muslo_3 = fields.Binary(string='''Muslo (regular)''', default=lambda self: self._get_default_musculo_esqueletico_muslo_3())
    musculo_esqueletico_muslo_4 = fields.Binary(string='''Muslo (pobre)''', default=lambda self: self._get_default_musculo_esqueletico_muslo_4())
    musculo_esqueletico_muslo_observaciones = fields.Text(string='''Muslo (observaciones)''')
    musculo_esqueletico_muslo_puntos = fields.Selection(string='''Muslo (puntuación)''',selection=[("1","1"),("2","2"),("3","3"),("4","4")], default='''1''')
    musculo_esqueletico_palm_up_test = fields.Boolean(string='''Palm-up test''')
    musculo_esqueletico_rangos_articulares_total = fields.Integer(string='''Rangos articulares (puntuación total)''', compute='''_compute_musculo_esqueletico_rangos_articulares_total''', store=True, readonly=True)
    musculo_esqueletico_rotacion_0_90_1 = fields.Binary(string='''Rotación externa 0° - 90° del hombro (óptimo)''', default=lambda self: self._get_default_musculo_esqueletico_rotacion_0_90_1())
    musculo_esqueletico_rotacion_0_90_2 = fields.Binary(string='''Rotación externa 0° - 90° del hombro (limitado)''', default=lambda self: self._get_default_musculo_esqueletico_rotacion_0_90_2())
    musculo_esqueletico_rotacion_0_90_3 = fields.Binary(string='''Rotación externa 0° - 90° del hombro (muy limitado)''', default=lambda self: self._get_default_musculo_esqueletico_rotacion_0_90_3())
    musculo_esqueletico_rotacion_0_90_dolor = fields.Boolean(string='''Rotación externa 0° - 90° del hombro (dolor contra resistencia)''')
    musculo_esqueletico_rotacion_0_90_puntos = fields.Selection(string='''Rotación externa 0° - 90° del hombro (puntuación)''',selection=[("1","1"),("2","2"),("3","3")], default='''1''')
    musculo_esqueletico_rotacion_interna_1 = fields.Binary(string='''Rotación interna del hombro (óptimo)''', default=lambda self: self._get_default_musculo_esqueletico_rotacion_interna_1())
    musculo_esqueletico_rotacion_interna_2 = fields.Binary(string='''Rotación interna del hombro (limitado)''', default=lambda self: self._get_default_musculo_esqueletico_rotacion_interna_2())
    musculo_esqueletico_rotacion_interna_3 = fields.Binary(string='''Rotación interna del hombro (muy limitado)''', default=lambda self: self._get_default_musculo_esqueletico_rotacion_interna_3())
    musculo_esqueletico_rotacion_interna_dolor = fields.Boolean(string='''Rotación interna del hombro (dolor contra resistencia)''')
    musculo_esqueletico_rotacion_interna_puntos = fields.Selection(string='''Rotación interna del hombro (puntuación)''',selection=[("1","1"),("2","2"),("3","3")], default='''1''')
    musculo_esqueletico_test_gerber = fields.Boolean(string='''Test de Gerber''')
    musculo_esqueletico_test_jobe = fields.Boolean(string='''Test de Jobe''')
    musculo_esqueletico_test_patte = fields.Boolean(string='''Test de Patte''')
    
    @api.depends('musculo_esqueletico_abdomen_puntos','musculo_esqueletico_cadera_puntos','musculo_esqueletico_muslo_puntos','musculo_esqueletico_abdomen_lateral_puntos')
    def _compute_musculo_esqueletico_flexibilidad_fuerza_total(self):
        for record in self :
            record.musculo_esqueletico_flexibilidad_fuerza_total = int(record.musculo_esqueletico_abdomen_puntos or 1) + int(record.musculo_esqueletico_cadera_puntos or 1) + int(record.musculo_esqueletico_muslo_puntos or 1) + int(record.musculo_esqueletico_abdomen_lateral_puntos or 1)
    
    @api.depends('musculo_esqueletico_abducacion_0_180_puntos','musculo_esqueletico_abducacion_0_60_puntos','musculo_esqueletico_rotacion_0_90_puntos','musculo_esqueletico_rotacion_interna_puntos')
    def _compute_musculo_esqueletico_rangos_articulares_total(self):
        for record in self :
            record.musculo_esqueletico_rangos_articulares_total = int(record.musculo_esqueletico_abducacion_0_180_puntos or 1) + int(record.musculo_esqueletico_abducacion_0_60_puntos or 1) + int(record.musculo_esqueletico_rotacion_0_90_puntos or 1) + int(record.musculo_esqueletico_rotacion_interna_puntos or 1)
    
    oftalmologia_agudeza_agujero_con_correccion_derecho = fields.Integer(string='''Agudeza visual con el agujero estenopeico con corrección en el ojo derecho''')
    oftalmologia_agudeza_agujero_con_correccion_izquierdo = fields.Integer(string='''Agudeza visual con el agujero estenopeico con corrección en el ojo izquierdo''')
    oftalmologia_agudeza_agujero_sin_correccion_derecho = fields.Integer(string='''Agudeza visual con el agujero estenopeico sin corrección en el ojo derecho''')
    oftalmologia_agudeza_agujero_sin_correccion_izquierdo = fields.Integer(string='''Agudeza visual con el agujero estenopeico sin corrección en el ojo izquierdo''')
    oftalmologia_agudeza_cerca_con_correccion_derecho = fields.Integer(string='''Agudeza visual de cerca con corrección en el ojo derecho''')
    oftalmologia_agudeza_cerca_con_correccion_izquierdo = fields.Integer(string='''Agudeza visual de cerca con corrección en el ojo izquierdo''')
    oftalmologia_agudeza_cerca_sin_correccion_derecho = fields.Integer(string='''Agudeza visual de cerca sin corrección en el ojo derecho''')
    oftalmologia_agudeza_cerca_sin_correccion_izquierdo = fields.Integer(string='''Agudeza visual de cerca sin corrección en el ojo izquierdo''')
    oftalmologia_agudeza_lejos_con_correccion_derecho = fields.Integer(string='''Agudeza visual de lejos con corrección en el ojo derecho''')
    oftalmologia_agudeza_lejos_con_correccion_izquierdo = fields.Integer(string='''Agudeza visual de lejos con corrección en el ojo izquierdo''')
    oftalmologia_agudeza_lejos_sin_correccion_derecho = fields.Integer(string='''Agudeza visual de lejos sin corrección en el ojo derecho''')
    oftalmologia_agudeza_lejos_sin_correccion_izquierdo = fields.Integer(string='''Agudeza visual de lejos sin corrección en el ojo izquierdo''')
    oftalmologia_ambliopia = fields.Boolean(string='''Ambliopía''')
    oftalmologia_antecedentes_otros = fields.Text(string='''Otros''')
    oftalmologia_blefaritis_derecho = fields.Boolean(string='''Blefaritis en el ojo derecho''')
    oftalmologia_blefaritis_izquierdo = fields.Boolean(string='''Blefaritis en el ojo izquierdo''')
    oftalmologia_campimetria_derecho = fields.Char(string='''Campimetría del ojo derecho''')
    oftalmologia_campimetria_izquierdo = fields.Char(string='''Campimetría del ojo izquierdo''')
    oftalmologia_chalazion_derecho = fields.Boolean(string='''Chalazion en el ojo derecho''')
    oftalmologia_chalazion_izquierdo = fields.Boolean(string='''Chalazion en el ojo izquierdo''')
    oftalmologia_colores_derecho = fields.Char(string='''Visión de colores en el ojo derecho''')
    oftalmologia_colores_izquierdo = fields.Char(string='''Visión de colores en el ojo izquierdo''')
    oftalmologia_conjuntivitis_derecho = fields.Boolean(string='''Conjuntivitis en el ojo derecho''')
    oftalmologia_conjuntivitis_izquierdo = fields.Boolean(string='''Conjuntivitis en el ojo izquierdo''')
    oftalmologia_corrector_ocular_presente = fields.Boolean(string='''Presencia de corrector ocular''')
    oftalmologia_corrector_ocular_utiliza = fields.Boolean(string='''Uso de corrector ocular''')
    oftalmologia_dermatocalasia_derecho = fields.Boolean(string='''Dermatocalasia en el ojo derecho''')
    oftalmologia_dermatocalasia_izquierdo = fields.Boolean(string='''Dermatocalasia en el ojo izquierdo''')
    oftalmologia_diabetes = fields.Boolean(string='''Diabetes''')
    oftalmologia_estereopsis = fields.Char(string='''Estereopsis (oftalmología)''')
    oftalmologia_estrabismo_derecho = fields.Boolean(string='''Estrabismo en el ojo derecho''')
    oftalmologia_estrabismo_izquierdo = fields.Boolean(string='''Estrabismo en el ojo izquierdo''')
    oftalmologia_examen_externo_derecho = fields.Char(string='''Examen externo en el ojo derecho''')
    oftalmologia_examen_externo_izquierdo = fields.Char(string='''Examen externo en el ojo izquierdo''')
    oftalmologia_fondo_ojo = fields.Char(string='''Fondo de ojos''')
    oftalmologia_glaucoma = fields.Boolean(string='''Glaucoma''')
    oftalmologia_hipertension_arterial = fields.Boolean(string='''HTA''')
    oftalmologia_hipertension_ocular = fields.Boolean(string='''Hipertensión ocular''')
    oftalmologia_otros_anexos_derecho = fields.Boolean(string='''Otros anexos en el ojo derecho''')
    oftalmologia_otros_anexos_izquierdo = fields.Boolean(string='''Otros anexos en el ojo izquierdo''')
    oftalmologia_pterigium_derecho = fields.Boolean(string='''Pterigium en el ojo derecho''')
    oftalmologia_pterigium_izquierdo = fields.Boolean(string='''Pterigium en el ojo izquierdo''')
    oftalmologia_ptosis_derecho = fields.Boolean(string='''Ptosis en el ojo derecho''')
    oftalmologia_ptosis_izquierdo = fields.Boolean(string='''Ptosis en el ojo izquierdo''')
    oftalmologia_radiaciones = fields.Boolean(string='''Radiaciones''')
    oftalmologia_reflejo_pupila_derecho = fields.Char(string='''Reflejos pupilares en el ojo derecho''')
    oftalmologia_reflejo_pupila_izquierdo = fields.Char(string='''Reflejos pupilares en el ojo izquierdo''')
    oftalmologia_refraccion_cerca_derecho_cilindrico = fields.Char(string='''Refracción de cerca en el ojo derecho - cilindrico''')
    oftalmologia_refraccion_cerca_derecho_eje = fields.Char(string='''Refracción de cerca en el ojo derecho - eje''')
    oftalmologia_refraccion_cerca_derecho_esfera = fields.Char(string='''Refracción de cerca en el ojo derecho - esfera''')
    oftalmologia_refraccion_cerca_derecho_pupila = fields.Char(string='''Refracción de cerca en el ojo derecho - distancia entre pupilas''')
    oftalmologia_refraccion_cerca_izquierdo_cilindrico = fields.Char(string='''Refracción de cerca en el ojo izquierdo - cilindrico''')
    oftalmologia_refraccion_cerca_izquierdo_eje = fields.Char(string='''Refracción de cerca en el ojo izquierdo - eje''')
    oftalmologia_refraccion_cerca_izquierdo_esfera = fields.Char(string='''Refracción de cerca en el ojo izquierdo - esfera''')
    oftalmologia_refraccion_cerca_izquierdo_pupila = fields.Char(string='''Refracción de cerca en el ojo izquierdo - distancia entre pupilas''')
    oftalmologia_refraccion_lejos_derecho_cilindrico = fields.Char(string='''Refracción de lejos en el ojo derecho - cilindrico''')
    oftalmologia_refraccion_lejos_derecho_eje = fields.Char(string='''Refracción de lejos en el ojo derecho - eje''')
    oftalmologia_refraccion_lejos_derecho_esfera = fields.Char(string='''Refracción de lejos en el ojo derecho - esfera''')
    oftalmologia_refraccion_lejos_derecho_pupila = fields.Char(string='''Refracción de lejos en el ojo derecho - distancia entre pupilas''')
    oftalmologia_refraccion_lejos_izquierdo_cilindrico = fields.Char(string='''Refracción de lejos en el ojo izquierdo - cilindrico''')
    oftalmologia_refraccion_lejos_izquierdo_eje = fields.Char(string='''Refracción de lejos en el ojo izquierdo - eje''')
    oftalmologia_refraccion_lejos_izquierdo_esfera = fields.Char(string='''Refracción de lejos en el ojo izquierdo - esfera''')
    oftalmologia_refraccion_lejos_izquierdo_pupila = fields.Char(string='''Refracción de lejos en el ojo izquierdo - distancia entre pupilas''')
    oftalmologia_soldadura = fields.Boolean(string='''Soldadura''')
    oftalmologia_sustancias_quimicas = fields.Boolean(string='''Sustancias químicas''')
    oftalmologia_tonometria_derecho = fields.Char(string='''Tonometría del ojo derecho''')
    oftalmologia_tonometria_izquierdo = fields.Char(string='''Tonometría del ojo izquierdo''')
    oftalmologia_traumatismo = fields.Boolean(string='''Traumatismo''')
    oftalmologia_vision_nocturna = fields.Char(string='''Visión nocturna''')
    oftalmologia_vision_profundidad = fields.Char(string='''Visión de profundidad''')
    
    psicologico_afectividad_observaciones = fields.Char(string='''Afectividad (informe psicológico)''')
    psicologico_afectividad_rasgos = fields.Char(string='''Afectividad (rasgos)''')
    psicologico_afectividad_sin_datos_relevantes = fields.Char(string='''Afectividad (sin datos relevantes)''')
    psicologico_afectividad_transtorno = fields.Char(string='''Afectividad (transtorno)''')
    psicologico_area_personalidad_rasgos = fields.Char(string='''Área de la personalidad (rasgos)''')
    psicologico_area_personalidad_sin_datos_relevantes = fields.Char(string='''Área de la personalidad (sin datos relevantes)''')
    psicologico_area_personalidad_transtorno = fields.Char(string='''Área de la personalidad (transtorno)''')
    psicologico_bateria_conductores = fields.Boolean(string='''Batería de conductores''')
    psicologico_bateria_dna_luria = fields.Boolean(string='''Batería DNA de Luria (diagnóstico neuropsicológico de adultos)''')
    psicologico_clima_laboral = fields.Boolean(string='''Clima laboral (técnica psicológica)''')
    psicologico_conclusiones = fields.Char(string='''Conclusiones (informe psicológico)''')
    psicologico_conducta_discurso_articulacion = fields.Selection(string='''Articulacion del discurso (informe psicológico)''',selection=[("con_dificultad","Con dificultad"),("sin_dificultad","Sin dificultad")])
    psicologico_conducta_discurso_ritmo = fields.Selection(string='''Ritmo del discurso (informe psicológico)''',selection=[("lento","Lento"),("rapido","Rápido"),("fluido","Fluído")])
    psicologico_conducta_discurso_tono = fields.Selection(string='''Tono del discurso (informe psicológico)''',selection=[("bajo","Bajo"),("moderado","Moderado"),("alto","Alto")])
    psicologico_conducta_orientacion_espacio = fields.Selection(string='''Orientación en el espacio (informe psicológico)''',selection=[("orientado","Orientado"),("desorientado","Desorientado")])
    psicologico_conducta_orientacion_persona = fields.Selection(string='''Orientación en la persona (informe psicológico)''',selection=[("orientado","Orientado"),("desorientado","Desorientado")])
    psicologico_conducta_orientacion_tiempo = fields.Selection(string='''Orientación en el tiempo (informe psicológico)''',selection=[("orientado","Orientado"),("desorientado","Desorientado")])
    psicologico_conducta_postura = fields.Selection(string='''Postura (informe psicológico)''',selection=[("erguida","Erguida"),("encorvada","Encorvada")])
    psicologico_conducta_presentacion = fields.Selection(string='''Presentación (informe psicológico)''',selection=[("adecuado","Adecuado"),("inadecuado","Inadecuado")])
    psicologico_coordinacion_observaciones = fields.Char(string='''Coordinación visomotriz (informe psicológico)''')
    psicologico_diagnostico = fields.Selection(string='''Tipo de diagnóstico (informe psicológico)''',selection=[("diagnostico_medicina_ocupacional","DiagMO"),("otros_diagnosticos","OtrosD")])
    psicologico_emocional = fields.Text(string='''Resultado emocional (informe psicológico)''')
    psicologico_entrevista = fields.Boolean(string='''Entrevista (técnica psicológica)''')
    psicologico_escala_apreciacion_estres = fields.Boolean(string='''Escala de apreciación del estrés (EAE)''')
    psicologico_escala_memoria_wechsler = fields.Boolean(string='''Escala de memoria de Wechsler''')
    psicologico_estres_observaciones = fields.Char(string='''Estrés (informe psicológico)''')
    psicologico_fatiga_laboral = fields.Selection(string='''Fatiga laboral (informe psicológico)''',selection=[("no_presenta","No presenta"),("presenta","Presenta")])
    psicologico_fobia_observaciones = fields.Char(string='''Fobia (informe psicológico)''')
    psicologico_inventario_ansiedad_zung = fields.Boolean(string='''Inventario de ansiedad Zung''')
    psicologico_inventario_depresion_zung = fields.Boolean(string='''Inventario de depresión Zung''')
    psicologico_mbi = fields.Boolean(string='''Inventario de "Burnout" de Maslach (MBI)''')
    psicologico_mips = fields.Boolean(string='''Inventario Millon de estilos de Personalidad (MIPS)''')
    psicologico_motivaciones_psicosociales = fields.Boolean(string='''Escala de motivaciones psicosociales (MPS)''')
    psicologico_motivo_evaluacion = fields.Char(string='''Motivo de la evaluación (informe psicológico)''')
    psicologico_nivel_intelectual_observaciones = fields.Char(string='''Nivel intelectual (informe psicológico)''')
    psicologico_nivel_memoria_observaciones = fields.Char(string='''Nivel de memoria (informe psicológico)''')
    psicologico_observacion = fields.Boolean(string='''Observación (técnica psicológica)''')
    psicologico_otras_tecnicas_instrumentos = fields.Char(string='''Otras técnicas o instrumentos utilizados (informe psicológico)''')
    psicologico_recomendaciones = fields.Text(string='''Recomendaciones (informe psicológico)''')
    psicologico_resultado_diagnostico = fields.Selection(string='''Resultado del diagnóstico (informe psicológico)''',selection=[("apto","Apto"),("apto_con_observaciones","Apto con observaciones"),("no_apto","No apto"),("apto_con_restricciones","Apto con restricciones")])
    psicologico_somnolencia_diurna = fields.Selection(string='''Somnolencia diurna (informe psicológico)''',selection=[("no_presenta","No presenta"),("presenta_alta_probabilidad","Presenta alta probabilidad")])
    psicologico_test_bender = fields.Boolean(string='''Test de Bender''')
    psicologico_test_benton = fields.Boolean(string='''Test de Benton''')
    psicologico_wais = fields.Boolean(string='''Escala Wechsler de Inteligencia para Adultos (WAIS)''')
    
    radiologia_comentario = fields.Text(string='''Comentario (radiología)''')
    
    test_sr_baja_peso_inexplicable = fields.Boolean(string='''Baja de peso inexplicable''')
    test_sr_conclusion = fields.Boolean(string='''Conclusión''')
    test_sr_familiares_amigos_tuberculosis = fields.Boolean(string='''Familiares o amigos con tuberculosis''')
    test_sr_observaciones = fields.Text(string='''Observaciones''')
    test_sr_resultado_bk_esputo_1 = fields.Text(string='''Resultado de Bk de Esputo 1°''')
    test_sr_resultado_radiografia_torax = fields.Text(string='''Resultado de radiografía de tórax''')
    test_sr_sospecha_tuberculosis = fields.Boolean(string='''Sospecha de tuberculosis''')
    test_sr_sudoracion_nocturna_importante = fields.Boolean(string='''Sudoración nocturna importante''')
    test_sr_tos_mas_15_dias = fields.Boolean(string='''Tos por más de 15 días''')
    test_sr_tos_sangre = fields.Boolean(string='''Tos con sangre''')
    test_sr_tuberculosis = fields.Boolean(string='''Tuberculosis''')
    
    tipo_cita = fields.Selection(string='''Tipo''',selection=[("diagnostico","Diagnóstico"),
                                                              ("triaje","Triaje"),
                                                              ("antecedentes_personales","Antecedentes Personales"),
                                                              ("historia_ocupacional","Historia Ocupacional"),
                                                              ("medicina","Medicina general"),
                                                              ("dermatologia","Dermatología"),
                                                              ("grandes_alturas","Anexo N°16 A"),
                                                              ("altura","Certificación de trabajo en altura"),
                                                              ("confinados","Trabajo en espacios confinados"),
                                                              ("electrocardiograma","Electrocardiograma"),
                                                              ("oftalmologia","Oftalmología"),
                                                              ("audiometria","Audiometría"),
                                                              ("psicologia","Psicología"),
                                                              ("odontograma","Odontograma"),
                                                              ("musculo_esqueletico","Músculo Esquelético"),
                                                              ("radiologia","Radiología"),
                                                              ("espirometria","Espirometría"),
                                                              ("tsr","Test de Sintomático Respiratorio"),
                                                              ("laboratorio","Laboratorio"),
                                                              ("consentimiento","Consentimiento"),
                                                              ("interconsultas","Interconsultas"),
                                                              ("encuesta","Encuesta")])
    fecha_cita = fields.Date(string='''Fecha''')
    paciente_id = fields.Many2one(comodel_name='''medical.patient''', string='''Paciente''')
    atencion_inicio = fields.Datetime(string='''Inicio de la atención''')
    atencion_fin = fields.Datetime(string='''Fin de la atención''')
    
    paciente_apellidos_nombres = fields.Char(string='''Apellidos y nombres''', compute='''_compute_paciente_datos''', store=True, readonly=True)
    paciente_cargo = fields.Char(string='''Cargo''', compute='''_compute_paciente_datos''', store=True, readonly=True)
    paciente_dni = fields.Char(string='''DNI''', compute='''_compute_paciente_datos''', store=True, readonly=True)
    paciente_edad = fields.Char(string='''Edad''', compute='''_compute_paciente_datos''', store=True, readonly=True)
    paciente_empresa_id = fields.Many2one(comodel_name='''res.partner''', string='''Empresa''', compute='''_compute_paciente_datos''', store=True, readonly=True)
    paciente_perfil_id = fields.Many2one(comodel_name='''medicina.paciente.perfil''', string='''Perfil''', compute='''_compute_paciente_datos''', store=True, readonly=True)
    paciente_sexo = fields.Selection(string='''Sexo''',selection=[('m', 'Male'),('f', 'Female')], compute='''_compute_paciente_datos''', store=True, readonly=True)
    tipo_examen_salud_ocupacional = fields.Selection(string='''Tipo de Examen de Salud Ocupacional''',selection=[("empo","EMPO"),("emoa","EMOA"),("emor","EMOR")])
    
    @api.depends('paciente_id')
    def _compute_paciente_datos(self):
        for record in self :
            record.paciente_apellidos_nombres = record.paciente_id.patient_id.name
            record.paciente_cargo = record.paciente_id.patient_id.function
            record.paciente_dni = record.paciente_id.patient_id.vat
            record.paciente_edad = record.paciente_id.age
            record.paciente_sexo = record.paciente_id.sex
            record.paciente_empresa_id = record.paciente_id.partner_address_id
            record.paciente_perfil_id = record.paciente_id.perfil_id
    
    auditado = fields.Boolean(string='''Auditado''')
    auditor = fields.Many2one(comodel='''res.partner''', string='''Auditor''')
    responsable = fields.Many2one(comodel='''res.partner''', string='''Responsable''')
    revisado = fields.Boolean(string='''Revisado''')
    medico = fields.Many2one(comodel='''res.partner''', string='''Médico''')
    evaluador = fields.Many2one(comodel='''res.partner''', string='''Evaluador''')
    
    diagnostico_ids = fields.One2many(comodel_name='''medicina.cita.diagnostico''', inverse_name='''cita_id''', string='''Diagnóstico''', domain=[('tipo_diagnostico_oido','=','bilateral')])
    diagnostico_oido_derecho_ids = fields.One2many(comodel_name='''medicina.cita.diagnostico''', inverse_name='''cita_id''', string='''Diagnóstico del oido derecho''', domain=[('tipo_diagnostico_oido','=','derecho')])
    diagnostico_oido_izquierdo_ids = fields.One2many(comodel_name='''medicina.cita.diagnostico''', inverse_name='''cita_id''', string='''Diagnóstico del oido izquierdo''', domain=[('tipo_diagnostico_oido','=','izquierdo')])
    historial_paciente = fields.Many2many(comodel_name='''medicina.cita''', relation='''medicina_cita_medicina_cita_rel''', column1='''cita_id1''', column2='''cita_id2''', string='''Historial del paciente''')
    
    name = fields.Char(string='''Cita''')

class MedicinaCitaDiagnostico(models.Model) :
    _name = 'medicina.cita.diagnostico'
    _description = 'Diagnóstico de la cita'
    
    cita_id = fields.Many2one(comodel_name='''medicina.cita''', string='''Cita origen''', ondelete='''cascade''')
    tipo_diagnostico_oido = fields.Selection(string='''Tipo de diagnóstico (oído)''',selection=[("bilateral","Bilateral"),("derecho","Derecho"),("izquierdo","Izquierdo")], default='''bilateral''')
    codigo_cie_10 = fields.Char(string='''Código CIE-10 del diagnóstico''')
    descripcion = fields.Char(string='''Descripción del diagnóstico''')
    recomendaciones = fields.Char(string='''Recomendaciones del diagnóstico''')
