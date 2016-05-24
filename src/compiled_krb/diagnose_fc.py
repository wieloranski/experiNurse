# diagnose_fc.py

from pyke import contexts, pattern, fc_rule, knowledge_base

pyke_version = '1.1.1'
compiler_version = 1

def collect_diagnosis(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('patient', 'feels', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        diseases = []
        with engine.lookup('choroby', 'symptom_of', context, \
                           rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            diseases.append(context.lookup_data('disease'))
        mark4 = context.mark(True)
        if rule.pattern(0).match_data(context, context,
                tuple(diseases)):
          context.end_save_all_undo()
          engine.assert_('patient', 'suffers_from',
                         (rule.pattern(1).as_data(context),
                          rule.pattern(0).as_data(context),)),
          rule.rule_base.num_fc_rules_triggered += 1
        else: context.end_save_all_undo()
        context.undo_to_mark(mark4)
  finally:
    context.done()

def populate(engine):
  This_rule_base = engine.get_create('diagnose')
  
  fc_rule.fc_rule('collect_diagnosis', This_rule_base, collect_diagnosis,
    (('patient', 'feels',
      (contexts.variable('patient'),
       contexts.variable('symptom'),),
      False),
     ('choroby', 'symptom_of',
      (contexts.variable('symptom'),
       contexts.variable('disease'),),
      True),),
    (contexts.variable('diseases'),
     contexts.variable('patient'),))


Krb_filename = '../knowledge_base/diagnose.krb'
Krb_lineno_map = (
    ((12, 16), (3, 3)),
    ((17, 17), (4, 4)),
    ((18, 21), (6, 6)),
    ((22, 22), (7, 7)),
    ((25, 25), (8, 8)),
    ((27, 29), (10, 10)),
)
