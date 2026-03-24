from hillclimber import HILL_CLIMBER

hc = HILL_CLIMBER()
hc.parent.Evaluate(directOrGUI="GUI")  # first random robot

hc.Evolve()

hc.Show_Best()  # final evolution
