(deftemplate entorno
  (slot suelo)
  (slot lluvia)
  (slot estacion)
  (slot temperatura (type FLOAT)))

(deftemplate recomendacion
  (slot cultivo)
  (slot motivo))

(defrule arroz
  (entorno (suelo arcilloso) (lluvia alta) (temperatura ?t&:(>= ?t 25)))
  =>
  (assert (recomendacion (cultivo arroz)
                         (motivo "El arroz requiere suelos arcillosos, alta humedad y temperaturas cálidas."))))

(defrule maiz
  (entorno (suelo franco) (lluvia media) (temperatura ?t&:(and (>= ?t 18) (<= ?t 30))))
  =>
  (assert (recomendacion (cultivo maiz)
                         (motivo "El maíz se adapta a suelos francos con lluvias medias y temperaturas moderadas."))))

(defrule trigo
  (entorno (suelo limoso) (lluvia media) (estacion otoño))
  =>
  (assert (recomendacion (cultivo trigo)
                         (motivo "El trigo crece bien en suelos limosos durante el otoño."))))

(defrule mani
  (entorno (suelo arenoso) (lluvia baja) (temperatura ?t&:(> ?t 20)))
  =>
  (assert (recomendacion (cultivo mani)
                         (motivo "El maní prospera en suelos arenosos con climas cálidos y secos."))))

(defrule papa
  (entorno (suelo franco) (lluvia alta) (estacion verano))
  =>
  (assert (recomendacion (cultivo papa)
                         (motivo "La papa necesita suelos francos, alta humedad y clima cálido."))))

(defrule cana
  (entorno (suelo arcilloso) (lluvia alta) (temperatura ?t&:(> ?t 28)))
  =>
  (assert (recomendacion (cultivo cana_de_azucar)
                         (motivo "La caña de azúcar requiere mucho calor y humedad en suelos arcillosos."))))

(defrule sorgo
  (entorno (suelo arenoso) (lluvia baja) (temperatura ?t&:(> ?t 30)))
  =>
  (assert (recomendacion (cultivo sorgo)
                         (motivo "El sorgo es resistente a la sequía y al calor, ideal para suelos arenosos."))))

(defrule soja
  (entorno (suelo franco) (lluvia media) (estacion primavera))
  =>
  (assert (recomendacion (cultivo soja)
                         (motivo "La soja crece bien en primavera con suelos francos y lluvias moderadas."))))
