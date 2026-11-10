"""Transparent forward-chaining toy expert system. Educational demo, not medical advice."""
RULES=[
 ({"fever","cough"},"respiratory_symptom_pattern","Fever AND cough -> respiratory symptom pattern"),
 ({"respiratory_symptom_pattern","fatigue"},"needs_assessment","Pattern AND fatigue -> needs professional assessment"),
 ({"rash","itching"},"skin_symptom_pattern","Rash AND itching -> skin symptom pattern"),
 ({"skin_symptom_pattern"},"avoid_self_diagnosis","Skin pattern -> avoid self-diagnosis; seek clinician if persistent/severe"),
]
def infer(initial):
 facts=set(initial);log=[];changed=True
 while changed:
  changed=False
  for required,conclusion,explanation in RULES:
   if required<=facts and conclusion not in facts:
    facts.add(conclusion);log.append(explanation);changed=True
 return facts,log
if __name__=="__main__":
 raw=input("Enter facts comma-separated (demo: fever,cough,fatigue): ")
 facts,trace=infer({x.strip().lower() for x in raw.split(",") if x.strip()})
 print("\\nInference trace:")
 for i,s in enumerate(trace,1):print(f"{i}. {s}")
 print("\\nConclusions:",sorted(facts))
 print("Safety: rules are illustrative; not a diagnostic system. Do not use for treatment decisions.")
