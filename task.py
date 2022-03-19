import cobra

from cobra import Model,Reaction,Metabolite

model=Model('model_task')

v0=Reaction('v0')#======>glc
v0.name='v0'
v0.lower_bound=1
v0.upper_bound=1

v1=Reaction('v1')#glc=======>AA
v1.name='v1'
v1.lower_bound=0
v1.upper_bound=1000

v2=Reaction('v2')#AA=======>Biomass
v2.name='v2'
v2.lower_bound=0
v2.upper_bound=1000

M=Reaction('M')#Biomass=======>
M.name='M'
M.lower_bound=0
M.upper_bound=1000

glc=Metabolite('glc',compartment='c')
AA=Metabolite('AA',compartment='c')
Biomass=Metabolite('Biomass',compartment='c')


v0.add_metabolites({glc:1})

v1.add_metabolites({glc:-1,AA:1})

v2.add_metabolites({AA:-9.09,Biomass:1})

M.add_metabolites({Biomass:-1})

model.add_reactions([v0,v1,v2,M])

model.objective='M'

model.optimize()

model.summary()

cobra.io.save_json_model(model,"test2.json")

import escher

from escher import Builder

builder=Builder()

builder

