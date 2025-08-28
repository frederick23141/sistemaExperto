#pip install clipspy
import clips

sistemaExperto= clips.Environment()

sistemaExperto.clear()

reglaUno =('(defrule rUno (A)=>(assert(B)))')

sistemaExperto.build(reglaUno)

reglaLluvia = ("(defrule reglaLluvia (lluvia) => (assert(paraguas)))")
reglaSol = ("(defrule reglaSol (sol)=> (assert(bloqueador)))")

sistemaExperto.build(reglaLluvia)
sistemaExperto.build(reglaSol)

#ver reglas  (rules)
for r in sistemaExperto.rules():
  print(r)

reglaArcoiris = ("(defrule reglaArcoiris (lluvia)(sol) => (assert(arcoiris)))")
sistemaExperto.build(reglaArcoiris)  

# (assert (jorge))
sistemaExperto.assert_string('(jorge)')

#ver hechos (facts)
for fact in sistemaExperto.facts():
  print(fact)

elHecho=input("Digite hecho -> ")
sistemaExperto.assert_string(f"({elHecho})")  

#agenda
for ac in sistemaExperto.activations():
  print(ac)

sistemaExperto.run()
for fact in sistemaExperto.facts():
    factString=str(fact)
    if "paraguas" in factString:
      print ("abrir el paraguas que se moja")
    if "bloqueador" in factString:
      print ("protegerse la piel del sol con bloqueador")
    if "arcoiris" in factString:
      print ("Disfrutar de la vista")