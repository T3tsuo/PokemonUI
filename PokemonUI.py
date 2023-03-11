import httpimport

n = input("1 for EverstoneFarming, 2 for PlantorWater, 3 for LevelFarming: ")

if n == "1":
    with httpimport.github_repo(username='T3tsuo', repo='EverstoneFarming', ref='main'):
        import EverstoneFarming
elif n == "2":
    with httpimport.github_repo(username='T3tsuo', repo='PlantorWater', ref='main'):
        import PlantorWater
elif n == "3":
    with httpimport.github_repo(username='T3tsuo', repo='LevelFarming', ref='main'):
        import LevelFarming
